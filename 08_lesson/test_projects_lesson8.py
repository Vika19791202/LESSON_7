import uuid
import pytest


def test_post_create_project_positive(api_client):
    unique_name = f"Test Project {uuid.uuid4()}"
    resp = api_client.create_project(unique_name)
    assert resp.status_code == 201, f"Ожидался 201, получен {resp.status_code}: {resp.text}"
    project_id = resp.json()["id"]
    get_resp = api_client.get_project(project_id)
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == unique_name


def test_post_create_project_negative_empty_name(api_client):
    resp = api_client.create_project("")
    assert resp.status_code in (400, 422), f"Ожидался 400/422, получен {resp.status_code}"
    assert "title should not be empty" in resp.text or "title must be a string" in resp.text


def test_get_project_positive(api_client):
    create_resp = api_client.create_project(f"Temp Project {uuid.uuid4()}")
    assert create_resp.status_code == 201
    project_id = create_resp.json()["id"]
    get_resp = api_client.get_project(project_id)
    assert get_resp.status_code == 200
    assert get_resp.json()["id"] == project_id


def test_get_project_negative_invalid_id(api_client):
    resp = api_client.get_project("invalid-id-123")
    assert resp.status_code == 404


def test_put_update_project_positive(api_client):
    create_resp = api_client.create_project(f"Original {uuid.uuid4()}")
    assert create_resp.status_code == 201
    project_id = create_resp.json()["id"]
    new_name = f"Updated {uuid.uuid4()}"
    update_resp = api_client.update_project(project_id, name=new_name)
    assert update_resp.status_code == 200
    get_resp = api_client.get_project(project_id)
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == new_name


def test_put_update_project_negative_invalid_id(api_client):
    resp = api_client.update_project("invalid-id-123", name="New Name")
    assert resp.status_code == 404
