# Bu repo edalet_22 tərəfindən yazılıb
# Öz adına çıxaran peysərdi
# Bu yazıları silmədən işlədin

# t.me/RoBotlarimTg | YouTube: RoBotlarimTg | t.me/EdaletSup
# t.me/aykhan_s | t.me/edalet_22
# GitHub: EdaletRoBot



from telethon import TelegramClient
from telethon import events
İmport random 


# Config məlumatları
API_ID = *******
API_HASH = "**********************************"
bot_token = "**********************************"

# Telegram Client (Telethon)
edalet = TelegramClient('edalet', API_ID, API_HASH).start(bot_token=bot_token)


#@edalet_22 terefindən @RoBotlarimTg üçün yazilib silmədən istifadə edin
@edalet.on(events.NewMessage(pattern='@edalet_22'))
@edalet.on(events.NewMessage(pattern='edalet_22'))
@edalet.on(events.NewMessage(pattern='ədoş'))
@edalet.on(events.NewMessage(pattern='edalet'))
async def handler(event):
    await event.reply(random.choice(edalet))



edalet = (
    "Az tağ elə sahibimi",
    "",
)


print(">> Bot işləyir narahat olmayın. @edalet_22 Məlumat almaq üçün <<")
edalet.run_until_disconnected()
