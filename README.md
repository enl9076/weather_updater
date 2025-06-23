## ![image](https://github.com/user-attachments/assets/bbb1e383-1be4-4762-911f-757a337b4510) Weather Updater

Simple utility script I made that sends me a desktop notification when I log on to my PC letting know what the weather is for the day. Helped me get familiar with using APIs and working with JSON data. 

#### How it works:
*Python file*:
* Sends a GET request to the Google Weather API
* Returns the JSON data with the current weather information
* Parses the JSON data to retrieve info I am interested in (e.g., current temp, feels like temp, chance of storms, etc.)
* Sets up a Windows notification to deliver this information in a nice human readable format
  
*Batch file*:
* Calls the Python script to run
* The .bat file itself is called by Windows Task Scheduler every time I log on to my computer



#### How you can use this:
* git clone this repo into a local folder
* `pip install -r requiremenets.txt` to ensure the required packages are installed
* Create a .env file within the same directory and add your Google Maps API key, latitude, and longitude
* If you don't need to set up a schedule to run the script/just running it once, no further action needed, just run it like any other Python script
* OTHERWISE - in most cases your won't need to change anything in the batch file, but if you run it and it fails then edit it to reference the full paths to your python.exe and the script
*   - On Windows -> Go to Task Scheduler and create a new action that calls the .bat file
    - On Linux -> Create a cron job (`crontab`) that runs the python file. The batch file is not needed but you may want to add a shebang line at the top of the script (`#!/usr/bin/python3`)
