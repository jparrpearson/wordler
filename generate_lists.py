#
# Creates a series of word lists based on word length from a master URL.
#
# Usage:
# $ pip install requests
# $ python generate_lists.py
# $ wc -l word-lists/* | sort -n
#

import os
import requests

WORDLIST_URL = "https://www.mit.edu/~ecprice/wordlist.10000"
OUTPUT_DIR = "word-lists"

def fetch_wordlist(url):
    response = requests.get(url)
    response.raise_for_status()
    return [word for word in response.text.splitlines() if word.strip()]

def split_words_by_length(words):
    word_files = {}

    # Sort words
    for word in words:
        length = len(word)
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        filename = os.path.join(OUTPUT_DIR, f"words{length}.txt")
        if filename not in word_files:
            word_files[filename] = []
        word_files[filename].append(word)

    # Write files
    for filename, word_list in word_files.items():
        with open(filename, "w") as f:
            f.write("\n".join(word_list))
        print(f"Saved {len(word_list)} words to {filename}")

if __name__ == "__main__":
    words = fetch_wordlist(WORDLIST_URL)
    split_words_by_length(words)
