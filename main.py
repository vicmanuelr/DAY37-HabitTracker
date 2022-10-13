import requests
import os

PIXELA_HEADER ={
    "X-USER-TOKEN": os.environ.get("PASSWORD")
}
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "vicmanuelr"
PASSWORD = os.environ.get("PASSWORD")
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
CREATE_USER_PARAMS = {
    "token": PASSWORD,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
GRAPH_PARAMS = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "minutes",
    "type": "float",
    "color": "shibafu"
}


def create_user(user_parameters: dict):
    response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
    print(response.text)


# create_user(CREATE_USER_PARAMS)

def create_graph(graph_parameters: dict, auth_headers: dict):
    response = requests.post(url=GRAPH_ENDPOINT, headers=auth_headers, json=graph_parameters)
    print(response.text)


# create_graph(GRAPH_PARAMS, PIXELA_HEADER)
