import webbrowser

from pages.quotes_page import QuotesPage

chrome = webbrowser.Chrome(executable_path='/Users/ju_wi/Desktop/PASTA DA BIA/python/chromedriver_win32.exe')
chrome.get('http://quotes.toscrape.com')
#page_content = requests.get('http://quotes.toscrape.com').content
page = QuotesPage(chrome)

for quote in page.quotes:
    print(quote)