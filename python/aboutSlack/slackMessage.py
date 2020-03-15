from slacker import Slacker

TOKEN = ''
CHANNEL_FACE = ''

slack = Slacker(TOKEN)
slack.chat.post_message(channel=CHANNEL_FACE, text='Slacker 테스트')
