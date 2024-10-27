import asyncio

from aiogram import Dispatcher, Bot, Router
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN

# ROUTERS
from handlers.main_handlers import main_commands_router
from handlers.handlers import router_handlers
# ROUTERS

router = Router()


async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    await asyncio.gather(
        run_bot(bot=bot, dp=dp),
    )

async def run_bot(bot, dp):

    storage = MemoryStorage()
    dp["dp"] = dp
    dp["storage"] = storage



    dp.include_routers(
        router,
        main_commands_router,
        router_handlers,
    )

    await bot.delete_webhook(drop_pending_updates=True)
    print('Bot rolling')
    await dp.start_polling(bot)




if __name__ == '__main__':
    asyncio.run(main())


