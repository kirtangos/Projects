import requests

USERNAME="gosaliakirtan8904"
TOKEN="Enter your tokenid"
GRAPH_ID="graph999"

pixela_endpoint="https://pixe.la/v1/users"

user_params = {
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
    "name":"Water Conusmption",
    "unit":"Litre",
    "type":"float",
    "color":"ajisai"
}

headers={
    "X-USER-TOKEN":TOKEN
}
# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

pixel_creation=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data={
    "date":"20250118",
    "quantity":"5",
}

response=requests.post(url=pixel_creation,json=pixel_data,headers=headers)
print(response.text)