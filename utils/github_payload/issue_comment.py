def issue_comment_handler(data):
    action = data['action']
    if action == 'created':
        return issue_comment_created(data)
    elif action == 'edited':
        return issue_comment_edited(data)
    elif action == 'deleted':
        return issue_comment_deleted(data)
    else:
        return data

def issue_comment_created(data):
    title = data['issue']['title']
    url = data['issue']['html_url']
    user = data['comment']['user']['login']
    repos = data['repository']['full_name']
    return "New comment created by {} on the issue \"{}\" at {} ({})".format(user, title, repos, url)

def issue_comment_edited(data):
    title = data['issue']['title']
    url = data['issue']['html_url']
    user = data['comment']['user']['login']
    repos = data['repository']['full_name']
    return "The comment created by {} on the issue \"{}\" at {} ({}) is edited".format(user, title, repos, url)

def issue_comment_deleted(data):
    title = data['issue']['title']
    url = data['issue']['html_url']
    user = data['comment']['user']['login']
    repos = data['repository']['full_name']
    return "The comment created by {} on the issue \"{}\" at {} ({}) is deleted".format(user, title, repos, url)

