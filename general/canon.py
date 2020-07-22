#dependencies and librabries to help make it easy to scrap the web for informations
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


#assigning the url to this
ebay_auction_url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=canon+6d+mark+ii&_sacat=0&rt=nc&LH_Auction=1'
#ebay_url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1312.R1.TR0.TRC1.A0.H0.Xcanon.TRS4&_nkw=canon+6d+mark+ii&_sacat=0'
#bestbuy_url = 'https://www.bestbuy.com/site/searchpage.jsp?st=canon+6d+mark+ii&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys'
#amazon_url = 'https://www.amazon.com/s?k=canon+eos+6d+mark+ii&ref=nb_sb_noss_1'



#opening up the connection and getting all the necessary information from the webpage
uClient_one = uReq(ebay_auction_url)
#uClient_two = uReq(ebay_url)
#uClient_three = uReq(bestbuy_url)
#uClient_four = uReq(amazon)


#read the information on the webpage
ebay_auction_html = uClient_one.read()
#ebay_html = uClient_two.read()
#bestbuy_html = uClient_three.read()
#amazon_html = uClient_four.read()

#close the connection
uClient_one.close()
#uClient_two.close()
#uClient_three.close()
#uClient_four.close()

#parsing informations
ebay_auction_page = soup(ebay_auction_html, "html.parser")
#ebay_page = soup(ebay_html, "html.parser")
#bestbuy_page = soup(bestbuy_html, "html.parser")
#amazon_page = soup(amazon, "html.parser")


#printing how many items are here
ebay_auction_products = ebay_auction_page.findAll("div", {"class": "s-item__wrapper clearfix" })
print(len(ebay_auction_products))

#ebay_products = ebay_page.findAll("div", {"class" : "s-item__wrapper clearfix"})
#print(len(ebay_products))



product = ebay_auction_products[0]
print("\nProduct Name: " + product.div.img["alt"]) #name of the products

#subclass title of the product
product_sub_title = product.findAll("div", {"class": "s-item__subtitle"})
print("Subtitle: " + product_sub_title[0].text)

#price of the products now
price_of_product = product.findAll("span", {"class" : "s-item__price"})
print("Price: " + price_of_product[0].text)

rating = product.findAll("div", {"class": "s-item__reviews"})
print("Ratings: " + rating[0].text)

bids_now  = product.findAll("span", {"class": "s-item__bids s-item__bidCount"})
for i in range(len(bids_now)):
    print("Bids Count: " + bids_now[i].text)

#how many days left for the bid to be done
days_left = product.findAll("span" , {"class" : "s-item__time-left"})

for j in range(len(days_left)):
    print("Days Left For Bids to End: " +  days_left[j].text)

date = product.findAll("span", {"class": "s-item__time-end"})
for h in range(len(date)):
    print("Day and Day for the Auction to End: " + date[h].text)


shipping_cost = product.findAll("span", {"class": "s-item__shipping s-item__logisticsCost"})
print("Shipping Cost: " + shipping_cost[0].text)




#Going through the products to print out all the options
for product in ebay_auction_products:



    product_name = product.div.img["alt"] #name of the products
    print("\n")
    #print(product)
    print(product_name)

    #subclass title of the product
    product_sub_title = product.findAll("div", {"class": "s-item__subtitle"})
    subtitle = product_sub_title[0].text
    print(subtitle)

    #rating
    #ratings = product.findAll("div", {"class": "s-item__reviews"})
    #rating = ratings[0].text.strip()
    #print(rating)

    #price of the products now
    price_of_product = product.findAll("span", {"class" : "s-item__price"})
    price = price_of_product[0].text.strip()
    print(price)

    bids_now  = product.findAll("span", {"class": "s-item__bids s-item__bidCount"})
    print(bids_now[0].text)


    #how many days left for the bid to be done
    days_left = product.findAll("span" , {"class" : "s-item__time-left"})
    days = days_left[0].text
    print(days)

    #shipping cost
    shipping_cost = product.findAll("span", {"class": "s-item__shipping s-item__logisticsCost"})
    shipping = shipping_cost[0].text
    print(shipping)
