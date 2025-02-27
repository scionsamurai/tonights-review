#!/usr/bin/env python3
import os
import tempfile
from anthropic import Anthropic
from dotenv import load_dotenv
from extract_reviews_from_imdb import extract_reviews, save_as_markdown

def get_user_summaries():
    """Get optional context summaries from the user"""
    print("\nWould you like to add any context summaries (e.g. previous season recaps)?")
    print("Enter summaries one at a time. Press Enter twice when done.\n")
    
    summaries = []
    while True:
        summary = input("Enter a summary (or press Enter to finish): ").strip()
        if not summary:
            if summaries:  # Only break if we have at least one summary
                break
            print("Please enter at least one summary.")
            continue
        summaries.append(summary)
    
    return summaries

def generate_blog_suggestions(reviews_markdown, summaries):
    """Generate blog post suggestions using Claude"""
    # Load environment variables from .env file
    load_dotenv()
    
    # Check for API key
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in environment variables")
        return None
    
    # Initialize Anthropic client
    client = Anthropic(api_key=api_key)
    
    # Prepare context from summaries
    context = "\n\n".join([
        "Previous Context:",
        *[f"- {summary}" for summary in summaries]
    ])
    
    # Generate suggestions using Claude
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=4096,
        temperature=0.7,
        messages=[{
            "role": "user",
            "content": f"""Based on these user reviews and previous context, suggest 5 blog post topics that address questions or concerns expressed by the reviewers.

{context}

Reviews:
{reviews_markdown}

Generate 5 blog post suggestions in this format:
1. [Question/Title]
   Brief explanation of why this topic matters to viewers

Each suggestion should be a question that viewers would want answered based on the reviews."""
        }]
    )
    
    return str(message.content[0].text)

def main():
    # Check if input file exists
    if not os.path.exists('imdb_reviews.html'):
        print("Error: imdb_reviews.html not found")
        return 1
    
    # Read and extract reviews
    print("Extracting reviews from imdb_reviews.html...")
    with open('imdb_reviews.html', 'r', encoding='utf-8') as file:
        html_text = file.read()
    
    reviews = extract_reviews(html_text)
    
    # Save reviews to temporary markdown file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as temp_file:
        save_as_markdown(reviews, temp_file.name)
        
        # Read the markdown content
        with open(temp_file.name, 'r') as f:
            reviews_markdown = f.read()
    
    # Get summaries from user
    summaries = get_user_summaries()
    
    # Generate blog suggestions
    print("\nGenerating blog post suggestions...")
    suggestions = generate_blog_suggestions(reviews_markdown, summaries)
    
    # Save suggestions to file
    with open('blog_suggestions.md', 'w') as f:
        f.write(suggestions)
    
    print("\nBlog post suggestions have been saved to blog_suggestions.md")
    return 0

if __name__ == '__main__':
    exit(main())
