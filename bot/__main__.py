import os
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from dotenv import load_dotenv, find_dotenv
from bot.dialogs.start import start_dialog
from bot.handlers.default_cmd import router as start_router

load_dotenv(find_dotenv())

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

setup_dialogs(dp)

# MAIN ROUTER REGISTRATION MUST BE UPPER THAN AIOGRAM_DIALOG routers
dp.include_routers(start_router)
dp.include_routers(start_dialog)
logging.basicConfig(level=logging.INFO)
dp.run_polling(bot)

