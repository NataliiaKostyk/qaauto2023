import pytest
from modules.api.clients.github import GitHub

class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Nataliia"
        self.second_name = "Kostyk"

    def remove(self):
        self.name = ""
        self.second_name = ""

@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()

def test_change_name(user):
    assert user.name == "Nataliia"

def test_change_second_name(user):
    assert user.second_name == "Kostyk"

@pytest.fixture
def github_api():
    api = GitHub()
    yield api 
