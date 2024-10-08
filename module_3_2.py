def send_mail(message, recipient, *, sender='university.help@gmail.com'):
    if recipient[:-5:-1] != 'moc.' and recipient[:-5:-1] != 'ten.' and recipient[:-4:-1] != 'ur.' or '@' not in recipient:
        print('Недопустимый адрес получателя!')
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}\n")
    elif sender[:-5:-1] != 'moc.' and sender[:-5:-1] != 'ten.' and sender[:-4:-1] != 'ur.' or '@' not in sender:
        print('Недопустимый адрес отправителя!')
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}\n")
    elif sender == recipient:
        print('Нельзя отправить сообщение самому себе!\n')
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.\n")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.\n")


send_mail('Привет', 'samorodov-artem@mail.ru')
send_mail('Привет', 'samorodov-artem@mail.ru', sender='noreplay@gmail.co')
send_mail('Привет', 'samorodov-artem@mail.r', sender='noreplay@gmail.com')
send_mail('Привет', 'samorodov-artem@mail.ru', sender='samorodov-artem@mail.ru')
send_mail('Привет', 'samorodov-artem@mail.ru', sender='noreplay@gmail.com')
