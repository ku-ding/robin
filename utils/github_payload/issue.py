def issues_handler(data):
    action = data['action']
    if action == 'opened':
        return issue_opened(data)
    elif action == 'edited':
        return issue_edited(data)
    elif action == 'closed':
        return issue_closed(data)
    elif action == 'deleted':
        return issue_deleted(data)
    elif action == 'locked':
        return issue_locked(data)
    elif action == 'unlocked':
        return issue_unlocked(data)
    elif action == 'pinned':
        return issue_pinned(data)
    elif action == 'unpinned':
        return issue_unpinned(data)
    elif action == 'assigned':
        return issue_assigned(data)
    elif action == 'unassigned':
        return issue_unassigned(data)
    else:
        return data

def issue_opened(data):
    title = data['issue']['title']
    url = data['issue']['html_url']
    user = data['issue']['user']['login']
    repos = data['repository']['full_name']
    return "New issue \"{}\" created by {} at {} ({})".format(title, user, repos, url)

def issue_edited(data):
    title = data['issue']['title']
    url = data['issue']['html_url']
    user = data['issue']['user']['login']
    repos = data['repository']['full_name']
    return "The issue \"{}\" created by {} at {} ({}) is edited".format(title, user, repos, url)

def issue_closed(data):
    title = data['issue']['title']
    url = data['issue']['html_url']
    user = data['issue']['user']['login']
    repos = data['repository']['full_name']
    return "The issue \"{}\" created by {} at {} ({}) is closed".format(title, user, repos, url)

def issue_deleted(data):
    title = data['issue']['title']
    url = data['issue']['html_url']
    user = data['issue']['user']['login']
    repos = data['repository']['full_name']
    return "The issue \"{}\" created by {} at {} ({}) is deleted".format(title, user, repos, url)

def issue_locked(data):
    title = data['issue']['title']
    url = data['issue']['html_url']
    user = data['issue']['user']['login']
    repos = data['repository']['full_name']
    return "Conversation locked on the issue \"{}\" created by {} at {} ({})".format(title, user, repos, url)

def issue_unlocked(data):
    title = data['issue']['title']
    url = data['issue']['html_url']
    user = data['issue']['user']['login']
    repos = data['repository']['full_name']
    return "Conversation unlocked on the issue \"{}\" created by {} at {} ({})".format(title, user, repos, url)

def issue_pinned(data):
    title = data['issue']['title']
    url = data['issue']['html_url']
    user = data['issue']['user']['login']
    repos = data['repository']['full_name']
    return "The issue \"{}\" created by {} at {} ({}) is pinned".format(title, user, repos, url)

def issue_unpinned(data):
    title = data['issue']['title']
    url = data['issue']['html_url']
    user = data['issue']['user']['login']
    repos = data['repository']['full_name']
    return "The issue \"{}\" created by {} at {} ({}) is unpinned".format(title, user, repos, url)

def issue_assigned(data):
    title = data['issue']['title']
    url = data['issue']['html_url']
    user = data['issue']['user']['login']
    repos = data['repository']['full_name']
    assignee = data['assignee']['login']
    return "The issue \"{}\" created by {} at {} ({}) assigned to {}".format(title, user, repos, url, assignee)

def issue_unassigned(data):
    title = data['issue']['title']
    url = data['issue']['html_url']
    user = data['issue']['user']['login']
    repos = data['repository']['full_name']
    assignee = data['assignee']['login']
    return "The issue \"{}\" created by {} at {} ({}) unassigned to {}".format(title, user, repos, url, assignee)

