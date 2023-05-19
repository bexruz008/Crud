from aiogram.types import ReplyKeyboardMarkup, KeyboardButton




def user_rkm():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="/Menu")
    button2 = KeyboardButton(text="☎Kontakt")
    rkm.add(button, button2)
    return rkm



def menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="🥂Ichimliklar")
    button2 = KeyboardButton(text="🍡Shashliklar")
    button3 = KeyboardButton(text="🍽Ovqatlar")
    rkm.add(button, button2, button3)
    return rkm


# def cancel():
#     rkm = ReplyKeyboardMarkup(resize_keyboard=True)
#     button = KeyboardButton(text="Back")