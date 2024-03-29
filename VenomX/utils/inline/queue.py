from typing import Union
from config import OWNER_ID, SUPPORT_CHAT

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    not_dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
            ),
        ],
         [
            InlineKeyboardButton(
                text="✅ Digər Botlar", url=f"https://t.me/oToBoTBLoG",
            ),
            InlineKeyboardButton(
                text="🩶 Kanal", url="https://t.me/Trouvaille_7",
            ),
        ],
    ]
    dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_2"].format(played, dur),
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
            ),
        ],
         [
            InlineKeyboardButton(
                text="✅ Digər Botlar", url=f"https://t.me/oToBoTBLoG",
            ),
            InlineKeyboardButton(
                text="🩶 Kanal", url="https://t.me/Trouvaille_7",
            ),
        ],
    ]
    upl = InlineKeyboardMarkup(not_dur if DURATION == "Unknown" else dur)
    return upl


def queue_back_markup(_, CPLAY):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"queue_back_timer {CPLAY}",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
           ],
             [
            InlineKeyboardButton(
                text="✅ Digər Botlar", url=f"https://t.me/oToBoTBLoG",
            ),
            InlineKeyboardButton(
                text="🩶 Kanal", url="https://t.me/Trouvaille_7",
            ),
        ],
        ]
    )
    return upl


def aq_markup(_, chat_id):
    buttons = [
         [
            InlineKeyboardButton(
                text="✅ Digər Botlar", url=f"https://t.me/oToBoTBLoG",
            ),
            InlineKeyboardButton(
                text="🩶 Kanal", url="https://t.me/Trouvaille_7",
            ),
        ],
    ]
    return buttons
