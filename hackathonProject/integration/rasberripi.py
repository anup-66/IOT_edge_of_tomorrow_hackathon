import requests
import json

data_send1 ={
    "collection":"products",
    "database":"test",
    "dataSource":"Cluster0",
    "document":{
      "id":0.0,
    "name": "pepsi",
    "price": 35}

}

data_send2 ={
    "collection":"products",
    "database":"test",
    "dataSource":"Cluster0",
    "document":{
      "id":1.0,
    "name": "jimjam",
    "price": 45}
}

data_send3 ={
    "collection":"products",
    "database":"test",
    "dataSource":"Cluster0",
    "document":{
      "id":2.0,
    "name": "facewash",
    "price": 60}
}
json_data1 = json.dumps(data_send1)
json_data2 = json.dumps(data_send2)
json_data3= json.dumps(data_send3)


url = "https://ap-south-1.aws.data.mongodb-api.com/app/data-flqkg/endpoint/data/v1/action/insertOne"
headers = {
    "Content-Type": "application/json",
    "Access-Control-Request-Headers":"*",
    "api-key" : "dUg8fYThs52SJYFtj4K2sJv0SpXoPjLgGiZo0MW8s42QdQKMnr5RclK5XCacPMZI",
    "Accept": "application/json"
}
class Send:
    def send_data_database(self,id):
        if id==0.0:
            response = requests.post(url, data=json_data1, headers=headers)
        elif id==1.0:
            response = requests.post(url, data=json_data2, headers=headers)
        elif id==2.0:
            response = requests.post(url, data=json_data3, headers=headers)
        print(response.text)
if __name__=="__main__":
    val = Send()
    value = val.send_data_database(0.0)