from aiogram import Dispatcher, Bot, types, executor
import os
import hashlib

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


@dp.inline_handler()
async def inline_search(query: types.InlineQuery):
    text = query.query or 'echo'
    link = 'https://en.wikipedia.org/wiki/' + text
    result_id: str = hashlib.md5(text.encode()).hexdigest()

    articles = [types.InlineQueryResultArticle(
        id=result_id,
        title='Стаття з Wikipedia:',
        url=link,
        input_message_content=types.InputTextMessageContent(message_text=link))]

    await query.answer(articles, cache_time=1, is_personal=True)


executor.start_polling(dp, skip_updates=True)
