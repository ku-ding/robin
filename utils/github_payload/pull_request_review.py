def pull_request_review_handler(data):
    action = data['action']
    if action == 'submitted':
        return pull_request_review_submitted(data)
    elif action == 'edited':
        return pull_request_review_edited(data)
    elif action == 'dismissed':
        return pull_request_review_dismissed(data)
    else:
        return data

def pull_request_review_submitted(data):
    title = data['pull_request']['title']
    url = data['pull_request']['html_url']
    user = data['review']['user']['login']
    repos = data['repository']['full_name']

    return "New review on PR \"{}\" by {} at {} ({})".format(title, user, repos, url)

def pull_request_review_edited(data):
    title = data['pull_request']['title']
    url = data['pull_request']['html_url']
    user = data['review']['user']['login']
    repos = data['repository']['full_name']

    return "The review on PR \"{}\" by {} at {} ({}) is edited".format(title, user, repos, url)

def pull_request_review_dismissed(data):
    title = data['pull_request']['title']
    url = data['pull_request']['html_url']
    user = data['review']['user']['login']
    repos = data['repository']['full_name']

    return "The review on PR \"{}\" by {} at {} ({}) is dismissed".format(title, user, repos, url)

