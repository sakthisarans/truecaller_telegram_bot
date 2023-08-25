import truecallerpy,time
import telebot 

botkey='********************************'
key='a1i0E--h2AgmFVBVLxGy4mvzItlPtBbdfSknT1nD069TUKg-Dt6ubMnIU6uLGEqE'

bot=telebot.TeleBot(botkey)

@bot.message_handler(commands='start')
def bot_status(msg):
    bot.reply_to(msg, "welcome "+msg.from_user.first_name+"\n"
                    "bot is up and running")

@bot.message_handler(commands='search')
def decrypt(msg):
    bot.send_message(chat_id=msg.from_user.id,text="send number")
    bot.register_next_step_handler(msg,search)

def search(msg):
    try:
    # print(msg)
        data=truecallerpy.search_phonenumber(regionCode='IN',phoneNumber=msg.text,installationId=key)
        name=(data['data'][0]['name'])
        # print(json.dumps(data,indent=4))
        bot.send_message(msg.from_user.id,text=str(name))
    except Exception as ex:
        bot.send_message(msg.from_user.id,text=str(ex))
try:
    bot.polling(non_stop=True)
except Exception as e:
    print(e)
    time.sleep(1)
