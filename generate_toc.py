import os
import re

GITHUB_BASE_URL = "https://github.com/amargupta28/leetCode/blob/main/"

def filename_to_title(filename):
    name = os.path.splitext(filename)[0]
    title = name.replace('_', ' ').title()
    return title

def title_to_leetcode_url(title):
    slug = title.lower()
    slug = re.sub(r'^\d+[\.\-\s]*', '', slug)
    slug = slug.replace(' ', '-')
    slug = re.sub(r'[^a-z0-9\-]', '', slug)
    url = f"https://leetcode.com/problems/{slug}/"
    return url

def generate_toc(directory='.'):
    files = [f for f in os.listdir(directory) if f.endswith('.py')]
    files.sort()

    print("| # | Problem | LeetCode Link | Solution File |")
    print("|---|---------|--------------|---------------|")

    for i, filename in enumerate(files, 1):
        title = filename_to_title(filename)
        leetcode_url = title_to_leetcode_url(title)
        github_url = GITHUB_BASE_URL + filename

        leetcode_link = f'<a href="{leetcode_url}" target="_blank" rel="noopener noreferrer">Link</a>'
        github_link = f'<a href="{github_url}" target="_blank" rel="noopener noreferrer">{filename}</a>'

        print(f"| {i} | {title} | {leetcode_link} | {github_link} |")

if __name__ == "__main__":
    generate_toc()
