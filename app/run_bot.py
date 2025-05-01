import telebot
import json

bot = telebot.TeleBot("7186731988:AAGj2kEO-taQ-ACoC6JLzaVHxDDpVdbjVWU")

def send_order_to_group(phone_number, order_items):
    chat_id = -4757061565
    order = f"📞 *Buyurtmachi raqami:* `{phone_number}`\n\n📦 *Buyurtma tafsilotlari:*\n"
    
    for item in order_items:
        name = item['name']
        quantity = item['quantity']
        price = item['price']
        total = quantity * price
        order += f"▪️ *{name}*\n   └ {quantity} × {price:,} = {total:,} so'm\n"

    total_sum = sum(item['quantity'] * item['price'] for item in order_items)
    order += f"\n💰 *Umumiy summa:* {total_sum:,} so'm"

    # Optional: qo'shimcha formatlangan JSON ko'rinishini yuborish
    # order += f"\n\n📄 *Buyurtma JSON ko‘rinishi:*\n<pre>{json.dumps(order_items, ensure_ascii=False, indent=2)}</pre>"

    bot.send_message(chat_id=chat_id, text=order, parse_mode="Markdown")
