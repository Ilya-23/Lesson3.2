mail1 = 'com'
mail2 = 'net'
mail3 = '.ru'


def send_email(message, recipient, sender="university.help@gmail.com"):
    text_check = True
    for i in range(len(sender)):
        if sender[i] == '@':
            text_check = True
            break
        else:
            text_check = False
    mail_check1 = sender[len(sender) - 3: len(sender)]
    mail_check2 = recipient[len(recipient) - 3: len(recipient)]
    if text_check == False or (mail_check1 != mail1 and mail_check1 != mail2 and \
                               mail_check1 != mail3) or (mail_check2 != mail1 and \
                                                         mail_check2 != mail2 and mail_check2 != mail3):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif sender == recipient:
        print('Невозможно отправить письмо самому себе!')
    elif sender != "university.help@gmail.com":
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
