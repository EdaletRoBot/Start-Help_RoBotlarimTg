from telethon import events
from telethon import TelegramClient
from time import time


#config
API_ID = 1234567
API_HASH = "1234567asdfghklmnb"
bot_token = "12345678:aciencowqxqwpomewc"


edalet = TelegramClient('edalet', API_ID, API_HASH).start(bot_token=bot_token)


#@edalet_22 terefindən @RoBotlarimTg üçün yazilib silmədən istifadə edin
@edalet.on(events.NewMessage(pattern="^/telegraph$"))
async def telegraph(event):
        if event.reply_to_msg_id:
            reply_message = await event.get_reply_message()
            if reply_message.media:
                downloaded_file_name = await edalet.download_media(reply_message)
                response = post("https://telegra.ph/upload", files={"file": ("file.png", open(downloaded_file_name, "rb"))})
                remove(downloaded_file_name)
                await edalet.send_message(event.chat_id, f"**Link:** https://telegra.ph{response.json()[0]['src']}", reply_to=event.reply_to_msg_id)
            else:
                await edalet.send_message(event.chat_id, "Bir şəkilə cavab verin", reply_to=event.reply_to_msg_id)
        else:
            await edalet.send_message(event.chat_id, "Bir şəkilə cavab verin", reply_to=event.reply_to_msg_id)




print(">> Bot işləyir narahat olmayın. @edalet_22 Məlumat almaq üçün <<")
edalet.run_until_disconnected()
