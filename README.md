# RoundData Domains Limited Website

A Flask website built from the supplied RoundData Domains Limited company profile. The visual identity uses the supplied logo artwork and the navy/teal brand colours present in the profile.

## Run locally

```text
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

## Deploy

Start command:

```text
gunicorn app:app
```

Before production, change the Flask secret key and replace the demonstration CSV enquiry storage with a secure database or email workflow.
