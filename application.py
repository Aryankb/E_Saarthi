from flask import Flask, request, jsonify, render_template, redirect, url_for
import folium
import pymysql
from googletrans import Translator
import pandas as pd
import torch
#import ai4bharat_transliteration
from transformers import BertTokenizer, BertForSequenceClassification
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
translator=Translator()
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='MY@sqlary#n27',
    database='minor'
)




vikas = pd.read_csv('dataset/vikaskhand.csv')
gram = pd.read_csv('dataset/gram_panchayat.csv')
ngr = pd.read_csv('dataset/nagar_panchayat.csv')
vibhag = pd.read_csv('dataset/vibhag.csv')




application = Flask(__name__)
app=application


















@app.route('/')
def index():
    return render_template('index.html')



@app.route('/complain',methods=['GET','POST'])
def complain():
    if request.method == 'POST':
        name = str(request.form.get('name'))
        mobile = str(request.form.get('mobile'))
        complain = str(request.form.get('complain'))
        gram_panchayat = int(request.form.get('gramPanchayat'))
        nagar_panchayat = int(request.form.get('nagarPanchayat'))
        vikas_khand = int(request.form.get('vikasKhand'))

        #translation of complaint from hindi to  english
        translated = translator.translate(complain, dest='en')
        translated=str(translated.text)
        #spam detection

        model = BertForSequenceClassification.from_pretrained("models/aryan_spam_detector")
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='MY@sqlary#n27',
            database='minor'
        )
        sample_data = [str(translated)]
        sample_tokenised = tokenizer(sample_data, padding=True, truncation=True, return_tensors='pt')
        outputs = model(**sample_tokenised)
        predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
        predictions = predictions.detach().numpy()
        if predictions[0][0] > predictions[0][1]:
            r='REGISTERED SUCCESSFULLY'
            spam=0
            cursor = connection.cursor()
            cursor.execute("select eng_comp from complaints where (status=0 and mobile_no=%s and vikashkhand_id=%s and gram_panchayat=%s and ngr_panchayat=%s and eng_comp=%s);",(mobile,vikas_khand,gram_panchayat,nagar_panchayat,translated))
            rows=cursor.fetchall()
            cursor.close()
            if(len(rows)>=1):
                r='SUSPECTED AS REPEATED COMPLAINT. CALM DOWN PLEASE ! '
                spam=1
        else:
            r='SUSPECTED AS SPAM !!'
            spam=1



        cursor = connection.cursor()
        print(cursor)
        query="INSERT INTO complaints (name, mobile_no, vikashkhand_id, gram_panchayat, ngr_panchayat, subject,eng_comp, maybe_spam) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
        cursor.execute(query,(name,mobile,vikas_khand,gram_panchayat,nagar_panchayat,complain,translated,spam))
        connection.commit()
        cursor.close()
        connection.close()


        #department, disposal

        # Return a response
        return f"Hi {name} ! Your complain has been {r}."
    else:
        return render_template('complain.html')


@app.route('/show_status',methods=['GET','POST'])
def status():
    if request == 'POST':

        pass
        # #sql se complaint extract karo
        # mobile_number = request.json.get('mobileNumber')  # Get mobile number from the POST request

        # # Filter complaints based on the provided mobile number
        # filtered_complaints = [complaint for complaint in complaints_data if complaint['mobile_number'] == mobile_number]

        # return jsonify({'complaints': filtered_complaints})

    else:
        return render_template('show_status.html')


@app.route('/dashboard',methods=['GET','POST'])
def dash():
    if request == 'POST':
        pass
    else:
        return render_template('dashboard.html')




@app.route('/geographical-analysis', methods=['POST'])
def handle_geographical_analysis():
    geo = {}
    mas_aavedan = pd.read_csv('dataset/mas_aavedan.csv')

    my_map1 = folium.Map(location=[21.18, 81.28], zoom_start=10)
    my_map1.save('dataset/my_map_1.html')
    my_map2 = folium.Map(location=[21.18, 81.28], zoom_start=10)
    my_map2.save('dataset/my_map_2.html')
    my_map3 = folium.Map(location=[21.18, 81.28], zoom_start=10)
    my_map3.save('dataset/my_map_3.html')
    selected_option = int(request.json['option'])
    print(selected_option)
    d1 = {}
    for i in mas_aavedan['vikashkhand_id'].unique():
        d = dict(list((mas_aavedan.groupby('vikashkhand_id'))))[i]
        d1[i] = d['depart_id'].value_counts().to_dict()
    geo['vikashkhand_id'] = d1

    d1 = {}
    for i in mas_aavedan['ngr_panchayat'].unique():
        d = dict(list((mas_aavedan.groupby('ngr_panchayat'))))[i]
        d1[i] = d['depart_id'].value_counts().to_dict()
    geo['ngr_panchayat'] = d1

    d1 = {}
    for i in mas_aavedan['gram_panchayat'].unique():
        d = dict(list((mas_aavedan.groupby('gram_panchayat'))))[i]
        d1[i] = d['depart_id'].value_counts().to_dict()
    geo['gram_panchayat'] = d1

    if selected_option == 1:
        # geo by gram_panchayat
        for i in geo['gram_panchayat'].keys():
            pup = 'TOTAL:' + str(sum(geo['gram_panchayat'][i].values())) + '\n'
            for j in geo['gram_panchayat'][i].keys():
                try:
                    pup += "#" + list(vibhag[vibhag['vid'] == j]['vname'])[0] + ':' + str(
                        geo['gram_panchayat'][i][j]) + "\n"
                except:
                    pass
            try:

                folium.Marker([gram[gram['gp_id'] == i]['latitude'], gram[gram['gp_id'] == i]['longitude']], popup=pup,
                              tooltip=list(gram[gram['gp_id'] == i]['gp_name'])[0]).add_to(my_map3)
            except:
                pass
        # my_map3.save('templates/my_map_3.html')
        # return render_template('my_map_3.html')
        map_html = my_map3.get_root().render()
    elif selected_option == 2:
        # geo by nagar_panch
        for i in geo['ngr_panchayat'].keys():
            pup = 'TOTAL:' + str(sum(geo['ngr_panchayat'][i].values())) + '\n'
            for j in geo['ngr_panchayat'][i].keys():
                try:
                    pup += "#" + list(vibhag[vibhag['vid'] == j]['vname'])[0] + ':' + str(
                        geo['ngr_panchayat'][i][j]) + "\n"
                except:
                    pass
            try:

                folium.Marker([ngr[ngr['ngp_id'] == i]['latitude'], ngr[ngr['ngp_id'] == i]['longitude']], popup=pup,
                              tooltip=list(ngr[ngr['ngp_id'] == i]['nagar_name'])[0]).add_to(my_map2)
            except:
                pass
        # my_map2.save('templates/my_map_2.html')
        # return render_template('my_map_2.html')
        map_html = my_map2.get_root().render()
    elif selected_option == 3:
        # geo by vikashkhand
        for i in geo['vikashkhand_id'].keys():
            pup = 'TOTAL:' + str(sum(geo['vikashkhand_id'][i].values())) + '\n'
            for j in geo['vikashkhand_id'][i].keys():
                try:
                    pup += "#" + list(vibhag[vibhag['vid'] == j]['vname'])[0] + ':' + str(
                        geo['vikashkhand_id'][i][j]) + "\n"
                except:
                    pass
            try:
                folium.Marker(
                    [vikas[vikas['vikaskhand_id'] == i]['latitude'], vikas[vikas['vikaskhand_id'] == i]['longitude']],
                    popup=pup, tooltip=list(vikas[vikas['vikaskhand_id'] == i]['name'])[0]).add_to(my_map1)
            except:
                pass
        # my_map1.save('templates/my_map_1.html')
        # return render_template('my_map_1.html')
        map_html = my_map1.get_root().render()
    else:
        return "<h1>error</h1>"

    return map_html



if __name__ == '__main__':
    app.run(host="0.0.0.0")   #it maps the ip to wherever this app is running
