import requests
import os
import datetime as dt

PIXELA_HEADER ={
    "X-USER-TOKEN": os.environ.get("PASSWORD")
}
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "vicmanuelr"
PASSWORD = os.environ.get("PASSWORD")
GRAPH_ID = "graph1"

def create_user():
    create_user_params = {
        "token": PASSWORD,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=PIXELA_ENDPOINT, json=create_user_params)
    print(response.text)


# create_user(CREATE_USER_PARAMS)


def create_graph(auth_headers: dict):
    graph_params = {
        "id": "graph1",
        "name": "Coding Graph",
        "unit": "minutes",
        "type": "float",
        "color": "shibafu"
    }
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
    response = requests.post(url=graph_endpoint, headers=auth_headers, json=graph_params)
    print(response.text)


# create_graph(graph_params, PIXELA_HEADER)


def post_pixel(auth_headers: dict, quantity: int):
    post_pixel_params = {
        "date": dt.date.today().strftime("%Y%m%d"),
        "quantity": f"{quantity}",
    }
    post_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
    response = requests.post(url=post_endpoint, headers=auth_headers, json=post_pixel_params)
    print(response.text)


post_pixel(PIXELA_HEADER, 50)
