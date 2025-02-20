import requests

def fecth_html (url): 
  response = requests.get(url)
  try:
    if response.status_code == 200:
      return response.text
  except Exception as Error_404:
    print(f"Error: {Error_404}")


