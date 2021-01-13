def check_run_handler(data):
    action = data['action']
    if action == 'created':
        return check_run_created(data)
    elif action == 'completed':
        return check_run_completed(data)
    elif action == 'rerequested':
        return check_run_rerequested(data)
    else:
        return data

def check_run_created(data):
    repos = data['repository']['full_name']
    url = data['repository']['html_url']
    branch = data['check_run']['check_suite']['head_branch']
    status = data['check_run']['status']
    name = data['check_run']['name']
    app = data['check_run']['app']['name']

    return "\"{}\" of {} on {}:{} ({}) is {}".format(name, app, repos, branch, url, status)

def check_run_completed(data):
    repos = data['repository']['full_name']
    url = data['repository']['html_url']
    branch = data['check_run']['check_suite']['head_branch']
    status = data['check_run']['status']
    name = data['check_run']['name']
    app = data['check_run']['app']['name']
    conclusion = data['check_run']['conclusion']

    return "\"{}\" of {} on {}:{} ({}) is {} - {}".format(name, app, repos, branch, url, status, conclusion)

def check_run_rerequested(data):
    repos = data['repository']['full_name']
    url = data['repository']['html_url']
    branch = data['check_run']['check_suite']['head_branch']
    status = data['check_run']['status']
    name = data['check_run']['name']
    app = data['check_run']['app']['name']

    return "\"{}\" of {} on {}:{} ({}) is {}".format(name, app, repos, branch, url, status)

