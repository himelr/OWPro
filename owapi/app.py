#!flask/bin/python
import requests
from flask import Flask,jsonify
from bs4 import BeautifulSoup

from owapi.BlizzardInterface import get_stats


HEADERS = {'user-agent': 'Himel Rahman, overwatcher.tk, rebelhaze@gmail.com'}
BASE_URL = "https://playoverwatch.com/en-us/career/pc/"


app = Flask(__name__)

@app.route('/')

def index():

    stats = _get_stats_json()


    return jsonify({'stats': stats})





def _get_stats_json():

    # stats = get_stats('quickplay')
    user = 'chipshajen-2102'
    soup = _get_soup(user)

    stats_qck = get_stats(soup, mode='quickplay')
    stats_comp = get_stats(soup)

    stats = {}
    stats['competitive'] = stats_comp
    stats['quickplay'] = stats_qck
    stats['user'] = {"username": user}
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