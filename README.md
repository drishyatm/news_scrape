# news_scrape
This project is to scrap the news website and fetch the headlines or main headings into a csv.
In this project I am achieving this using two different methods.
1. Heading fetching using feedsearch and saving to csv as list
2. Heading fetching using Beautifulsoup and saving as dataframe to csv using pandas.

How to Run : 

First will run the requirements file necessary to run the python script.
pip install -r requirements.txt

This is the file using the feedparser and feedsearch in fetching the headlines of news 
python headline_fetch_nytimes.py 

Running the script will create a headline_nytimes.csv file with the data titles and date published.

Second script is using the Beautifulsoup

python scrape_nbcnews.py

Running the script will create a nbc_news.csv with the data of only heading