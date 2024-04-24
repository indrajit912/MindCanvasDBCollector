"""
A script utilizing the MindCanvas API endpoint GET /api/export_db to retrieve data and store it locally.

Author: Indrajit Ghosh
Created on: Apr 24, 2024
"""
import requests
import json
from datetime import datetime
from dotenv import load_dotenv
import os
import logging
from os.path import join, dirname
from pathlib import Path

# Configure logging
logging.basicConfig(filename='fetch_mindcanvas_db.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MINDCANVAS_HOST = os.environ.get("MINDCANVAS_HOST")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
MINDCANVAS_DATA = Path(__file__).parent.absolute() / "mindcanvas_data"

def fetch_and_save_data():
    """
    Fetches data from the Mindcanvas API and saves it to a JSON file.

    The function sends a GET request to the Mindcanvas API to fetch data. It uses
    the provided bearer token for authentication. The fetched data is saved into a
    JSON file with a filename containing the current date.

    Returns:
        None
    """
    if not MINDCANVAS_DATA.exists():
        MINDCANVAS_DATA.mkdir()
    
    url = MINDCANVAS_HOST + "/api/export_db"
    headers = {
        'Authorization': f'Bearer {BEARER_TOKEN}'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Generate the filename based on the current date
        today = datetime.today()
        filename = f"mindcanvas_db_{today.strftime('%b_%d_%Y')}.json".lower()
        filepath = MINDCANVAS_DATA / filename

        # Write the response content (JSON data) into the file
        with open(filepath, 'w') as file:
            json.dump(response.json(), file, indent=4)
        logging.info(f"Data saved to {str(filepath)}")
    else:
        logging.error(f"Failed to fetch data: {response.status_code} - {response.text}")

# Call the function to fetch and save the data
fetch_and_save_data()
