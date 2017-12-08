
TITLES = []


def get_stats(soup, mode = "competitive"):


    comp_box = soup.find('div', attrs={'id': mode})
    all_heroes = comp_box.find('div', attrs={'class': 'row js-stats toggle-display gutter-18@md spacer-12 spacer-18@md is-active'})


    temp = {}
    i = 0

    for table in all_heroes:

       data = _parse_table(table)
       temp2={}


       for champ in data:


            temp2[champ[0]] = champ[1]



       temp[TITLES[i]] = temp2
       i += 1


    return temp

    #print(comp['competitive'][0]["Solo Kills - Most in Game"])

def get_img(soup):
    # print(soup.find('img', attrs={'class': 'player-portrait'})['src'])
    return soup.find('img', attrs={'class': 'player-portrait'})['src']

def get_rank(soup):

    rank = {}
    parsed  = soup.find('div', attrs={'class': 'competitive-rank'})
    img = parsed.find('img')['src']
    ranking = parsed.find('div', attrs={'class': 'u-align-center h5'}).text
    rank["img"] = img
    rank["ranking"] = ranking

    return rank
def _parse_table(table):

    table_body = table.find('tbody')
    table_head = table.find('h5', attrs={'class': 'stat-title'})
    TITLES.append(table_head.text)

    rows = table_body.find_all('tr')
    data = []


    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    return data












