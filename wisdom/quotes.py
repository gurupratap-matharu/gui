"""
Script to fetch a wisdom quote.
"""
import json
import logging
from urllib.request import urlopen

logger = logging.getLogger(__name__)


URL = "https://api.themotivate365.com/stoic-quote"


def get_quote():
    """
    Fetch a random quote from the API
    """

    logger.info("📡 fetching quote from api...")

    with urlopen(URL) as response:
        body = response.read()
        quote = json.loads(body)

    return quote.get("quote")
