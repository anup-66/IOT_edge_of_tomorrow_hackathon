import requests
import json

datap = {
    "collection": "products",
    "database": "test",
    "dataSource": "Cluster0",
    "projection": {"_id": 0, "name": 1, "price": 2}
}
data_delete = {
    "collection": "products",
    "database": "test",
    "dataSource": "Cluster0",
    "filter": {}
}
json_datap = json.dumps(datap)
json_data_delete = json.dumps(data_delete)
url_get = "https://ap-south-1.aws.data.mongodb-api.com/app/data-flqkg/endpoint/data/v1/action/find"
url_delete = "https://ap-south-1.aws.data.mongodb-api.com/app/data-flqkg/endpoint/data/v1/action/deleteMany"

# Define the headers for the HTTP request
headers = {
    "Content-Type": "application/json",
    "Access-Control-Request-Headers": "*",
    "api-key": "dUg8fYThs52SJYFtj4K2sJv0SpXoPjLgGiZo0MW8s42QdQKMnr5RclK5XCacPMZI",
    "Accept": "application/json"
}
key = "dUg8fYThs52SJYFtj4K2sJv0SpXoPjLgGiZo0MW8s42QdQKMnr5RclK5XCacPMZI"

# Make the HTTP request

import json
from prettytable import PrettyTable


class request:
    def get_data(self):
        response = requests.post(url_get, data=json_datap, headers=headers)
        response2 = requests.post(url_delete,data = json_data_delete,headers = headers)
        print(response.json())
        print(response2.text)
        data = response.json()["documents"]
        print(data)
        headerq = ["name", "price"]
        mytable = PrettyTable(headerq)
        Total = 0
        # Dict = {}
        # for data in data:
        #     for val in data.keys():
        #         if val in Dict.keys():
        #             if Dict and Dict[val] in Dict.values() and val=="price":
        #                 Dict[val]+=data[val]
        #             else:
        #                 Dict[val] =
        #         else:
        #             Dict[val] = data[val]
        # print(Dict,"huhuhuhu")
        for data in data:
            header = []
            values = []

            for key in data:
                head = key
                value = ""
                value = data[key]
                header.append(head)
                values.append(value)
                if key == "price":
                    Total += value

            mytable.add_row(values)
        mytable.add_row(["Total", Total])

        return response.json()['documents']

"""
curl --location --request POST 'https://ap-south-1.aws.data.mongodb-api.com/app/data-flqkg/endpoint/data/v1/action/findOne' \
--header 'Content-Type: application/json' \
--header 'Access-Control-Request-Headers: *' \
--header 'api-key: dUg8fYThs52SJYFtj4K2sJv0SpXoPjLgGiZo0MW8s42QdQKMnr5RclK5XCacPMZI' \
--header 'Accept: application/ejson' \
--data-raw '{
    "collection":"products",
    "database":"test",
    "dataSource":"Cluster0",
    "projection": {"_id": 1}
}'
"""
