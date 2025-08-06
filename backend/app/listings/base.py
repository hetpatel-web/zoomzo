"""Base classes and utilities for listing scrapers."""


class ListingSource:
    """Placeholder base class for scraping listings."""
    def fetch_listings(self):
        """Placeholder method to fetch listings."""
        raise NotImplementedError
