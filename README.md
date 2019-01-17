# About Web Scrapping:
Web scraping is a technique of extracting information or data from a webpage or any other websites using some tools and Libraries. This technique mostly focuses on the transformation of unstructured data (HTML format) on the web into structured data (database or spreadsheet)


# Why Web Scraping?
Let's say you find data from the web, and there is no direct way to download it, in that situation web scraping using Python is a skill you can use to extract the data into a useful form that can be imported.

# Tools required for web scraping:

You will need to install only these packages:

1. requests for performing your HTTP requests.
2. BeautifulSoup4 for handling all of your HTML processing.
3. urllib2 is a Python module that can be used for fetching URLs.

## Installing these dependencies with pip:

```
pip install requests 
pip install BeautifulSoup4
pip install urllib2
```
## Steps to follow for scraping:

1. Import necessary libraries.
2. Use function “prettify” to look at nested structure of HTML page.
3. Work with HTML tags.
4. Find the right table.
5. Extract the information to DataFrame.
