import requests

class GitHub:
    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body
    
    def search_repo(self,name):
        r = requests.get('https://api.github.com/search/repositories',
            params={"q": name})
        body = r.json()

        return body
    
    def get_org(self, org):
        r = requests.get(f'https://api.github.com/orgs/{org}')
        body = r.json()

        return body
    
    def get_list_of_commits(self, owner, repo):
        r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits')
        body = r.json()

        return body

