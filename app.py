#!flask/bin/python
import requests,json
from flask import Flask,jsonify
from bs4 import BeautifulSoup
from mongo_util import save_stats
from mongo_util import find_one
from mongo_util import save_rank
from mongo_util import fetch_all_pros
from mongo_util import find_profile
from mongo_util import add_player
from mongo_util import save_heroboard
from mongo_util import fetch_heroboard
from blizzard_interface import get_stats, get_img, get_rank, calculate_hero
from leaderboard import Calculated
from bson.json_util import dumps
from heroboard import HeroCalculations





HEADERS = {'user-agent': 'Himel Rahman, overwatcher.tk, rebelhaze@gmail.com'}
BASE_URL = "https://playoverwatch.com/en-us/career/pc/"
pro_players = [
    "EFFECT-31630",
    "Custa-1679",
    "chipshajen-2102",
    "Taimou-2526",
    "xQc-11273",
    "HarryHook-2309",
    "Mickie-11702",
    "cocco-2188",
    "Surefour-2559",
    "Mendokusaii-2955",
    "ShaDowBurn-2301",
    "Seagull-1894",
    "TviQ-1503",
    "aKm-2452",
    "SoOn-2543",
    "LiNkzr-2434",
    "Miro-31858",
    "zunba-3237",
    "EscA-31708",
    "KnOxXx-21951",
    "Nevix-2877",
    "uNKOE-2828",
    "ryujehong-31878",
    "sinatraa-11809",
    "Wraxu-1747"]

test_players = [
    "EFFECT-31630",
    "Custa-1679",
    "chipshajen-2102",
    # "sinatraa-11809"

]

app = Flask(__name__)

@app.route('/')

def index():

    stats = _get_stats_json("xQc-11273")
    calc = Calculated(stats)

    calc.calculate()

    doc = jsonify({'stats': stats})
    #save_stats(stats)

    return doc


@app.route('/u/stats/<username>')

def find_user_stats(username):

    stats = find_one(username)

    #stats2 = json.dumps(stats)
    if stats is None:

        stats2 = _get_stats_json(username)

        if stats2 != None:
            save_stats(stats2)
            return jsonify(json.loads(dumps(stats2)))
        else:
            return jsonify({"error":"no player"})
    else:

        statC = json.loads(stats)

        return jsonify(statC)


@app.route('/u/score/<username>')

def parse_user_stats(username):

    stats = _get_stats_json(username)
    #stats2 = json.dumps(stats)
    statC = json.loads(stats)

    return jsonify(statC)

@app.route('/leaderboard/update/')

def update_leaderboard():

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

@app.route('/score/get/<name>')

def get_score(name):
    stats = _get_stats_json(name)
    c = Calculated(stats)
    scoresJson = {}
    scores = c.calculate()
    scoresJson['scores'] = scores

    return jsonify(scoresJson)


@app.route('/profile/get/<name>')

def get_profile(name):

    try:
         ret = jsonify(json.loads(find_profile(name)))
         return ret

    except TypeError:
        return jsonify({"error" : "no user"})

@app.route('/profile/add/<user>/<name>')

def add_player_to(user,name):

   if add_player(user,name):
       return jsonify({"success" : "added"})
   else:
       return jsonify({"error": "failed"})


def get_score(name):
    stats = _get_stats_json(name)
    c = Calculated(stats)
    scoresJson = {}
    scores = c.calculate()
    scoresJson['scores'] = scores

    return jsonify(scoresJson)

@app.route('/update/heroboard/')

def hero_data():

   # soup = _get_soup("chipshajen-2102")
   # soup2 = _get_soup("Taimou-2526")
   # soup3 = _get_soup("EFFECT-31630")
   # hero_data = get_hero(soup)
   # hero_data2 = get_hero(soup2)
   # hero_data3 = get_hero(soup3)
   # data = calculate_hero( hero_data)
   # data2 = calculate_hero(hero_data2)
   # data3 = calculate_hero(hero_data3)
   hc = HeroCalculations()

   for player in pro_players:
     print(player + " hero data parse")
     soup = _get_soup(player)
     data = calculate_hero(soup)
     hc.calculate_top(data)

   hc.fix_scores()
   save_heroboard(hc.data)

   return jsonify(hc.data)

@app.route('/get/heroboard/')

def get_heroboard():

    return jsonify(json.loads(fetch_heroboard()))

@app.route('/u/herostats/<user>')

def get_herostats(user):
    soup = _get_soup(user)
    if soup != None:
        data = calculate_hero(soup)
        return jsonify(data)
    else:
        return jsonify({"error": "no player"})



def _get_stats_json(user):

    # stats = get_stats('quickplay')
    #Taimou-2526 , chipshajen-2102 Custa-1679 xQc-11273
    #user = 'xQc-11273'
    soup = _get_soup(user)

    if soup == None:
        return None

    stats_qck = get_stats(soup, mode='quickplay')
    stats_comp = get_stats(soup)

    stats = {}
    stats['competitive'] = stats_comp
    stats['quickplay'] = stats_qck
    stats['user'] = {"username": user, "img" : get_img(soup),"rank" : get_rank(soup) }



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