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



        print(self.SUPPORT)
        # print(self.OBJECTIVE)
        print(self.ATTACK)
        #print(self.stat['competitive']['Combat']['Barrier Damage Done'])
        return 10;

    async def _calculate_support(self, mode = "competitive"):
        combat = ["Hero Damage Done", "Barrier Damage Done", "Eliminations", "Deaths", "Objective Kills"]
        assists = ["Defensive Assists" , "Healing Done" ,"Offensive Assists"]


        t = 0
        s = self.stat
        hoursT = s[mode]['Game']['Time Played'].split(' ')

        h = int(hoursT[0]) * 60



        for w in combat:
            # print(w)
            # print(_get_int(s[mode]['Combat'][w]) / h  * get_multiplier(w, "support_mp"))
            t += _get_int(s[mode]['Combat'][w]) / h * get_multiplier(w,"support_mp")

        for w in assists:
            # print(w)
            # print(_get_int(s[mode]['Assists'][w]) / h * get_multiplier(w, "assists_mp"))
            t += _get_int(s[mode]['Assists'][w]) / h * get_multiplier(w, "assists_mp")

        if mode == 'quickplay':
            self.SUPPORT+= int(t / 2)

        else:
            self.SUPPORT+= int(t)



    async def _calculate_objective(self, mode = "competitive"):

        combat = ["Hero Damage Done", "Barrier Damage Done", "Eliminations", "Deaths", "Objective Kills"]


        t = 0
        s = self.stat
        hoursT = s[mode]['Game']['Time Played'].split(' ')

        h = int(hoursT[0]) * 60

        for w in combat:
            # print(w)
            # print(_get_int(s[mode]['Combat'][w]) / h  * get_multiplier(w, "support_mp"))
            t += _get_int(s[mode]['Combat'][w]) / h * get_multiplier(w, "objective_mp")

        # for w in assists:
        #     # print(w)
        #     # print(_get_int(s[mode]['Assists'][w]) / h * get_multiplier(w, "assists_mp"))
        #     t += _get_int(s[mode]['Assists'][w]) / h * get_multiplier(w, "assists_mp")

        if mode == 'quickplay':
            self.OBJECTIVE += int(t / 2)

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



        # t +=  _get_int(s[mode]['Average']['Barrier Damage Done - Avg per 10 Min']) * 1
        # t += _get_int(s[mode]['Average']['Eliminations - Avg per 10 Min']) * 1
        # t += _get_int(s[mode]['Average']['Final Blows - Avg per 10 Min']) * 1
        # t += _get_int(s[mode]['Average']['Solo Kills - Avg per 10 Min']) * 1
        # t += _get_int(s[mode]['Average']['Hero Damage Done - Avg per 10 Min']) * 1



        for w in combat:

            # print(w)
            # print(_get_int(s[mode]['Combat'][w]) / h  * get_multiplier(w))


            t+= _get_int(s[mode]['Combat'][w]) / h * get_multiplier(w, "combat_mp")


        if mode == 'quickplay':
            self.ATTACK += int(t / 2)

        else:
            self.ATTACK += int(t)




    def lazy_range(up_to):
        """Generator to return the sequence of integers from 0 to up_to, exclusive."""
        index = 0
        while index < up_to:
            yield index
            index += 1


def get_multiplier(stat, dict):

    combat_mp = {"Hero Damage Done" : 0.1,"Final Blows" : 25, "Multikills" : 1000, "All Damage Done" : 0.04, "Barrier Damage Done" : 0.09, "Eliminations" : 35 ,"Solo Kills" : 120}
    support_mp = {"Hero Damage Done" : 0.5, "Barrier Damage Done": 0.15, "Eliminations" : 25, "Deaths": -80, "Objective Kills": 80}
    assists_mp = {"Defensive Assists" : 65 , "Healing Done" : 0.4 , "Offensive Assists" : 65}

    if dict == "combat_mp":
        return combat_mp[stat]

    elif dict == "support_mp":
        return support_mp[stat]

    elif dict == "assists_mp":
        return assists_mp[stat]

    else:
        return 1



def _get_int(c):
    return int(c.replace(",", ""))


def main():
    c = Calculated("s")
    c.calculate()


if __name__ == '__main__':
    main()
