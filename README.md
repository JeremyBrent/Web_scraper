# Web Scraper 

## Displayed web page:
![Mars scraper homepage!](Assets/screenshots/screenshot.png "Mars scraper homepage")


## How to run the code (TBA -- I am having chromedriver bugs):
1. Clone the repository to your local computer, python
2. If you are using Windows, in the scrape_mars.py file, you will need to uncomment lines 9-10 and comment lines 13-14.
3. Download the most recent chromedriver (It is important that the version of chrome and the chromedriver match).
4. Put the Chromedriver in the HD -> usr -> local -> bin directory.
5. Install requirements into python environment: splinter==0.7.6.
    - Command: pip install splinter
6. Open you terminal.
7. 'cd' into the directory that holds the repo.
8. Run the command "python app.py".
9. Open your browser and go to "http://localhost:5000/".
10. Click the "Scrap New Data Button" on the web page. It will take about a few moments for the scraping to complete. Once the scraping function is complete, the updated data will be displayed on the webpage.
