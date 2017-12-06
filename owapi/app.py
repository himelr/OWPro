#!flask/bin/python
import requests,json
from flask import Flask,jsonify
from bs4 import BeautifulSoup

#from owapi.mongo_util import save_stats
from owapi.mongo_util import find_one

from owapi.blizzard_interface import get_stats, get_img
from owapi.leaderboard import Calculated




HEADERS = {'user-agent': 'Himel Rahman, overwatcher.tk, rebelhaze@gmail.com'}
BASE_URL = "https://playoverwatch.com/en-us/career/pc/"


app = Flask(__name__)

@app.route('/')

def index():



    stats = _get_stats_json()
    calc = Calculated(stats)

    calc.calculate()

    doc = jsonify({'stats': stats})
    #save_stats(stats)





    return doc





@app.route('/u/find/<username>')

def find_user_stats(username):

    stats = find_one(username)
    #stats2 = json.dumps(stats)
    statC = json.loads(stats)


    return jsonify(statC)




def _get_stats_json():

    # stats = get_stats('quickplay')
    #Taimou-2526 , chipshajen-2102 Custa-1679 xQc-11273
    user = 'Custa-1679'
    soup = _get_soup(user)

    stats_qck = get_stats(soup, mode='quickplay')
    stats_comp = get_stats(soup)

    stats = {}
    stats['competitive'] = stats_comp
    stats['quickplay'] = stats_qck
    stats['user'] = {"username": user, "img" : get_img(soup) }



    # stats.append(stats_comp)
    # stats.append(stats_qck)

    return stats



def _get_soup(user):

    result = requests.get(BASE_URL + user, headers=HEADERS)



    if result.status_code == 200:
        print("200")
        c = result.content
        soup = BeautifulSoup(c, 'lxml')
        return soup

    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)




# if __name__ == '__main__':
#  main()