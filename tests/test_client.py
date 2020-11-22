import pytest

from src.server import app


@pytest.fixture
def test_client():
    with app.test_client() as client:
        yield client


@pytest.mark.parametrize('url', ['/', '/quick'])
def test_calculation(test_client, url):
    res = test_client.get(url)
    assert res.status_code == 405
    res = test_client.post(url)
    assert res.status_code == 400
    res = test_client.post(url, json={"a": "b"})
    assert res.status_code == 400
    res = test_client.post(url, json={"chessPiece": "queen", "n": 9})
    assert res.status_code == 400
    res = test_client.post(url, json={"chessPiece": "queen2", "n": 6})
    assert res.status_code == 400
    res = test_client.post(url, json={"n": 6})
    assert res.status_code == 400
    res = test_client.post(url, json={"chessPiece": "rook", "n": 6})
    assert res.status_code == 200
    assert res.json == {'solutionsCount': 720}
