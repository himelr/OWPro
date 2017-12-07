#!flask/bin/python
import requests,json
from flask import Flask,jsonify
from bs4 import BeautifulSoup

from mongo_util import save_stats
from mongo_util import find_one
from mongo_util import save_rank
from mongo_util import fetch_all_pros
from blizzard_interface import get_stats, get_img
from leaderboard import Calculated




HEADERS = {'user-agent': 'Himel Rahman, overwatcher.tk, rebelhaze@gmail.com'}
BASE_URL = "https://playoverwatch.com/en-us/career/pc/"


app = Flask(__name__)

@app.route('/')

def index():



    stats = _get_stats_json("xQc-11273")
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




@app.route('/leaderboard/update/')

def update_leaderboard():
    pro_players = ["Custa-1679","chipshajen-2102","Taimou-2526","xQc-11273", "HarryHook-2309", "Mickie-11702"]

    for player in pro_players:
        print(player + " parsing")
        stats = _get_stats_json(player)
        c = Calculated(stats)
        scores = c.calculate()

        ld_json = {}
        ld_json["scores"] = scores
        ld_json["user"] = stats["user"]

        save_rank(ld_json)


    return "Done"
@app.route('/leaderboard/get/')
def fetch_leaderboard():
    leaderboard = fetch_all_pros()

    ld_json = json.loads(leaderboard)
    return jsonify(ld_json)


def _get_stats_json(user):

    # stats = get_stats('quickplay')
    #Taimou-2526 , chipshajen-2102 Custa-1679 xQc-11273
    #user = 'xQc-11273'
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

        c = result.content
        soup = BeautifulSoup(c, 'lxml')
        return soup

    else:
        return None

if __name__ == '__main__':

    app.run(debug=True, host = '0.0.0.0')
    #app.run(debug=True)




# if __name__ == '__main__':
#  main()