#
#
# import requests
# from bs4 import BeautifulSoup
# import csv
#
# # Amazon India URL to scrape
# url = 'https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar'
#
# # Send a GET request to the URL and get the response
# while True:
#     response = requests.get(url)
#     if response:
#         break
#
# # Parse the response using Beautiful Soup
# soup = BeautifulSoup(response.content, 'html.parser')
#
# # Find all product items on the page
# product_items = soup.find_all('div', {'class': 'sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20'})
#
# # Create a CSV file to store the product details
# # with open('amazon_products.csv', mode='w', newline='', encoding='utf-8') as csv_file:
#     # Create a CSV writer object
#     # writer = csv.writer(csv_file)
#
#     # Write the header row
#     # writer.writerow(['Product Name', 'Price', 'Rating', 'Seller Name'])
#
#     # Loop through each product item and extract the details
# for item in product_items:
#     # Get the product name
#     product_name = item.find('span', {'class': "a-size-base-plus a-color-base a-text-normal"}).text.split("|")[0]
#     print(product_name)
#
#     # Get the product price
#     product_price = item.find('span', {'class': 'a-offscreen'})
#     if product_price:
#         product_price = product_price.text.strip()
#         # print("price",product_price)
#     else:
#         continue
#
#     # Get the product rating
#     product_rating = item.find('span', {'class': 'a-icon-alt'})
#     if product_rating:
#         product_rating = product_rating.text.strip()
#     else:
#         product_rating = 'No rating'
#     # Get the product seller name from the following link generated from within this page.
#     name_find= item.find('a',{'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
#     link = "https://www.amazon.in"+name_find['href']
#     ress = requests.get(link)
#     soup1 = BeautifulSoup(ress.content, 'html.parser')
#     in_stock = soup1.find('div',{'id':'availability'})
#     seller_name = ""
#     if in_stock:
#         if in_stock.text.strip()=="In stock":
#             seller_name = soup1.find('div',{'id':'merchant-info'}).text.strip()
#         else:
#             seller_name = "not available"
#
#     # Write the product details to the CSV file
#     # writer.writerow([product_name, product_price, product_rating, seller_name])
#
#
# import os
# # Function to rename multiple files
# def main():
# 	i = 1
# 	path="D:/PYTHON_PROJECTS/ecs_objectdetection/TFODCourse/Tensorflow/workspace/images/collectedimages/colgate/"
# 	for filename in os.listdir(path):
# 		my_dest ="colgate" + str(i) + ".jpg"
# 		my_source =path + filename
# 		my_dest =path + my_dest
# 		# rename() function will
# 		# rename all the files
# 		os.rename(my_source, my_dest)
# 		i += 1
# # Driver Code
# if __name__ == '__main__':
# 	# Calling main() function
# 	main()
#
#
# from requests impo
# import json
#
# # Define the data to send
# data = {
#     "name": "pepsi",
#     "price": 35
# }
# json_data = json.dumps(data)
#
# # Define the API endpoint URL
# url = "http://115.244.41.195:3000/products"
#
# # Define the headers for the HTTP request
# headers = {
#     "Content-Type": "application/json"
# }
#
# # Make the HTTP request
# # response = requests.post(url, data=json_data, headers=headers)
# res = requests.get(url)
# # Print the response
# print(res.text)

import json
from prettytable import PrettyTable
data = {"documents":[{"name":"jimjam","price":45},{"name":"pepsi","price":35}]}
# print(data)
# dict = json.loads(data[0])
data = data["documents"]
print(data)
header = ["name","price"]
mytable = PrettyTable(header)
Total = 0
for data in data:
    header = []
    values = []

    for key in data:
        head = key
        value = ""
        print(head)
        if type(data[key])==type({}):
            for key2 in data[key]:
                head +="/"+key2
                value = data[key][key2]
                header.append(head)
                values.append(value)
        else:
            value = data[key]
            header.append(head)
            values.append(value)
        if key=="price":
            Total += value
    mytable.add_row(values)
mytable.add_row(["Total",Total])
print(mytable)


