from woocommerce import API
from urlparse import urlparse, parse_qs
from random import randint
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

wcapi = API(
    url=config['WC']['url'],
    consumer_key=config['WC']['key'],
    consumer_secret=config['WC']['secret']
)

# request first product page
r = wcapi.get('products')

# figure out how many pages there are total
last_url = r.links['last']['url']
url_object = urlparse(last_url)
queries = parse_qs(url_object.query)
page_count = queries['page'][0]  # was a string, need to convert to int

# pick a random page number to pull up and get those 10 products
page = randint(1, int(page_count))
r = wcapi.get('products?page=' + str(page)).json()

# choose one of the 10 products in the list of products and return its url
product_number = randint(0, 9)
url = r['products'][product_number]['permalink']
print url
