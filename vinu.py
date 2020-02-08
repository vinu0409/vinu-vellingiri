import time, datetime
import telepot
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

now = datetime.datetime.now()

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)

    if command == 'Hi':
        telegram_bot.sendMessage (chat_id, str("Yup! Vinu"))
    elif command == 'Time':
        telegram_bot.sendMessage(chat_id, now.strftime("%H:%M"))
    elif command == 'Image':
        telegram_bot.sendPhoto (chat_id, photo=open('/home/pi/vinu.jpg'))
    elif command == 'Date':
        telegram_bot.sendMessage(chat_id, now.strftime("%Y-%m-%d"))
    elif command == 'Forge':
        telegram_bot.sendPhoto(chat_id, photo="https://www.forgeforward.in/images/forge-logo-04-trimmed.png")
    elif command == 'On':
       telegram_bot.sendMessage(chat_id, GPIO.output(8,GPIO.HIGH))
    elif command =='Off':
       telegram_bot.sendMessage(chat_id, GPIO.output(8,GPIO.LOW))

telegram_bot = telepot.Bot('1081507754:AAHpoGp_vptv9P0YvQH3ZFrMR0YYNGlVn1M')
print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print 'Up and Running....'

while 1:
    time.sleep(10)