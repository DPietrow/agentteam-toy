import pytest

from toyapp.app import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}


def test_notes_start_empty(client):
    assert client.get("/notes").get_json() == []


def test_create_and_list_note(client):
    res = client.post("/notes", json={"text": "  buy milk "})
    assert res.status_code == 201
    assert res.get_json() == {"id": 1, "text": "buy milk"}
    assert client.get("/notes").get_json() == [{"id": 1, "text": "buy milk"}]


@pytest.mark.parametrize("body", [{}, {"text": ""}, {"text": "   "}, {"text": 5}])
def test_create_note_rejects_bad_input(client, body):
    res = client.post("/notes", json=body)
    assert res.status_code == 400
    assert "error" in res.get_json()
