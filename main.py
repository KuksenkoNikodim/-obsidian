import random

def load_quotes():
    quotes = [
        "The only limit is your mind. — Unknown",
        "Code is poetry. — Machine",
        "Keep it simple, stupid! — KISS principle",
        "Git commit, git push, and pray. — Developer"
    ]
    return quotes

def get_random_quote(quotes):
    return random.choice(quotes)

if __name__ == "__main__":
    quotes = load_quotes()
    print("Your random quote:")
    print(get_random_quote(quotes))
