def test_get_flasktemplate():
    import requests

    ENDPOINT = 'http://127.0.0.1:8000/flasktemplate'
    response = requests.get(url=ENDPOINT)

    assert response.text == "get: url configured correctly kwargs: {}"

def test_post_flasktemplate():
    import requests

    ENDPOINT = 'http://127.0.0.1:8000/flasktemplate'
    headers = {'Content-Type': 'application/json'}
    data = {"id": 1, "request": "test_requests"}

    response = requests.post(url=ENDPOINT, json=data)

    assert response.text == str(data)
