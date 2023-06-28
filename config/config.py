import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

if os.path.exists("Internal"):
   load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
que = {}
admins = {}

#------------------------ Important Stuff 🤎 -----------------------

APP_ID = int(getenv("APP_ID", "23243649"))
API_HASH = getenv("API_HASH", "9ce91443843c0cad8c2cb16455f2b65f")
TG_BOT_TOKEN = getenv("TG_BOT_TOKEN", "5939229355:AAHq0cfdEa3qZp7QaorQlxjny4qwtBbb-QI")
TG_BOT_USERNAME = getenv("TG_BOT_USERNAME", "smsxxnbot")
STRING_SESSION = getenv("STRING_SESSION", "1BJWap1wBuwbkFT8xPrc0xBFMvIGrpOgvQ5_WyqwXqhy-E4z4uLvgI0TsVkxS7ij_6x_r7n1sRuvMFzUGkc8ot8mk7emAzLkEfHT6YbZPkpxlGQ8e39wh2JnQjHHMe6g7RM_LGL1Ng94ARkXZRDx3M74VmsPhesey2Z1Tl0lgc3mt-yW5abnTGe3P27pxOkqihf1MdVbEwWQSdvHnbNVuQ5m1z0pAwbrJGtBZ-uFsyY63YZ3I-p4rPvgntEO8MflB2Pbp8peGxvwx22hPv-kAJY7e48L5RHmOFsz9VFdTZNIQtxSjB5O_Q4y0D6q7PiW37JVYUpKjcNgRphjc1n_fOtSs8E-BgcQ=")
COMMAND_HAND_LER = list(getenv("COMMAND_HAND_LER", ".").split())
ENV = getenv("ENV", "ANYTHING")

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid ••••••••••• 
DATABASE_URL = getenv("DATABASE_URL", "postgres://saclkzuf:Qvo7hD5AHcSwJpNZJvac9UKZgjOrQ1TF@snuffleupagus.db.elephantsql.com/saclkzuf")
