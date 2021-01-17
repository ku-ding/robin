def push_handler(data):
    repos = data['repository']['full_name']
    url = data['repository']['html_url']
    pusher = data['pusher']['name']
    forced = data['forced']
    commit_count = len(data['commits'])
    if data['head_commit'] is None:
        return "Empty push by {} at {} ({})".format(pusher, repos, url)
    head_commit = data['head_commit']['message']
    head_committer = data['head_commit']['author']['username']

    if forced:
        if commit_count == 1:
            return "A commit \"{}\" by {} pushed FORCE by {} at {} ({})".format(head_commit, head_committer, pusher, repos, url)
        else:
            return "The {} commits include \"{}\" by {} pushed FORCE by {} at {} ({})".format(commit_count, head_commit, head_committer, pusher, repos, url)
    else:
        if commit_count == 1:
            return "A commit \"{}\" by {} pushed by {} at {} ({})".format(head_commit, head_committer, pusher, repos, url)
        else:
            return "The {} commits include \"{}\" by {} pushed by {} at {} ({})".format(commit_count, head_commit, head_committer, pusher, repos, url)

