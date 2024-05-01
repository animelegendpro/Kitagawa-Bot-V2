# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper




from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>๏ Creator :</b> <a href='tg://user?id={OWNER_ID}'>This Person</a>\n<b>๏ Language :</b> <code>Python3</code>\n<b>๏ Library :</b> <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n<b>๏ Source Code :</b> <a href='https://github.com'>Click here</a>\n<b>๏ Channel :</b> <a href='https://t.me/ZPro_Bots_V1'>ZPro Bots V1</a>\n<b>๏ Support Group :</b> <a href='https://t.me/+FGM0HOnjDC45ZDk1'>Support</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
