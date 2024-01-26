import pytest

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api 
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 54
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api 
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0

@pytest.mark.api 
def test_repo_with_single_char_can_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

@pytest.mark.api 
def test_get_organization(github_api):
    r = github_api.get_org('github')

    assert r['login'] == 'github'

@pytest.mark.api 
def test_get_non_exist_org(github_api):
    r = github_api.get_org('non_exist')
    
    assert r['message'] == "Not Found"

@pytest.mark.api 
def test_get_list_commits(github_api):
    r = github_api.get_list_of_commits('NataliiaKostyk', 'qaauto2023')

    assert r['name'] == "Nataliia Kostyk"

@pytest.mark.api 
def test_commit_not_found(github_api):
    r = github_api.get_list_of_commits('NataliiaKostyk', 'prometheus')

    assert r['message'] == "Not Found"
