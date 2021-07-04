
from telethon import TelegramClient, events, Button, types
from decouple import config
from ProfanityDetector import detector
import logging
from telethon.tl.functions.channels import GetParticipantRequest

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)

log = logging.getLogger(__name__)

# vars
apiid = 6
apihash = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
BOT_TOKEN = config("BOT_TOKEN", default=None)

log.info("Starting Bot...")

bot = TelegramClient("bot", apiid, apihash).start(bot_token=BOT_TOKEN)

# check admins
async def check_if_admin(message):
    result = await bot(
        GetParticipantRequest(
            channel=message.chat_id,
            user_id=message.sender_id,
        )
    )
    p = result.participant
    return isinstance(
        p, (types.ChannelParticipantCreator, types.ChannelParticipantAdmin)
    )


@bot.on(
    events.NewMessage(incoming=True, pattern="^/start$", func=lambda e: e.is_private)
)
async def start_msg(event):
    sender = await bot.get_entity(event.sender_id)
    await event.reply(
        f"Hi {sender.first_name}!\nI am a Telegram profanity detector bot.\n\nMake me admin in your group with `delete messages` permission and I'll delete messsages containing abuses!",
        buttons=[
            [Button.inline("Help", data="help")],
            [
                Button.url(
                    "Add me to a group ➕",
                    url=f"http://t.me/{(await bot.get_me()).username}?startgroup=botstart",
                )
            ],
            [
                Button.url("👨‍🔧updates Channel👨‍🔧", url="https://t.me/disneygrou"),
                Button.url(
                    "Package 📦", url="https://pypi.org/project/ProfanityDetector/"
                ),
            ],
        ],
    )


@bot.on(events.NewMessage(incoming=True, pattern="^/start", func=lambda e: e.is_group))
async def start_grp(event):
    sender = await bot.get_entity(event.sender_id)
    await event.reply(
        f"Hey {sender.first_name}!\n__I'm up, protecting this group!__\n**False positives?** Report them to @disneyteamchat!"
    )


@bot.on(events.callbackquery.CallbackQuery(data="help"))
async def helper_(event):
    sender = await bot.get_entity(event.sender_id)
    await event.edit(
        f"""
{sender.first_name}, here is the help menu.\n
**How to use?**
- Add me to a group, and make me admin, with \"delete messages\" permission.
- If the bot is not admin, it will not be deleting messages containing blacklisted words.\n
**Report False Positives:**
- You are free to report False detections in @disneyteamchat.""",
        buttons=[[Button.inline("Back", data="start")]],
    )


@bot.on(events.callbackquery.CallbackQuery(data="start"))
async def start_msg(event):
    sender = await bot.get_entity(event.sender_id)
    await event.edit(
        f"Hi {sender.first_name}!\nI am a Telegram profanity detector bot.\n\nMake me admin in your group with `delete messages` permission and I'll delete messsages containing abuses!",
        buttons=[
            [Button.inline("Help", data="help")],
            [
                Button.url(
                    "Add me to a group ➕",
                    url=f"http://t.me/{(await bot.get_me()).username}?startgroup=botstart",
                )
            ],
            [
                Button.url("👨‍🔧updates Channel👨‍🔧", url="https://t.me/disneygrou"),
                Button.url(
                    "Package 📦", url="https://pypi.org/project/ProfanityDetector/"
                ),
            ],
        ],
    )


@bot.on(events.NewMessage(incoming=True, func=lambda e: e.is_group))
async def deleter_(event):
    try:
        if await check_if_admin(event):
            return
    except:
        return
    sentence = event.raw_text
    sender = await bot.get_entity(event.sender_id)
    word, detected = detector(sentence)
    if detected:
        try:
            await event.reply(
                f"Hey {sender.first_name}, you used a blacklisted word and so your message has been deleted contact @doreamonfans1!"
            )
            await event.delete()
        except:
            log.info(f"Cannot delete messages in {(await event.get_chat()).title}.")


log.info("Bot has started!")
bot.run_until_disconnected()
from telethon import TelegramClient, events, Button, types
from decouple import config
from ProfanityDetector import detector
import logging
from telethon.tl.functions.channels import GetParticipantRequest

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)

log = logging.getLogger(__name__)

# vars
apiid = 6
apihash = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
BOT_TOKEN = config("BOT_TOKEN", default=None)

log.info("Starting Bot...")

bot = TelegramClient("bot", apiid, apihash).start(bot_token=BOT_TOKEN)

# check admins
async def check_if_admin(message):
    result = await bot(
        GetParticipantRequest(
            channel=message.chat_id,
            user_id=message.sender_id,
        )
    )
    p = result.participant
    return isinstance(
        p, (types.ChannelParticipantCreator, types.ChannelParticipantAdmin)
    )


@bot.on(
    events.NewMessage(incoming=True, pattern="^/start$", func=lambda e: e.is_private)
)
async def start_msg(event):
    sender = await bot.get_entity(event.sender_id)
    await event.reply(
        f"Hi {sender.first_name}!\nI am a Telegram profanity detector bot.\n\nMake me admin in your group with `delete messages` permission and I'll delete messsages containing abuses!",
        buttons=[
            [Button.inline("Help", data="help")],
            [
                Button.url(
                    "Add me to a group ➕",
                    url=f"http://t.me/{(await bot.get_me()).username}?startgroup=botstart",
                )
            ],
            [
                Button.url("👨‍🔧updates Channel👨‍🔧", url="https://t.me/disneygrou"),
                Button.url(
                    "Package 📦", url="https://pypi.org/project/ProfanityDetector/"
                ),
            ],
        ],
    )


@bot.on(events.NewMessage(incoming=True, pattern="^/start", func=lambda e: e.is_group))
async def start_grp(event):
    sender = await bot.get_entity(event.sender_id)
    await event.reply(
        f"Hey {sender.first_name}!\n__I'm up, protecting this group!__\n**False positives?** Report them to @disneyteamchat!"
    )


@bot.on(events.callbackquery.CallbackQuery(data="help"))
async def helper_(event):
    sender = await bot.get_entity(event.sender_id)
    await event.edit(
        f"""
{sender.first_name}, here is the help menu.\n
**How to use?**
- Add me to a group, and make me admin, with \"delete messages\" permission.
- If the bot is not admin, it will not be deleting messages containing blacklisted words.\n
**Report False Positives:**
- You are free to report False detections in @disneyteamchat.""",
        buttons=[[Button.inline("Back", data="start")]],
    )


@bot.on(events.callbackquery.CallbackQuery(data="start"))
async def start_msg(event):
    sender = await bot.get_entity(event.sender_id)
    await event.edit(
        f"Hi {sender.first_name}!\nI am a Telegram profanity detector bot.\n\nMake me admin in your group with `delete messages` permission and I'll delete messsages containing abuses!",
        buttons=[
            [Button.inline("Help", data="help")],
            [
                Button.url(
                    "Add me to a group ➕",
                    url=f"http://t.me/{(await bot.get_me()).username}?startgroup=botstart",
                )
            ],
            [
                Button.url("👨‍🔧updates Channel👨‍🔧", url="https://t.me/disneygrou"),
                Button.url(
                    "Package 📦", url="https://pypi.org/project/ProfanityDetector/"
                ),
            ],
        ],
    )


@bot.on(events.NewMessage(incoming=True, func=lambda e: e.is_group))
async def deleter_(event):
    try:
        if await check_if_admin(event):
            return
    except:
        return
    sentence = event.raw_text
    sender = await bot.get_entity(event.sender_id)
    word, detected = detector(sentence)
    if detected:
        try:
            await event.reply(
                f"Hey {sender.first_name}, you used a blacklisted word and so your message has been deleted contact @doreamonfans1!"
            )
            await event.delete()
        except:
            log.info(f"Cannot delete messages in {(await event.get_chat()).title}.")


log.info("Bot has started!")
bot.run_until_disconnected()
from telethon import TelegramClient, events, Button, types
from decouple import config
from ProfanityDetector import detector
import logging
from telethon.tl.functions.channels import GetParticipantRequest

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)

log = logging.getLogger(__name__)

# vars
apiid = 6
apihash = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
BOT_TOKEN = config("BOT_TOKEN", default=None)

log.info("Starting Bot...")

bot = TelegramClient("bot", apiid, apihash).start(bot_token=BOT_TOKEN)

# check admins
async def check_if_admin(message):
    result = await bot(
        GetParticipantRequest(
            channel=message.chat_id,
            user_id=message.sender_id,
        )
    )
    p = result.participant
    return isinstance(
        p, (types.ChannelParticipantCreator, types.ChannelParticipantAdmin)
    )


@bot.on(
    events.NewMessage(incoming=True, pattern="^/start$", func=lambda e: e.is_private)
)
async def start_msg(event):
    sender = await bot.get_entity(event.sender_id)
    await event.reply(
        f"Hi {sender.first_name}!\nI am a Telegram profanity detector bot.\n\nMake me admin in your group with `delete messages` permission and I'll delete messsages containing abuses!",
        buttons=[
            [Button.inline("Help", data="help")],
            [
                Button.url(
                    "Add me to a group ➕",
                    url=f"http://t.me/{(await bot.get_me()).username}?startgroup=botstart",
                )
            ],
            [
                Button.url("👨‍🔧updates Channel👨‍🔧", url="https://t.me/disneygrou"),
                Button.url(
                    "Package 📦", url="https://pypi.org/project/ProfanityDetector/"
                ),
            ],
        ],
    )


@bot.on(events.NewMessage(incoming=True, pattern="^/start", func=lambda e: e.is_group))
async def start_grp(event):
    sender = await bot.get_entity(event.sender_id)
    await event.reply(
        f"Hey {sender.first_name}!\n__I'm up, protecting this group!__\n**False positives?** Report them to @disneyteamchat!"
    )


@bot.on(events.callbackquery.CallbackQuery(data="help"))
async def helper_(event):
    sender = await bot.get_entity(event.sender_id)
    await event.edit(
        f"""
{sender.first_name}, here is the help menu.\n
**How to use?**
- Add me to a group, and make me admin, with \"delete messages\" permission.
- If the bot is not admin, it will not be deleting messages containing blacklisted words.\n
**Report False Positives:**
- You are free to report False detections in @disneyteamchat.""",
        buttons=[[Button.inline("Back", data="start")]],
    )


@bot.on(events.callbackquery.CallbackQuery(data="start"))
async def start_msg(event):
    sender = await bot.get_entity(event.sender_id)
    await event.edit(
        f"Hi {sender.first_name}!\nI am a Telegram profanity detector bot.\n\nMake me admin in your group with `delete messages` permission and I'll delete messsages containing abuses!",
        buttons=[
            [Button.inline("Help", data="help")],
            [
                Button.url(
                    "Add me to a group ➕",
                    url=f"http://t.me/{(await bot.get_me()).username}?startgroup=botstart",
                )
            ],
            [
                Button.url("👨‍🔧updates Channel👨‍🔧", url="https://t.me/disneygrou"),
                Button.url(
                    "Package 📦", url="https://pypi.org/project/ProfanityDetector/"
                ),
            ],
        ],
    )


@bot.on(events.NewMessage(incoming=True, func=lambda e: e.is_group))
async def deleter_(event):
    try:
        if await check_if_admin(event):
            return
    except:
        return
    sentence = event.raw_text
    sender = await bot.get_entity(event.sender_id)
    word, detected = detector(sentence)
    if detected:
        try:
            await event.reply(
                f"Hey {sender.first_name}, you used a blacklisted word and so your message has been deleted contact @doreamonfans1!"
            )
            await event.delete()
        except:
            log.info(f"Cannot delete messages in {(await event.get_chat()).title}.")


log.info("Bot has started!")
bot.run_until_disconnected()
from telethon import TelegramClient, events, Button, types
from decouple import config
from ProfanityDetector import detector
import logging
from telethon.tl.functions.channels import GetParticipantRequest

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)

log = logging.getLogger(__name__)

# vars
apiid = 6
apihash = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
BOT_TOKEN = config("BOT_TOKEN", default=None)

log.info("Starting Bot...")

bot = TelegramClient("bot", apiid, apihash).start(bot_token=BOT_TOKEN)

# check admins
async def check_if_admin(message):
    result = await bot(
        GetParticipantRequest(
            channel=message.chat_id,
            user_id=message.sender_id,
        )
    )
    p = result.participant
    return isinstance(
        p, (types.ChannelParticipantCreator, types.ChannelParticipantAdmin)
    )


@bot.on(
    events.NewMessage(incoming=True, pattern="^/start$", func=lambda e: e.is_private)
)
async def start_msg(event):
    sender = await bot.get_entity(event.sender_id)
    await event.reply(
        f"Hi {sender.first_name}!\nI am a Telegram profanity detector bot.\n\nMake me admin in your group with `delete messages` permission and I'll delete messsages containing abuses!",
        buttons=[
            [Button.inline("Help", data="help")],
            [
                Button.url(
                    "Add me to a group ➕",
                    url=f"http://t.me/{(await bot.get_me()).username}?startgroup=botstart",
                )
            ],
            [
                Button.url("👨‍🔧updates Channel👨‍🔧", url="https://t.me/disneygrou"),
                Button.url(
                    "Package 📦", url="https://pypi.org/project/ProfanityDetector/"
                ),
            ],
        ],
    )


@bot.on(events.NewMessage(incoming=True, pattern="^/start", func=lambda e: e.is_group))
async def start_grp(event):
    sender = await bot.get_entity(event.sender_id)
    await event.reply(
        f"Hey {sender.first_name}!\n__I'm up, protecting this group!__\n**False positives?** Report them to @disneyteamchat!"
    )


@bot.on(events.callbackquery.CallbackQuery(data="help"))
async def helper_(event):
    sender = await bot.get_entity(event.sender_id)
    await event.edit(
        f"""
{sender.first_name}, here is the help menu.\n
**How to use?**
- Add me to a group, and make me admin, with \"delete messages\" permission.
- If the bot is not admin, it will not be deleting messages containing blacklisted words.\n
**Report False Positives:**
- You are free to report False detections in @disneyteamchat.""",
        buttons=[[Button.inline("Back", data="start")]],
    )


@bot.on(events.callbackquery.CallbackQuery(data="start"))
async def start_msg(event):
    sender = await bot.get_entity(event.sender_id)
    await event.edit(
        f"Hi {sender.first_name}!\nI am a Telegram profanity detector bot.\n\nMake me admin in your group with `delete messages` permission and I'll delete messsages containing abuses!",
        buttons=[
            [Button.inline("Help", data="help")],
            [
                Button.url(
                    "Add me to a group ➕",
                    url=f"http://t.me/{(await bot.get_me()).username}?startgroup=botstart",
                )
            ],
            [
                Button.url("👨‍🔧updates Channel👨‍🔧", url="https://t.me/disneygrou"),
                Button.url(
                    "Package 📦", url="https://pypi.org/project/ProfanityDetector/"
                ),
            ],
        ],
    )


@bot.on(events.NewMessage(incoming=True, func=lambda e: e.is_group))
async def deleter_(event):
    try:
        if await check_if_admin(event):
            return
    except:
        return
    sentence = event.raw_text
    sender = await bot.get_entity(event.sender_id)
    word, detected = detector(sentence)
    if detected:
        try:
            await event.reply(
                f"Hey {sender.first_name}, you used a blacklisted word and so your message has been deleted contact @doreamonfans1!"
            )
            await event.delete()
        except:
            log.info(f"Cannot delete messages in {(await event.get_chat()).title}.")


log.info("Bot has started!")
bot.run_until_disconnected()
from telethon import TelegramClient, events, Button, types
from decouple import config
from ProfanityDetector import detector
import logging
from telethon.tl.functions.channels import GetParticipantRequest

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)

log = logging.getLogger(__name__)

# vars
apiid = 6
apihash = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
BOT_TOKEN = config("BOT_TOKEN", default=None)

log.info("Starting Bot...")

bot = TelegramClient("bot", apiid, apihash).start(bot_token=BOT_TOKEN)

# check admins
async def check_if_admin(message):
    result = await bot(
        GetParticipantRequest(
            channel=message.chat_id,
            user_id=message.sender_id,
        )
    )
    p = result.participant
    return isinstance(
        p, (types.ChannelParticipantCreator, types.ChannelParticipantAdmin)
    )


@bot.on(
    events.NewMessage(incoming=True, pattern="^/start$", func=lambda e: e.is_private)
)
async def start_msg(event):
    sender = await bot.get_entity(event.sender_id)
    await event.reply(
        f"Hi {sender.first_name}!\nI am a Telegram profanity detector bot.\n\nMake me admin in your group with `delete messages` permission and I'll delete messsages containing abuses!",
        buttons=[
            [Button.inline("Help", data="help")],
            [
                Button.url(
                    "Add me to a group ➕",
                    url=f"http://t.me/{(await bot.get_me()).username}?startgroup=botstart",
                )
            ],
            [
                Button.url("👨‍🔧updates Channel👨‍🔧", url="https://t.me/disneygrou"),
                Button.url(
                    "Package 📦", url="https://pypi.org/project/ProfanityDetector/"
                ),
            ],
        ],
    )


@bot.on(events.NewMessage(incoming=True, pattern="^/start", func=lambda e: e.is_group))
async def start_grp(event):
    sender = await bot.get_entity(event.sender_id)
    await event.reply(
        f"Hey {sender.first_name}!\n__I'm up, protecting this group!__\n**False positives?** Report them to @disneyteamchat!"
    )


@bot.on(events.callbackquery.CallbackQuery(data="help"))
async def helper_(event):
    sender = await bot.get_entity(event.sender_id)
    await event.edit(
        f"""
{sender.first_name}, here is the help menu.\n
**How to use?**
- Add me to a group, and make me admin, with \"delete messages\" permission.
- If the bot is not admin, it will not be deleting messages containing blacklisted words.\n
**Report False Positives:**
- You are free to report False detections in @disneyteamchat.""",
        buttons=[[Button.inline("Back", data="start")]],
    )


@bot.on(events.callbackquery.CallbackQuery(data="start"))
async def start_msg(event):
    sender = await bot.get_entity(event.sender_id)
    await event.edit(
        f"Hi {sender.first_name}!\nI am a Telegram profanity detector bot.\n\nMake me admin in your group with `delete messages` permission and I'll delete messsages containing abuses!",
        buttons=[
            [Button.inline("Help", data="help")],
            [
                Button.url(
                    "Add me to a group ➕",
                    url=f"http://t.me/{(await bot.get_me()).username}?startgroup=botstart",
                )
            ],
            [
                Button.url("👨‍🔧updates Channel👨‍🔧", url="https://t.me/disneygrou"),
                Button.url(
                    "Package 📦", url="https://pypi.org/project/ProfanityDetector/"
                ),
            ],
        ],
    )


@bot.on(events.NewMessage(incoming=True, func=lambda e: e.is_group))
async def deleter_(event):
    try:
        if await check_if_admin(event):
            return
    except:
        return
    sentence = event.raw_text
    sender = await bot.get_entity(event.sender_id)
    word, detected = detector(sentence)
    if detected:
        try:
            await event.reply(
                f"Hey {sender.first_name}, you used a blacklisted word and so your message has been deleted contact @doreamonfans1!"
            )
            await event.delete()
        except:
            log.info(f"Cannot delete messages in {(await event.get_chat()).title}.")


log.info("Bot has started!")
bot.run_until_disconnected()
from telethon import TelegramClient, events, Button, types
from decouple import config
from ProfanityDetector import detector
import logging
from telethon.tl.functions.channels import GetParticipantRequest

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)

log = logging.getLogger(__name__)

# vars
apiid = 6
apihash = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
BOT_TOKEN = config("BOT_TOKEN", default=None)

log.info("Starting Bot...")

bot = TelegramClient("bot", apiid, apihash).start(bot_token=BOT_TOKEN)

# check admins
async def check_if_admin(message):
    result = await bot(
        GetParticipantRequest(
            channel=message.chat_id,
            user_id=message.sender_id,
        )
    )
    p = result.participant
    return isinstance(
        p, (types.ChannelParticipantCreator, types.ChannelParticipantAdmin)
    )


@bot.on(
    events.NewMessage(incoming=True, pattern="^/start$", func=lambda e: e.is_private)
)
async def start_msg(event):
    sender = await bot.get_entity(event.sender_id)
    await event.reply(
        f"Hi {sender.first_name}!\nI am a Telegram profanity detector bot.\n\nMake me admin in your group with `delete messages` permission and I'll delete messsages containing abuses!",
        buttons=[
            [Button.inline("Help", data="help")],
            [
                Button.url(
                    "Add me to a group ➕",
                    url=f"http://t.me/{(await bot.get_me()).username}?startgroup=botstart",
                )
            ],
            [
                Button.url("👨‍🔧updates Channel👨‍🔧", url="https://t.me/disneygrou"),
                Button.url(
                    "Package 📦", url="https://pypi.org/project/ProfanityDetector/"
                ),
            ],
        ],
    )


@bot.on(events.NewMessage(incoming=True, pattern="^/start", func=lambda e: e.is_group))
async def start_grp(event):
    sender = await bot.get_entity(event.sender_id)
    await event.reply(
        f"Hey {sender.first_name}!\n__I'm up, protecting this group!__\n**False positives?** Report them to @disneyteamchat!"
    )


@bot.on(events.callbackquery.CallbackQuery(data="help"))
async def helper_(event):
    sender = await bot.get_entity(event.sender_id)
    await event.edit(
        f"""
{sender.first_name}, here is the help menu.\n
**How to use?**
- Add me to a group, and make me admin, with \"delete messages\" permission.
- If the bot is not admin, it will not be deleting messages containing blacklisted words.\n
**Report False Positives:**
- You are free to report False detections in @disneyteamchat.""",
        buttons=[[Button.inline("Back", data="start")]],
    )


@bot.on(events.callbackquery.CallbackQuery(data="start"))
async def start_msg(event):
    sender = await bot.get_entity(event.sender_id)
    await event.edit(
        f"Hi {sender.first_name}!\nI am a Telegram profanity detector bot.\n\nMake me admin in your group with `delete messages` permission and I'll delete messsages containing abuses!",
        buttons=[
            [Button.inline("Help", data="help")],
            [
                Button.url(
                    "Add me to a group ➕",
                    url=f"http://t.me/{(await bot.get_me()).username}?startgroup=botstart",
                )
            ],
            [
                Button.url("👨‍🔧updates Channel👨‍🔧", url="https://t.me/disneygrou"),
                Button.url(
                    "Package 📦", url="https://pypi.org/project/ProfanityDetector/"
                ),
            ],
        ],
    )


@bot.on(events.NewMessage(incoming=True, func=lambda e: e.is_group))
async def deleter_(event):
    try:
        if await check_if_admin(event):
            return
    except:
        return
    sentence = event.raw_text
    sender = await bot.get_entity(event.sender_id)
    word, detected = detector(sentence)
    if detected:
        try:
            await event.reply(
                f"Hey {sender.first_name}, you used a blacklisted word and so your message has been deleted contact @doreamonfans1!"
            )
            await event.delete()
        except:
            log.info(f"Cannot delete messages in {(await event.get_chat()).title}.")


log.info("Bot has started!")
bot.run_until_disconnected()
from telethon import TelegramClient, events, Button, types
from decouple import config
from ProfanityDetector import detector
import logging
from telethon.tl.functions.channels import GetParticipantRequest

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)

log = logging.getLogger(__name__)

# vars
apiid = 6
apihash = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
BOT_TOKEN = config("BOT_TOKEN", default=None)

log.info("Starting Bot...")

bot = TelegramClient("bot", apiid, apihash).start(bot_token=BOT_TOKEN)

# check admins
async def check_if_admin(message):
    result = await bot(
        GetParticipantRequest(
            channel=message.chat_id,
            user_id=message.sender_id,
        )
    )
    p = result.participant
    return isinstance(
        p, (types.ChannelParticipantCreator, types.ChannelParticipantAdmin)
    )


@bot.on(
    events.NewMessage(incoming=True, pattern="^/start$", func=lambda e: e.is_private)
)
async def start_msg(event):
    sender = await bot.get_entity(event.sender_id)
    await event.reply(
        f"Hi {sender.first_name}!\nI am a Telegram profanity detector bot.\n\nMake me admin in your group with `delete messages` permission and I'll delete messsages containing abuses!",
        buttons=[
            [Button.inline("Help", data="help")],
            [
                Button.url(
                    "Add me to a group ➕",
                    url=f"http://t.me/{(await bot.get_me()).username}?startgroup=botstart",
                )
            ],
            [
                Button.url("👨‍🔧updates Channel👨‍🔧", url="https://t.me/disneygrou"),
                Button.url(
                    "Package 📦", url="https://pypi.org/project/ProfanityDetector/"
                ),
            ],
        ],
    )


@bot.on(events.NewMessage(incoming=True, pattern="^/start", func=lambda e: e.is_group))
async def start_grp(event):
    sender = await bot.get_entity(event.sender_id)
    await event.reply(
        f"Hey {sender.first_name}!\n__I'm up, protecting this group!__\n**False positives?** Report them to @disneyteamchat!"
    )


@bot.on(events.callbackquery.CallbackQuery(data="help"))
async def helper_(event):
    sender = await bot.get_entity(event.sender_id)
    await event.edit(
        f"""
{sender.first_name}, here is the help menu.\n
**How to use?**
- Add me to a group, and make me admin, with \"delete messages\" permission.
- If the bot is not admin, it will not be deleting messages containing blacklisted words.\n
**Report False Positives:**
- You are free to report False detections in @disneyteamchat.""",
        buttons=[[Button.inline("Back", data="start")]],
    )


@bot.on(events.callbackquery.CallbackQuery(data="start"))
async def start_msg(event):
    sender = await bot.get_entity(event.sender_id)
    await event.edit(
        f"Hi {sender.first_name}!\nI am a Telegram profanity detector bot.\n\nMake me admin in your group with `delete messages` permission and I'll delete messsages containing abuses!",
        buttons=[
            [Button.inline("Help", data="help")],
            [
                Button.url(
                    "Add me to a group ➕",
                    url=f"http://t.me/{(await bot.get_me()).username}?startgroup=botstart",
                )
            ],
            [
                Button.url("👨‍🔧updates Channel👨‍🔧", url="https://t.me/disneygrou"),
                Button.url(
                    "Package 📦", url="https://pypi.org/project/ProfanityDetector/"
                ),
            ],
        ],
    )


@bot.on(events.NewMessage(incoming=True, func=lambda e: e.is_group))
async def deleter_(event):
    try:
        if await check_if_admin(event):
            return
    except:
        return
    sentence = event.raw_text
    sender = await bot.get_entity(event.sender_id)
    word, detected = detector(sentence)
    if detected:
        try:
            await event.reply(
                f"Hey {sender.first_name}, you used a blacklisted word and so your message has been deleted contact @doreamonfans1!"
            )
            await event.delete()
        except:
            log.info(f"Cannot delete messages in {(await event.get_chat()).title}.")


log.info("Bot has started!")
bot.run_until_disconnected()
from telethon import TelegramClient, events, Button, types
from decouple import config
from ProfanityDetector import detector
import logging
from telethon.tl.functions.channels import GetParticipantRequest

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)

log = logging.getLogger(__name__)

# vars
apiid = 6
apihash = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
BOT_TOKEN = config("BOT_TOKEN", default=None)

log.info("Starting Bot...")

bot = TelegramClient("bot", apiid, apihash).start(bot_token=BOT_TOKEN)

# check admins
async def check_if_admin(message):
    result = await bot(
        GetParticipantRequest(
            channel=message.chat_id,
            user_id=message.sender_id,
        )
    )
    p = result.participant
    return isinstance(
        p, (types.ChannelParticipantCreator, types.ChannelParticipantAdmin)
    )


@bot.on(
    events.NewMessage(incoming=True, pattern="^/start$", func=lambda e: e.is_private)
)
async def start_msg(event):
    sender = await bot.get_entity(event.sender_id)
    await event.reply(
        f"Hi {sender.first_name}!\nI am a Telegram profanity detector bot.\n\nMake me admin in your group with `delete messages` permission and I'll delete messsages containing abuses!",
        buttons=[
            [Button.inline("Help", data="help")],
            [
                Button.url(
                    "Add me to a group ➕",
                    url=f"http://t.me/{(await bot.get_me()).username}?startgroup=botstart",
                )
            ],
            [
                Button.url("👨‍🔧updates Channel👨‍🔧", url="https://t.me/disneygrou"),
                Button.url(
                    "Package 📦", url="https://pypi.org/project/ProfanityDetector/"
                ),
            ],
        ],
    )


@bot.on(events.NewMessage(incoming=True, pattern="^/start", func=lambda e: e.is_group))
async def start_grp(event):
    sender = await bot.get_entity(event.sender_id)
    await event.reply(
        f"Hey {sender.first_name}!\n__I'm up, protecting this group!__\n**False positives?** Report them to @disneyteamchat!"
    )


@bot.on(events.callbackquery.CallbackQuery(data="help"))
async def helper_(event):
    sender = await bot.get_entity(event.sender_id)
    await event.edit(
        f"""
{sender.first_name}, here is the help menu.\n
**How to use?**
- Add me to a group, and make me admin, with \"delete messages\" permission.
- If the bot is not admin, it will not be deleting messages containing blacklisted words.\n
**Report False Positives:**
- You are free to report False detections in @disneyteamchat.""",
        buttons=[[Button.inline("Back", data="start")]],
    )


@bot.on(events.callbackquery.CallbackQuery(data="start"))
async def start_msg(event):
    sender = await bot.get_entity(event.sender_id)
    await event.edit(
        f"Hi {sender.first_name}!\nI am a Telegram profanity detector bot.\n\nMake me admin in your group with `delete messages` permission and I'll delete messsages containing abuses!",
        buttons=[
            [Button.inline("Help", data="help")],
            [
                Button.url(
                    "Add me to a group ➕",
                    url=f"http://t.me/{(await bot.get_me()).username}?startgroup=botstart",
                )
            ],
            [
                Button.url("👨‍🔧updates Channel👨‍🔧", url="https://t.me/disneygrou"),
                Button.url(
                    "Package 📦", url="https://pypi.org/project/ProfanityDetector/"
                ),
            ],
        ],
    )


@bot.on(events.NewMessage(incoming=True, func=lambda e: e.is_group))
async def deleter_(event):
    try:
        if await check_if_admin(event):
            return
    except:
        return
    sentence = event.raw_text
    sender = await bot.get_entity(event.sender_id)
    word, detected = detector(sentence)
    if detected:
        try:
            await event.reply(
                f"Hey {sender.first_name}, you used a blacklisted word and so your message has been deleted contact @doreamonfans1!"
            )
            await event.delete()
        except:
            log.info(f"Cannot delete messages in {(await event.get_chat()).title}.")


log.info("Bot has started!")
bot.run_until_disconnected()
from telethon import TelegramClient, events, Button, types
from decouple import config
from ProfanityDetector import detector
import logging
from telethon.tl.functions.channels import GetParticipantRequest

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)

log = logging.getLogger(__name__)

# vars
apiid = 6
apihash = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
BOT_TOKEN = config("BOT_TOKEN", default=None)

log.info("Starting Bot...")

bot = TelegramClient("bot", apiid, apihash).start(bot_token=BOT_TOKEN)

# check admins
async def check_if_admin(message):
    result = await bot(
        GetParticipantRequest(
            channel=message.chat_id,
            user_id=message.sender_id,
        )
    )
    p = result.participant
    return isinstance(
        p, (types.ChannelParticipantCreator, types.ChannelParticipantAdmin)
    )


@bot.on(
    events.NewMessage(incoming=True, pattern="^/start$", func=lambda e: e.is_private)
)
async def start_msg(event):
    sender = await bot.get_entity(event.sender_id)
    await event.reply(
        f"Hi {sender.first_name}!\nI am a Telegram profanity detector bot.\n\nMake me admin in your group with `delete messages` permission and I'll delete messsages containing abuses!",
        buttons=[
            [Button.inline("Help", data="help")],
            [
                Button.url(
                    "Add me to a group ➕",
                    url=f"http://t.me/{(await bot.get_me()).username}?startgroup=botstart",
                )
            ],
            [
                Button.url("👨‍🔧updates Channel👨‍🔧", url="https://t.me/disneygrou"),
                Button.url(
                    "Package 📦", url="https://pypi.org/project/ProfanityDetector/"
                ),
            ],
        ],
    )


@bot.on(events.NewMessage(incoming=True, pattern="^/start", func=lambda e: e.is_group))
async def start_grp(event):
    sender = await bot.get_entity(event.sender_id)
    await event.reply(
        f"Hey {sender.first_name}!\n__I'm up, protecting this group!__\n**False positives?** Report them to @disneyteamchat!"
    )


@bot.on(events.callbackquery.CallbackQuery(data="help"))
async def helper_(event):
    sender = await bot.get_entity(event.sender_id)
    await event.edit(
        f"""
{sender.first_name}, here is the help menu.\n
**How to use?**
- Add me to a group, and make me admin, with \"delete messages\" permission.
- If the bot is not admin, it will not be deleting messages containing blacklisted words.\n
**Report False Positives:**
- You are free to report False detections in @disneyteamchat.""",
        buttons=[[Button.inline("Back", data="start")]],
    )


@bot.on(events.callbackquery.CallbackQuery(data="start"))
async def start_msg(event):
    sender = await bot.get_entity(event.sender_id)
    await event.edit(
        f"Hi {sender.first_name}!\nI am a Telegram profanity detector bot.\n\nMake me admin in your group with `delete messages` permission and I'll delete messsages containing abuses!",
        buttons=[
            [Button.inline("Help", data="help")],
            [
                Button.url(
                    "Add me to a group ➕",
                    url=f"http://t.me/{(await bot.get_me()).username}?startgroup=botstart",
                )
            ],
            [
                Button.url("👨‍🔧updates Channel👨‍🔧", url="https://t.me/disneygrou"),
                Button.url(
                    "Package 📦", url="https://pypi.org/project/ProfanityDetector/"
                ),
            ],
        ],
    )


@bot.on(events.NewMessage(incoming=True, func=lambda e: e.is_group))
async def deleter_(event):
    try:
        if await check_if_admin(event):
            return
    except:
        return
    sentence = event.raw_text
    sender = await bot.get_entity(event.sender_id)
    word, detected = detector(sentence)
    if detected:
        try:
            await event.reply(
                f"Hey {sender.first_name}, you used a blacklisted word and so your message has been deleted contact @doreamonfans1!"
            )
            await event.delete()
        except:
            log.info(f"Cannot delete messages in {(await event.get_chat()).title}.")


log.info("Bot has started!")
bot.run_until_disconnected()
from telethon import TelegramClient, events, Button, types
from decouple import config
from ProfanityDetector import detector
import logging
from telethon.tl.functions.channels import GetParticipantRequest

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)

log = logging.getLogger(__name__)

# vars
apiid = 6
apihash = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
BOT_TOKEN = config("BOT_TOKEN", default=None)

log.info("Starting Bot...")

bot = TelegramClient("bot", apiid, apihash).start(bot_token=BOT_TOKEN)

# check admins
async def check_if_admin(message):
    result = await bot(
        GetParticipantRequest(
            channel=message.chat_id,
            user_id=message.sender_id,
        )
    )
    p = result.participant
    return isinstance(
        p, (types.ChannelParticipantCreator, types.ChannelParticipantAdmin)
    )


@bot.on(
    events.NewMessage(incoming=True, pattern="^/start$", func=lambda e: e.is_private)
)
async def start_msg(event):
    sender = await bot.get_entity(event.sender_id)
    await event.reply(
        f"Hi {sender.first_name}!\nI am a Telegram profanity detector bot.\n\nMake me admin in your group with `delete messages` permission and I'll delete messsages containing abuses!",
        buttons=[
            [Button.inline("Help", data="help")],
            [
                Button.url(
                    "Add me to a group ➕",
                    url=f"http://t.me/{(await bot.get_me()).username}?startgroup=botstart",
                )
            ],
            [
                Button.url("👨‍🔧updates Channel👨‍🔧", url="https://t.me/disneygrou"),
                Button.url(
                    "Package 📦", url="https://pypi.org/project/ProfanityDetector/"
                ),
            ],
        ],
    )


@bot.on(events.NewMessage(incoming=True, pattern="^/start", func=lambda e: e.is_group))
async def start_grp(event):
    sender = await bot.get_entity(event.sender_id)
    await event.reply(
        f"Hey {sender.first_name}!\n__I'm up, protecting this group!__\n**False positives?** Report them to @disneyteamchat!"
    )


@bot.on(events.callbackquery.CallbackQuery(data="help"))
async def helper_(event):
    sender = await bot.get_entity(event.sender_id)
    await event.edit(
        f"""
{sender.first_name}, here is the help menu.\n
**How to use?**
- Add me to a group, and make me admin, with \"delete messages\" permission.
- If the bot is not admin, it will not be deleting messages containing blacklisted words.\n
**Report False Positives:**
- You are free to report False detections in @disneyteamchat.""",
        buttons=[[Button.inline("Back", data="start")]],
    )


@bot.on(events.callbackquery.CallbackQuery(data="start"))
async def start_msg(event):
    sender = await bot.get_entity(event.sender_id)
    await event.edit(
        f"Hi {sender.first_name}!\nI am a Telegram profanity detector bot.\n\nMake me admin in your group with `delete messages` permission and I'll delete messsages containing abuses!",
        buttons=[
            [Button.inline("Help", data="help")],
            [
                Button.url(
                    "Add me to a group ➕",
                    url=f"http://t.me/{(await bot.get_me()).username}?startgroup=botstart",
                )
            ],
            [
                Button.url("👨‍🔧updates Channel👨‍🔧", url="https://t.me/disneygrou"),
                Button.url(
                    "Package 📦", url="https://pypi.org/project/ProfanityDetector/"
                ),
            ],
        ],
    )


@bot.on(events.NewMessage(incoming=True, func=lambda e: e.is_group))
async def deleter_(event):
    try:
        if await check_if_admin(event):
            return
    except:
        return
    sentence = event.raw_text
    sender = await bot.get_entity(event.sender_id)
    word, detected = detector(sentence)
    if detected:
        try:
            await event.reply(
                f"Hey {sender.first_name}, you used a blacklisted word and so your message has been deleted contact @doreamonfans1!"
            )
            await event.delete()
        except:
            log.info(f"Cannot delete messages in {(await event.get_chat()).title}.")


log.info("Bot has started!")
bot.run_until_disconnected()
from telethon import TelegramClient, events, Button, types
from decouple import config
from ProfanityDetector import detector
import logging
from telethon.tl.functions.channels import GetParticipantRequest

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)

log = logging.getLogger(__name__)

# vars
apiid = 6
apihash = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
BOT_TOKEN = config("BOT_TOKEN", default=None)

log.info("Starting Bot...")

bot = TelegramClient("bot", apiid, apihash).start(bot_token=BOT_TOKEN)

# check admins
async def check_if_admin(message):
    result = await bot(
        GetParticipantRequest(
            channel=message.chat_id,
            user_id=message.sender_id,
        )
    )
    p = result.participant
    return isinstance(
        p, (types.ChannelParticipantCreator, types.ChannelParticipantAdmin)
    )


@bot.on(
    events.NewMessage(incoming=True, pattern="^/start$", func=lambda e: e.is_private)
)
async def start_msg(event):
    sender = await bot.get_entity(event.sender_id)
    await event.reply(
        f"Hi {sender.first_name}!\nI am a Telegram profanity detector bot.\n\nMake me admin in your group with `delete messages` permission and I'll delete messsages containing abuses!",
        buttons=[
            [Button.inline("Help", data="help")],
            [
                Button.url(
                    "Add me to a group ➕",
                    url=f"http://t.me/{(await bot.get_me()).username}?startgroup=botstart",
                )
            ],
            [
                Button.url("👨‍🔧updates Channel👨‍🔧", url="https://t.me/disneygrou"),
                Button.url(
                    "Package 📦", url="https://pypi.org/project/ProfanityDetector/"
                ),
            ],
        ],
    )


@bot.on(events.NewMessage(incoming=True, pattern="^/start", func=lambda e: e.is_group))
async def start_grp(event):
    sender = await bot.get_entity(event.sender_id)
    await event.reply(
        f"Hey {sender.first_name}!\n__I'm up, protecting this group!__\n**False positives?** Report them to @disneyteamchat!"
    )


@bot.on(events.callbackquery.CallbackQuery(data="help"))
async def helper_(event):
    sender = await bot.get_entity(event.sender_id)
    await event.edit(
        f"""
{sender.first_name}, here is the help menu.\n
**How to use?**
- Add me to a group, and make me admin, with \"delete messages\" permission.
- If the bot is not admin, it will not be deleting messages containing blacklisted words.\n
**Report False Positives:**
- You are free to report False detections in @disneyteamchat.""",
        buttons=[[Button.inline("Back", data="start")]],
    )


@bot.on(events.callbackquery.CallbackQuery(data="start"))
async def start_msg(event):
    sender = await bot.get_entity(event.sender_id)
    await event.edit(
        f"Hi {sender.first_name}!\nI am a Telegram profanity detector bot.\n\nMake me admin in your group with `delete messages` permission and I'll delete messsages containing abuses!",
        buttons=[
            [Button.inline("Help", data="help")],
            [
                Button.url(
                    "Add me to a group ➕",
                    url=f"http://t.me/{(await bot.get_me()).username}?startgroup=botstart",
                )
            ],
            [
                Button.url("👨‍🔧updates Channel👨‍🔧", url="https://t.me/disneygrou"),
                Button.url(
                    "Package 📦", url="https://pypi.org/project/ProfanityDetector/"
                ),
            ],
        ],
    )


@bot.on(events.NewMessage(incoming=True, func=lambda e: e.is_group))
async def deleter_(event):
    try:
        if await check_if_admin(event):
            return
    except:
        return
    sentence = event.raw_text
    sender = await bot.get_entity(event.sender_id)
    word, detected = detector(sentence)
    if detected:
        try:
            await event.reply(
                f"Hey {sender.first_name}, you used a blacklisted word and so your message has been deleted contact @doreamonfans1!"
            )
            await event.delete()
        except:
            log.info(f"Cannot delete messages in {(await event.get_chat()).title}.")


log.info("Bot has started!")
bot.run_until_disconnected()
