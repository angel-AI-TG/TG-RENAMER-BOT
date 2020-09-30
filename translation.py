from sample_config import Config

class Translation(object):
    START_TEXT = """Hello <i><b>{}</b></i>,

This is a simple Telegram Rename Bot!

I Can rename ✍ with custom thumbnail and upload as video/file

Type /help for more details."""
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "Jσιɳ συɾ ƈԋαɳɳҽʅ\n  @AI_bot_projects"
    DOWNLOAD_START_VIDEO = "Downloading to my server.....📥\nplease wait"
    DOWNLOAD_START = "Downloading to my server.....📥\nplease wait"
    UPLOAD_START_VIDEO = "Uploading as video.....📤\nplease wait"
    UPLOAD_START = "Uploading as File.....📤\nplease wait"
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations.I can't do anything for that 🤷‍♂️."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "**Thank you for Using Me🤓.**\n\n[Jσιɳ συɾ ƈԋαɳɳҽʅ](https://t.me/AI_bot_projects)**"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://t.me/Ns_Bot_supporters'>Ns Bot Supporters</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Custom File thumbnail saved ✅️ . This image will be deleted with in 24hr"
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = "\n\nrenamed by\n@TGrenamebyAI_bot"
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_PLAN_DETAILS = """Current plan details
--------
Telegram ID: <code>{}</code>
Plan name: Free User
Expires on: 22ᵗʰ every month"""
    HELP_USER = """Hai <b><i>{}</i></b>, 


📌 If you need custom Thumbnail send the picture first (Optional)..

📌 Now Send me any Telegram File which you want to Rename .

📌 Reply to that message with <code>/rename new name.extension</code>. with custom thumbnail support.\n(upload as file)

📌 Reply to that message with <code>/rename_video new name.extension</code>. with custom thumbnail support.\n(uploading as Video)

   
<b>⚠️ Do one By One rename. Otherwise you will get Permenent Ban 🤷 ⚠️</b>

--------
Send /plan to know current plan details

Support Group : @AI_BOT_HELP"""
    REPLY_TO_DOC_FOR_RENAME_FILE = "🤦‍♂️ Reply to a Telegram media to `/rename New Name.extension` with custom thumbnail support.\n\n(For uploading as file).\n\nSee /help for mor information. "
    REPLY_TO_DOC_FOR_RENAME_VIDEO = "🤦‍♂️ Reply to a Telegram media to `/rename_video New Name.extension` with custom thumbnail support.\n\n(For uploading as video).\n\nSee /help for mor information."
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    IFLONG_FILE_NAME = """File Name limit allowed by Telegram is {alimit} characters.
The given file name has {num} characters.

<b>Essays Not allowed in Telegram file name!</b>
©️ <code>@TGrenamebyAI_bot</code>
Please short your file name and try again!"""

    About = """Hi __{}__,

**📝 Language:** Python 3

**🧰 Framework:** Pyrogram

**📮 Channel:** [AI BOT UPDATES](https://t.me/AI_bot_projects)

**👥 Group:** [AI BOT HELP](https://t.me/AI_BOT_HELP)

**💻 Source Code:**[Press Me](https://t.me/AI_bots_code)"""
