## Weather Updater

Simple utility script I made to get familiar with using APIs and working with JSON data. Pretty useful and convenient though.

#### How it works:
*Python file*:
* Sends a GET request to the Google Weather API
* Returns the JSON data with the current weather information
* Parses the JSON data to retrieve info I am interested in (e.g., current temp, feels like temp, chance of storms, etc.)
* Sets up a Windows notification to deliver this information in a nice human readable format
  
*Batch file*:
* Calls the Python script to run
* The .bat file itself is called by Windows Task Scheduler every time I log on to my computer
