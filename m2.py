#GROUP_ID=-848508924
#обрабочтк стикеров
@dp.message_handler(content_types=["sticker"])
async def check_sticker(message: types.Message):
    await message.answer(message.sticker.file_id)
    await bot.send_message(message.from_user.id, message.chat.id)
#обработичк документов и фото
@dp.message_handler(content_types=["document", "photo"])
async def forward_message(message: types.Message):
    await bot.forward_message(os.getenv("GROUP_ID"), message.from_user.id, message.message_id)