import time
from audioop import tomono
from rpyc import timed
from wxauto import *
from ai import ai
import re
import json
wx = WeChat()
pattern = ''
which_chat = ''
wx.GetSessionList()
wx.ChatWith(which_chat)
chat_list = []
memorydir = { }
while True:
    msgs = wx.GetAllMessage()
    who = msgs[-1][0]
    print(who)
    if msgs[-1][0] != 'Self' and msgs[-1][0] != 'SYS':
        result = re.sub(pattern, '', msgs[-1][1]).strip()
        if re.search(pattern, msgs[-1][1]) and msgs[-1][1] not in chat_list and result != '':
            print(result)
            res = ai(result)
            wx.SendMsg(res['result'], which_chat)
            print(msgs[-1][1], res)
            chat_list.append(msgs[-1][1])
    time.sleep(2)