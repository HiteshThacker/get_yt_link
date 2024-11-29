import requests
from bs4 import BeautifulSoup

def scrape_amazon_categories(url):
    try:
        # Send a GET request to the Amazon URL
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP request errors

        # Parse the page content
        soup = BeautifulSoup(response.content, "html.parser")

        # Locate the categories section
        categories_section = soup.find("div", {"id": "nav-xshop-container"})
        if not categories_section:
            print("Categories section not found!")
            return

        # Find all category links
        categories = categories_section.find_all("a")
        categories_data = {}
        
        for category in categories:
            category_name = category.get_text()
            category_link = category["href"]
            categories_data[category_name] = "https://www.amazon.in" + category_link

        # Print the scraped data
        for category, link in categories_data.items():
            print(f"Category: {category}, Link: {link}")

        return categories_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")

# Example usage
if __name__ == "__main__":
    amazon_url = "https://www.amazon.in/"  # Base Amazon India URL
    categories = scrape_amazon_categories(amazon_url)
