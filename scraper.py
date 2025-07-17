import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MITSScraper:
    def __init__(self):
        self.base_url = "https://mits.ac.in"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        
    def get_page_content(self, url):
        """Get content from a specific page"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html5lib')
        except requests.RequestException as e:
            logger.error(f"Error fetching {url}: {e}")
            return None
    
    def scrape_homepage(self):
        """Scrape main homepage for general information"""
        soup = self.get_page_content(self.base_url)
        if not soup:
            return {}
        
        data = {}
        
        # Try to extract news/announcements
        news_sections = soup.find_all(['div', 'section'], class_=lambda x: x and ('news' in x.lower() or 'announcement' in x.lower()))
        if news_sections:
            data['news'] = []
            for section in news_sections[:5]:  # Limit to 5 items
                text = section.get_text(strip=True)
                if text and len(text) > 10:
                    data['news'].append(text[:200] + "..." if len(text) > 200 else text)
        
        # Try to extract events
        event_sections = soup.find_all(['div', 'section'], class_=lambda x: x and 'event' in x.lower())
        if event_sections:
            data['events'] = []
            for section in event_sections[:5]:
                text = section.get_text(strip=True)
                if text and len(text) > 10:
                    data['events'].append(text[:200] + "..." if len(text) > 200 else text)
        
        return data
    
    def scrape_departments(self):
        """Scrape department information"""
        departments_url = f"{self.base_url}/departments"
        soup = self.get_page_content(departments_url)
        if not soup:
            return {}
        
        departments = {}
        
        # Look for department links or sections
        dept_links = soup.find_all('a', href=lambda x: x and 'department' in x.lower())
        for link in dept_links:
            dept_name = link.get_text(strip=True)
            if dept_name:
                departments[dept_name] = link.get('href')
        
        return departments
    
    def scrape_admissions(self):
        """Scrape admission information"""
        admissions_url = f"{self.base_url}/admissions"
        soup = self.get_page_content(admissions_url)
        if not soup:
            return {}
        
        data = {}
        
        # Look for admission-related content
        admission_sections = soup.find_all(['div', 'section'], class_=lambda x: x and 'admission' in x.lower())
        if admission_sections:
            data['admission_info'] = []
            for section in admission_sections[:3]:
                text = section.get_text(strip=True)
                if text and len(text) > 10:
                    data['admission_info'].append(text[:300] + "..." if len(text) > 300 else text)
        
        return data
    
    def scrape_all_data(self):
        """Scrape all available data from the website"""
        logger.info("Starting to scrape MITS website...")
        
        all_data = {
            'last_updated': datetime.now().isoformat(),
            'homepage': self.scrape_homepage(),
            'departments': self.scrape_departments(),
            'admissions': self.scrape_admissions()
        }
        
        logger.info("Scraping completed successfully")
        return all_data
    
    def save_data(self, data, filename='mits_data.json'):
        """Save scraped data to JSON file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logger.info(f"Data saved to {filename}")
        except Exception as e:
            logger.error(f"Error saving data: {e}")
    
    def load_data(self, filename='mits_data.json'):
        """Load scraped data from JSON file"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning(f"Data file {filename} not found")
            return {}
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            return {}

def main():
    """Main function to run the scraper"""
    scraper = MITSScraper()
    
    # Scrape data
    data = scraper.scrape_all_data()
    
    # Save to file
    scraper.save_data(data)
    
    # Display some results
    print(f"Scraped data updated at: {data['last_updated']}")
    print(f"Homepage data: {len(data.get('homepage', {}))} sections")
    print(f"Departments found: {len(data.get('departments', {}))}")
    print(f"Admission info sections: {len(data.get('admissions', {}).get('admission_info', []))}")

if __name__ == "__main__":
    main()
