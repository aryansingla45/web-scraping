import os
from src.scrape import scrape_articles
from src.processor import process_data

def main():
    input_file = 'Input.xlsx'
    scraped_file = os.path.join('artifacts', 'scraped_articles.csv')
    output_file = os.path.join('artifacts', 'analyzed_output.xlsx')
    
    # Step 1: Scrape articles
    scrape_articles(input_file, scraped_file)
    
    # Step 2: Process data
    process_data(scraped_file, output_file)
    
    print("Processing complete. Check the 'artifacts' directory for the output files.")

if __name__ == "__main__":
    main()
