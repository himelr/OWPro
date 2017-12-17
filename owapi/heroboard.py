from owapi.blizzard_interface import hero_data_div_ids, data_category_ids


class HeroCalculations:

    def __init__(self):
        self.data = None
        self.count = 0
        self.half = self._halftable()

    def calculate_top(self, hero_data):
        if self.data != None:
            for key, value in data_category_ids.items():

                for hero, score in hero_data[key].items():
                    if hero_data[key][hero] != 0:
                        self.data[key][hero] += hero_data[key][hero]
                        self.half[key][hero] += 1
                    # print(hero + str(score))

        # 3+6+5
        else:
            self.data = hero_data

        self.count += 1

    def _halftable(self):
        half = {}
        for key, value in data_category_ids.items():
            sub_data = {}
            for hero, score in hero_data_div_ids.items():
                sub_data[hero] = 1
                half[key] = sub_data

        return half

    # Fixes scores to represent average.
    def fix_scores(self):
        for key, value in data_category_ids.items():
            for hero, score in self.data[key].items():
                if key == "eliminations_per_life":
                    self.data[key][hero] = round(self.data[key][hero] / self.half[key][hero], 2)
                else:
                    self.data[key][hero] = int(self.data[key][hero] / self.half[key][hero])

#
#
