from pyrogram import *

#   ________           .___       __    
#  /  _____/  ____   __| _/__  __|  | __
# /   \  ___ /  _ \ / __ |\  \/  /  |/ /
# \    \_\  (  <_> ) /_/ | >    <|    < 
#  \______  /\____/\____ |/__/\_ \__|_ \
#         \/            \/      \/    \/

api_id = 1
api_hash = "1"
phnumber = "numero voip"
phnumber2 = "numero vostro"



processchat = "@"  #tag canale

apps = [Client("mysession",api_id, api_hash,phone_number= phnumber),Client("mysession2",api_id, api_hash,phone_number= phnumber2)]
app = Client("mysession",api_id, api_hash,phone_number= phnumber)
app2 = Client("mysession2",api_id, api_hash,phone_number= phnumber2)
@app.on_message(filters.command("setfeedname", "/"))
def setfeedname(Client,message):
        try:    
            message.delete()
            app.update_profile(first_name=message.text.split("/setfeedname")[1])
        except Exception as error: app.edit_message_text(message.chat.id, message.message_id,"✖ ERRORE ✖ \n{Errore}".format(Errore = error))


@app.on_message(filters.command("createfeed", "/"))
def setfeedname(Client,message):  
        try:
            message.delete()
            app.send_message(processchat, message.text.split("/createfeed")[1])
        except Exception as error: app.edit_message_text(message.chat.id, message.message_id,"✖ ERRORE ✖ \n{Errore}".format(Errore = error))


@app.on_message(filters.command("info","/"))
def info(Client,message):
    message.delete()
    app.edit_message_text(message.chat.id, message.message_id, "**FakeFeeder Ubot by @godxk\nVersione Bot: 1.0**", parse_mode="markdown")

@app2.on_message(filters.command('aaa'))
async def fffff(Client, msg):
    await msg.delete()

app.run()

