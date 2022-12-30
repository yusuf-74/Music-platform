import pytest
from rest_framework.test import APIClient
from users.serializers import UserSerializer
from users.models import User


@pytest.fixture
def user():
    return User.objects.create_user("asdfasdf", "asdfasdf@gmail.com", "asdfasdF1!", bio="asdfasdfasdf")


@pytest.fixture
def auth_client(user):
    def api_client(user_instance=None):
        if user_instance is None:
            client = APIClient()

            login_response = client.post(
                '/auth/login/', dict(username="asdfasdf", password="asdfasdF1!"))

            token = login_response.data["token"]

            client.credentials(HTTP_AUTHORIZATION='Token ' + token)

            return client, user.id
        else:
            client = APIClient()

            random_user = User.objects.create_user(
                user_instance['username'], user_instance['email'], user_instance['password'])

            login_response = client.post('/auth/login/', dict(
                username=user_instance["username"], password=user_instance["password"]))

            token = login_response.data["token"]

            client.credentials(HTTP_AUTHORIZATION='Token ' + token)

            return client, random_user.id

    return api_client


@pytest.fixture
def client(user):
    return APIClient()
