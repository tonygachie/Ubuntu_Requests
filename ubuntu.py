import requests
import os
from urllib.parse import urlparse
import uuid

def fetch_image():
    print("Ubuntu Wisdom: 'I am because we are' 🌍")
    url = input("Please enter the URL of an image: ").strip()

    # Directory for storing images
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    try:
        # Try to fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad responses (4xx, 5xx)

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no valid filename, generate one
        if not filename or "." not in filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        # Save file path
        filepath = os.path.join(folder, filename)

        # Write image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✅ Image successfully fetched and saved as: {filepath}")

    except requests.exceptions.MissingSchema:
        print("❌ Invalid URL. Please enter a valid URL starting with http:// or https://")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Unable to reach the server.")
    except requests.exceptions.Timeout:
        print("❌ Request timed out. Please try again later.")
    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP Error occurred: {http_err}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    fetch_image()
