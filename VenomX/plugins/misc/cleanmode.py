import asyncio
from datetime import datetime, timedelta

from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.errors import FloodWait
from pyrogram.raw import types

import config
from config import adminlist, chatstats, clean, userstats
from VenomX import app, userbot
from VenomX.misc import SUDOERS
from VenomX.utils.database import (get_active_chats,
                                       get_authuser_names, get_client,
                                       
 get_served_chats,
 get_served_users, is_cleanmode_on, set_queries)
                                       
from VenomX.utils.decorators.language import language
from VenomX.utils.formatters import alpha_to_int

AUTO_DELETE = config.CLEANMODE_DELETE_MINS
AUTO_SLEEP = 5
IS_BROADCASTING = False
cleanmode_group = 15