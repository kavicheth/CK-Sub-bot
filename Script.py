class script(object):
    START_TXT = """<b>ʜᴇʏ {}, <i>{}</i>
    
මම සබ් හොයන බොටෙක්🤖. මං ලග ගොඩක් සිංහල සබ් තියෙනවා😏. මගේ වැඩ බලන්න මාව ඔයාගේ group එකට add කරලා මට admin දීලා බලන්න⚡. ආස හිතෙයි💗.

👨🏻‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=https://t.me/KING_WMP>Chethmina Kavishan</a></b>"""

    MY_ABOUT_TXT = """<b>🤖 ᴍʏ ɴᴀᴍᴇ: <a href=https://t.me/SinhalaSubCK_Bot>Sinhala Sub Bot</a>
👨🏻‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=https://t.me/KING_WMP>Chethmina Kavishan</a>
📡 ꜱᴇʀᴠᴇʀ: <a href=https://www.heroku.com>Heroku</a>
🗄 ᴅᴀᴛᴀʙᴀꜱᴇ: <a href=https://www.mongodb.com>MongoDB</a>
📝 ʟᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Python</a>
📚 ʟɪʙʀᴀʀʏ: <a href=https://pyrogram.org>Pyrogram</a>
📢 ᴜᴘᴅᴀᴛᴇꜱ: <a href=https://t.me/CK4U2>CK4U2</a></b>"""

    MY_OWNER_TXT = """<b>👨🏻‍💻 Name: Chethmina Kavishan
🔎 Username: @KING_WMP
🔮 About: @About_KingWMP
🔑 ID: <code>5042338756</code>
🌍 Country: Sri Lanka🇱🇰</b>"""

    STATUS_TXT = """🗂 Total Files: <code>{}</code>
👤 Total Users: <code>{}</code>
👥 Total Chats: <code>{}</code>
🤑 Premium Users: <code>{}</code>
✨ Used Storage: <code>{}</code>
🗳 Free Storage: <code>{}</code>
🚀 Bot Uptime: <code>{}</code>"""

    NEW_GROUP_TXT = """#NewGroup
Title - {}
ID - <code>{}</code>
Username - {}
Total - <code>{}</code>"""

    NEW_USER_TXT = """#NewUser
★ Name: {}
★ ID: <code>{}</code>"""

    NO_RESULT_TXT = """#NoResult
★ Group Name: {}
★ Group ID: <code>{}</code>
★ Name: {}

★ Message: {}"""

    REQUEST_TXT = """★ Name: {}
★ ID: <code>{}</code>

★ Message: {}"""

    NOT_FILE_TXT = """👋 Hello {},

I can't find the <b>{}</b> in my database! 🥲

මං ලග සබ් එක නෑ වගේ. #request කියලා ඔයාල ඉල්ලපු සබ් එකේ නම් දාන්න."""
    
    EARN_TXT = """<b>ʜᴏᴡ ᴛᴏ ᴇᴀʀɴ ꜰʀᴏᴍ ᴛʜɪs ʙᴏᴛ

➥ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴇᴀʀɴ ᴍᴏɴᴇʏ ʙʏ ᴜsɪɴɢ ᴛʜɪꜱ ʙᴏᴛ.

» sᴛᴇᴘ 1:- ғɪʀsᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴀᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ.

» sᴛᴇᴘ 2:- ᴍᴀᴋᴇ ᴀᴄᴄᴏᴜɴᴛ ᴏɴ <a href=https://telegram.me/how_to_download_channel/14>mdisklink.link</a> [ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴜsᴇ ᴏᴛʜᴇʀ sʜᴏʀᴛɴᴇʀ ᴡᴇʙsɪᴛᴇ ]

» sᴛᴇᴘ 3:- ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ɢɪᴠᴇɴ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ sʜᴏʀᴛɴᴇʀ ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ.

➥ ᴛʜɪꜱ ʙᴏᴛ ɪs ꜰʀᴇᴇ ꜰᴏʀ ᴀʟʟ, ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘs ғᴏʀ ꜰʀᴇᴇ ᴏꜰ ᴄᴏꜱᴛ.</b>"""

    HOW_TXT = """<b>ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ‼️

➥ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ᴛʜᴇɴ ᴊᴜsᴛ sᴇɴᴅ ᴛʜᴇ ɢɪᴠᴇɴ ᴅᴇᴛᴀɪʟs ɪɴ ᴄᴏʀʀᴇᴄᴛ ꜰᴏʀᴍᴀᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ

➥ ғᴏʀᴍᴀᴛ ↓↓↓

<code>/set_shortlink sʜᴏʀᴛɴᴇʀ sɪᴛᴇ sʜᴏʀᴛɴᴇʀ ᴀᴘɪ</code>

➥ ᴇxᴀᴍᴘʟᴇ ↓↓↓

<code>/set_shortlink mdisklink.link 5843c3cc645f5077b2200a2c77e0344879880b3e</code>

➥ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄʜᴇᴄᴋ ᴡʜɪᴄʜ sʜᴏʀᴛᴇɴᴇʀ ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛʜᴇɴ sᴇɴᴅ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ /get_shortlink

📝 ɴᴏᴛᴇ:- ʏᴏᴜ sʜᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ ɪɴ ɢʀᴏᴜᴘ. sᴇɴᴅ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜᴏᴜᴛ ʙᴇɪɴɢ ᴀɴ ᴀɴᴏɴʏᴍᴜs ᴀᴅᴍɪɴ.</b>"""

    IMDB_TEMPLATE = """✅ I Found: <code>{query}</code>

<b>🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating} / 10</a>
🔊 Languages: {languages}
⏰ RunTime: {runtime} Minutes</b>

ʀᴇQᴜᴇꜱᴛᴇᴅ ʙʏ: {message.from_user.mention}

<b>⚡ᴘᴏᴡᴇʀᴇᴅ ʙʏ <i>@CK4U2</i></b>"""

    FILE_CAPTION = """<b>🎞ɴᴀᴍᴇ:</b> <code>{file_name}</code>
<b>📥ꜱɪᴢᴇ: {file_size}</b>

<b>⚡ᴘᴏᴡᴇʀᴇᴅ ʙʏ <i>@CK4U2</i></b>"""

    WELCOME_TEXT = """👋 Hello {mention}, Welcome to {title} group! 💞"""

    HELP_TXT = """<b>Note - <spoiler>Try each command without any argument to see more details 😹</spoiler></b>"""
    
    ADMIN_COMMAND_TXT = """<b>Here is bot admin commands 👇

/index_channels - to check how many index channel id added
/delete - to delete files using query
/delete_all - to delete all indexed file
/broadcast - to send message to all bot users
/grp_broadcast - to send message to all groups
/pin_broadcast - to send message as pin to all bot users.
/pin_grp_broadcast - to send message as pin to all groups.
/restart - to restart bot
/leave - to leave your bot from particular group
/unban_grp - to enable group
/ban_grp - to disable group
/ban_user - to ban a users from bot
/unban_user - to unban a users from bot
/users - to get all users details
/chats - to get all groups
/invite_link - to generate invite link
/index - to index bot accessible channels</b>"""
    
    USER_COMMAND_TXT = """<b>Here is bot user commands 👇

/start - to check bot alive or not
/stats - to get bot status
/settings - to change group settings as your wish
/set_shortlink - group admin can set custom shortlink
/get_custom_settings - to get your group settings details
/set_welcome - to set custom new joined users welcome message for group
/set_tutorial - to set custom tutorial link in result page button
/id - to check group or channel id</b>"""

    SOURCE_TXT = """<b>🔮ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ- <a href=https://t.me/+VhJIV2F3RxljNTNl>Click Here</a>

👨🏻‍💻ᴅᴇᴠʟᴏᴘᴇʀ - <a href=https://telegram.me/KING_WMP>Chethmina Kavishan</a>
⚡ᴘᴏᴡᴇʀᴇᴅ ʙʏ - <a href=https://telegram.me/CK4U2>CK4U2</a></b>"""

    SPAM_TXT = """{} Don't Spam, Wait For {}

Else, You Can Buy Our Subscriptions.
<a href={}>Click Here</a> To Learn More"""
