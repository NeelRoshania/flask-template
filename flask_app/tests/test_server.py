def test_connection():
    import requests

    ENDPOINT = 'http://127.0.0.1:8000'
    response = requests.get(url=ENDPOINT)

    assert response.status_code is not None
