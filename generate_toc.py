import os
import re

def filename_to_title(filename):
    name = os.path.splitext(filename)[0]
    # Replace underscores with spaces and capitalize words
    title = name.replace('_', ' ').title()
    return title

def title_to_leetcode_url(title):
    slug = title.lower()
    slug = re.sub(r'^\d+[\.\-\s]*', '', slug)  # Remove leading problem numbers and punctuation
    slug = slug.replace(' ', '-')
    slug = re.sub(r'[^a-z0-9\-]', '', slug)  # Remove invalid URL chars
    url = f"https://leetcode.com/problems/{slug}/"
    return url

def generate_toc(directory='.'):
    files = [f for f in os.listdir(directory) if f.endswith('.py')]
    files.sort()
    print("# Table of Contents\n")
    for i, filename in enumerate(files, 1):
        title = filename_to_title(filename)
        url = title_to_leetcode_url(title)
        print(f"{i}. [{title}]({url}) - `{filename}`")

if __name__ == "__main__":
    generate_toc()
