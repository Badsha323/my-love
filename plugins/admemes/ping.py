"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "ʏᴇs ɪ ᴀᴍ ᴀʟɪᴠᴇ 🥱 ᴍʏ ʟɪꜰᴇ ɪs ɴᴏᴛ ᴇᴀsʏ , ᴇᴠᴇʀʏ ᴛɪᴍᴇ ᴇᴠᴇʀʏ sᴇᴄᴇɴᴅ ɪ ʜᴀᴠᴇ ᴛᴏ ᴀᴄᴄᴇᴘᴛ ᴡɪsʜᴇs ᴏꜰ ᴍᴀɴʏ ᴘᴇᴏᴘʟᴇ 😇" 
REPO = "<b>ʀᴇᴘᴏ ᴘʀɪᴄᴇ ɪs 2.5ᴋ ... ᴄᴏɴᴛᴀᴄᴛ ›› https://t.me/PAY_FOR_BOTS</b>"
CHANNEL = "<b>𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻</b> ›› https://youtube.com/channel/UCFjqpS7MmN42sybrG0Vr0NQ\n\n<b>𝚄𝙿𝙳𝙰𝚃𝙴𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ›› https://t.me/+plmG4aUd4Gw4MGE1</b>\n\n<b>ɢʀᴏᴜᴘ ›› https://t.me/Badsha_OTT</b>"
AJAX = "<b>𝙱𝙾𝚃 ›› https://t.me/BetterFilters_Bot</b>"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)


@Client.on_message(filters.command("group", COMMAND_HAND_LER) & f_onw_fliter)
async def group(_, message):
    await message.reply_text(GROUP)


@Client.on_message(filters.command("channel", COMMAND_HAND_LER) & f_onw_fliter)
async def channel(_, message):
    await message.reply_text(CHANNEL)


@Client.on_message(filters.command("ajax", COMMAND_HAND_LER) & f_onw_fliter)
async def ajax(_, message):
    await message.reply_text(AJAX)


