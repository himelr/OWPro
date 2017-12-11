from blizzard_interface import hero_data_div_ids,data_category_ids

class HeroCalculations:

    def __init__(self):
        self.data = None
        self.count = 0
        self.half = self._halftable()




    def calculate_top(self,hero_data):
        if self.data != None:
            for key, value in data_category_ids.items():

                for hero, score in hero_data[key].items():
                    if hero_data[key][hero] != 0:
                        self.data[key][hero] += hero_data[key][hero]
                        self.half[key][hero] += 1
                    #print(hero + str(score))

#3+6+5
        else:
            self.data = hero_data

        self.count+=1

    def _halftable(self):
        half = {}
        for key, value in data_category_ids.items():
            sub_data = {}
            for hero, score in hero_data_div_ids.items():
                sub_data[hero] = 1
                half[key] = sub_data

        return half
    #Fixes scores to represent average.
    def fix_scores(self):
        for key,value in data_category_ids.items():
            for hero, score in self.data[key].items():
                if key == "eliminations_per_life":
                    self.data[key][hero] = round(self.data[key][hero] / self.half[key][hero],2)
                else:
                    self.data[key][hero] = int(self.data[key][hero] / self.half[key][hero])






































# hero_data_div_ids = {
#     "reaper": "0x02E0000000000002",
#     "tracer": "0x02E0000000000003",
#     "mercy": "0x02E0000000000004",
#     "hanzo": "0x02E0000000000005",
#     "torbjorn": "0x02E0000000000006",
#     "reinhardt": "0x02E0000000000007",
#     "pharah": "0x02E0000000000008",
#     "winston": "0x02E0000000000009",
#     "widowmaker": "0x02E000000000000A",
#     "bastion": "0x02E0000000000015",
#     "symmetra": "0x02E0000000000016",
#     "zenyatta": "0x02E0000000000020",
#     "genji": "0x02E0000000000029",
#     "roadhog": "0x02E0000000000040",
#     "mccree": "0x02E0000000000042",
#     "junkrat": "0x02E0000000000065",
#     "zarya": "0x02E0000000000068",
#     "soldier76": "0x02E000000000006E",
#     "lucio": "0x02E0000000000079",
#     "dva": "0x02E000000000007A",
#     "mei": "0x02E00000000000DD",
#     "ana": "0x02E000000000013B",
#     "sombra": "0x02E000000000012E",
#     "orisa": "0x02E000000000013E",
#     "doomfist": "0x02E000000000012F"
# }
# data_category_ids= {
#     "games_won": "0x0860000000000039",
#     "multikill_best" : "0x0860000000000346",
#     "eliminations_per_life" : "0x08600000000003D2",
#     "weapon_accuracy" : "0x086000000000002F",
#     "time_played" : "0x0860000000000021"}
#
#
#
#
# def calculate_hero(soup):
#
#     complete_hero_data = {}
#     for key, value  in data_category_ids.items():
#         category = soup.find('div', attrs={'data-category-id': 'overwatch.guid.' + value})
#
#         data =_player_hero(category,mode = key)
#         complete_hero_data[key] = data
#
#
#     return complete_hero_data
#
# def _player_hero(category, mode):
#
#     hero_data = {}
#
#     for key, value in hero_data_div_ids.items():
#         hero_div = category.find('div', attrs={'data-hero-guid': value})
#         titl = hero_div.find('div', attrs={'class': "title"}).text
#
#         desc = None
#         if mode == "games_won" or mode == "multikill_best":
#             desc = int(hero_div.find('div', attrs={'class': "description"}).text)
#
#         elif mode =="eliminations_per_life":
#             desc = float(hero_div.find('div', attrs={'class': "description"}).text)
#
#         elif mode == "weapon_accuracy":
#             desc = int(hero_div.find('div', attrs={'class': "description"}).text[:-1])
#
#         elif mode == "time_played":
#             split = hero_div.find('div', attrs={'class': "description"}).text.split()
#             try:
#                 if split[1] == "hours":
#
#                     desc = int(split[0])
#
#                 elif split[1] == "hour":
#
#                     desc = 1
#
#                 elif split[1] == "minutes":
#
#                     if int(split[0]) >= 30:
#                         desc = 1
#                     else:
#                         desc = 0
#                 else:
#                     desc = 0
#             except IndexError:
#                 desc = 0
#                 #
#         else:
#             desc = hero_div.find('div', attrs={'class': "description"}).text
#         hero_data[titl] = desc;
#
#     return hero_data
#
#
#
#
#
