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
            "content": f"""Based on these user reviews and previous context, suggest 10 blog post topics that address questions or concerns expressed by the reviewers.

{context}

Reviews:
{reviews_markdown}

Generate 10 blog post suggestions in this format:
1. [Question/Title]
   Brief explanation of why this topic matters to viewers

Each suggestion should be a question that viewers would want answered based on the reviews."""
        }]
    )
    
    suggestions = str(message.content[0].text)
    
    # Parse suggestions into a list
    suggestion_list = []
    current_suggestion = []
    
    for line in suggestions.split('\n'):
        if line.strip().startswith(tuple('123456789')):
            if current_suggestion:
                suggestion_list.append('\n'.join(current_suggestion))
                current_suggestion = []
            current_suggestion.append(line.strip())
        elif line.strip():
            current_suggestion.append(line.strip())
    
    if current_suggestion:
        suggestion_list.append('\n'.join(current_suggestion))
    
    return suggestion_list

def get_user_selection(suggestions):
    """Display suggestions and get user selection"""
    print("\nBlog post suggestions:")
    for suggestion in suggestions:
        print(f"\n{suggestion}")
    
    print("\nPlease copy and paste your chosen suggestion (use CTRL+SHIFT+C to copy, CTRL+SHIFT+V to paste):")
    while True:
        selected_text = input().strip()
        
        # Find the suggestion that matches the user's input
        for i, suggestion in enumerate(suggestions, 1):
            if selected_text in suggestion:
                return i, suggestion
        
        print("\nCouldn't find that suggestion. Please copy and paste the exact suggestion text:")

def extract_relevant_content(reviews_markdown, selected_topic):
    """Extract relevant content from reviews for the selected topic"""
    client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
    
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=4096,
        temperature=0.7,
        messages=[{
            "role": "user",
            "content": f"""Given this selected blog topic:

{selected_topic}

Please analyze these reviews and extract the most relevant details, opinions, and insights that relate to this topic. Compose them into 2-3 coherent paragraphs that we can use as source material for the blog post:

{reviews_markdown}"""
        }]
    )
    
    return str(message.content[0].text)

def generate_blog_outline(topic, extracted_content):
    """Generate a detailed blog post outline"""
    client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
    
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=4096,
        temperature=0.7,
        messages=[{
            "role": "user",
            "content": f"""Create a detailed outline for a blog post addressing this topic:

{topic}

Using these extracted insights from user reviews:

{extracted_content}

Generate an outline with main sections and key points to cover in each section."""
        }]
    )
    
    return str(message.content[0].text)

def generate_blog_post(topic, outline, extracted_content):
    """Generate the final blog post"""
    client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
    
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=4096,
        temperature=0.7,
        messages=[{
            "role": "user",
            "content": f"""Write a comprehensive blog post following this outline:

{outline}

Use these extracted insights from user reviews as source material:

{extracted_content}

The blog post should address this topic:
{topic}

Write in a clear, engaging style with proper formatting and structure."""
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
    
    # Get user selection
    selection_num, selected_topic = get_user_selection(suggestions)
    
    # Extract relevant content
    print("\nExtracting relevant content from reviews...")
    extracted_content = extract_relevant_content(reviews_markdown, selected_topic)
    
    # Generate outline
    print("\nGenerating blog post outline...")
    outline = generate_blog_outline(selected_topic, extracted_content)
    print("\nBlog Post Outline:")
    print(outline)
    
    # Generate final blog post
    print("\nGenerating final blog post...")
    blog_post = generate_blog_post(selected_topic, outline, extracted_content)
    
    # Save the blog post
    filename = f"blog_post_{selection_num}.md"
    with open(filename, 'w') as f:
        f.write(blog_post)
    
    print(f"\nBlog post has been saved to {filename}")
    return 0

if __name__ == '__main__':
    exit(main())
