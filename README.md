# WooCommerce Product Picker

This little script reaches out to your site's WC API, pulls down a random page of products, then returns the URL for one specific product. I'm using this to help me pick products to promote a product each day on social media.

## Setup & running

Install dependancies:

````
pip install -r requirements.txt
````

Set 3 environment configs for your WC site:

````
export URL='SITE_URL'
export CONSUMER_KEY='YOUR_KEY'
export CONSUMER_SECRET='YOUR_SECRET'
````

Run program:

````
python product-picker.py
````
