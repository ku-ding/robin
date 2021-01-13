def pull_request_review_comment_handler(data):
    action = data['action']
    if action == 'created':
        return pull_request_review_comment_created(data)
    elif action == 'edited':
        return pull_request_review_comment_edited(data)
    elif action == 'deleted':
        return pull_request_review_comment_deleted(data)
    else:
        return data

def pull_request_review_comment_created(data):
    title = data['pull_request']['title']
    url = data['pull_request']['html_url']
    user = data['comment']['user']['login']
    repos = data['repository']['full_name']

    return "New comment on PR \"{}\" by {} at {} ({})".format(title, user, repos, url)

def pull_request_review_comment_edited(data):
    title = data['pull_request']['title']
    url = data['pull_request']['html_url']
    user = data['comment']['user']['login']
    repos = data['repository']['full_name']

    return "The comment on PR \"{}\" by {} at {} ({}) is edited".format(title, user, repos, url)

def pull_request_review_comment_deleted(data):
    title = data['pull_request']['title']
    url = data['pull_request']['html_url']
    user = data['comment']['user']['login']
    repos = data['repository']['full_name']

    return "The comment on PR \"{}\" by {} at {} ({}) is deleted".format(title, user, repos, url)

