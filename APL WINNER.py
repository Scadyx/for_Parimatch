import bs4
import requests
from random import shuffle


if __name__ == '__main__':
    url = 'https://www.premierleague.com/clubs'
    response = requests.get(url).content
    soup = bs4.BeautifulSoup(response, 'html.parser')
    divs = soup.findAll('div', {"class": "nameContainer"})
    teams_names = []

    for div in divs:
        headers = div.findAll('h4', {"class": "clubName"}, text=True)
        for header in headers:
            teams_names.append(header.get_text().strip())
    teams_names = list(set(teams_names))
    shuffle(teams_names)
    print(f"\033[91mСледующий победитель АПЛ - {teams_names[0]}")
    input()
    print("helloworld")