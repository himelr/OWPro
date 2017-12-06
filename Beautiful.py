# import libraries

import requests
import urllib3,json
from bs4 import BeautifulSoup


http = urllib3.PoolManager()
headers = {'user-agent' : 'Himel Rahman, overwatcher.tk, rebelhaze@gmail.com'}

#quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
result = requests.get("https://playoverwatch.com/en-us/career/pc/chipshajen-2102",headers=headers)
c = result.content


#response = http.request('GET', quote_page)
soup = BeautifulSoup(c,'html.parser')
#print(soup.prettify())
comp_box = soup.find('div', attrs={'id': 'competitive'})
comp_table = comp_box.find('table', attrs={'class': 'data-table'})
table_body = comp_table.find('tbody')
rows = table_body.find_all('tr')
#name = name_box.text.strip()

print(table_body)

data = []

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

jsonob = {}
comp =  {}
comp['competitive'] = []

comp2 =  {}
comp2['competitive'] = []

i = 0
for champ in data:
    comp['competitive'].append(champ[0] + ' : ' + champ[1])
    jsonob[champ[0]] = champ[1]



json_string = json.dumps(comp)
json_ob = json.loads(json_string);
comp2['competitive'].append(jsonob)


print(json_string)

print("w")

print(comp)

print("c")

print(json_ob)

#sta = json.loads(comp['competitive'])

print(comp2['competitive'][0]["Barrier Damage Done"])


comp_table2 = comp_box.findAll('table', attrs={'class': 'data-table'})

for cmpt in comp_table2:
    print(cmpt)


table_body = comp_table.find('tbody')
rows = table_body.find_all('tr')


def parsedata(data):
    for champ in data:
        comp['competitive'].append(champ[0] + ' : ' + champ[1])
        jsonob[champ[0]] = champ[1]


#print(jsonob)
#
# price_box = soup.find('div', attrs={'class':'price'})
# price = price_box.text







