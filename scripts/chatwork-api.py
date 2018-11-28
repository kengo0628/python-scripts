# coding: utf-8
import requests

#ChatworkのAPIトークン
chatwork_APItoken = 'YOUR API TOKEN HERE'

#ChatworkAPIのURL
chatwork_baseurl = 'https://api.chatwork.com/v2/'

#ChatworkAPI用のパラメータ(デフォルト)
chatwork_headers = {
    'X-ChatWorkToken': chatwork_APItoken,
}

#ChatworkID
chatwork_room_id = 00000000 #roomのURLにある"#!rid"以下の数字


#チャットワークのAPIでメッセージを送る
def post_to_chatwork(data, room_id, headers=chatwork_headers):
    url = chatwork_baseurl + 'rooms/' + str(room_id) + '/messages'
    params = {
        'body': data,
        'self_unread': 1,
    }
    r = requests.post(url, headers=headers, params=params)
    return r

def main():
    data = '(dance)\n'\
            '[info]囲みも使えます[/info]'
    post_chatwork_request(data, chatwork_room_id)

if __name__ == '__main__':
    main()