#Deniapple'ın zımbırtıları (açık kaynak kodlu)
#Lütfen bu projeyi kendinizin gibi gösterip insanlara vermeyiniz. Emek harcadım buna.

import turtle
import random
import time




print("Deniapple'ın zımbırtılarına hoş gelsiniz! (a1.0)")
choosed_task = input("Ne yapmak istersiniz? (spam aracı(1), şifre oluşturucu(2), rastgele şekil oluşturucu(3))")

if choosed_task == "spam aracı" or choosed_task == "Spam aracı" or choosed_task == "1":
    spammed_word = input("Neyi spamlememi istersiniz?")
    spammed_word_count = int(input("Ne kadar spamlememi istersiniz?"))
    print(spammed_word * spammed_word_count)
    time.sleep(5)
elif choosed_task == "şifre oluşturucu" or choosed_task == "Şifre oluşturucu" or choosed_task == "2":
    input("Kullanıcı adınızı giriniz...")
    print("Şifre oluşturuluyor... Lütfen bekliyiniz...")
    password = random.randint(100,100000)
    print("Şifreniz", password)
elif choosed_task == "rastgele şekil oluşturucu" or choosed_task == "Rastgele şekil oluşturucu" or choosed_task == "3":
    t = turtle.Turtle()
    t.shape("classic")
    while True:
        t.fd(random.randint(1,50))
        t.rt(random.randint(1,50))
        t.fd(random.randint(1,50))
        t.circle(random.randint(1,50))

























