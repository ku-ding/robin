from flask import Flask, request

application = Flask(__name__)


@application.route("/webhook", methods=["POST"])
def webhook():
    event = request.headers["X-GitHub-Event"]
    result = request.json
    repos = result["repository"]["full_name"]

    if event == "ping":
        result = repos + " connected"

    elif event == "issues":
        action = result["action"]
        title = result["issue"]["title"]
        url = result["issue"]["html_url"]
        user = result["issue"]["user"]["login"]
        result = "Issue {} - title : {} | url : {} | user : {} | repository : {}".format(
            action, title, url, user, repos
        )

    elif event == "issue_comment":
        action = result["action"]
        title = result["issue"]["title"]
        url = result["issue"]["html_url"]
        user = result["comment"]["user"]["login"]
        result = "Comment {} - title : {} | url : {} | user : {} | repository : {}".format(
            action, title, url, user, repos
        )

    elif event == "push":
        url = result["repository"]["html_url"]
        pusher = result["pusher"]["name"]
        result = "Commit - pusher : {} | url : {} | respository : {}".format(
            pusher, url, repos
        )

    elif event == "pull_request":
        action = result["action"]
        title = result["pull_request"]["title"]
        url = result["pull_request"]["html_url"]
        user = result["pull_request"]["user"]["login"]
        head_repos = result["pull_request"]["head"]["repo"]["full_name"]
        head_branch = result["pull_request"]["head"]["ref"]
        base_repos = result["pull_request"]["base"]["repo"]["full_name"]
        base_branch = result["pull_request"]["base"]["ref"]
        result = "Pull Request {} - title : {} | url : {} | user : {} | head repository : {} | head branch : {} | base repository : {} | bash branch : {}".format(
            action, title, url, user, head_repos, head_branch, base_repos, base_branch
        )

    return result
