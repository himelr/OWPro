import asyncio

class Calculated:


    def __init__(self,stat):
        self.stat = stat
        self.SUPPORT = 0
        self.ATTACK = 0
        self.DEFENSE = 0


    def calculate(self):

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        calculations=[
            asyncio.ensure_future(self._calculate_attack()),
            asyncio.ensure_future(self._calculate_support()),
            asyncio.ensure_future(self._calculate_defense()),
            asyncio.ensure_future(self._calculate_attack('quickplay')),
            asyncio.ensure_future(self._calculate_support('quickplay')),
            asyncio.ensure_future(self._calculate_defense('quickplay'))
        ]
        loop.run_until_complete(asyncio.wait(calculations))
        loop.close()



        print(self.SUPPORT)
        print(self.DEFENSE)
        print(self.ATTACK)
        print(self.stat['competitive']['Combat']['Barrier Damage Done'])
        return 10;

    async def _calculate_support(self, mode = "competitive"):


       self.SUPPORT += 5
       print()

    async def _calculate_defense(self, mode = "competitive"):
       self.DEFENSE += 3

    async def _calculate_attack(self, mode = "competitive"):

        self.ATTACK += 2

    def lazy_range(up_to):
        """Generator to return the sequence of integers from 0 to up_to, exclusive."""
        index = 0
        while index < up_to:
            yield index
            index += 1

def main():
    c = Calculated("s")
    c.calculate()


if __name__ == '__main__':
    main()
