import telegram
from constants import TOKEN, GROUP_CHAT_ID, CHAT_ID

def send_grocery_list(groceries):
    bot = telegram.Bot(TOKEN)
    text_to_send = "Here is your grocery list: \n" + groceries
    bot.send_message(text = text_to_send, chat_id = GROUP_CHAT_ID)
 