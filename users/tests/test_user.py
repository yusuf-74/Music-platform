import pytest
from rest_framework.test import APIClient
from users.models import User
from knox.models import AuthToken

pytestmark = pytest.mark.django_db


class TestUser():

    def test_put_method(self, auth_client):
        client, id = auth_client()
        response = client.put("/users/1/", {
            "username": "Update",
            "email": "asdfasdf@gmail.com",
            "bio": "Success"
        })
        assert response.status_code == 200
        user = User.objects.get(id=id)
        assert user.bio == "Success"
        assert user.username == "Update"
        assert user.email == "asdfasdf@gmail.com"

    def test_get_method(self, auth_client):
        client, id = auth_client()
        response = client.get("/users/1/")
        assert response.status_code == 200
        data = response.data
        user = User.objects.get(id=id)
        assert data['username'] == user.username
        assert data['email'] == user.email
        assert data['bio'] == user.bio

    def test_patch_method(self, auth_client):
        client, id = auth_client()
        response = client.patch("/users/1/", {
            "username": "updatedUserName",
        })
        assert response.status_code == 200
        user = User.objects.get(id=id)
        assert user.username == "updatedUserName"
