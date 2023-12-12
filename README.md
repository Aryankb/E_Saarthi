# AI in Governance - Complaint Portal
## Description
This project aims at leveraging the power of AI for handling the ambiguities in the complaints submitted through the portal by __detecting spam and repeated complaints__. This project also helps the admin to analyse and classify the complaints on the basis of location with the help of __map view__ classification.

## Table of Contents
__Installation__  
__Usage__  
__Dependencies__  
__Endpoints__  
__License__  
## Installation
To run this project locally, follow these steps:  
  
1. Install Git LFS on your system, clone the repository, run "__git lfs pull__" to fetch and download the actual large files tracked by __Git LFS__. The model.safetensors file (400 MB+) is tracked by Git LFS.  
  
2. Install the required dependencies using __pip install -r requirements.txt__.  

3. The nagar , gram, vikaskhand datasets are __geocoded according to location__. Make same changes in the corresponding SQL tables or directly use these csv files according to conveniwence. Make sure to download all datasets in .csv format only.
  
4. mas_aavedan.csv file will show the geographical analysis of old complaints only, because all NEW COMPLAINTS are saved in the LOCAL SQL SERVER.  
  
5. Geographical Analysis can be done by importing real time complaint records from MYSQL SERVER instead of mas_aavedan.csv file.
  
6. The mas_aavedan.csv dataset saves the old complaints and don't contain spam feature. Where as all new complaints are saved in the complaints table located in the LOCAL SQL SERVER. The complaints table contains a new feature __SPAM__ which takes values 0 or 1 according to the result of prediction of trained __BERT MODEL__.  
  
## Usage
Run the Flask application using python app.py. Access the application through a web browser at http://localhost:5000 or [specific URL if applicable] if deployed.
  
1. The geographical analysis shows the name of location on hovering over the marker. It shows the number and type of complaints from that location if clicked on the marker.  
  
2. User can submit a complain in both english or hindi. The software will translate it to english before passing it to the trained model.
  
3. On submitting a complain, Output on the screen will be SUSPECTED SPAM!! if the complaint submitted was ambiguous or irrelevant.
  
4. Output will be SUSPECTED REPEATED! if the same complaint is registered from the same location by the person having same mobile no.
  
6. Output will be REGISTERED SUCCESSFULLY in all other cases.  


## Dependencies
__Flask__  
__Folium__  
__PyMySQL__  
__Googletrans__  
__Pandas__  
__Torch__  
__Transformers__   
## Endpoints (Handled using FLASK)
1. __/__ :  Home page  
  
2. __/complain__ :  User will fill a form to submit the complaint and an output statement will pop on the screen regarding weather the complaint was registered successfully or suspected spam or suspected repeated.  In the first case, spam column will contain 0. In the last 2 cases, spam column in the database will have a value 1.  
  
3. __/show_status__ :  Shows the status of all complaints registered till now.  
  
4. __/dashboard__ :  Shows the analysis of each type of classification of complaints.  
  
5. __/geographical-analysis__ :  Endpoint for geographical analysis on the basis of gram / nagar / vikaskhand. 
  
## License
__IIIT - NAYA RAIPUR__,  
under the supervsion of __Dr. Srinivas KG__

