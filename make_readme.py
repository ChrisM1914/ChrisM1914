USERNAME = "ChrisM1914"

readme = f"""# Hi, I'm {USERNAME} 👋

## About me
Student building skills in Python, Git, and data tools.

## Tools I use
- Python (Anaconda)
- Jupyter Notebook
- VS Code
- GitHub Desktop

## Links
- [My GitHub](https://github.com/{USERNAME})
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print("README.md created for", USERNAME)

# GitHub username: ChrisM1914