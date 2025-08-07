"""FastAPI application entry point for Zoomzo backend."""

from fastapi import FastAPI

from app.listings.kijiji import scrape_kijiji


app = FastAPI()


@app.get("/")
def read_root() -> dict:
    """Simple health check endpoint."""
    return {"Zoomzo": "Backend is running!"}


@app.get("/listings/kijiji")
def get_kijiji_listings() -> list:
    """Return dummy listings from Kijiji."""
    return scrape_kijiji()


__all__ = ["app", "read_root", "get_kijiji_listings"]

