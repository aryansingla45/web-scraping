import pandas as pd
from newspaper import Article

def scrape_articles(input_file, output_file):
    data = pd.read_excel(input_file)
    data = data[0:100]
    urls = data['URL'].dropna().tolist()
    
    scraped_data = []
    
    for url in urls:
        title, text = scrape_article(url)
        if title and text:
            scraped_data.append({'url': url, 'title': title, 'text': text})
    
    df = pd.DataFrame(scraped_data)
    df.to_csv(output_file, index=False)
    
    print(f"Scraping completed and data saved to {output_file}.")

def scrape_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.title, article.text
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None, None
