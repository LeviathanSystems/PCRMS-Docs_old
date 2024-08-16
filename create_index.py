import os
from datetime import datetime

# Directory where your posts are stored
posts_dir = "docs"
index_file = os.path.join(posts_dir, "latest_news.md")


def extract_title(file_path):
    """Extract the title from the first line of the markdown file that starts with '#'."""
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("# "):  # Assuming title is the first header
                return line.strip("# ").strip()
    return os.path.basename(file_path).replace(".md", "").replace("-", " ").title()


# Get all Markdown files from the directory and subdirectories
all_files = []
for root, dirs, files in os.walk(posts_dir):
    for file in files:
        if file == "index.md":
            continue  # Skip the index file
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            all_files.append(filepath)

# Sort files by last modified date
sorted_files = sorted(all_files, key=lambda f: os.path.getmtime(f), reverse=True)

# Create content for posts/index.md
content = """
# 📚 Recent Articles

Welcome to our collection of recent articles! Below you'll find a list of the latest additions to our site.

---

"""

# Define the maximum number of articles to list
max_articles = 10
for file in sorted_files[:max_articles]:
    modified_time = os.path.getmtime(file)
    modified_date = datetime.fromtimestamp(modified_time).strftime("%B %d, %Y %I:%M %p")
    relative_path = os.path.relpath(file, posts_dir).replace("\\", "/")

    # Extract title from the Markdown file
    title = extract_title(file)

    # Add article link and date to content
    content += f"### [{title}]({relative_path})\n"
    content += f"_Last Updated: {modified_date}_\n\n"
    content += "---\n\n"

# Write to posts/index.md
with open(index_file, "w") as f:
    f.write(content)

print("posts/index.md updated with recent articles.")
