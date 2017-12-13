from lxml import html
import requests

def main():
    page = requests.get(' https://www.nettiauto.com/vaihtoautot?pfrom=3000&pto=7000')
    tree = html.fromstring(page.content)
    # This will create a list of buyers:





    buyers = tree.xpath('//*[@id="listingData"]/div[3]/div/div[2]/div[2]/div[1]/div[1]/text()')
    # # This will create a list of prices
    # prices = tree.xpath('//span[@class="item-price"]/text()')
    # losses = int(misc_box.xpath(".//text()[. = 'Games Lost']/../..")[0][1].text
    #              .replace(",", ""))




    print(buyers)
    # stat_groups = tree.xpath(
    #         ".//div[@id='competitive']"
    #         "//div[@data-group-id='stats' and @data-category-id='0x02E00000FFFFFFFF']"
    #     )[0]
    #
    # game_box = stat_groups[6]
    # g = game_box.xpath(".//text()[. = 'Games Played']/../..")
    # #wins = int(game_box.xpath(".//text()[. = 'Games Won']/../..")[0][1].text.replace(",", ""))
    #
    # misc_box = stat_groups[7]
    # losses = int(misc_box.xpath(".//text()[. = 'Games Lost']/../..")[0][1].text
    #              .replace(",", ""))
    #
    # print(losses)
    # print(stat_groups)
    # print(game_box)
    # print(g)


if __name__ == '__main__':
    main()


