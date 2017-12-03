# import libraries

import json




titles = []
count = 0





def get_stats(soup, mode = "competitive"):


    comp_box = soup.find('div', attrs={'id': mode})
    all_heroes = comp_box.find('div', attrs={'class': 'row js-stats toggle-display gutter-18@md spacer-12 spacer-18@md is-active'})

    #comp_table2 = comp_box.find('table', attrs={'class': 'data-table'})
    #all_heroes = comp_box.findAll('table', attrs={'class': 'data-table'})
    jsonobj = {}
    comp = {}
    comp2 = {}
    qck = {}

    comp['competitive'] = []
    qck['quickplay'] = []
    comp2['competitive'] = []

    temp = {}
    i = 0

    for table in all_heroes:
       data = _parse_table(table,i)


       temp2={}
       #temp.append(titles[i])

       #print(titles[i])


       #comp2['competitive'].append(titles[i])

       print(temp)
       for champ in data:

            jsonobj[champ[0]] = champ[1]
            temp2[champ[0]] = champ[1]
       #temp[titles[i]].append(jsonobj)


       temp[titles[i]] = temp2
       i += 1

       #temjs = json.dumps(temp)
       # tempoo = json.loads(temjs)
       #x = json.loads(temjs, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
       #temp.append(temp2)
       # comp2.append(temp)
       #comp2['competitive'][i].append(jsonobj)


       #comp2['competitive'][0][titles[i]].append(jsonobj)


    return temp

    #comp['competitive'].append(temp)
    print(comp['competitive'][0]["Solo Kills - Most in Game"])


def _parse_table(table, count):

    table_body = table.find('tbody')
    table_head = table.find('h5', attrs={'class': 'stat-title'})
    titles.append(table_head.text)

    rows = table_body.find_all('tr')
    data = []


    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    return data












