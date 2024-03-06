import logging

from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup 
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from button import bosh_tugma, bosh_menu1, Yunusobod_hotels_keyboard, Chilonzo_hotels_keyboard, Olmazor_hotels_keyboard, MirzoUlugbek_hotels_keyboard, shayxontoxur_hotels_keyboard

API_TOKEN = '6284110724:AAG3EnIqc-GdmM76s0vDpf1T7inu8Z8qr6c'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class Otziv(StatesGroup):
    # fullname = State()
    WAITING_FOR_REVIEW = State('waiting_for_review')

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu aleykum  bu HOTEL BOT", reply_markup=bosh_tugma)


@dp.message_handler(text="🏨Hotellar🏨")
async def send_welcome(message: types.Message):
    await message.reply("Mana siz tanlagan bo'limingiz", reply_markup=bosh_menu1)
 

@dp.message_handler(text="✍️Izoh qoldirish✍️")
async def send_welcome(message: types.Message):
    # Вход в состояние ожидания отзыва
    await Otziv.WAITING_FOR_REVIEW.set()

    # Запрашиваем у пользователя отзыв
    await message.reply("Iltimos, o'z izohingizni qoldiring:",reply_markup=bosh_tugma)  

# Обработчик для получения отзыва в состоянии WAITING_FOR_REVIEW
@dp.message_handler(state=Otziv.WAITING_FOR_REVIEW)
async def process_review(message: types.Message, state: FSMContext):
    # Получаем отзыв от пользователя
    review_text = message.text

    await state.finish()

    await message.reply("O'z fikiringizni qoldirganingiz uchun rahmat.") 


# YUNUSOBOD TUMANI 


@dp.message_handler(text="Yunusobod tumani")
async def echo(message: types.Message):
    await message.answer("Mana Yunusobotdagi HOTELLAR", reply_markup=Yunusobod_hotels_keyboard)


@dp.message_handler(text="the elements hotel")
async def echo(message: types.Message):
    await message.answer("the elements hotel")
    await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiDpgIlxSCOvGnywVCiQ-bCBOE7bSV6AuredjKoFvusMaO5wlN2754uxDgK4gSSX3AnNk&usqp=CAU",
                               caption="100$")
    await message.answer_location(41.36141514469666, 69.28966354096475)
                               

@dp.message_handler(text="Sano hotel")
async def echo(message: types.Message):
    await message.answer("Sano hotel haqida")
    await message.answer_photo("https://avatars.mds.yandex.net/get-altay/6527792/2a00000181c45b562aa69fbcee12fd46ac0a/L_height",
                               caption="88$")
    await message.answer_location(41.365677229579994, 69.28894355259881)
    
@dp.message_handler(text="Garnet hotel")
async def echo(message: types.Message):
    await message.answer("Garnet hotel haqida")
    await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSalN9Up0RvL0CvmuvoclxFsNsBgwHax432KSrVihufA86D2Pbtu9n0kJeadEWggUJ20OU&usqp=CAU",
                               caption="94$")
    await message.answer_location(41.359500539551135, 69.27804961212803)
    
@dp.message_handler(text="Khan orda hotel")
async def echo(message: types.Message):
    await message.answer("Khan orda hotel")
    await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyeU-yHTTdLu4e4pLj-ZYDAE4Ht97bKz8CLWUDpsydcol8ZWYPTtxgtTbIfAFBK2tr6PQ&usqp=CAU",
                               caption="94$")
    await message.answer_location(41.37008664423973, 69.28572336794551)
    
@dp.message_handler(text="VELARA hotel")
async def echo(message: types.Message):
    await message.answer("VELARA hotel")
    await message.answer_photo("https://avatars.mds.yandex.net/get-altay/5104421/2a0000018157d9d5ed69219bf7d672aba89d/L_height",
                               caption="76$")
    await message.answer_location(41.356062310460885, 69.28497011212795)



# CHILONZOR TUMANI

@dp.message_handler(text="Chilonzor tumani")
async def echo(message: types.Message):
    await message.answer("Mana Chilonzor HOTELLAR", reply_markup=Chilonzo_hotels_keyboard)


@dp.message_handler(text="Grand Nur hotel")
async def echo(message: types.Message):
    await message.answer("Grand Nur hotel")
    await message.answer_photo("https://q-xx.bstatic.com/xdata/images/hotel/max1024x768/157538360.jpg?k=c3baba288a0f9814091423217243715a9282e9795a86a89427927a6d4cf0b397&o=",
                               caption="50$")
    await message.answer_location(41.34843581818272, 69.23775592561756)
                               

@dp.message_handler(text="Asil Makon hotel")
async def echo(message: types.Message):
    await message.answer("Asil Makon hotel haqida")
    await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRA3vG9boFlxiOKT1i6elpMkQM1vps04jZ53cfuV802q6w0ey1Z4PoEukmvzRuBhghV0wc&usqp=CAU",
                               caption="109$")
    await message.answer_location(41.32799203210797, 69.34415973522486)
    
@dp.message_handler(text="Lake park")
async def echo(message: types.Message):
    await message.answer("Lake park haqida")
    await message.answer_photo("https://cf.bstatic.com/xdata/images/hotel/max1024x768/159813558.jpg?k=c1db2291409373a41593b73a0aa5600ba5ccf93001d2469d68e0f2de3e9fdcaa&o=&hp=1",
                               caption="94$")
    await message.answer_location(41.300608824284346, 69.24102117904535)
    
@dp.message_handler(text="The Royal Mezbon Hotel and SPA")
async def echo(message: types.Message):
    await message.answer("The Royal Mezbon Hotel and SPA haqida")
    await message.answer_photo("https://frankfurt.apollo.olxcdn.com/v1/files/ba4f7msbf1c12-UZ/image;s=800x799",
                               caption="94$")
    await message.answer_location(41.26681207294168, 69.24359609983321)
    
@dp.message_handler(text="Bolo xona hotel")
async def echo(message: types.Message):
    await message.answer("Bolo xona hotel haqida")
    await message.answer_photo("https://cf.bstatic.com/xdata/images/hotel/max1024x768/297874585.jpg?k=df731d39f3aeaf3527d97cabfbbbea1abe9ae7a2ed93d200f0321ddb09dabd84&o=&hp=1",
                               caption="76$")
    await message.answer_location(41.28384335541949, 69.17886689677773)
    
@dp.message_handler(text="Hostel Point hotel")
async def echo(message: types.Message):
    await message.answer("Hostel Point hotel haqida")
    await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnRJdub9oM2gC6Uf5ah8R0RyJof-uhBLhmW28qcftG9U1eel6oacBlnBTuz83LUzZwLmc&usqp=CAU",
                               caption="18$")
    await message.answer_location(41.34599053444643, 69.2775344888597)




# Olmazor tumani


@dp.message_handler(text="Olmazor tumani")
async def echo(message: types.Message):
    await message.answer("Any text", reply_markup=Olmazor_hotels_keyboard)

@dp.message_handler(text="Sebzor hotel")
async def echo(message: types.Message):
    await message.answer("Sebzor hotel haqida")
    await message.answer_photo("https://q-xx.bstatic.com/xdata/images/hotel/max500/398972053.jpg?k=5874fd3d5fbab9bc214bb1f86dcc519a41ca81f464f48f08522f0b5c232675ac&o=",
                               caption="25$")
    await message.answer_location(41.33785171489793, 69.25446791212698)


@dp.message_handler(text="Taht hotel")
async def echo(message: types.Message):
    await message.answer("Taht hotell haqida")
    await message.answer_photo("https://cf.bstatic.com/xdata/images/hotel/max500/353172157.jpg?k=76c08b1c83538bb870dc557e19f72b0f7e3b9542c5c61d58e94f66a350332cd9&o=&hp=1",
                               caption="36$")
    await message.answer_location(41.342837224281695, 69.25694748143432)
        

@dp.message_handler(text="Hostel point hotel")
async def echo(message: types.Message):
    await message.answer("Hostel point hotel haqida")
    await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnRJdub9oM2gC6Uf5ah8R0RyJof-uhBLhmW28qcftG9U1eel6oacBlnBTuz83LUzZwLmc&usqp=CAU",
                               caption="18$")
    await message.answer_location(41.34599053444643, 69.2775344888597)

    

@dp.message_handler(text="ok hotelok hotel")
async def echo(message: types.Message):
    await message.answer("ok hotel haqida")
    await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZDw7SQkv4QhwyHSJnmhg-aHBithJSn9KE8EDGRSHKUpT9q3nxJpkgqVnxPaok6dNdq8o&usqp=CAU",
                               caption="40$")
    await message.answer_location(41.363394175707, 69.1844336084136)
    

@dp.message_handler(text="Taxptapul hotel")
async def echo(message: types.Message):
    await message.answer("Taxptapul hotel haqida")
    await message.answer_photo("https://cf.bstatic.com/xdata/images/hotel/max1024x768/328440596.jpg?k=150ffdb8e3221c2c03e1f59ee046bc4c276598f651bb4133086ca984e561b176&o=&hp=1",
                               caption="18$")
    await message.answer_location(41.34069734037661, 69.26176437165672)


@dp.message_handler(text="Grand Way hotel")
async def echo(message: types.Message):
    await message.answer("Grand Way hotel haqida")
    await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsK8dJUWTtfI-tu5FiMa2bqbSKJYDRLCEdUKjyfEPcVx33NnQtJ5zozkLWKf7MsBP0Ahs&usqp=CAU",
                               caption="18$")





# Mirzo Ulugbek tumani

@dp.message_handler(text="Mirzo Ulugbek tumani")
async def echo(message: types.Message):
    await message.answer("Any text", reply_markup=MirzoUlugbek_hotels_keyboard)
    
@dp.message_handler(text="Darhan Boutique Hotel")
async def echo(message: types.Message):
    await message.answer("Darhan Boutique Hotel haqida")
    await message.answer_photo("https://cf.bstatic.com/xdata/images/hotel/max1024x768/354459604.jpg?k=ef76d651d68b386f0ac77f22fdae764d5a9373fa47d3742c2ab67a38f619677b&o=&hp=1",
                               caption="98$")
    await message.answer_location(41.32002757130844, 69.30074879492328)
 
@dp.message_handler(text="SHAKH SULTON Hotel")
async def echo(message: types.Message):
    await message.answer("SHAKH SULTON Hotel haqida")
    await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCToTqlTlMvjNdUGaJYQaZQwtza1yEYk2X6YouDkP7xI9e5VfaWhZBNgWQCswhaGSttq8&usqp=CAU",
                               caption="56$")
    await message.answer_location(41.34027979624027, 69.30727514844668)

@dp.message_handler(text="International Hotel")
async def echo(message: types.Message):
    await message.answer("International Hotel haqida")
    await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRo2z0xpKMT51N9IVtO974RZH0ccgX7BC2lvh17ybmFWv1-b3gaAqhrnHBT7sx7tJ9m92I&usqp=CAU",
                               caption="110$")
    await message.answer_location(41.341652310931174, 69.28182899404834)


@dp.message_handler(text="Eurolux  Boutique Hotel")
async def echo(message: types.Message):
    await message.answer("Eurolux  Boutique Hotel haqida")
    await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUNb-4XO4SNKdr46KsIvy6NezPk9kgmnUh7fuv_-AdhrTjzE_b9Em4wcJszwHXrhoY8j4&usqp=CAU",
                               caption="40$")
    await message.answer_location(41.31211217569092, 69.30881515259604)


@dp.message_handler(text="Paradise hotel ")
async def echo(message: types.Message):
    await message.answer("Paradise hotel haqida")
    await message.answer_photo("https://cf.bstatic.com/xdata/images/hotel/max1024x768/301534091.jpg?k=9c6ca67e8a2c9bc2d29402135afc86238616e936c6d51bb145bcd65453aabad2&o=&hp=1",
                               caption="37$")
    await message.answer_location(41.318741091877556, 69.27507087940475)


@dp.message_handler(text="Friday hotel")
async def echo(message: types.Message):
    await message.answer("Friday hotel haqida")
    await message.answer_photo("https://lh5.googleusercontent.com/p/AF1QipOLSXmzvjS4gr7JcfX-l7y-C4bizKD3gM9TKYxV=w408-h272-k-no",
                               caption="50$")
    await message.answer_location(41.34095610585282, 69.29397745305356)

# Shayxontoxur tumani

@dp.message_handler(text="Shayxontoxur tumani")
async def echo(message: types.Message):
    await message.answer("Any text", reply_markup=shayxontoxur_hotels_keyboard)



@dp.message_handler(text="Лотте Сити Хотел Ташкент Палас")
async def echo(message: types.Message):
    await message.answer("Лотте Сити Хотел Ташкент Палас hotel haqida")
    await message.answer_photo("https://lh3.googleusercontent.com/gps-proxy/AE4_-5Gg1rJtmHt5mR8GpvLEJcAPjvDVX8o03gWJfRIWEKJyW1Zg_3e6Qzmd2qH9aMlQ8K4jegD5_O9MuEM8PqikRVs4MR7oWtM1DbY1NQOS0h4-VgxyX3drvWgSI2UCRFLVQjW3kVGO1kRoVUGHNVdv4wuKL5iHzTWFsr_JTAO2g8WcOg8a-S-7AoBK=w408-h272-k-no",
                               caption="168$")
    await message.answer_location(41.309786105166225, 69.26861513521855)

@dp.message_handler(text="Huvaydo Hotel")
async def echo(message: types.Message):
    await message.answer("Huvaydo Hotel haqida")
    await message.answer_photo("https://lh3.googleusercontent.com/gps-proxy/AE4_-5EZMyCJ46JCbu6fdqSPxDwp3RtsRr6jZL6wzQKrlZ7nbT6svpTmSTjn4TYNcmNPc09dIH7JfaSndS8u3rOPGipBnKXIwPlPIPyXmf2s1Ei6FbbOE5-wlyOcPyvmeE-qshEnIuzy0xaTdde1-PahoH8oZ2V0aoqxnbuks8DX5cQXpe1MWF2A9ayv=w408-h269-k-no",
                               caption="100$")
    await message.answer_location(41.33754522027134, 69.21401302672517)

@dp.message_handler(text="Чорсу Инн отель")
async def echo(message: types.Message):
    await message.answer("Чорсу Инн отель Hotel haqida")
    await message.answer_photo("https://lh3.googleusercontent.com/gps-proxy/AE4_-5GVO1qPqd4eXz1Jk0b4p2ntIOPg3Rj5a53LJD6UgbrMvITXAbApenYaQnRf5wX9kyl1HzXqt9q_woAnDrC8qT_hpXogU3bCbHBLv_XmFYBwiIm4LLPwce7Zatm8tjX1AkfMlolEHVXdDyQByQF1twyEvFuKpCmgJRtAT1lFUZh31GdjljnTuJ4c=w408-h306-k-no",
                               caption="97$")
    await message.answer_location(41.32960160947331, 69.22714348476704)

@dp.message_handler(text="Hotel Suzuk-Ota")
async def echo(message: types.Message):
    await message.answer("Hotel Suzuk-Ota haqida")
    await message.answer_photo("https://lh5.googleusercontent.com/p/AF1QipNxAuxpBwwUiLq0qexSJmBw1O4XG8QlQWqMCkMZ=w426-h240-k-no",
                               caption="57$")
    await message.answer_location(41.318016756815624, 69.22432413910622)


@dp.message_handler(text="Mirzo Boutique Hotel")
async def echo(message: types.Message):
    await message.answer("Mirzo Boutique Hotel haqida")
    await message.answer_photo("https://lh3.googleusercontent.com/gps-proxy/AE4_-5GfkXNLqb5jkNTTL2Bw73qVQ0vetW0ZovU0IM_jseeZOfxKNqxCH-ym2BIxAWTWklSIHtKQkN7Aiw4e2Iqzm1Kb0KNKvco-1os3t_7oS77_RdZ6ltaD5S4XJ__3HoYsNQZFh7SCNedJmfgoPXK_f6xPufsphqn20LB-vM6zzuXOe0H_ljORG2LY4g=w437-h240-k-no",
                               caption="?$")
    await message.answer_location(41.32432958598635, 69.24187238514597)


@dp.message_handler(text="Old City Hotel Tashkent")
async def echo(message: types.Message):
    await message.answer("Old City Hotel Tashkent haqida")
    await message.answer_photo("https://lh5.googleusercontent.com/p/AF1QipO9YvKwxTGVJsKoZrwi_LpFK-QAUga21nsisdY0=w408-h724-k-no",
                               caption="54$")
    await message.answer_location(41.32414811559613, 69.24075742561642)



@dp.message_handler(text="⬅Ortga")
async def echo(message: types.Message):
    await message.answer("mana bosh menu", reply_markup=bosh_menu1)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Any text")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
