def send_mail(message, recipient, sender="university.help@gmail.com"):
    if recipient[:-5:-1] != 'moc.' and recipient[:-5:-1] != 'ten.' and recipient[:-4:-1] != 'ur.' or '@' not in recipient:
        print('Недопустимый адрес получателя!')
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender[:-5:-1] != 'moc.' and sender[:-5:-1] != 'ten.' and sender[:-4:-1] != 'ur.' or '@' not in sender:
        print('Недопустимый адрес отправителя!')
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print('Нельзя отправить сообщение самому себе!')
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_mail('Привет', 'samorodov-artem@mail.ru')
send_mail('Привет', 'samorodov-artem@mail.r', 'noreplay@gmail.com')
send_mail('Привет', 'samorodov-artem@mail.ru', 'noreplaygmail.com')
send_mail('Привет', 'samorodov-artem@mail.ru', 'samorodov-artem@mail.ru')
send_mail('Привет', 'samorodov-artem@mail.ru', 'noreplay@gmail.com')
