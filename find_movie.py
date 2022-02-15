import requests
from bs4 import BeautifulSoup

while True:
    title = input()
    url = f'https://www.filmweb.pl/search?q={title}',
    p = {
        'q': title
    }

    title = title.lower()

    response = requests.get('https://www.filmweb.pl/search', params=p)
    soup = BeautifulSoup(response.text, 'html.parser')

    for marker in soup.find_all(class_='filmPreview__title'):
        marker_title = marker.text.lower()
        if title == marker_title:
            print(f"https://www.filmweb.pl{marker.parent['href']}")
