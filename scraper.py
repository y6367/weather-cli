import requests, time
from bs4 import BeautifulSoup

def scrape_all_quotes():
    all_quotes = []
    page = 1

    while True:
        url = f"http://quotes.toscrape.com/page/{page}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for quote_div in soup.find_all("div", class_="quote"):
            text = quote_div.find("span", class_="text").get_text()
            author = quote_div.find("small", class_="author").get_text()
            all_quotes.append({"quote": text, "author": author})

        next_button = soup.find("li", class_="next")
        if not next_button:
            break

        page += 1
        print(f"Scraped page {page - 1}, total so far: {len(all_quotes)}")
        time.sleep(1)
    
    return all_quotes

data = scrape_all_quotes()
print(f"Done! Total quotes: {len(data)}")

count = 1
for quote in data:
    print(f"Quote #{count}: {quote.get('quote')} - {quote.get('author')}")
    count += 1


# response = requests.get("http://quotes.toscrape.com")
# print(response.status_code)

# soup = BeautifulSoup(response.text, "html.parser")

# print(soup.prettify()[:1000])

# quote = soup.find("div", class_="quote")
# print(quote)

# all_quotes = soup.find_all("div", class_="quote")
# print(all_quotes)

# for div in all_quotes:
    # text = div.find("span", class_="text").get_text()
    # print(div.find("span", class_="text").get_text())

# text = quote.find("span", class_="text").get_text()
# print(text)