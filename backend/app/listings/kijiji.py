"""Dummy scraper for Kijiji car listings."""


def scrape_kijiji() -> list:
    """Return hard-coded listings from Kijiji for testing."""
    return [
        {"title": "2011 Honda Civic", "price": "$4,500", "location": "Hamilton"},
        {"title": "2010 Toyota Matrix", "price": "$5,200", "location": "Kitchener"},
    ]


__all__ = ["scrape_kijiji"]

