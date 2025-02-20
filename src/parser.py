from bs4 import BeautifulSoup

def parser_book(html):
  soup = BeautifulSoup(html, 'html.parser') # Parse o HTML da página 
  book = []
  
  for article in soup.find_all('article', class_='product_pod'):
    title = article.h3.a.attrs['title']
    price = article.find('p', class_='price_color').text.strip()
    availability = article.find('p', class_='instock availability').text.strip()
    book.append({'title': title, 'price': price, 'availability': availability})
  return book

