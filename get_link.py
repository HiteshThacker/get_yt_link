import requests
from bs4 import BeautifulSoup

def get_youtube_links(search_query, max_results=10):
    try:
        # Encode the search query for the URL
        query = search_query.replace(" ", "+")
        url = f"https://www.youtube.com/results?search_query={query}"

        # Set up headers to mimic a browser request
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }

        # Send the request to YouTube
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error if the request fails

        # Parse the HTML response
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all video links
        video_links = []
        for video in soup.find_all("a", {"href": True}):
            href = video["href"]
            if "/watch?v=" in href:
                full_link = f"https://www.youtube.com{href}"
                if full_link not in video_links:
                    video_links.append(full_link)
                    if len(video_links) >= max_results:
                        break

        return video_links

    except Exception as e:
        print(f"Error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    search_term = "Python tutorials"
    results = get_youtube_links(search_term, max_results=5)
    print("YouTube Links:")
    for link in results:
        print(link)
