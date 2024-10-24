import requests

# AnkiConnect API URL
url = "http://localhost:8765"

def invoke(action, params):
    """Helper function to send a request to AnkiConnect."""
    response = requests.post(url, json={"action": action, "version": 6, "params": params})
    if response.status_code != 200:
        raise ConnectionError(f"Failed to connect to AnkiConnect: {response.status_code}")
    return response.json()

def create_deck_if_not_exists(deck_name):
    """Create a deck if it doesn't already exist."""
    response = invoke("deckNames", {})
    if deck_name not in response["result"]:
        invoke("createDeck", {"deck": deck_name})
        print(f"Deck '{deck_name}' created successfully.")
    else:
        print(f"Deck '{deck_name}' already exists.")

def add_word_to_anki(deck_name, front, back):
    """Add a word to the specified Anki deck."""
    note = {
        "modelName": "Basic",
        "fields": {
            "Front": front,
            "Back": back
        },
        "tags": [],
        "options": {
            "allowDuplicate": False
        }
    }
    
    response = invoke("addNote", {"note": note})
    if response["error"] is None:
        print(f"Successfully added: {front}")
    else:
        print(f"Error adding {front}: {response['error']}")

def main():
    deck_name = "MyWordList"
    
    # Create the deck if it doesn't exist
    create_deck_if_not_exists(deck_name)

    # Word list to add to Anki
    word_list = [
        {"front": "banaani", "back": "banana"},
        {"front": "baari", "back": "bar"},
        {"front": "bussi", "back": "bus"},
        {"front": "elefantti", "back": "elephant"},
        {"front": "energia", "back": "energy"},
        {"front": "faksi", "back": "taxi"},
        {"front": "filmi", "back": "film"},
        {"front": "galleria", "back": "gallery"},
        {"front": "gangsteri", "back": "gangster"}
    ]

    # Add words to the deck
    for word in word_list:
        add_word_to_anki(deck_name, word["front"], word["back"])

if __name__ == "__main__":
    main()
