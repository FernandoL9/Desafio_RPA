from src.fecth import fecth_html
from src.parser import parser_book
from src.save_data import save_data_sqlite
from src.save_extracting_data import save_data_excel

def main():
  url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"

  print('buscando html da página...')
  html = fecth_html(url)

  print('extraindo dados do livro...')
  book = parser_book(html)

  print('Salvando dados do livros no banco de dados...')
  save_data_sqlite(book)

  print('Extraindo dados do banco e salvando em excel')
  save_data_excel()

  print(book)

if __name__ == "__main__":
  main()