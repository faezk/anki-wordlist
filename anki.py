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
        "deckName": deck_name,  # Specify the deck name here
        "fields": {
            "Front": front,
            "Back": back
        },
        "tags": [],
        "options": {
            "allowDuplicate": False
        }
    }

    # API call with the note only
    response = invoke("addNote", {"note": note})  # Removed deckName from here
    if response["error"] is None:
        print(f"Successfully added: {front}")
    else:
        print(f"Error adding {front}: {response['error']}")

def main():
    deck_name = "Finish question word"
    
    # Create the deck if it doesn't exist
    create_deck_if_not_exists(deck_name)

    # Word list with Finnish sentences on front and English translations on back
    word_list = [
        {"front": "Missä hotelli Sokos on?", "back": "Where is the Sokos hotel?"},
        {"front": "Missä Itsenäisyydenkatu on?", "back": "Where is the street Itsenäisyydenkatu?"},
        {"front": "Missä sairaala on?", "back": "Where is the hospital?"},
        {"front": "Missä vessa on?", "back": "Where is the toilet?"},
        {"front": "Missä naisten vessa on?", "back": "Where is the ladies toilet?"},
        {"front": "Missä miesten vessa on?", "back": "Where is the men’s toilet?"},
        {"front": "Entä muuta? (in the store)", "back": "Do you want anything else?"},
        {"front": "Kuittia? (in the store)", "back": "Do you want the receipt?"},
        {"front": "Mitä saisi olla? (in the store)", "back": "What would you like?"},
        {"front": "Minkämaalainen sinä olet?", "back": "What nationality are you?"},
        {"front": "Puhutko englantia?", "back": "Do you speak English?"},
        {"front": "Voisitko puhua englantia?", "back": "Could you speak English?"},
        {"front": "Puhuuko kukaan täällä englantia?", "back": "Does anyone speak English here?"},
        {"front": "Voisitko kirjoittaa sen ylös?", "back": "Could you write that down?"},
        {"front": "Voisitko toistaa?", "back": "Could you please repeat that?"},
        {"front": "Voisitko auttaa minua?", "back": "Could you help me?"},
        {"front": "Mitä kuuluu?", "back": "How are you?"},
        {"front": "Oletko kunnossa?", "back": "Are you okay?"},
        {"front": "Onko tämä paikka vapaa?", "back": "Is this spot free?"},
        {"front": "Missä saan tupakoida?", "back": "Where am I allowed to smoke?"},
        {"front": "Saisinko vettä?", "back": "Could I get some water?"},
        {"front": "Paljonko se maksaa?", "back": "How much does it cost?"}
    ]

    # Add words to the deck
    for word in word_list:
        add_word_to_anki(deck_name, word["front"], word["back"])

if __name__ == "__main__":
    main()
