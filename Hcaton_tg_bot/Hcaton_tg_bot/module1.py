import telebot
from telebot import types

bot = telebot.TeleBot('6356182801:AAEjfBROuMVLsgZBs2YoI2Yj3Om8N0NsYPA')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Hellow, I am your bot-assistant for navigation and use of the AVITO service (to continue, enter /request_category )")

@bot.message_handler(commands=['request_category'])
def get_text_choise(message):
       markup = types.InlineKeyboardMarkup(row_width=1)
       btn1 = types.InlineKeyboardButton('Order status stuck', callback_data='button1')
       btn2 = types.InlineKeyboardButton('No money returned', callback_data='button2')
       btn3 = types.InlineKeyboardButton("Late delivery",callback_data='button3')
       btn4 = types.InlineKeyboardButton("Other",callback_data='button4')
       markup.add(btn1, btn2, btn3, btn4)
       bot.send_message(message.from_user.id, "Select request category (After that select comand /text)", reply_markup=markup) #îòâåò áîòà

def after_text_request(message):
    groops=[["статус отправлен на rejected","завис на rejected","статус завис на started","отправлен на refunding","статус завис на cancelled","завис на refunding","статусзавис на lost","статус отправлен на sorted","статус завис на submitted","завис на confirmed","статус отправлен на cancelled","завис на sorted","статус отправлен на confirmed","статус завис на refunding","отправлен на submitted","статус отправлен на refund"],
        ["деньги не вернулись","деньги из за статуса refunding","деньги из за статуса lost","зависли деньги","деньги из за статуса sorted","деньги из за статуса confirmed","деньги из за статуса submitted","деньги из за статуса started","деньги из за статуса cancelled","деньги из за статуса rejected","возвращаются"],
        ["касаемо доставки","профиле","трекингу заказ получен","трек-номера","трекингу заказ получен в опс","трек-номера заказ получен","трекингу заказ","дополнительные вопросы касаемо доставки","DBS","RDBS","DBS и RDBS","трек-номера","EXMAI","API","EXMAIL сообщили","Срок","кросс-доставки","возвратного трек-номера","трек-номер"],
        ["просьба убрать уведомления","просьба перевести","просьба убрать","просьба","уведомление по претензии","убрать уведомления по претензии","убрать","уведомления по претензии","уведомления","убрать уведомление"]]

    request=message.text
    list_req=request.split()
    solution_about_groops=[0,0,0,0]
    for k in range(len(groops)):
        set_word=set()
        for frase in groops[k]:
            if " " in frase:
                list_word=frase.split()
            else:
                list_word=list(frase)
            
            for word in list_word:
                if word in list_req:
                    if word not in set_word:
                        solution_about_groops[k]+=1
                        set_word.add(word)


    print(solution_about_groops.index(max(solution_about_groops))+1,"-я группа")

   

def after_text_original_id(message):
    print("Original_id :",message.text)
    msg2=bot.send_message(message.from_user.id, "Enter your request")
    bot.register_next_step_handler(msg2, after_text_request)
    

def after_text_is_pinned(message):
    if message.text=="true" or message.text=="false":
        print("Is_pinned :",message.text)
        msg2=bot.send_message(message.from_user.id, "Please, enter the current original_id (or enter NO if you has not got in)")
        bot.register_next_step_handler(msg2, after_text_original_id)
    else:
        msg1 =bot.send_message(message.from_user.id, "Please, try to enter the current condition (true/false) correctly again")
        bot.register_next_step_handler(msg1, after_text_is_pinned)

def after_text_delete_at(message):
    mess=set()
    for i in message.text:
        mess.add(i)
    if mess<={"0","1","2","3","4","5","6","7","8","9"}:
        print("Delete_at :",int(message.text))
        msg2=bot.send_message(message.from_user.id, "Please, enter the current condition (true/false) of is_pinned")
        bot.register_next_step_handler(msg2, after_text_is_pinned)
    else:
        msg1 =bot.send_message(message.from_user.id, "Please, try to enter your number of delete_at correctly again")
        bot.register_next_step_handler(msg1, after_text_delete_at)

def after_text_edit_at(message):
    mess=set()
    for i in message.text:
        mess.add(i)
    if mess<={"0","1","2","3","4","5","6","7","8","9"}:
        print("Edit_at :",int(message.text))
        msg2=bot.send_message(message.from_user.id, "Please, enter the current number of delete_at")
        bot.register_next_step_handler(msg2, after_text_delete_at)
    else:
        msg1 =bot.send_message(message.from_user.id, "Please, try to enter your number of edit_at correctly again")
        bot.register_next_step_handler(msg1, after_text_edit_at)

def after_text_root_id(message):
    print("Root_id :",message.text)
    msg2=bot.send_message(message.from_user.id, "Please, enter the current number of edit_at")
    bot.register_next_step_handler(msg2, after_text_edit_at)

def after_text_apdate_at(message):
    mess=set()
    for i in message.text:
        mess.add(i)
    if mess<={"0","1","2","3","4","5","6","7","8","9"}:
        print("Apdate_at :",int(message.text))
        msg2=bot.send_message(message.from_user.id, "Please, enter the current root_id")
        bot.register_next_step_handler(msg2, after_text_root_id)
    else:
        msg1 =bot.send_message(message.from_user.id, "Please, try to enter your number of apdate_at correctly again")
        bot.register_next_step_handler(msg1, after_text_apdate_at)

def after_text_create_at(message):
    mess=set()
    for i in message.text:
        mess.add(i)
    if mess<={"0","1","2","3","4","5","6","7","8","9"}:
        print("Create_at :",int(message.text))
        msg2=bot.send_message(message.from_user.id, "Please, enter the current number of apdate_at")
        bot.register_next_step_handler(msg2, after_text_apdate_at)
    else:
        msg1 =bot.send_message(message.from_user.id, "Please, try to enter your number of create_at correctly again")
        bot.register_next_step_handler(msg1, after_text_create_at)

def after_text_chanelid(message):
    mess=set()
    for i in message.text:
        mess.add(i)
    if mess<={"0","1","2","3","4","5","6","7","8","9"}:
        print("Chanel_id :",int(message.text))
        msg2=bot.send_message(message.from_user.id, "Please, enter the current number of create_at")
        bot.register_next_step_handler(msg2, after_text_create_at)
    else:
        msg1 =bot.send_message(message.from_user.id, "Please, try to enter your chanel_id correctly again")
        bot.register_next_step_handler(msg1, after_text_chanelid)

def after_text_userid(message):
    mess=set()
    for i in message.text:
        mess.add(i)
    if mess<={"0","1","2","3","4","5","6","7","8","9"}:
        print("User_id :",int(message.text))
        msg2=bot.send_message(message.from_user.id, "Please, enter the current chanel_id")
        bot.register_next_step_handler(msg2, after_text_chanelid)
    else:
        msg1 =bot.send_message(message.from_user.id, "Please, try to enter your id correctly again")
        bot.register_next_step_handler(msg1, after_text_userid)
        
def after_text_numb(message):
    mess=set()
    for i in message.text:
        mess.add(i)
    if mess<={"0","1","2","3","4","5","6","7","8","9"}:
        print("Number :", int(message.text))
        msg2=bot.send_message(message.from_user.id, "Please, enter the current user_id")
        bot.register_next_step_handler(msg2, after_text_userid)
    else:
        msg1 =bot.send_message(message.from_user.id, "Please, try to enter your number correctly again")
        bot.register_next_step_handler(msg1, after_text_numb)       

@bot.message_handler(commands=['text'])
def get_text_form(message):
    if (message.text=="/text"):
       msg1 =bot.send_message(message.from_user.id, "Please, enter your order number:")
       bot.register_next_step_handler(msg1, after_text_numb)

bot.polling()
