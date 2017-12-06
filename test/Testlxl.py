# from lxml import html
# import requests
#
# def main():
#     page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
#     tree = html.fromstring(page.content)
#     # This will create a list of buyers:
#     buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#     # This will create a list of prices
#     prices = tree.xpath('//span[@class="item-price"]/text()')
#     print('Buyers: ', buyers)
#     print('Prices: ', prices)
#
#
#
# if __name__ == '__main__':
#     main()
#
#
