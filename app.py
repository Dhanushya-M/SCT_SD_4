from flask import Flask, render_template, request, send_file
from ecommerce_scraper import scrape_products
import csv

app = Flask(__name__)

@app.route('/')
def index():
    products = scrape_products()

    # Search & filter logic (optional but included for continuity)
    title_query = request.args.get('title', '').lower()
    rating_query = request.args.get('rating', '')

    if title_query:
        products = [p for p in products if title_query in p['title'].lower()]
    if rating_query and rating_query != "All":
        products = [p for p in products if p['rating'].lower() == rating_query.lower()]

    return render_template('index.html', products=products, title_query=title_query, rating_query=rating_query)


# ✅ NEW: Download CSV route
@app.route('/download')
def download_csv():
    products = scrape_products()
    
    # Save products to CSV
    filename = "products.csv"
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'price', 'rating', 'link'])
        writer.writeheader()
        for product in products:
            writer.writerow(product)

    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
