#ππ°πΈπ³ πΏππΎπΉπ΄π²π 
#ππ πΌπΎππ·π΄ππ΅ππ²πΊπ΄π πΈπ΅ π πΊπ°π½πΆ π°π½π³ π³πΎπ½'π πΆπΈππ΄ π²ππ΄π³πΈππ π‘
#πΌπΎπ³πΈπ΅π΄π³ π΅πΎπ π°π»π΄ππ° πΌπππΈπ² 

from os import path

from pyrogram import Client, filters
from pyrogram.types import Message

from time import time
from datetime import datetime
from config import ALIVE_IMG, BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command, other_filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(filters.command(["alive", f"alive@{BOT_USERNAME}"]))
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=f"""**ΰΌβπ ππ π,π  [{BOT_NAME}](https://t.me/{BOT_USERNAME})**

 **ΰΌβππππππ πππππ πππππππ ππππ
**

 **ΰΌβπ₯πππππ πππππ πππππππΰΌββ€ πΆ.π½.πΆ ππππππ**

 **ΰΌβπ₯πππππΰΌββ€ [{OWNER_NAME}](https://t.me/{OWNER_NAME})**

 **ΰΌβπΈππππππΰΌββ€ `{uptime}`**

**ΰΌβπ₯ππππ πππ πππππ πππππ πππππΰΌββ€**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ΰΌβπΊπππππππΰΌββ€", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "ΰΌβπ₯πππππππΰΌββ€", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""β¨ **πππππ** {message.from_user.mention()} !
Β» **press the button below to read the explanation and see the list of available commands !**
β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="ΰΌβππππππ πππππΰΌββ€", callback_data="cbguide")]]
        ),
    )

@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    delta_ping = time() - start
    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=f"`γ β α­ΟΙ³Φ! β γ`\n" f"γπ₯`{delta_ping * 1000:.3f} ms`γ")


@Client.on_message(filters.command(["uptime", f"uptime@{BOT_USERNAME}"]))
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=f"""**ΰΌβππππ ππππππΰΌββ€ β\n**
 **ΰΌβπ₯ππππππΰΌββ€ β** `{uptime}`\n**
 **ΰΌβπΊπππππ ππππΰΌββ€ β** `{START_TIME_ISO}`**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ΰΌβπ₯πππππππΰΌββ€", url=f"https://t.me/{UPDATES_CHANNEL}"
                   )
                ]
            ]
        )
    ) 
