
TITLES = []

hero_data_div_ids = {
    "Reaper": "0x02E0000000000002",
    "Tracer": "0x02E0000000000003",
    "Mercy": "0x02E0000000000004",
    "Hanzo": "0x02E0000000000005",
    "Torbjörn": "0x02E0000000000006",
    "Reinhardt": "0x02E0000000000007",
    "Pharah": "0x02E0000000000008",
    "Winston": "0x02E0000000000009",
    "Widowmaker": "0x02E000000000000A",
    "Bastion": "0x02E0000000000015",
    "Symmetra": "0x02E0000000000016",
    "Zenyatta": "0x02E0000000000020",
    "Genji": "0x02E0000000000029",
    "Roadhog": "0x02E0000000000040",
    "McCree": "0x02E0000000000042",
    "Junkrat": "0x02E0000000000065",
    "Zarya": "0x02E0000000000068",
    "Soldier: 76": "0x02E000000000006E",
    "Lúcio": "0x02E0000000000079",
    "D.Va": "0x02E000000000007A",
    "Mei": "0x02E00000000000DD",
    "Ana": "0x02E000000000013B",
    "Sombra": "0x02E000000000012E",
    "Orisa": "0x02E000000000013E",
    "Doomfist": "0x02E000000000012F"
}


data_category_ids= {
    "games_won": "0x0860000000000039",
    "multikill_best" : "0x0860000000000346",
    "eliminations_per_life" : "0x08600000000003D2",
    "weapon_accuracy" : "0x086000000000002F",
    "time_played" : "0x0860000000000021"}



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


def get_hero(soup):
    parsed = soup.find('section', attrs={'class': 'hero-comparison-section'})


    return parsed


    print("s")
def calculate_hero(soup):

    player_hero_data = {}
    soup2 = soup.find('div', attrs={'id': 'competitive'})
    for key, value  in data_category_ids.items():
        category = soup2.find('div', attrs={'data-category-id': 'overwatch.guid.' + value})

        data =_player_hero(category,mode = key)
        player_hero_data[key] = data

    player_hero_data["img"] = hero_data_div_ids
    return player_hero_data

def _player_hero(category, mode):

    hero_data = {}

    for key, value in hero_data_div_ids.items():
        hero_div = category.find('div', attrs={'data-hero-guid': value})
        titl = hero_div.find('div', attrs={'class': "title"}).text

        desc = None
        if mode == "games_won" or mode == "multikill_best":
            desc = int(hero_div.find('div', attrs={'class': "description"}).text)

        elif mode =="eliminations_per_life":
            desc = float(hero_div.find('div', attrs={'class': "description"}).text)

        elif mode == "weapon_accuracy":
            desc = int(hero_div.find('div', attrs={'class': "description"}).text[:-1])

        elif mode == "time_played":
            split = hero_div.find('div', attrs={'class': "description"}).text.split()
            try:
                if split[1] == "hours":

                    desc = int(split[0])

                elif split[1] == "hour":

                    desc = 1

                elif split[1] == "minutes":

                    if int(split[0]) >= 30:
                        desc = 1
                    else:
                        desc = 0
                else:
                    desc = 0
            except IndexError:
                desc = 0
                #
        else:
            desc = hero_div.find('div', attrs={'class': "description"}).text
        hero_data[titl] = desc;

    return hero_data

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







