import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USER_PARAMS = {
    "token": "Google@2018",
    "username": "vicmanuelr",
    "agreeTermsOfService": "Yes",
    "notMinor": "Yes",
}
HEADER ={
    "X-USER-TOKEN": "Google@2018"
}

requests.post(url=PIXELA_ENDPOINT, params=USER_PARAMS)