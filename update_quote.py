import random
import re

# Ta liste de citations inspirantes / geek
quotes = [
    "“Every bug is just another level of understanding.”",
    "“Talk is cheap. Show me the code.” – Linus Torvalds",
    "“Programs must be written for people to read, and only incidentally for machines to execute.”",
    "“Before software can be reusable it first has to be usable.” – Ralph Johnson",
    "“Computers are good at following instructions, but not at reading your mind.”",
    "“Deleted code is debugged code.” – Jeff Sickel",
    "“It’s not a bug – it’s an undocumented feature.”",
    "“Simplicity is the soul of efficiency.” – Austin Freeman",
    "“First, solve the problem. Then, write the code.” – John Johnson",
    "“Code is like humor. When you have to explain it, it’s bad.” – Cory House"
]

def update_readme():
    # Choisir une citation au hasard
    selected_quote = random.choice(quotes)
    
    # Lire le fichier README
    with open("README.md", "r", encoding="utf-8") as file:
        content = file.read()
    
    # Remplacer le contenu entre les balises
    pattern = r"(<!-- START_QUOTE -->\n)(.*)(\n<!-- END_QUOTE -->)"
    replacement = f"\\1{selected_quote}\\3"
    
    new_content = re.sub(pattern, replacement, content)
    
    # Sauvegarder les modifications
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(new_content)

if __name__ == "__main__":
    update_readme()
