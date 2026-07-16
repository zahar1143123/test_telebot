from telebot import *
import webbrowser
import requests
import json
from sqlite3 import *

print('hello world')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "hello user i'm glad to see you here😊")

@bot.message_handler(content_types=['text'])
def getweather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        obj = {
            'temp' : f'{data["main"]["temp"]}'
        }
        bot.reply_to(message, f'Now the weather: {obj["temp"]}')
    else:
        bot.reply_to(message,'this city not exist')

# name = None

# @bot.message_handler(commands=['start'])
# def go(message):
#     con = connect('zakhar.sql')
#     cur = con.cursor()

#     cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
#     con.commit()
#     cur.close()
#     con.close()

#     bot.send_message(message.chat.id, 'Hi , now we will register you! Input your name')
#     bot.register_next_step_handler(message, user_name)

# def user_name(message):
#     global name
#     name = message.text.strip()
#     bot.send_message(message.chat.id, 'Enter password')
#     bot.register_next_step_handler(message, user_pass)

# def user_pass(message):
#     password = message.text.strip()


#     con = connect('zakhar.sql')
#     cur = con.cursor()

#     cur.execute("INSERT INTO users (name,pass) VALUES ('%s', '%s')" % (name, password))
#     con.commit()
#     cur.close()
#     con.close()

#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('List of users', callback_data='users'))
#     bot.send_message(message.chat.id, 'User was registered', reply_markup=markup)

# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     con = connect('zakhar.sql')
#     cur = con.cursor()

#     cur.execute('SELECT * FROM users')
#     users = cur.fetchall()

#     info = ''
#     for el in users:
#         info += f'Name: {el[1]} Password: {el[2]}\n'

#     cur.close()
#     con.close()
    
#     bot.send_message(call.message.chat.id, info)


# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton('go to site')
#     btn2 = types.KeyboardButton('Delete photo')
#     btn3 = types.KeyboardButton('Edit photo')
#     markup.row(btn1,btn2, btn3)
#     bot.send_message(message.chat.id, 'Hi')
#     file = open('./gallery1.jpg','rb')
#     bot.send_photo(message.chat.id, file, reply_markup=markup)
#     bot.register_next_step_handler(message, on_click)
#     @bot.message_handler(content_types=['text'])
#     def on_click(message):
#         if message.text == 'go to site':
#             bot.send_message(message.chat.id, 'WebSite is open')
#         elif message.text == 'Delete photo':
#             bot.send_message(message.chat.id, 'Deleted')

# @bot.message_handler(commands=['site', 'website'])
# def site(message):
#     webbrowser.open('https://www.youtube.com/')

# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton('go to site', url='https://www.google.com/')
#     markup.row(btn1)
#     btn2 = types.InlineKeyboardButton('Delete photo', callback_data='delete')
#     btn3 = types.InlineKeyboardButton('Edit photo', callback_data='edit')
#     markup.row(btn2, btn3)
#     bot.reply_to(message, 'Fantastic Photo !', reply_markup=markup)
#     @bot.callback_query_handler(func=lambda callback: True)
#     def callback_message(callback):
#         if callback.data == 'delete':
#             bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
#         elif callback.data == 'edit':
#             bot.edit_message_text('Edited' ,callback.message.chat.id, callback.message.message_id )

# @bot.message_handler(commands=['start', 'hi', 'hello'])
# def main(message):
#     bot.send_message(message.chat.id,  f'Hi, {message.from_user.first_name} {message.from_user.last_name}')

# @bot.message_handler(commands=['help'])
# def main(message):
#     bot.send_message(message.chat.id, '<b>help information</b> \n <em>/start - start</em> \n /hi or /hello - sayhello', parse_mode='html')

# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'hi':
#         bot.send_message(message.chat.id,  f'Hi, {message.from_user.first_name} {message.from_user.last_name}')
#     elif message.text.lower() == 'id':
#         bot.reply_to(message, f'ID: {message.from_user.id}')



bot.infinity_polling()
