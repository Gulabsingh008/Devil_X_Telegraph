from pyrogram import StopPropagation
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message
)
from pyrogram import Client, filters


joinButton = InlineKeyboardMarkup([
    [InlineKeyboardButton(
        "😈𝙾𝙽𝚆𝙴𝚁😈",
        url="http://t.me/mrdevil12")],
    [InlineKeyboardButton(
        "🔥𝚄𝙿𝙳𝙰𝚃𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻🔥",
        url="https://t.me/devilbots971")],
    [InlineKeyboardButton(
        "🔥𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿🔥",
        url="https://t.me/devilbotsupport")],
])


@Client.on_message(filters.command("start"))
async def start(_, ryui: Message):
    user_and_chats = ryui.from_user.first_name
    await ryui.reply_photo(
        "https://graph.org/file/b609a772e749668d82661.jpg",
        reply_markup=joinButton,
        caption=f"""ᗪEᐯIᒪ ᙭ TEᒪEGᖇᗩᑭᕼ
             𝐇𝐎𝐖 𝐀𝐑𝐄 𝐘𝐎𝐔 **__`{user_and_chats}`__**,
           
🏷 ɪᴍᴀɢᴇ ᴛᴏ ᴜʀʟ ʙᴏᴛ ᴄᴀɴ ᴄᴏɴᴠᴇʀᴛ ᴛʜᴇꜱᴇ ʙᴇʟᴏᴡ ꜰɪʟᴇ ᴛʏᴘᴇꜱ ᴛᴏ [ᴛᴇʟᴇɢʀᴀᴘʜ](https://pypi.org/project/telegraph/) ᴜʀʟ.
🏷 ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴘʜᴏᴛᴏ ᴇɪᴛʜᴇʀ ɪɴ ᴄᴏᴍᴘʀᴇꜱꜱᴇᴅ ᴏʀ ᴜɴᴄᴏᴍᴘʀᴇꜱꜱᴇᴅ ꜰᴏʀᴍᴀᴛ
- `JPG`
- `JPEG`
- `PNG`
- `GIF` __(send as a document)__
- `Mp4` __(send as a document)__
- `Mp3` __(send as a document)__
🏷 ᴋᴇᴇᴘ ꜱᴇɴᴅɪɴɢ ʏᴏᴜʀ ʀᴇQᴜɪʀᴇᴅ ᴛʏᴘᴇ ꜰɪʟᴇꜱ ᴏɴᴇ ʙʏ ᴏɴᴇ.
🏷 ꜰɪʟᴇꜱ ᴍᴏʀᴇ ᴛʜᴇɴ 5ᴍʙ ɪꜱ ɴᴏᴛ ꜱᴜᴘᴘᴏʀᴛᴇᴅ ʙʏ ᴛᴇʟᴇɢʀᴀᴘʜ.


🖥 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃 𝙸𝚂 𝙲𝚁𝙴𝙰𝚃𝙴𝙳 𝙱𝚈 [𝙈𝙍 𝘿𝙀𝙑𝙄𝙇](http://t.me/mrdevil12)
𝙵𝙾𝚁 𝚄𝙿𝙳𝙰𝚃𝙴 𝙹𝙾𝙸𝙽 𝙾𝚄𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻  [𝘿𝙀𝙑𝙄𝙇 𝘽𝙊𝙏'𝙎](https://t.me/devilbots971)""")
    raise StopPropagation
