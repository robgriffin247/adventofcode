import httpx
import os 
from dotenv import load_dotenv

load_dotenv()

def scrape(day):
    
    url = f'https://adventofcode.com/2024/day/{day}/input'

    response = httpx.get(url, cookies={'session':os.getenv('cookie')}, timeout=20.0)

    print(f"Data for day {day} scraped - happy coding!")

    return response.content
