# Zoomzo Backend

This directory contains the Python backend responsible for scraping car listings,
applying filters, and sending notifications.

## Setup

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the server

Start a development server with:

```bash
uvicorn app.main:app --reload
```

## Testing

Run the test suite with `pytest`:

```bash
pytest
```
