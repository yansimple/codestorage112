from rocketgram import Bot, Dispatcher, UpdatesExecutor
from rocketgram import context, commonfilters
from rocketgram import SendMessage

token = '1754713578:AAGDhexcie3scpbCf8zXSFHgw22qrP2Aw10'

router = Dispatcher()
bot = Bot(token, router=router)

@router.handler
@commonfilters.command('/start')
async def start_command():
    await SendMessage(context.user.user_id, 'Hello there!').send()

@router.handler
@commonfilters.command('/help')
async def start_command():
    await SendMessage(context.user.user_id, 'Some userful help!').send()

UpdatesExecutor.run(bot)