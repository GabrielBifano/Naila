import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

def scrape_signa_website():
  """
  Scrape the SIGNA website and save content to a text file
  """
  url = "https://www.signa.pt/"
  
  # Headers to mimic a real browser
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'pt-PT,pt;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
  }
  
  try:
    print("Connecting to https://www.signa.pt/...")
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    
    print("Successfully connected! Parsing content...")
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract various elements from the page
    scraped_data = extract_signa_content(soup)
    
    # Save to text file
    save_to_txt(scraped_data, url)
    
    print("Scraping completed successfully!")
    return True
      
  except requests.RequestException as e:
    print(f"Error fetching the webpage: {e}")
    return False
  except Exception as e:
    print(f"Unexpected error: {e}")
    return False

def extract_signa_content(soup):
  """
  Extract specific content from the SIGNA website
  """
  content = []
  
  # Add header with timestamp
  content.append("="*60)
  content.append("SIGNA WEBSITE SCRAPE")
  content.append(f"Scraped on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
  content.append("URL: https://www.signa.pt/")
  content.append("="*60)
  content.append("")
  
  # Extract page title
  title = soup.find('title')
  if title:
    content.append(f"PAGE TITLE: {title.get_text().strip()}")
    content.append("-" * 30)
    content.append("")
  
  # Extract meta description
  meta_desc = soup.find('meta', attrs={'name': 'description'})
  if meta_desc:
    content.append(f"DESCRIPTION: {meta_desc.get('content', '').strip()}")
    content.append("-" * 30)
    content.append("")
  
  # Extract main headings (h1, h2, h3)
  headings = soup.find_all(['h1', 'h2', 'h3', 'h4'])
  if headings:
    content.append("HEADINGS:")
    for heading in headings:
      heading_text = heading.get_text().strip()
      if heading_text:
        content.append(f"  {heading.name.upper()}: {heading_text}")
    content.append("-" * 30)
    content.append("")
  
  # Extract all paragraphs
  paragraphs = soup.find_all('p')
  if paragraphs:
    content.append("PARAGRAPHS:")
    for i, p in enumerate(paragraphs, 1):
      para_text = p.get_text().strip()
      if para_text and len(para_text) > 10:  # Filter out very short paragraphs
        content.append(f"  [{i}] {para_text}")
        content.append("")
    content.append("-" * 30)
    content.append("")
  
  # Extract all links
  links = soup.find_all('a', href=True)
  if links:
    content.append("LINKS:")
    for link in links:
      link_text = link.get_text().strip()
      link_url = link.get('href')
      if link_text and link_url:
        # Convert relative URLs to absolute
        if link_url.startswith('/'):
          link_url = 'https://www.signa.pt' + link_url
        content.append(f"  Text: {link_text}")
        content.append(f"  URL:  {link_url}")
        content.append("")
    content.append("-" * 30)
    content.append("")
  
  # Extract images
  images = soup.find_all('img')
  if images:
    content.append("IMAGES:")
    for i, img in enumerate(images, 1):
      img_src = img.get('src', '')
      img_alt = img.get('alt', 'No alt text')
      if img_src:
        # Convert relative URLs to absolute
        if img_src.startswith('/'):
          img_src = 'https://www.signa.pt' + img_src
        content.append(f"  [{i}] Alt: {img_alt}")
        content.append(f"      Src: {img_src}")
        content.append("")
    content.append("-" * 30)
    content.append("")

  # Extract any contact information (emails, phones)
  all_text = soup.get_text()
  import re
  
  # Find email addresses
  emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', all_text)
  if emails:
    content.append("EMAIL ADDRESSES FOUND:")
    for email in set(emails):  # Remove duplicates
      content.append(f"  {email}")
    content.append("-" * 30)
    content.append("")
  
  # Find phone numbers (Portuguese format)
  phones = re.findall(r'(?:\+351\s?)?[29]\d{2}\s?\d{3}\s?\d{3}', all_text)
  if phones:
    content.append("PHONE NUMBERS FOUND:")
    for phone in set(phones):  # Remove duplicates
      content.append(f"  {phone}")
    content.append("-" * 30)
    content.append("")

  # Add raw text content at the end (cleaned)
  content.append("COMPLETE TEXT CONTENT:")
  content.append("=" * 30)
  
  # Clean and add the full text
  full_text = soup.get_text()
  lines = full_text.split('\n')
  cleaned_lines = [line.strip() for line in lines if line.strip()]
  
  for line in cleaned_lines:
    content.append(line)
  
  return content

def save_to_txt(content, url):
  """
  Save scraped content to a text file
  """
  # Create filename with timestamp
  timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
  filename = f'signa_scrape_{timestamp}.txt'
  
  try:
    with open(filename, 'w', encoding='utf-8') as file:
      for line in content:
        file.write(line + '\n')
    
    print(f"Content successfully saved to: {filename}")
    print(f"File size: {os.path.getsize(filename)} bytes")
      
  except Exception as e:
    print(f"Error saving file: {e}")


# Uncomment code below to scrap

# if __name__ == "__main__":
#   print("Starting SIGNA website scraping...")
#   print("This will save all content to a text file.")
#   success = scrape_signa_website()
#   if success:
#     print("\n✓ Scraping completed successfully!")
#     print("Check the generated .txt file for the scraped content.")
#   else:
#     print("\n✗ Scraping failed. Please check your internet connection and try again.")