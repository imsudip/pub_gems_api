import requests
from bs4 import BeautifulSoup


def get_home_page():
    url = "https://fluttergems.dev/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    page_data = []
    # find all 'cat-group' divs
    cat_groups = soup.find_all('div', class_='cat-group')
    for cat_group in cat_groups:
        title = cat_group.find('h2').text
        cards = cat_group.find_all('a', class_='custom-card')
        cards_data = []
        for card in cards:
            card_data = {}
            card_data['title'] = card.find('h5').text
            card_data['count'] = card.find('small', class_='text-muted').text
            card_data['link'] = card.get('href').replace('/', '')
            card_data['image'] = card.find('img').get('src')
            card_data['tags'] = card.find(
                'small', class_='d-none cat-packages').text
            cards_data.append(card_data)
        page_data.append({'title': title, 'cards': cards_data})
    return page_data


def get_category_page(category):
    url = "https://fluttergems.dev/" + category
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    page_data = []
    # find all 'card shadow mb-2 rounded-0' divs
    cards = soup.find_all('div', class_='card shadow mb-2 rounded-0')
    for card in cards:
        card_data = {}
        card_data['title'] = card.find('h5').text
        card_data['image'] = card.find('img').get(
            'src') if card.find('img') else ''
        card_data['likes'] = card.find(
            'h6', class_='card-subtitle mb-2 text-muted').text.split('👍')[1].strip()
        card_data['null_safe'] = card.find(
            'h6', class_='card-subtitle mb-2 text-muted').text.split('👍')[0].strip()
        card_data['link'] = card.find('a').get('href')
        plat_div = card.find('div', class_='card-subtitle mb-1')
        card_data['platforms'] = []
        if plat_div:
            for plat in plat_div.find_all('img'):
                card_data['platforms'].append(plat.get('title'))
        card_data['description'] = card.find('p').text
        page_data.append(card_data)
    return page_data


# main
# if __name__ == '__main__':
#     data = get_home_page()
#     print(data)
