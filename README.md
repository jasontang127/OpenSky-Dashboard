# opensky-dashboard
A Python Dash dashboard for analyzing flight data
# Functionality
* Displays flight data analytics through multiple visualizations
* Takes in user input to filter the data based on datetime
* Dynamically updates the visualizations based on the input
  * Line chart: displays the number of flights over time for the given time frame

  ![image](https://github.com/user-attachments/assets/7c55ed16-284f-456d-b331-9e22de762313)


  * Pie chart: displays flights' countries of origin for the given time frame

  ![image](https://github.com/user-attachments/assets/8c7c6687-c94e-4746-8fbc-1b16704b62f2)

# Usage
Setup
* Register for an OpenSky account
* Install the OpenSky API (follow the instructions here: https://github.com/openskynetwork/opensky-api/blob/master/README.md)
* Install numpy, pandas, dash, matplotlib, and plotly using pip
* Run the app.py Python file
Navigating the Dashboard
* Input date range in Epoch time, and hit submit to filter the data on date
  
![image](https://github.com/user-attachments/assets/bb0e99cb-fb81-4965-a05f-b50a7cf68925)

# Technologies Used
* Python
  * Numpy
  * Pandas
  * Dash
  * OpenSky-API

# Further Enhancements
* Clean up date range input (calendar selection rather than inputting epoch time)
* Add more charts (heatmap, histogram)
* Incorporate larger dataset/rolling data functionality
* Deploy to cloud
