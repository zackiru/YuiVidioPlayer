import asyncio
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from helper.filters import command
from helper.decorators import authorized_users_only, errors
from bot.videoplayer import app as USER
from config import BOT_USERNAME, SUDO_USERS


@Client.on_message(command(["join", f"join@{BOT_USERNAME}"]) & ~filters.private & ~filters.bot)
@errors
async def entergroup(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>💡 promote me as admin first to do that !</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "assistant"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "🤖: i'm joined here for streaming video on video chat")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>✅ assistant already entered this group</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🔴 FLOODWAIT ERROR 🔴\n\n user {user.first_name} couldn't join your group due to heavy join requests for userbot! make sure assistant is not banned in this group."
        )
        return
    await message.reply_text(
        "<b>✅ assistant userbot joined your chat</b>",
    )


@Client.on_message(command(["leave", f"leave@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def leavegroup(client, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            "<b>❌ assistant can't leave from group because floodwaits.\n\n» you can manually kick me from this group</b>"
        )

        return


@Client.on_message(command(["leaveall", f"leaveall@{BOT_USERNAME}"]))
async def outall(client, message):
    if message.from_user.id not in SUDO_USERS:
        return

    left=0
    failed=0
    lol = await message.reply("🔁 assistant leaving all chats")
    async for dialog in USER.iter_dialogs():
        try:
            await USER.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(f"🔁 assistant leaving...\n⏳ Left: {left} chats.\n\n❌ Failed: {failed} chats.")
        except:
            failed += 1
            await lol.edit(f"🔁 assistant leaving...\n⏳ Left: {left} chats.\n\n❌ Failed: {failed} chats.")
        await asyncio.sleep(0.7)
    await client.send_message(message.chat.id, f"✅ Left {left} chats.\n\n❌ Failed {failed} chats.")
