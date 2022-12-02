from users.serializers import UserSerializer
import pytest
from users.models import User
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


class TestEndpoints:

    def test_register_success(self):
        client = APIClient()
        response = client.post("/auth/register/", 
                        {
                            "username": "remarema",
                            "email": "asdfadfsd@gmail.com",
                            "password": "ldifuhtrl23!",
                            "password1": "ldifuhtrl23!"
                        })
        assert response.status_code == 201

    def test_register_username_missing(self, auth_client):
        client = APIClient()
        payload = dict(
            email="remarema@email.com",
            password="remaremaF!",
            password1="remaremaF!"
        )
        response = client.post("/auth/register/", payload)
        data = response.data
        assert response.status_code == 400
        assert "username" in data

    def test_register_email_missing(self, auth_client):
        client = APIClient()
        payload = dict(
            username="remarema",
            password="remaremaF!",
            password1="remaremaF!"
        )
        response = client.post("/auth/register/", payload)
        data = response.data
        assert response.status_code == 400
        assert "email" in data

    def test_register_password_missing(self, auth_client):
        client = APIClient()
        payload = dict(
            username="remarema",
            email="remarema@email.com",
            password1="remaremaF!"
        )
        response = client.post("/auth/register/", payload)
        data = response.data
        assert response.status_code == 400
        assert "password" in data

    def test_register_password1_missing(self, auth_client):
        client = APIClient()
        payload = dict(
            username="remarema",
            email="remarema@email.com",
            password="remaremaF!",
        )
        response = client.post("/auth/register/", payload)
        data = response.data
        assert response.status_code == 400
        assert "password1" in data

    def test_register_passwords_not_match(self, auth_client):
        client = APIClient()
        payload = dict(
            username="qwerqwer",
            email="qwerqwer@gmail.com",
            password="reamream1!",
            password1="reamream1!!"
        )
        response = client.post("/auth/register/", payload)
        assert response.status_code == 400

    def test_register_common_password(self, auth_client):
        client = APIClient()
        payload = dict(
            username="asdfasdff",
            email="asdfasdfdf@gmail.com",
            password="123456789",
            password1="123456789"
        )
        response = client.post("/auth/register/", payload)
        assert response.status_code == 400

    def test_register_invalid_mail(self, auth_client):
        client = APIClient()
        payload = dict(
            username="asdfasdfsdf",
            email="asdfjjsdfiosdif",
            password="asdfasdfF!",
            password1="asdfasdfF!"
        )
        response = client.post("/auth/register/", payload)
        assert response.status_code == 400

    def test_register_uniqe_username(self, auth_client):
        client = APIClient()
        payload = dict(
            username="asdfasdf",  # same as the user used in auth client
            email="asdfmdlk@gmail.com",
            password="asdfasdf!1",
            password1="asdfasdf1!"
        )
        response = client.post("/auth/register/", payload)
        assert response.status_code == 400

    def test_register_unique_email(self, auth_client):
        client = APIClient()
        payload = dict(
            username="asdfsdfasdfsd",  # same as the user used in auth client
            email="asdfasdf@gmail.com",
            password="asdfasdf!1",
            password1="asdfasdf1!"
        )
        response = client.post("/auth/register/", payload)
        assert response.status_code == 400

    def test_login_success(self, user, auth_client):
        client = APIClient()
        payload = {
            "username": "asdfasdf",
            "password": "asdfasdF1!"
        }
        response = client.post("/auth/login/", payload)
        assert response.status_code == 202
        data = response.data
        assert "token" in data
        assert "user" in data
        assert data['user']['username'] == user.username

    def test_login_fail(self, auth_client):
        client = APIClient()
        payload = {
            "username": "remarema",
            "password": "ldifuhtrl23"
        }
        response = client.post("/auth/login/", payload)
        assert response.status_code == 400

    def test_logout_user(self, auth_client):
        client , id = auth_client()
        response = client.post('/auth/logout/')

        assert response.status_code == 204

    def test_logout_user_unauthenticated(self, client):
        response = client.post('/auth/logout/')

        assert response.status_code == 401
