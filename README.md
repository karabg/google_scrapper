# Google Search Scraper

This Python script, `main.py`, performs a Google search for a specified query and retrieves the top results. It leverages the `requests` and `BeautifulSoup` libraries to extract URLs from Google’s search results page.

## Features
- Fetches a customizable number of URLs (up to 100 by default) based on the specified search query.
- Uses command-line arguments for easy configuration.

## Requirements
Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Usage
Run the script from the command line, specifying your search query and (optionally) the number of results:

```bash
python main.py "your search query" --count 100
```

Replace `"your search query"` with your search term and adjust `--count` to the desired number of results.

## Example
```bash
python main.py "e-commerce" --count 50
```

## Files
- **main.py**: The main script for scraping search results.
- **requirements.txt**: Contains the required Python packages (`requests` and `beautifulsoup4`).