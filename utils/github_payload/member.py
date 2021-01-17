def member_handler(data):
    action = data['action']
    if action == 'added':
        return member_added(data)
    else:
        return data

def member_added(data):
    repos = data['repository']['full_name']
    url = data['repository']['html_url']
    user = data['member']['login']

    return "Welcome! {} joined {} ({})".format(user, repos, url)

