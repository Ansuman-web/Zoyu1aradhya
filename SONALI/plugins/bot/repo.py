from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI import app
from config import BOT_USERNAME
from SONALI.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
ॐ 
भूर्भुवः
स्वः तत्सवितुर्वरेण्यं 
भर्गो देवस्य धीमहि 
धियो यो नः प्रचोदयात्
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔ᴅᴅ ᴍᴇ 𝗠ᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗗𝗽_𝗰𝗼𝗹𝗹𝗲𝗰𝘁𝗶𝗼𝗻", url="https://t.me/DP_WORLD7"),
          InlineKeyboardButton("𝙕𝙀𝙐𝙎", url="https://t.me/unbornedvillian"),
          ],
               [
                InlineKeyboardButton("𝗧ᴇᴀᴍ 𝗜ɴᴄʀɪᴄɪʙʟᴇ 𝗕ᴏᴛs", url=f"https://t.me/ll_BOTCHAMBER_ll"),
],
[
InlineKeyboardButton("𝗠ᴀɪɴ 𝗕ᴏᴛ", url=f"https://t.me/ZEUS_MUSIC_ROBOT"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/82343d78ee04548159967-2e2723755765f6a6d5.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
