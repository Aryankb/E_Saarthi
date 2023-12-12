# AI in Governance - Complaint Portal
## Description
This project aims at leveraging the power of AI for handling the ambiguities in the complaints submitted through the portal by __detecting spam and repeated complaints__. This project also helps the admin to analyse and classify the complaints on the basis of location with the help of __map view__

## Table of Contents
Installation  
Usage  
Dependencies  
Endpoints  
License  
## Installation
To run this project locally, follow these steps:  
  
Clone the repository.  
Install the required dependencies using pip install -r requirements.txt.  
Set up the database by [describe any necessary database setup].  
[Any additional installation steps required].  
## Usage
Run the Flask application using python app.py.  
Access the application through a web browser at http://localhost:5000 or [specific URL if applicable].  
[Instructions on how to use the application].  
## Dependencies
__Flask__  
__Folium__  
__PyMySQL__  
__Googletrans__  
__Pandas__  
__Torch__  
__Transformers__   
## Endpoints
__/__: Home page  
__/complain__: User will fill a form to submit the complaint and an output statement will pop on the screen regarding weather the complaint was registered successfully or suspected spam or suspected repeated.  In the first case, spam column will contain 0. In the last 2 cases, spam column in the database will have a value 1.  
__/show_status__: Shows the status of all complaints registered till now.  
__/dashboard__: Shows the analysis of each type of classification of complaints.  
__/geographical-analysis__: Endpoint for geographical analysis on the basis of gram / nagar / vikaskhand.  
## License
__IIIT - NAYA RAIPUR__,  
under the supervsion of __Dr. Srinivas KG__

