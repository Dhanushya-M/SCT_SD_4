# 🛒 Task 04 – E-Commerce Web Scraper & Data Exporter

This project is developed as part of **SkillCraft Technology Internship – Task 04**. 

The goal is to build a web application that extracts **product information** from an 
e-commerce site (🛍️), such as names, prices, and ratings, and stores them in a structured format like a **CSV file** for analysis and reuse.

---

## 📘 Task Description

> **"Create a program that extracts product information, such as names, prices, and ratings, from an online e-commerce website and stores the data in a structured format like a CSV file."**

In this task, I developed a **web-based scraper** using **Python**, **Flask**, and **BeautifulSoup** that fetches real-time product details from a public site and displays them in a web interface. Users can also **download the data as a CSV** file.

---

## 🧠 Key Features

✨ Web scraping from a real website (`http://books.toscrape.com/`)  
📦 Extracts: Product Title, Price, Rating, Product Link  
📁 Exports data into a clean, well-structured `.csv` file  
🔍 Optional search & rating filter on UI  
🌐 Flask-based dynamic frontend  
📥 One-click **Download CSV** button

---

## 🛠️ Technologies Used


| 🧩 Component        | 🔧 Technology         |
|--------------------|----------------------|
| Web Framework      | Flask (Python)       |
| Scraping Engine    | BeautifulSoup + Requests |
| Frontend           | HTML, Jinja2         |
| Output Format      | CSV (UTF-8 encoded)  |
| Hosting (Optional) | Localhost or Render  |

---

## 📁 File Structure

ecommerce-scraper/

├── app.py # Flask app with routes and CSV logic

├── ecommerce_scraper.py # Web scraping logic

├── templates/

│ └── index.html # Frontend display

├── static/ # (Optional) CSS / JS

├── products.csv # Exported data

├── .gitignore # Git ignored files

├── LICENSE # MIT License

└── README.md # This file


---

## 🚀 How to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ecommerce-scraper.git
   cd ecommerce-scraper

2.**Install dependencies**

pip install flask beautifulsoup4 requests

3.**Run the Flask app**

python app.py

4.**Access in browser**

Open http://127.0.0.1:5000

✔ View product data
💾 Click “Download CSV” to save


## 🧪 Sample Output

Example CSV:

title,price,rating,link
"The Great Gatsby","£20.99","Four","http://books.toscrape.com/catalogue/..."
"Python Basics","£45.00","Five","http://books.toscrape.com/catalogue/..."
...

## 🧠 Learning Outcomes

✅ Implemented real-time web scraping logic
✅ Worked with HTML parsing using BeautifulSoup
✅ Built a full-stack app with Flask
✅ Exported scraped data to a CSV file dynamically
✅ Improved understanding of client-server interactions and RESTful design


## 📬 Contact Me

👩‍💻 Name: Dhanushya M

📧 Email: dhanushyamahendran2004@gmail.com

💼 LinkedIn: linkedin.com/in/dhanushya-m


## 🪪 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute it for both personal and professional purposes.
View the full license in LICENSE


## 🔖 Built with passion as part of SkillCraft Technology Internship – Task 04

🛍️ "From web to CSV — making e-commerce data useful!"


