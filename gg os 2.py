import time
import webbrowser
import random
from pyowm import OWM
import os
print('процес входа')
c = 0
time.sleep(5)
print('welcome to GGos')
print('app, app2,  cmd , browser, weather, bios, auction,  suprise, game,   q = выйти')
b = input('пожайлуста , выберайте приложение:')
if b == 'app':
    print: str = ("я дед инсайд мне 7 лет")
    a = ('1000 - 7')
    while True:
        time.sleep(0.40)
        print(a)
        webbrowser.open('https://www.google.com', new=2)
elif b == 'app2':
    w = input('веддите число')
    s = input('веддите 2 число')
    d = input('выбериай действие + -')
    if d == '+':
        p = w + s
    print(p)
elif b == 'q':
    print("завершение работы всего хорошего")
    time.sleep(10)
    quit()

elif b == 'browser':
    print("список сайтов:")
    print("text-host.com")
    print('-kartinki.com')
    print('info-gg.info')
    print('google')
    print('izvestia')
    print('wikipedia')
    site = input('выбирайте сайт пожайлуста')
    if site == 'info-gg.info':
        print('OS:gg.os v.e.r:1.0')
        site = input('выбирайте сайт пожайлуста')
    if site == 'text-host.com':
        print('орк - это фантасчическое существо которого в реальности не существует')
        print('python - язык прогорамирования самый распостронёный язык в мире ')
        site = input('выбирайте сайт пожайлуста')
    if site == '-kartinki.com':
        print('хаха это кликбейт')
        time.sleep(3)
        quit()
    if site == 'google':
        webbrowser.open('https://www.google.com', new=2)
    if site == 'izvestia':
        webbrowser.open('https://iz.ru', new=2)
    if site == 'wikipedia':
        webbrowser.open('https://ru.wikipedia.org', new=2)
elif b == 'cmd':
    c = input('C:Users/:')
if c == 'help':
    print('activate')
    print('quit')
elif c == 'activate':
    print("Активация gg os")
    time.sleep(3)
    print("поздровляем активация прошла успешно")
    c = input('C:Users/:')
elif c == 'quit':
    quit()
elif b == 'weather':
    owm = OWM('d1e401a41c9cfe121b98b2a9e2c9e3a0')

    place = input(
        'В каком городе хотите узнать погоду на пример  Moscow .Веддите на англиском точное название города: ')
    monitoring = owm.weather_manager().weather_at_place(place)
    weather = monitoring.weather
    status = weather.detailed_status
    print(f' {status} в {place} сейчас.')
elif b == 'bios':
    update = input('update')
    if update == 'y':
        brick = bool(random.choice([True, False]))
        if brick == False:
            print('your system is brick')
            time.sleep(3)
            quit()
        else:
            print('your system is update')
elif b == 'auction':
    print('Добро пожаловать на аукцион')
    print('passport 0 егориков')
    print('chips doritos 1000 егориков')
    print('kick бесплатно')
    print('0 егориков 100000 егориков')
    price = input('какой товар хотите взять')
    print('отлично, по поводу ' + price + (" обращаетесь по тел.  +7 (917) 007 43 56"))
elif b == 'suprise':
    os.mkdir('لاييبابيلتايبلتنيلتنبلينبتابينابنتبايتبيابيمبيت')
elif b == 'game':
    print('добро пожаловать в симулятор боксов!')
    megayashikov140 = input('купите акцию 2 ящиков да = y')
    if megayashikov140 == 'y':
        awsd = input('press f:')
    if awsd == 'f':
        print('содержимое 10 плейегориков и боец')
        boyec = input('нажмите f чтобы узнать инфармацию о бойце')
    if boyec == 'f':
        print('Егор харестиристики: Владелец сервера, одобрил множество идей xp:5000 - 6000  lvl: 5000 power: 130')
        yashik = input('открыть ещё да = y:')
    if yashik == 'y':
        awsd2 = input('press f:')
    if awsd2 == 'f':
        print("содержимое 10 плейегориков и боец")
        print("Федя харестеристики: админ сервера, карьерная лестница xp: 3000 - 4000 lvl:1000 power: 100")
        magaz = input("зайти в магаз??? y = да")
    if magaz == 'y':
        syperyashiks = input("купить ящиик цена 20 баланс 20 y = да")
        yashiks = input("press f:")
    if yashiks == 'f':
        print("содержимое 20 плейегориков и боец")
        boyecs = input("нажмите f чтобы узнать инфармацию о бойце")
    if boyecs == 'f':
        print(
            "вы открыли секретного бойца Сергей харестеристики: хранитель сервера сделал огромный вклад в сервер среди других имено он создал и придумал gg os и все идеи были его на сервере (почти) xp:5000 - 6000 lvL: 250 power: 120")
        play = input("зайти в игру??? y = да")
    if play == 'y':
        boyec_p = input('выбери бойца Сергей , Федя, Егор')
    if boyec_p == "Сергей":
        point1 = 120
        point_bot = 110
        if point1 > point_bot:
            print("Вы выиграли :)")
            print('coming soon')
        if point1 < point_bot:
            print("Вы проиграли :(")
            print('coming soon')
    elif boyec_p == "Федя":
        point2 = 100
        point_bot = 110
        if point2 > point_bot:
            print("Вы выиграли :)")
            print('coming soon')
        if point2 < point_bot:
            print("Вы проиграли :(")
            print('coming soon')
    elif boyec_p == "Егор":
        point3 = 130
        point_bot = 110
        if point3 > point_bot:
            print("Вы выиграли :)")
            print("coming soon")
        if point3 < point_bot:
            print("Вы проиграли :(")
            print("coming soon")

