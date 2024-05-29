from aiogram import Bot, Dispatcher, executor, types
from config import TELEGRAM_TOKEN
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard= True)
button_1 = KeyboardButton('ЧИКЕН РАНЧ')
button_2 = KeyboardButton('ГАВАЙСКАЯ')
button_3 = KeyboardButton('ДОН БЕКОН')
button_4 = KeyboardButton('ЧЕТЫРЕ СЫРА')
button_5 = KeyboardButton('ПЕППЕРОНИ')
button_6 = KeyboardButton('БЬЯНКО')
button_7 = KeyboardButton('ОФОРМИТЬ ЗАКАЗ')
keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7)

keyboard_2 = ReplyKeyboardMarkup(resize_keyboard= True)
button_8 = KeyboardButton('Вернуться в меню')
keyboard_2.add(button_8)


@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('Приветствуем вас в нашей пиццерии! Добро пожаловать в мир ароматной и вкусной пиццы, где каждый кусочек - это настоящее удовольствие. 😄', reply_markup= keyboard)

@dp.message_handler(lambda message: message.text == 'ЧИКЕН РАНЧ')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://yandex.ru/images/search?family=yes&from=tabbar&img_url=https%3A%2F%2Fsun9-55.userapi.com%2Fimpg%2FUI2alCIFM4OtJ7mqBW3uI53au5DdXnFPipLqDg%2FZNIJ1WNDYrw.jpg%3Fsize%3D604x403%26quality%3D95%26sign%3De0a2f82afa9d57b8732b7a86fd5e62fa%26c_uniq_tag%3D8vPQHGE8Tu3tqZdcMv1eVfG79glzAuH4PhoD-jkSOm4%26type%3Dalbum&lr=213&pos=7&rpt=simage&text=%D0%BF%D0%B8%D1%86%D1%86%D0%B0%20%D1%87%D0%B8%D0%BA%D0%B5%D0%BD%20%D1%80%D0%B0%D0%BD%D1%87', caption= 'ЧИКЕН РАНЧ - 8.5$')

@dp.message_handler(lambda message: message.text == 'ГАВАЙСКАЯ')
async def button_2_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://yandex.ru/images/search?family=yes&from=tabbar&img_url=https%3A%2F%2Fmaxvps.ru%2Fwp-content%2Fuploads%2F2%2Fc%2Ff%2F2cf4e20b986baf7767b5cdbfe889947b.jpeg&lr=213&pos=17&rpt=simage&text=%D0%BF%D0%B8%D1%86%D1%86%D0%B0%20%D0%B3%D0%B0%D0%B2%D0%B0%D0%B9%D1%81%D0%BA%D0%B0%D1%8F', caption= 'ГАВАЙСКАЯ пицца - 7$')

@dp.message_handler(lambda message: message.text == 'ДОН БЕКОН')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://yandex.ru/images/search?family=yes&from=tabbar&img_url=https%3A%2F%2Fsun9-42.userapi.com%2Fc854216%2Fv854216511%2F23b555%2Fy2eyLxQn2sI.jpg&lr=213&pos=6&rpt=simage&text=%D0%BF%D0%B8%D1%86%D1%86%D0%B0%20%D0%B4%D0%BE%D0%BD%20%D0%B1%D0%B5%D0%BA%D0%BE%D0%BD', caption= 'ДОН БЕКОН - 7.5$')

@dp.message_handler(lambda message: message.text == 'ЧЕТЫРЕ СЫРА')
async def button_4_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://yandex.ru/images/search?family=yes&from=tabbar&img_url=https%3A%2F%2Ffood.pibig.info%2Fuploads%2Fposts%2F2023-03%2F1677852640_food-pibig-info-p-tvorozhnaya-pitstsa-krasivo-78.jpg&lr=213&pos=4&rpt=simage&text=%D0%BF%D0%B8%D1%86%D1%86%D0%B0%20%D1%87%D0%B5%D1%82%D1%8B%D1%80%D0%B5%20%D1%81%D1%8B%D1%80%D0%B0', caption= 'ЧЕТЫРЕ СЫРА - 6.5$')

@dp.message_handler(lambda message: message.text == 'ПЕППЕРОНИ')
async def button_5_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://yandex.ru/images/search?family=yes&from=tabbar&img_url=https%3A%2F%2Fsun9-51.userapi.com%2Fimpg%2F7FMEsAyEoePq7yLwUn5c-LMk1XGmvrx8ZM7TTA%2FYhxMa9dXl4M.jpg%3Fsize%3D604x402%26quality%3D95%26sign%3Deff37e3506acdf7dfe48c2e7228eecdb%26c_uniq_tag%3DK66pTdxGmz-LfB-88wkX7HrbTyt2MS8fkOvIaQiov0o%26type%3Dalbum&lr=213&pos=7&rpt=simage&text=%D0%BF%D0%B8%D1%86%D1%86%D0%B0%20%D0%9F%D0%95%D0%9F%D0%9F%D0%95%D0%A0%D0%9E%D0%9D%D0%98', caption= 'ПЕППЕРОНИ - 6$')

@dp.message_handler(lambda message: message.text == 'ОФОРМИТЬ ЗАКАЗ')
async def button_7_click(message: types.Message):
    await message.answer('Спасибо! Чтобы оформить заказ с доставкой на дом позвоните нам на телефон 89692834998, ждём вас снова)))', reply_markup=keyboard_2)

@dp.message_handler(lambda message: message.text == 'БЬЯНКО')
async def button_6_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://yandex.ru/images/search?family=yes&from=tabbar&img_url=https%3A%2F%2Fscontent-hel3-1.cdninstagram.com%2Fv%2Ft51.2885-15%2Fe35%2F242831061_387103276460318_3857503111714520882_n.jpg%3F_nc_ht%3Dscontent-hel3-1.cdninstagram.com%26_nc_cat%3D102%26_nc_ohc%3DdL8ZrGxdpWQAX8brP9Y%26edm%3DABfd0MgBAAAA%26ccb%3D7-4%26oh%3D719f87e75f835f53e548069d831b10ea%26oe%3D6157AB9D%26_nc_sid%3D7bff83&lr=213&p=1&pos=18&rpt=simage&text=%D0%BF%D0%B8%D1%86%D1%86%D0%B0%20%D0%B1%D0%AC%D0%AF%D0%9D%D0%9A%D0%9E', caption= 'БЬЯНКО - 7$')


@dp.message_handler(lambda message: message.text == 'Вернуться в меню')
async def button_8_click(message: types.Message):
    await message.answer('Вы вышли в меню', reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True)


