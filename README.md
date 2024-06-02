# Web Scraping and Data Analysis Project

This project involves web scraping articles from provided URLs, processing the textual data to extract various metrics, and saving the results to output files. The project is structured to work as a standalone Python application.

### How to Run

- Install the requirement/ dependencies
  `pip install -r requirements.txt`

- Run the Application
  `python src/main.py`

### Approach

1. Web Scraping
The scrape.py script is responsible for scraping articles from the URLs provided in the Input.xlsx file. It uses the newspaper3k library to download and parse the articles, extracting the title and text. The results are saved to artifacts/scraped_articles.csv.

2. Data Processing
The process.py script processes the scraped articles to calculate various metrics such as positivity score, polarity, subjectivity, average word length, and more. It utilizes libraries like TextBlob, textstat, and nltk for text analysis. The processed data is then saved to artifacts/analyzed_output.xlsx.

3. Utility Functions
Utility functions for text cleaning, syllable counting, and personal pronoun counting are defined in utils.py.

4. Main Script
The main.py script coordinates the entire workflow. It first calls the scraping function to collect data from the web and then processes the collected data to generate the required output.

### Raw Approach

First , i used bueatifulsoup to web scrape the data but as every article contains different div class so i used newspaper3k library and used Article to extract the article from a particlar website. i passed all the url to the function and saved the files to artifacts. then i created different methods which are used to preprocess the data which we have to save to the output file. i created a dataframe which have all the field in correct order and then export to the artifacts.
the expirement folder contains an .ipynb file where i tried all this.


