import random
import telebot
from telebot import types
from khayyam import JalaliDatetime
import gtts
import qrcode

bot = telebot.TeleBot("5897000242:AAFAMZ7Bf6yKxBr753bZY7VRV9P7FTt-AEo", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, message.from_user.first_name + " عزیز سلام؛ خوش آمدی. برای راهنمایی /help را وارد کن.")


@bot.message_handler(commands=['game'])
def input_game(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    key = types.KeyboardButton('New Game')
    markup.add(key)
    message = bot.reply_to(message,"یک عدد بین 1 تا 100 حدس بزنید:",reply_markup=markup)
    goal=random.randint(1,100)
    print(goal)
    bot.register_next_step_handler(message,game,goal)

def game(message,goal):
    user_ch = message.text
    print(user_ch)
    if user_ch == "new game" or user_ch == "/game":
        bot.send_message(message.chat.id,"New Game :")
        input_game(message)
    elif not user_ch.isdigit():
        message = bot.reply_to(message,"یک عدد صحیح بین 1 تا 100 وارد کنید: ")
        bot.register_next_step_handler(message,game,goal)
    user_num = int(user_ch)
    if goal>user_num:
        bot.send_message(message.chat.id,"برو بالا!")
        bot.register_next_step_handler(message,game,goal)
    elif goal<user_num:
        bot.send_message(message.chat.id,"برو پایین!")
        bot.register_next_step_handler(message,game,goal)
    elif goal == user_num:
        bot.send_message(message.chat.id,"آفرین! برنده شدی.")
        return


@bot.message_handler(commands=['age'])
def age1(message):
    message = bot.send_message(message.chat.id,"تاریخ تولد خود را وارد نمایید: مثال: 17/11/1364")
    bot.register_next_step_handler(message,age)

def age(message):
    birthday = message.text
    print(birthday)
    birth_lst = birthday.split("/")
    age=JalaliDatetime.now()-JalaliDatetime(birth_lst[0],birth_lst[1],birth_lst[2])//365
    bot.send_message(message.chat.id,"Your age: ", age)
    
@bot.message_handler(commands=['voice'])
def voice1(message):
    message = bot.send_message(message.chat.id,"یک جمله به زبان انگلیسی وارد نمایید: ")
    bot.register_next_step_handler(message,voice)

def voice(message):
    txt = message.text
    print(txt)
    s=gtts.gTTS(txt, lang="en",slow=False)
    s.save("pro.mp3")
    voice = open("pro.mp3",'rb')
    bot.send_voice(message.chat.id,voice)

@bot.message_handler(commands=['max'])
def max1(message):
    message = bot.send_message(message.chat.id,"یک آرایه متناهی دلخواه از اعداد وارد نمایید: ")
    bot.register_next_step_handler(message,max)

def max(message):
    str = message.text
    num_list = str.split(",")
    print(num_list)
    max_num = 0
    for num in num_list:
        if max_num<float(num):
            max_num = float(num)
    print(max_num)
    bot.send_message(message.chat.id,"MAX: ",max_num)

@bot.message_handler(commands=['argmax'])
def argmax1(message):
    message = bot.send_message(message.chat.id,"یک آرایه متناهی دلخواه از اعداد وارد نمایید: ")
    bot.register_next_step_handler(message,argmax)

def argmax(message):
    str = message.text
    num_list = str.split(",")
    print(num_list)
    max_num = 0
    i=0
    for num in num_list:
        if max_num<float(num):
            max_num = float(num)
            index = i+1
        i += 1
    print(max_num)
    bot.send_message(message.chat.id,"Index of MAX:", index)

@bot.message_handler(commands=['qrcode'])
def qrcode1(message):
    message = bot.send_message(message.chat.id,"یک جمله برای تبدیل شدن به کیو آر کد وارد نمایید: ")
    bot.register_next_step_handler(message,qr_code)

def qr_code(message):
    msg = message.text
    img = qrcode.make(msg)
    img.save("str-to_qrcode.png")
    f = open("str_to_qrcode.png",'rb')
    bot.send_photo(message.chat.id,f)



@bot.message_handler(commands=['help'])
def helping_menu(message):
	bot.send_message(message, """
    /game: \n بازی حدس عدد اجرا می شود. \n
    /age: \n تاریخ تولد شمسی شما را دریافت کرده و سن شما را محاسبه می نماید. \n
    /voice: \n یک جمله به زبان انگلیسی وارد کنید و تلفظ آن را دریافت نمایید. \n
    /max: \n یک آرایه از اعداد وارد نمایید تا بزرگترین عدد آن را برایتان مشخص کند. \n
    /argmax \n یک آرایه از اعداد وارد نمایید تا شماره بزرگترین عدد آن را برایتان مشخص کند. \n
    /qrcode \n یک رشته از شما دریافت کرده، QRcode آن را میسازد. \n
    """)


bot.infinity_polling()