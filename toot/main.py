import argparse
import requests
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="Share text on the Fediverse")
    parser.add_argument("text", help="Text to share on the Fediverse")
    args = parser.parse_args()

    # Define the instance URL and the access token
    instance_url = os.getenv("MASTODON_INSTANCE_URL")  
    access_token = os.getenv("MASTODON_ACCESS_TOKEN") 

    # Compose a toot (ActivityPub message)
    toot = {
        "type": "Note",
        "status": args.text
    }

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Send the toot to the instance
    response = requests.post(f"{instance_url}/api/v1/statuses", json=toot, headers=headers)

    if response.status_code == 200:
        print("Successfully shared the text on the Fediverse!")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    main()
