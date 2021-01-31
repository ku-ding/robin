import os
import requests
from dotenv import load_dotenv

load_dotenv(verbose=True)
token = os.getenv('GITHUB_TOKEN')

headers = {
    'Authorization': 'token {}'.format(token),
}

# Return the list of the issues with state `state` of `owner`/`repo` repository if `assigned=False`
# Return the list of the assigned issues with state `state` of `owner`/`repo` repository if `assigned=True`
def get_issues(owner, repo, state, assigned=None):
    if assigned:
        params = (
            ('state', state),
            ('assignee', assigned),
        )
    else:
        params = (
            ('state', state),
        )

    response = requests.get('https://api.github.com/repos/{}/{}/issues'.format(owner, repo), headers=headers, params=params).json()

    issues = []
    for issue in response:
        issues.append({'title': issue['title'], 'url': issue['html_url'], 'username': issue['user']['login']})

    return issues

def get_repository_info(owner, repo):
    response = requests.get('https://api.github.com/repos/{}/{}'.format(owner, repo), headers=headers).json()
    
    return {
        'forks': response['forks_count'],
        'stars': response['stargazers_count'],
        'watchers': response['watchers_count'],
        'open_issue': response['open_issues_count'],
        'created': response['created_at'],
        'updated': response['updated_at']
    }


# Return the list of {username, contributions}
def get_contributions(owner, repo):
    response = requests.get('https://api.github.com/repos/{}/{}/contributors'.format(owner, repo), headers=headers).json()

    contributors = []
    for user in response:
        contributors.append({'username': user['login'], 'contributions': user['contributions']})

    return contributors

# Return the list of {filename, url}
def search_keyword(owner, repo, keyword):
    params = (
        ('q', '{}+repo:{}/{}'.format(keyword, owner, repo)),
    )
    response = requests.get('https://api.github.com/search/code', headers=headers, params=params).json()
    
    items = response['items']
    files = []
    for item in items:
        files.append({'filename': item['name'], 'url': item['html_url']})

    return files

