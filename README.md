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
  
Install Git LFS on your system, clone the repository, run __git lfs pull__ to fetch and download the actual large files tracked by __Git LFS__. The model.safetensors file (400 MB+) is tracked by Git LFS.  
  
Install the required dependencies using __pip install -r requirements.txt__.  

The nagar , gram, vikaskhand datasets are __geocoded according to location__.  
Download all datasets in .csv format. (csv files are used in geographical analysis. Geographical Analysis can be done by importing real time complaint record from MYSQL SERVER if all csv files are saved in the MYSQL server.)  

All SQL tables are same as the .csv files of dataset folder except the mas_aavedan.csv table.  
The mas_aavedan.csv dataset saves the old complaints. All new complaints are saved in the complaints table located in the LOCAL SQL SERVER. The complaints table contains a new feature __SPAM__ which takes values 0 or 1 according to the result of prediction of trained __BERT MODEL__.
  
## Usage
Run the Flask application using python app.py.  
Access the application through a web browser at http://localhost:5000 or [specific URL if applicable].  

## Dependencies
__Flask__  
__Folium__  
__PyMySQL__  
__Googletrans__  
__Pandas__  
__Torch__  
__Transformers__   
## Endpoints
__/__ :  Home page  
  
__/complain__ :  User will fill a form to submit the complaint and an output statement will pop on the screen regarding weather the complaint was registered successfully or suspected spam or suspected repeated.  In the first case, spam column will contain 0. In the last 2 cases, spam column in the database will have a value 1.  
  
__/show_status__ :  Shows the status of all complaints registered till now.  
  
__/dashboard__ :  Shows the analysis of each type of classification of complaints.  
  
__/geographical-analysis__ :  Endpoint for geographical analysis on the basis of gram / nagar / vikaskhand. 
  
## License
__IIIT - NAYA RAIPUR__,  
under the supervsion of __Dr. Srinivas KG__

