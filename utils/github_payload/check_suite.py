def check_suite_handler(data):
    action = data['action']
    if action == 'completed':
        return check_suite_completed(data)
    elif action == 'requested' or action == 'rerequested':
        return check_suite_requested(data)
    else:
        return data

def check_suite_completed(data):
    repos = data['repository']['full_name']
    url = data['repository']['html_url']
    branch = data['check_suite']['head_branch']
    status = data['check_suite']['status']
    app = data['check_suite']['app']['name']
    conclusion = data['check_suite']['conclusion']

    return "Check suite of {} on {}:{} ({}) is {} - {}".format(app, repos, branch, url, status, conclusion)

def check_suite_requested(data):
    repos = data['repository']['full_name']
    url = data['repository']['html_url']
    branch = data['check_suite']['head_branch']
    status = data['check_suite']['status']
    app = data['check_suite']['app']['name']

    return "Check suite of {} on {}:{} ({}) is {}".format(app, repos, branch, url, status)

