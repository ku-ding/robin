from flask import Flask, request
application = Flask(__name__)

@application.route("/webhook", methods=['POST'])
def webhook():
	event = request.headers['X-GitHub-Event']
	result = request.json

	if event == 'ping':
		result = result['repository']['full_name'] + " connected"
	

	return result