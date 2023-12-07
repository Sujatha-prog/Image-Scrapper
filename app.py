from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape-images', methods=['POST'])
def scrape_images():
    try:
        # Get the URL from the JSON payload
        url = request.json.get('url', '')

        if not url:
            raise ValueError('URL is required')

        # Perform web scraping using BeautifulSoup and requests
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        images = [img['src'] for img in soup.find_all('img')]

        print("Scraped Images:", images)  # Add this line for debugging

        return jsonify({'images': images})

    except Exception as e:
        print("Error:", str(e))  # Add this line for debugging
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

