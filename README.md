# AI in Governance - Complaint Portal
## Description
This project aims at leveraging the power of AI for catering the

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
Flask  
Folium  
PyMySQL  
Googletrans  
Pandas  
Torch  
Transformers  
## Endpoints
/: Home page  
/complain: User will fill a form to submit the complaint and an output statement will pop on the screen regarding weather the complaint was registered successfully or suspected spam or suspected repeated.  In the first case, spam column will contain 0. In the last 2 cases, spam column in the database will have a value 1.  
/show_status: Shows the status of all complaints registered till now.  
/dashboard: Shows the analysis of each type of classification of complaints.  
/geographical-analysis: Endpoint for geographical analysis on the basis of gram / nagar / vikaskhand.  
## License
IIIT - NAYA RAIPUR,  
under the supervsion of Dr. Srinivas KG

