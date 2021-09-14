from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
Setting up
1) Add this Bot to your Group and Make it Admin 
2) Add @YuiVideoPlayer to your Group 
Commands
=>> Vidio Playing 🎧
- /stream : Reply to Video or File That You Want To stream In Vc.
- /stop  : Stop the stream
- /start :Start the bot
- /help  :To Help You
- /ly   : To Get lyrics Of Song
- /song : To Get Link From Youtube
- /quote: To Get Anime quote
- /tts : Replay to any text you want to make audio
- /uptime - check the bot uptime status
- /sysinfo - show the bot system information

**=>> More tools 🧑‍🔧**
- /join: Invite @YuiVideoPlayer Userbot to your chat

**=>> Commands for Sudo Users ⚔️**
 - /leaveall - remove assistant from all chats
 - /broadcast <reply to message> - globally brodcast replied message to all chats
*Sudo Users can execute any command in any groups

 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎵 Support Chat", url="https://t.me/safothebot"
                    )
                ]
            ]
        )
    )    
