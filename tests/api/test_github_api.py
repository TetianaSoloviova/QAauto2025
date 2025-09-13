import pytest


@pytest.mark.api
def test_user_exist(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'
    

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] =='Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 57
    assert'become-qa-auto' in r['items'][0]['name']
    print (r)

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0



@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0


@pytest.mark.api
def test_emojis_has_many_items(github_api):
    emojis = github_api.get_emojis()
    assert len(emojis) > 100, "Expected more than 100 emojis"


@pytest.mark.api
def test_emojis_contains_smile(github_api):
    emojis = github_api.get_emojis()
    assert "smile" in emojis, "'smile' має бути серед емодзі"
    assert emojis["smile"].startswith("https://"), "URL емодзі має починатися з https://"

@pytest.mark.api
def test_commit_has_author_and_message(github_api):
    commits = github_api.get_commits("octocat", "Hello-World")
    first_commit = commits[0]

    assert "commit" in first_commit, "Коміт має містити ключ 'commit'"
    assert "author" in first_commit["commit"], "Коміт має містити інформацію про автора"
    assert "name" in first_commit["commit"]["author"], "Ім’я автора має бути присутнє"

    assert "message" in first_commit["commit"], "Коміт має містити повідомлення про зміни"
    assert first_commit["commit"]["message"].strip() != "", "Повідомлення не має бути порожнім"

