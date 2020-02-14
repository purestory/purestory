import telepot
import os
from telepot.loop import MessageLoop

TOKEN ="1025638464:AAFY4Td65HyaWCIB5Nf0o4_i0sDokOu3L_w"

def handle(msg):
    content_type, chat_type, chat_id, msg_date, msg_id = telepot.glance(msg, long=True)
    #long으로 받으면 상세하게 데이터가 옴
    # https://telepot.readthedocs.io/en/latest/reference.html#telepot.glance
    print(content_type, chat_type, chat_id, msg_date, msg_id)
    print(msg)
    print('-'*36)

    if content_type == 'text':
        if msg['text'] == "/보내":
            filepath = './보내.txt'
            bot.sendMessage(chat_id, '알겠다 기다려 오래걸릴예정')
            bot.sendDocument(chat_id,open(filepath,'rb'))
        elif msg['text'] == "/사진보내":
            filepath = './사진보내.png'
            bot.sendMessage(chat_id, '알겠다 기다려 오래걸릴예정')
            bot.sendDocument(chat_id, open(filepath, 'rb')) #모든 파일형식 가능
            bot.sendPhoto(chat_id, open(filepath, 'rb')) #사진만 가능
        elif msg['text'].split()[0] == '/목록':
            path = msg['text'][len('/목록 '):]
            print(repr(path))
            fileList = get_dir_list(path)
            if fileList:
                res = '[{}경로 파일 목록]'.format(path)
                res += '\n'.join(fileList)
            else:
                res = '경로가 잘못되었습니다.'
            bot.sendMessage(chat_id, res)
        else:
            bot.sendMessage(chat_id, '(귀요미)\n'+msg['text'])

# 해당 폴더 파일리스트
def get_dir_list(path):
    if os.path.exists(path):
        return os.listdir(path)
    else:
        return None



import time
bot = telepot.Bot(TOKEN)
MessageLoop(bot,handle).run_forever() #메인스레드에서 수행
# MessageLoop(bot,handle).run_as_thread() #서브스레드를 생성하여 수행
print ('Listening ...')

while True:
    time.sleep(10)
