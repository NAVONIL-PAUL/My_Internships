from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.flipkart.com/search?q=iphone&otracker=start&as-show=on&as=off'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")


containers = page_soup.findAll("div", {"class": "_13oc-S"})
print(len(containers))

print(soup.prettify(containers[0]))

container = containers[0]
print(container.div.img["alt"])
#col col-5-12 nlI3QM
price = container.findAll("div", {"class": "col col-5-12 nlI3QM"})
print(price[0].text)

ratings = container.findAll("div", {"class": "gUuXy-"})
print(ratings[0].text)

filename="products.csv"
f=open(filename,"w")

headers="Product_Name,Pricing,Ratings\n"
f.write(headers)

for container in containers:
    product_name = container.div.img["alt"]

    price_container =  container.findAll("div", {"class": "col col-5-12 nlI3QM"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("div", {"class": "gUuXy-"})
    rating = rating_container[0].text

    print("product_name:" + product_name)
    print("price:" + price)
    print("ratings:" + rating)

    #string parsing
    trim_price = ''.join(price.split(','))
    rm_rupee = trim_price.split("â‚¹")
    add_rs_price = "Rs." + rm_rupee[1]
    split_price = add_rs_price.split('E')
    final_price = split_price[0]

    split_rating = rating.split(" ")
    final_rating = split_rating[0]

    print(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n")
    f.write(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n")

f.close()


