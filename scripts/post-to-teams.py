# coding: utf-8
import requests
import json
import traceback

webhook_url = 'YOUR SLACK-WEBHOOK URL HERE'

def post_to_teams(title, message):
    link_url = 'YOUR LINK URL HERE'
    body =  {
        '@type': 'MessageCard',
        '@context': 'https://schema.org/extensions',
        'themeColor': '1C4E63', #web color code
        'title': title,
        'text': message,
        'potentialAction': [ #action button with url
            {
                '@type': 'OpenUri',
                'name': 'BUTTON TEXT HERE',
                'targets': [
                    {
                        'os': 'default',
                        'uri': link_url
                    }
                ]
            }
        ]
    }
    try:
        requests.post(
            webhook_url,
            headers={'content-type': 'application/json'},
            data=json.dumps(body)
        )
    except:
        traceback.print_exc()
    return