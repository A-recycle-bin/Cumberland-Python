# Programme pour 'spam' un ami sur une app de messagerie


import pyautogui, time, datetime

time.sleep(2)

while True:
    print('Message envoyé à :', datetime.datetime.now())
    pyautogui.typewrite("Juste un petit rappel")
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(2)

