# import requests
# from wxpy import *
# import json


# #图灵机器人
# def talks_robot(info = 'yxpeng'):
#     api_url = 'http://www.tuling123.com/openapi/api'
#     apikey = '4b53b1f3faef475daba9c273b75d110e'
#     data = {'key': apikey,
#                 'info': info}
#     req = requests.post(api_url, data=data).text
#     replys = json.loads(req)['text']
#     return replys

# #微信自动回复
# robot = Robot()
# # 回复来自其他好友、群聊和公众号的消息
# @robot.register()
# def reply_my_friend(msg):
#     message = '{}'.format(msg.text)
#     replys = talks_robot(info=message)
#     return replys

# # 开始监听和自动处理消息
# robot.start()

# =======================================================
import requests
from wxpy import *
import json
import itchat, time


#图灵机器人
def talks_robot(info = '你叫什么名字'):
	api_url = 'http://www.tuling123.com/openapi/api'
#	apikey = '4b53b1f3faef475daba9c273b75d110e' http://www.tuling123.com/openapi/api
	apikey = 'ad53da57160e4f90bb8237869a7252c8'
	data = {'key': apikey,
				'info': info}
	req = requests.post(api_url, data=data).text
	replys = json.loads(req)['text']
	return replys

# #微信自动回复
# robot = Robot()
# # 回复来自其他好友、群聊和公众号的消息
# @robot.register()
# def reply_my_friend(msg):
#     message = '{}'.format(msg.text)
#     replys = talks_robot(info=message)
#     return replys

# # 开始监听和自动处理消息
# robot.start()

@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
def text_reply(msg):
	message = msg['Text']
	replys = talks_robot(info=message)
	itchat.send('%s RUA'%(replys,), msg['FromUserName'])
#	itchat.send(replys, msg['FromUserName'])
	print('%s RUA'%(replys,))

itchat.auto_login()
itchat.run()