import requests 
import datetime

TOKEN="jwiwiwoaoooppc92930"
USERNAME="pooja1474"
GRAPH_ID="graphstudy"
pixela_endpoint="https://pixe.la/v1/users"

user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",

}

# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config={
    "id":GRAPH_ID,
    "name":"Study Graph",
    "unit":"minutes",
    "type":"int",
    "color":"ajisai",
}
headers={
    "X-USER-TOKEN":TOKEN
}

# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)


pixel_endpoint=f"{graph_endpoint}/{GRAPH_ID}"
yesterday=datetime.datetime(year=2024,month=7,day=3)

today=datetime.datetime.now().strftime("%Y%m%d")

print(today)
pixel_config={
    "date":today,
    "quantity":input("How many minutescd .. did you study today? ")
}
response=requests.post(url=pixel_endpoint,json=pixel_config,headers=headers)
print(response.text)





# update_config={
#     "quantity":"10",
# }

up_del_endpoint=f"{pixel_endpoint}/{today}"

# response=requests.put(url=update_endpoint,json=update_config,headers=headers)
# print(response.text)

# response=requests.delete(url=up_del_endpoint,headers=headers)
# print(response.text)