# import libraries

import requests,json,lxml

from bs4 import BeautifulSoup

HEADERS = {'user-agent': 'Himel Rahman, overwatcher.tk, rebelhaze@gmail.com'}
BASE_URL = "https://playoverwatch.com/en-us/career/pc/"





def get_stats():

    soup = _get_soup("chipshajen-2102")
    comp_box = soup.find('div', attrs={'id': 'competitive'})
    all_heroes = comp_box.find('div', attrs={'class': 'row js-stats toggle-display gutter-18@md spacer-12 spacer-18@md is-active'})

    #comp_table2 = comp_box.find('table', attrs={'class': 'data-table'})
    #all_heroes = comp_box.findAll('table', attrs={'class': 'data-table'})
    jsonobj = {}
    comp = {}
    comp['competitive'] = []



    for table in all_heroes:
       data = _parse_table(table)

       for champ in data:
            jsonobj[champ[0]] = champ[1]

    comp['competitive'].append(jsonobj)
    print(comp['competitive'][0]["Solo Kills - Most in Game"])

    print(comp)

def _parse_table(table):
    table_body = table.find('tbody')
    table_head = table.find('h5', attrs={'class': 'stat-title'})
    rows = table_body.find_all('tr')
    data = []
    print(table_head.text)
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    return data





def _get_soup(user):

    result = requests.get(BASE_URL + user, headers=HEADERS)



    if result.status_code == 200:
        print("200")
        c = result.content
        soup = BeautifulSoup(c, 'lxml')
        return soup

    else:
        return None






