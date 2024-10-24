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
        "deckName": deck_name,  # Include deckName directly here
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
    deck_name = "phrase"
    
    # Create the deck if it doesn't exist
    create_deck_if_not_exists(deck_name)

    # Word list to add to Anki
    word_list = [
        {"front": "varo!", "back": "watch out!"},
        {"front": "apua!", "back": "help!"},
        {"front": "tulipalo!", "back": "fire!"},
        {"front": "varas!", "back": "thief!"},
        {"front": "poliisi", "back": "police"},
        {"front": "ambulanssi", "back": "ambulance"},
        {"front": "vaara", "back": "danger"},
        {"front": "seis", "back": "stop"},
        {"front": "huomio!", "back": "attention!"},
        {"front": "rikki", "back": "broken"},
        {"front": "epäkunnossa", "back": "out of order"},
        {"front": "kielletty", "back": "forbidden (pic)"},
        {"front": "suljettu", "back": "closed"},
        {"front": "eksynyt", "back": "lost"},
        {"front": "mene pois!", "back": "go away!"},
        {"front": "en ymmärrä", "back": "I don’t understand"},
        {"front": "myydään", "back": "for sale"},
        {"front": "vuokrataan", "back": "for rent"},
        {"front": "varattu", "back": "reserved"},
        {"front": "vapaa", "back": "free"},
        {"front": "ilmainen", "back": "free of charge (pic)"},
        {"front": "sisään", "back": "entrance “in” (pic)"},
        {"front": "ulos", "back": "exit “out”"},
        {"front": "varauloskäynti", "back": "emergency exit"},
        {"front": "ei sisäänkäyntiä", "back": "no entry"},
        {"front": "ale", "back": "sales"},
        {"front": "hissi", "back": "elevator (pic)"},
        {"front": "rullaportaat", "back": "escalator"},
        {"front": "taksi", "back": "taxi"},
        {"front": "avoinna ma-pe", "back": "open Mon-Fri"},
        {"front": "suljettu la-su", "back": "closed Sat-Sun"},
        {"front": "vedä", "back": "pull"},
        {"front": "työnnä", "back": "push"},
        {"front": "loppuunmyynti", "back": "final sales"},
        {"front": "loppuunmyyty", "back": "sold out"},
        {"front": "vuoronumero", "back": "queue number"},
        {"front": "WC N", "back": "ladies bathroom"},
        {"front": "WC M", "back": "men’s bathroom"},
        {"front": "tervetuloa", "back": "welcome"},
        {"front": "läpikulku kielletty", "back": "no thoroughfare"},
    ]

    # Add words to the deck
    for word in word_list:
        add_word_to_anki(deck_name, word["front"], word["back"])

if __name__ == "__main__":
    main()
