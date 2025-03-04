import re
from bs4 import BeautifulSoup

def extract_reviews(text):
    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(text, 'html.parser')
    
    # Find all review articles
    review_items = soup.find_all('article', class_='user-review-item')
    
    reviews = []
    
    for item in review_items:
        # Extract rating
        rating_span = item.find('span', class_='ipc-rating-star')
        if rating_span:
            # Look for the inner span with rating
            rating_inner_span = rating_span.find('span', class_='ipc-rating-star--rating')
            if rating_inner_span:
                rating = rating_inner_span.text
                # Convert rating to integer if it's a valid number
                try:
                    rating = int(rating)
                except ValueError:
                    rating = None
            else:
                rating = None
        else:
            rating = None
        
        # Extract reviewer name
        author_link = item.find('a', {'data-testid': 'author-link'})
        reviewer = author_link.text if author_link else "Anonymous"
        
        # Extract review content
        content_div = item.find('div', class_='ipc-html-content-inner-div')
        review_text = content_div.text.strip() if content_div else ""

        # Extract review permalink
        permalink = None
        permalink_link = item.find('a', {'data-testid': 'permalink-link'})
        if permalink_link and 'href' in permalink_link.attrs:
            permalink = permalink_link['href']
            # Make it an absolute URL if it's relative
            if permalink.startswith('/'):
                permalink = 'https://www.imdb.com' + permalink
        
        # Extract review title
        title_element = item.find('h3', class_='ipc-title__text')
        title = title_element.text.strip() if title_element else "No Title"
        # Remove any chevron icon text that might be included
        title = re.sub(r'\s*<svg.*$', '', title)
        
        reviews.append({
            'reviewer': reviewer,
            'rating': rating,
            'title': title,
            'review': review_text,
            'permalink': permalink
        })
    
    return reviews

def save_as_markdown(reviews, output_file='reviews.md'):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('# User Reviews\n\n')
        
        for i, review in enumerate(reviews, 1):
            # Write review header with title, reviewer and rating
            f.write(f"## {i}. {review['title']}\n\n")
            
            # Write reviewer and rating info
            f.write(f"**Reviewer:** {review['reviewer']}  \n")
            
            # Handle None ratings
            if review['rating'] is not None:
                stars = '★' * review['rating'] + '☆' * (10 - review['rating'])
                f.write(f"**Rating:** {review['rating']}/10 {stars}\n\n")
            else:
                f.write(f"**Rating:** Not provided\n\n")
            
            # Write review text
            f.write(f"{review['review']}\n\n")
            
            # Add permalink if available
            if review['permalink']:
                f.write(f"[Read full review on IMDb]({review['permalink']})\n\n")
            
            # Add separator between reviews except after the last one
            if i < len(reviews):
                f.write('---\n\n')
                
if __name__ == '__main__':
    # Test the function
    with open('imdb_reviews.html', 'r', encoding='utf-8') as file:
        html_text = file.read()
    
    reviews = extract_reviews(html_text)
    save_as_markdown(reviews, 'extracted_reviews.md')
    print(f"Successfully extracted {len(reviews)} reviews and saved to extracted_reviews.md")