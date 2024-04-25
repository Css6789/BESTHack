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
       bot.send_message(message.from_user.id, "Select request category (After that select comand /text)", reply_markup=markup) #����� ����

def after_text_request(message):
    groops=[["������ ��������� �� rejected","����� �� rejected","������ ����� �� started","��������� �� refunding","������ ����� �� cancelled","����� �� refunding","����������� �� lost","������ ��������� �� sorted","������ ����� �� submitted","����� �� confirmed","������ ��������� �� cancelled","����� �� sorted","������ ��������� �� confirmed","������ ����� �� refunding","��������� �� submitted","������ ��������� �� refund"],
        ["������ �� ���������","������ �� �� ������� refunding","������ �� �� ������� lost","������� ������","������ �� �� ������� sorted","������ �� �� ������� confirmed","������ �� �� ������� submitted","������ �� �� ������� started","������ �� �� ������� cancelled","������ �� �� ������� rejected","������������"],
        ["������� ��������","�������","�������� ����� �������","����-������","�������� ����� ������� � ���","����-������ ����� �������","�������� �����","�������������� ������� ������� ��������","DBS","RDBS","DBS � RDBS","����-������","EXMAI","API","EXMAIL ��������","����","�����-��������","����������� ����-������","����-�����"],
        ["������� ������ �����������","������� ���������","������� ������","�������","����������� �� ���������","������ ����������� �� ���������","������","����������� �� ���������","�����������","������ �����������"]]
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


    print(solution_about_groops.index(max(solution_about_groops))+1,"- � ������")

   

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