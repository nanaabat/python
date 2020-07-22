from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


my_url = 'https://www.flipkart.com/search?q=canon+6d+mark2&sid=jek%2Cp31%2Ctrv&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&as-pos=1&as-type=RECENT&suggestionId=canon+6d+mark2%7CDSLR+Camera&requestId=6d589c2f-eaa4-4437-8467-7c1b68d576bb&as-backfill=on'
uClient = uReq(my_url) #open up the connection and graps information from the url/webpage assigned to it to load the information
page_html = uClient.read() #this command reads or damps all the information from the webpage and saves it to page_html
uClient.close()  #this is to close the connection
page_soup = soup(page_html, "html.parser") #parse the html file because the file contains a lot of information



products = page_soup.findAll("div", {"class": "_3O0U0u"})
print(len(products))


#assigning the first element of the containers to container
product = products[0]
print(product.div.img["alt"])
print(" ")


price = product.findAll("div", {"class" : "_6BWGkk"}) #price of the product
for index in range(len(price)):
    print("\n" + price[index].text)


ratings = product.findAll("div" , {"class": "niH0FQ"}) #rating of the product
print("\n" + ratings[0].text)


filename = "product.csv" #filename
f = open(filename, "w") #opening the file

headers = "Product_Name, Pricing, Rating \n"
f.write(headers) #this statement is written on the file

for product in products:
    product_name = product.div.img["alt"]

    price_of_product = product.findAll("div", {"class": "_6BWGkk"})
    price = price_of_product[0].text.strip()

    rating_of_product =product.findAll("div", {"class": "niH0FQ"})
    rating = rating_of_product[0].text


    print("\nName of Product: "+ product_name)
    print("Price: " + price)
    print("Ratings: " + rating)


    #string parsing
    trim_price = ''.join(price.split(','))
    rm_rupee = trim_price.split("₹")
    add_rs_price = "Rs." + rm_rupee[1]
    split_price = add_rs_price.split('E')
    final_price = split_price[0]


    split_rating = rating.split(" ")
    final_rating = split_rating[0]


    print("\nName of Product: " + product_name.replace(",", " |") + "\nPrice: " + final_price + "\nRating: " + final_rating + "\n")
    f.write("\nName of Product: " + product_name.replace(",", " |") + "\nPrice: " + final_price + "\nRating: " + final_rating + "\n")


f.close()


'''

container = containers[0] #assigning the first elements on the container


price = container.findAll("div", {"class": "col col-5-12 _2o7WAb"})


ratings = container.findAll("div", {"class": "niHOFQ"})

filename = "products.csv"
f = open(filename, "w")


headers = "Produce_Name, Pricing, Ratings\n"
f.write(headers)

for container in containers:
    product_name = container.div.img["alt"]
'''
