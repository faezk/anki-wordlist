# Anki Wordlist

Create an Anki deck from your word list using Python.

## Installation Instructions

### 1. Install AnkiConnect
If you haven't already installed AnkiConnect, you need to do so. Here's how:

- Go to the [AnkiConnect plugin page](https://ankiweb.net/shared/info/2055492159) and get the add-on code (2055492159).
- Open Anki, navigate to **Tools > Add-ons > Get Add-ons**, and paste the code.
- Restart Anki to activate the add-on.

### 2. Check if AnkiConnect is Enabled
Once installed, ensure that AnkiConnect is enabled and running correctly:

- Go to **Tools > Add-ons** and confirm that AnkiConnect is listed and enabled.

### 3. Install Required Python Libraries
This script uses the `requests` library to make HTTP requests to the AnkiConnect API. Install it by running:

```bash
pip install requests
