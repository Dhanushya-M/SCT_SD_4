# ecommerce_scraper.py
import requests
from bs4 import BeautifulSoup

URL = "http://books.toscrape.com/"
BASE_URL = "http://books.toscrape.com/"

def scrape_products():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    products = []
    items = soup.find_all('article', class_='product_pod')
    
    for item in items:
        title = item.h3.a['title']
        price = item.find('p', class_='price_color').text.strip()
        rating_class = item.find('p')['class']
        rating = rating_class[1] if len(rating_class) > 1 else "No rating"
        link = BASE_URL + item.h3.a['href']
        
        products.append({
            'title': title,
            'price': price,
            'rating': rating,
            'link': link
        })

    return products
