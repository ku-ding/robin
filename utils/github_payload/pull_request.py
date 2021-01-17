def pull_request_handler(data):
    action = data['action']
    if action == 'opened':
        return pull_request_opened(data)
    elif action == 'edited':
        return pull_request_edited(data)
    elif action == 'closed':
        return pull_request_closed(data)
    elif action == 'reopened':
        return pull_request_reopened(data)
    elif action == 'assigned':
        return pull_request_assigned(data)
    elif action == 'unassigned':
        return pull_request_unassigned(data)
    elif action == 'review_requested':
        return pull_request_review_requested(data)
    elif action == 'review_request_removed':
        return pull_request_review_request_removed(data)
    else:
        return data

def pull_request_opened(data):
    title = data['pull_request']['title']
    url = data['pull_request']['html_url']
    user = data['pull_request']['user']['login']
    head_repos = data['pull_request']['head']['repo']['full_name']
    head_branch = data['pull_request']['head']['ref']
    base_repos = data['pull_request']['base']['repo']['full_name']
    base_branch = data['pull_request']['base']['ref']

    return "New PR \"{}\" from {}:{} to {}:{} ({}) opened by {}".format(title, head_repos, head_branch, base_repos, base_branch, url, user)

def pull_request_edited(data):
    title = data['pull_request']['title']
    url = data['pull_request']['html_url']
    user = data['pull_request']['user']['login']
    head_repos = data['pull_request']['head']['repo']['full_name']
    head_branch = data['pull_request']['head']['ref']
    base_repos = data['pull_request']['base']['repo']['full_name']
    base_branch = data['pull_request']['base']['ref']

    return "The PR \"{}\" from {}:{} to {}:{} ({}) opened by {} is edited".format(title, head_repos, head_branch, base_repos, base_branch, url, user)

def pull_request_closed(data):
    title = data['pull_request']['title']
    url = data['pull_request']['html_url']
    user = data['pull_request']['user']['login']
    head_repos = data['pull_request']['head']['repo']['full_name']
    head_branch = data['pull_request']['head']['ref']
    base_repos = data['pull_request']['base']['repo']['full_name']
    base_branch = data['pull_request']['base']['ref']

    return "The PR \"{}\" from {}:{} to {}:{} ({}) opened by {} is closed".format(title, head_repos, head_branch, base_repos, base_branch, url, user)

def pull_request_reopened(data):
    title = data['pull_request']['title']
    url = data['pull_request']['html_url']
    user = data['sender']['login']
    head_repos = data['pull_request']['head']['repo']['full_name']
    head_branch = data['pull_request']['head']['ref']
    base_repos = data['pull_request']['base']['repo']['full_name']
    base_branch = data['pull_request']['base']['ref']

    return "The PR \"{}\" from {}:{} to {}:{} ({}) reopened by {}".format(title, head_repos, head_branch, base_repos, base_branch, url, user)

def pull_request_assigned(data):
    title = data['pull_request']['title']
    url = data['pull_request']['html_url']
    user = data['assignee']['login']
    head_repos = data['pull_request']['head']['repo']['full_name']
    head_branch = data['pull_request']['head']['ref']
    base_repos = data['pull_request']['base']['repo']['full_name']
    base_branch = data['pull_request']['base']['ref']

    return "The PR \"{}\" from {}:{} to {}:{} ({}) assigned to {}".format(title, head_repos, head_branch, base_repos, base_branch, url, user)

def pull_request_unassigned(data):
    title = data['pull_request']['title']
    url = data['pull_request']['html_url']
    user = data['assignee']['login']
    head_repos = data['pull_request']['head']['repo']['full_name']
    head_branch = data['pull_request']['head']['ref']
    base_repos = data['pull_request']['base']['repo']['full_name']
    base_branch = data['pull_request']['base']['ref']

    return "The PR \"{}\" from {}:{} to {}:{} ({}) unassigned to {}".format(title, head_repos, head_branch, base_repos, base_branch, url, user)

def pull_request_review_requested(data):
    title = data['pull_request']['title']
    url = data['pull_request']['html_url']
    user = data['requested_reviewer']['login']
    head_repos = data['pull_request']['head']['repo']['full_name']
    head_branch = data['pull_request']['head']['ref']
    base_repos = data['pull_request']['base']['repo']['full_name']
    base_branch = data['pull_request']['base']['ref']

    return "New review request to {} for the PR \"{}\" from {}:{} to {}:{} ({})".format(user, title, head_repos, head_branch, base_repos, base_branch, url)

def pull_request_review_request_removed(data):
    title = data['pull_request']['title']
    url = data['pull_request']['html_url']
    user = data['requested_reviewer']['login']
    head_repos = data['pull_request']['head']['repo']['full_name']
    head_branch = data['pull_request']['head']['ref']
    base_repos = data['pull_request']['base']['repo']['full_name']
    base_branch = data['pull_request']['base']['ref']

    return "The review request to {} for the PR \"{}\" from {}:{} to {}:{} ({}) is removed".format(user, title, head_repos, head_branch, base_repos, base_branch, url)
