import telebot
import json

bot = telebot.TeleBot("7186731988:AAGj2kEO-taQ-ACoC6JLzaVHxDDpVdbjVWU")

def send_order_to_group(phone_number, order_items):
    chat_id =-4757061565
    order = f"Nomer: {phone_number}\n"
    for item in order_items:
        order += f" — {item['name']}: {item['quantity']} × {item['price']}\n"
    order+= f"\n\nBuyurtma: {json.dumps(order_items, ensure_ascii=False, indent=2)}"
    bot.send_message(chat_id=chat_id, text=order)