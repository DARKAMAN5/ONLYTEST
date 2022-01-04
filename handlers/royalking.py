from config import (
    BOT_USERNAME,
    que,
)
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import authorized_users_only
from helpers.filters import command, other_filters
from helpers.chattitle import CHAT_TITLE
from callsmusic.callsmusic import client as USER


@Client.on_message(command(["join", f"join@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
@sudo_users_only
async def join(client, message):
    chat_id = message.chat.id
    try:
        link = await client.export_chat_invite_link(chat_id)
    except BaseException:
        await message.reply("**Error:**\nAdd me as admin of your group!")
        return
    try:
        await USER.join_chat(link)
        await message.reply("**Userbot Joined**")
    except UserAlreadyParticipant:
        await message.reply("**Userbot Already Participant**")
