import requests
import rapidjson as json
from PIL import Image
import os
import asyncio
import re
from config import BOT_TOKEN
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.command("quote"))
def quote(_, message):
    quote = requests.get("https://animechan.vercel.app/api/random").json()
    message.reply_text('`'+quote['quote']+'`\n '+quote['anime']+' (In '+quote['character']+')')
