import asyncio
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from bot.videoplayer import app
from bot.videoplayer import call_py
bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="bot"),
)


bot.start()
app.start()
call_py.start()
idle()
