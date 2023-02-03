from telethon import events
from telethon import TelegramClient
from telethon.tl.types import ChannelParticipantsAdmins
import random

#config
API_ID = 1234567
API_HASH = "**"
bot_token = "***"


edalet = TelegramClient('edalet', API_ID, API_HASH).start(bot_token=bot_token)

SAHIB = 5540993505

#Bu kodu @edalet_22 tərəfindən @RoBotlarimTg kanalı üçün yazılmışdır (bu messagı silməyin!!!!!!)
@edalet.on(events.NewMessage(pattern="^/pin$"))
async def pin(event):
    if event.sender_id == SAHIB:
        if not event.reply_to_msg_id:
            return await event.reply("Bir mesajı cavablayın")
        await event.reply("Pinləndi")
        await event.client.pin_message(event.chat_id, event.reply_to_msg_id, notify=True)
    else:
        await event.reply("Sən sahib deyilsən pinləməyə çalışma")

#Bu kodu @edalet_22 tərəfindən @RoBotlarimTg kanalı üçün yazılmışdır (bu messagı silməyin!!!!!!)
@edalet.on(events.NewMessage(pattern="^/unpin$"))
async def unpin(event):
    if event.sender_id == SAHIB:
        if not event.reply_to_msg_id:
            return await event.reply("Bir pinlənən mesajı cavablayın")
        await event.reply("Unpinləndi")
        await event.client.unpin_message(event.chat_id)
    else:
        await event.reply("Sən sahib deyilsən unpinləməyə çalışma")



print(">> Bot işləyir narahat olmayın. @edalet_22 Məlumat almaq üçün <<")
edalet.run_until_disconnected()


