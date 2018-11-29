# coding: utf-8
import requests

webhook_url = 'YOUR SLACK-WEBHOOK URL HERE'

#slackに通知する
def post_to_slack(message):
    requests.post(
        webhook_url,
        headers={'content-type': 'application/json'},
        data=json.dumps({'text': ':no_entry_sign:' + message})
    )