from flask import Flask, request
import json

from ping import ping_handler
from issue import issues_handler
from issue_comment import issue_comment_handler
from push import push_handler
from pull_request import pull_request_handler
from pull_request_review import pull_request_review_handler
from pull_request_review_comment import pull_request_review_comment_handler
from check_run import check_run_handler
from check_suite import check_suite_handler
from member import member_handler
from create import create_handler
from delete import delete_handler

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    event = request.headers['X-GitHub-Event']
    result = request.json

    if event == "ping":
        result = ping_handler(result)
    elif event == 'issues':
        result = issues_handler(result)
    elif event == 'issue_comment':
        result = issue_comment_handler(result)
    elif event == 'push':
        result = push_handler(result)
    elif event == 'pull_request':
        result = pull_request_handler(result)
    elif event == 'pull_request_review':
        result = pull_request_review_handler(result)
    elif event == 'pull_request_review_comment':
        result = pull_request_review_comment_handler(result)
    elif event == 'check_run':
        result = check_run_handler(result)
    elif event == 'check_suite':
        result = check_suite_handler(result)
    elif event == 'create':
        result = create_handler(result)
    elif event == 'delete':
        result = delete_handler(result)
    
    app.logger.info(result)
    return result

