from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("info")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
=> Bot Devlopers
1) @PiroXPower
2) @ProErrorXD
3) @unk_937
4) @AmiFutami
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
