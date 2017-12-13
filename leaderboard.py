import asyncio


class Calculated:


    def __init__(self,stat):

        self.stat = stat
        self.SUPPORT = 0
        self.ATTACK = 0
        self.OBJECTIVE = 0


    def calculate(self):

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        calculations=[
            asyncio.ensure_future(self._calculate_attack()),
            asyncio.ensure_future(self._calculate_support()),
            asyncio.ensure_future(self._calculate_objective()),
            asyncio.ensure_future(self._calculate_attack('quickplay')),
            asyncio.ensure_future(self._calculate_support('quickplay')),
            asyncio.ensure_future(self._calculate_objective('quickplay'))
        ]
        loop.run_until_complete(asyncio.wait(calculations))
        loop.close()

        print("Objective "+ str(self.OBJECTIVE)+ " Support " + str(self.SUPPORT) + " Attack " + str(self.ATTACK))

        score = {}
        score["objective"] = self.OBJECTIVE
        score["support"] = self.SUPPORT
        score["attack"] = self.ATTACK


        return score

    async def _calculate_support(self, mode = "competitive"):
        combat = ["Hero Damage Done", "Barrier Damage Done", "Eliminations", "Deaths", "Objective Kills"]
        assists = ["Defensive Assists" , "Healing Done" ,"Offensive Assists"]



        t = 0
        s = self.stat
        hoursT = s[mode]['Game']['Time Played'].split(' ')

        h = int(hoursT[0]) * 60



        for w in combat:

            try:

                t += _get_int(s[mode]['Combat'][w]) / h * get_multiplier(w,"support_mp")
            except KeyError:
                t+=0
        for w in assists:

            try:

                t += _get_int(s[mode]['Assists'][w]) / h * get_multiplier(w, "assists_mp")
            except KeyError:
                t+=0
        if mode == 'quickplay':
            self.SUPPORT+= int(t / 3.5)

        else:
            self.SUPPORT+= int(t)



    async def _calculate_objective(self, mode = "competitive"):

        combat = ["Hero Damage Done", "Barrier Damage Done", "Eliminations", "Deaths", "Objective Kills"]
        awards = ["Medals - Bronze", "Medals - Gold", "Medals - Silver"]

        def _get_sec(time_str):

            try:
                h, m, s = time_str.split(':')
                return int(h) * 3600 + int(m) * 60 + int(s)

            except ValueError:

                try:
                    m, s = time_str.split(':')
                    return int(m) * 60 + int(s)

                except ValueError:

                    return 0;



        t = 0
        s = self.stat
        hoursT = s[mode]['Game']['Time Played'].split(' ')

        h = int(hoursT[0]) * 60

        for w in combat:

            try:
                t += _get_int(s[mode]['Combat'][w]) / h * get_multiplier(w, "support_mp2")  * 0.7

            except KeyError:

                t+= 0


        for a in awards:

            try:
                t += _get_int(s[mode]['Match Awards'][a]) / h * get_multiplier(a, "awards_mp")
            except KeyError:
                t+=0


        objective_time = _get_sec(s[mode]['Combat']["Objective Time"]) / h * 50

        t += objective_time

        if mode == 'quickplay':
            self.OBJECTIVE += int(t / 3.5)

        else:
            self.OBJECTIVE += int(t)


    async def _calculate_attack(self, mode = "competitive"):



        combat = ["Hero Damage Done","Final Blows", "Multikills",
                  "All Damage Done", "Barrier Damage Done",
                  "Eliminations" , "Solo Kills"]



        t = 0
        s = self.stat
        hoursT = s[mode]['Game']['Time Played'].split(' ')
        h = int(hoursT[0]) * 60


        for w in combat:

            try:

                t+= _get_int(s[mode]['Combat'][w]) / h * get_multiplier(w, "combat_mp")
            except KeyError:
                t+=0;


        if mode == 'quickplay':
            self.ATTACK += int(t / 3.5)

        else:
            self.ATTACK += int(t)

    def lazy_range(up_to):

        index = 0
        while index < up_to:
            yield index
            index += 1


def get_multiplier(stat, dict):

    combat_mp = {"Hero Damage Done" : 0.20,"Final Blows" : 25, "Multikills" : 3000, "All Damage Done" : 0.08, "Barrier Damage Done" : 0.30, "Eliminations" : 100 ,"Solo Kills" : 150}
    support_mp = {"Hero Damage Done" : 0.15, "Barrier Damage Done": 0.15, "Eliminations" : 25, "Deaths": -130, "Objective Kills": 80}
    support_mp2 = {"Hero Damage Done": 0.5, "Barrier Damage Done": 0.20, "Eliminations": 25, "Deaths": -100,"Objective Kills": 100}
    assists_mp = {"Defensive Assists" : 87 , "Healing Done" : 0.55 , "Offensive Assists" : 87}
    awards_mp = {"Medals - Bronze" : 200, "Medals - Gold" : 600, "Medals - Silver" : 400}

    if dict == "combat_mp":
        return combat_mp[stat]

    elif dict == "support_mp":
        return support_mp[stat]

    elif dict == "support_mp2":
        return support_mp2[stat]

    elif dict == "assists_mp":
        return assists_mp[stat]

    elif dict == "awards_mp":
        return awards_mp[stat]

    else:
        return 1



def _get_int(c):
    return int(c.replace(",", ""))


def main():
    c = Calculated("s")
    c.calculate()


if __name__ == '__main__':
    main()
