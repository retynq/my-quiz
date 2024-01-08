import time
from lforvic import *
cont = "akaary2009"
#порядковые числа на -ый
def posx(numx):
    if numx == 2 or numx == 6 or numx == 7 or numx == 8:
        print(numx,"- ой вопрос")
    elif numx == 3:
        print(numx,"- ий вопрос")
    else:
        print(numx,"- ый вопрос")
#пауза 1 сек
def pause():
    time.sleep(1)
#таймер
def countdown(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
#начало
while cont == "akaary2009":
    score = 0
    q_num = 1
    idx = 0
    print("привет! это тест насколько ты меня хорошо знаешь")
    print("в ответах пиши только число, без букв!")
    ready=""
    while ready == "":
        ready = input("в данном тесте 15 вопросов, сконцентрируйся, ты готов?(YES или NO):")
    if ready == "NO":
        print("Выход..")
        break
    elif ready == "YES":
        while q_num<16 and idx<15:
            posx(q_num)
            pause()
            print(questions[idx])
            pause()
            print(guesses[idx])
            pause()
            a = ""
            while a == "":
                a = input("ваш ответ:")
            if a == qa.get(q_num):
                score+=1
                print("правильно!")
            else:
                print("неправильно!")
            q_num +=1
            idx +=1
    elif ready != "YES" or ready != "NO":
        pause()
        print("ты даун, я не оптимизировала эту фигню, мне лень")
        pause()
        print("я тебя выгоняю, пошел. у тебя есть 5 секунд")
        countdown(5)
        break
    pause()
    results = (score*100)/15
    print("ваш результат:", results, "%")
    pause()
    if results < 30:
        print("ты норм, мы точно знакомы?")
    elif results >= 30 and results < 50:
        print("боже может узнаешь меня получше?")
    elif results >= 50 and results < 70:
        print("ну ладно прощаю >:(")
    elif results >= 70 and results < 80:
        print("ты моя лп похоже")
    elif results >=80  and results < 90:
        print("ТЫ ГЕНИЙ РЕАЛЬНО")
    elif results >= 90 and results < 100:
        print("КУДА ПРЕШЬ Я ТЕбЯ Лю")
    elif results == 100:
        print("мы не встречаемся?)")
    elif results > 100:
        print("читер я тебя придушу")
        pause()
        break
    pause()
    cont = input("чтобы выйти нажмите любую клавишу, чтобы начать заново введите akaary2009:")