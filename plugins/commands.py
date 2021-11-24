#credits - @pro_editor_tg @Joel_TG
import os
import time
import random
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from makkiri import START_MSG, CHANNELS, BANANA_BOI, AUTH_CHANNEL, CUSTOM_FILE_CAPTION
from utils import Media, get_file_details, get_size
from pyrogram.errors import UserNotParticipant
logger = logging.getLogger(__name__)

#stiker code kanged from @M_STER_TECH Channel !
#Add atleast 10+ Telegraph Links below 👇


MY_PIC = ["CAACAgUAAxkBAAEBV_hhnO9mZLq_YATtWpvPxRTUhvjqeQAClgAD7uqpLAoAAQFBgJ8y7x4E",
         "CAACAgUAAxkBAAEBV-hhnO87tRtiWOslzd7kJoO6uMDqbwACfQAD7uqpLHiaMiwKjyisHgQ",
         "CAACAgUAAxkBAAEBV-phnO9GxKZm8vA_b7VEbP6TGPOAOgACgAAD7uqpLETLm5t-yXJUHgQ",
         "CAACAgUAAxkBAAEBV-xhnO9K_TFC-3TuajXPprC40WP6KwACgQAD7uqpLKRHI19IyL5NHgQ",
         "CAACAgUAAxkBAAEBV-5hnO9LxgOYmb2NqTs7uvuAG-KIrwACggAD7uqpLAvrpPParzAvHgQ",
         "CAACAgUAAxkBAAEBV_BhnO9biV_3-KsHJIp47i76kwJggwAChgAD7uqpLOku03Tua9aFHgQ",
         "CAACAgUAAxkBAAEBV_JhnO9cB5V9E3qLUT_LfA7TkKJaNgAChQAD7uqpLNBghwABo7Sc3B4E",
         "CAACAgUAAxkBAAEBV_RhnO9fsJ5-wU8ghSBzLSkj4GgWawAChAAD7uqpLEk9Cot9nB5nHgQ",
         "CAACAgUAAxkBAAEBV_hhnO9mZLq_YATtWpvPxRTUhvjqeQAClgAD7uqpLAoAAQFBgJ8y7x4E",
         "CAACAgUAAxkBAAEBV_phnPATrg1b_lTal3A47TwCymRVQQACngAD7uqpLPs6j7QpOZk1HgQ",
         "CAACAgUAAxkBAAEBV_xhnPAWaMY502YFmo76LTMAAaKymR0AAqAAA-7qqSzkkOBFTuodoR4E",
         "CAACAgUAAxkBAAEBV_5hnPAYeQfROqWoJGvjbCKJ_PCcuAACnwAD7uqpLFloH7kzgOP-HgQ",
         "CAACAgUAAxkBAAEBWAJhnPBTrYJipkenlfb1iaLfcI86ngAC0wAD7uqpLEa3xUskHaiGHgQ",
]

@Client.on_message(filters.private & filters.user(BANANA_BOI) & filters.command(["broadcast"]))
async def broadcast(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("Geting All ids from database ...........")
   ids = getid()
   tot = len(ids)
   await ms.edit(f"Starting Broadcast .... \n Sending Message To {tot} Users")
   for id in ids:
     try:
     	await message.reply_to_message.copy(id)
     except:
     	pass


@Client.on_message(filters.command("start"))
async def start(bot, cmd):
    usr_cmdall1 = cmd.text
    if usr_cmdall1.startswith("/start subinps"):
        if AUTH_CHANNEL:
            invite_link = await bot.create_chat_invite_link(int(AUTH_CHANNEL))
            try:
                user = await bot.get_chat_member(int(AUTH_CHANNEL), cmd.from_user.id)
                if user.status == "kicked":
                    await bot.send_message(
                        chat_id=cmd.from_user.id,
                        text="Sorry Sir, You are Banned to use me.",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                ident, file_id = cmd.text.split("_-_-_-_")
                await bot.send_message(
                    chat_id=cmd.from_user.id,
                    text="**Please Join My Updates Channel to use this Bot!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🤖 Join Updates Channel", url='https://t.me/tg_bots_updates')
                            ],
                            [
                                InlineKeyboardButton(" 🔄 Try Again", callback_data=f"checksub#{file_id}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await bot.send_message(
                    chat_id=cmd.from_user.id,
                    text="Something went Wrong.",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        try:
            ident, file_id = cmd.text.split("_-_-_-_")
            filedetails = await get_file_details(file_id)
            for files in filedetails:
                title = files.file_name
                size=get_size(files.file_size)
                f_caption=files.caption
                if CUSTOM_FILE_CAPTION:
                    try:
                        f_caption=CUSTOM_FILE_CAPTION.format(file_name=title, file_size=size, file_caption=f_caption)
                    except Exception as e:
                        print(e)
                        f_caption=f_caption
                if f_caption is None:
                    f_caption = f"{files.file_name}"
                buttons = [
                    [
                        InlineKeyboardButton('🔍Search again🔎', switch_inline_query_current_chat=''),
                        InlineKeyboardButton('🤖More Bots🤖', url='https://t.me/tg_bots_updates')
                    ]
                    ]
                await bot.send_cached_media(
                    chat_id=cmd.from_user.id,
                    file_id=file_id,
                    caption=f_caption,
                    reply_markup=InlineKeyboardMarkup(buttons)
                    )
        except Exception as err:
            await cmd.reply_text(f"Something went wrong!\n\n**Error:** `{err}`")
    elif len(cmd.command) > 1 and cmd.command[1] == 'subscribe':
        invite_link = await bot.create_chat_invite_link(int(AUTH_CHANNEL))
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**Please Join My Updates Channel to use this Bot!**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 Join Updates Channel", url='https://t.me/tg_bots_updates')
                    ]
                ]
            )
        )
    else:
         await bot.send_sticker(
             sticker=random.choice(MY_PIC),
             reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("➕ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ➕", url="https://t.me/Dqautofl_bot?startgroup=true")
                    ],[
                        InlineKeyboardButton("sᴇᴀʀᴄʜ", callback_data="about"),
                        InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help")
                    ]
                ]
            )
        )


@Client.on_message(filters.command('channel') & filters.user(BANANA_BOI))
async def channel_info(bot, message):
    """Send basic information of channel"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Unexpected type of CHANNELS")

    text = '📑 **Indexed channels/groups**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(CHANNELS)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)


@Client.on_message(filters.command('total') & filters.user(BANANA_BOI))
async def total(bot, message):
    """Show total files in database"""
    msg = await message.reply("Processing...⏳", quote=True)
    try:
        total = await Media.count_documents()
        await msg.edit(f'📁 Saved files: {total}')
    except Exception as e:
        logger.exception('Failed to check total files')
        await msg.edit(f'Error: {e}')


@Client.on_message(filters.command('logger') & filters.user(BANANA_BOI))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))


@Client.on_message(filters.command('delete') & filters.user(BANANA_BOI))
async def delete(bot, message):
    """Delete file from database"""
    reply = message.reply_to_message
    if reply and reply.media:
        msg = await message.reply("Processing...⏳", quote=True)
    else:
        await message.reply('Reply to file with /delete which you want to delete', quote=True)
        return

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('This is not supported file format')
        return

    result = await Media.collection.delete_one({
        'file_name': media.file_name,
        'file_size': media.file_size,
        'mime_type': media.mime_type
    })
    if result.deleted_count:
        await msg.edit('File is successfully deleted from database')
    else:
        await msg.edit('File not found in database')
@Client.on_message(filters.command('about'))
async def bot_info(bot, message):
    buttons = [
        [
            InlineKeyboardButton('Update Channel', url='https://t.me/tg_bots_updates'),
            InlineKeyboardButton('Source Code', url='https://github.com/Lallu-lallus/ALPHA-AUTO-FILTER-BOT')
        ]
        ]
    await message.reply(text="Language : <code>Python3</code>\nLibrary : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio</a>\nSource Code : <a href='https://github.com/Lallu-lallus/ALPHA-AUTO-FILTER-BOT'>Click here</a>\nUpdate Channel : <a href='https://t.me/tg_bots_updates'>ALPH_BOTZ</a> </b>", reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)
