name = "Тед"
for character in name:
    print(character)
    
shows = ["во все тяжкие", "секретные материалы", "фарго"]
for show in shows:
    print(show)
    

coms = ("теория большого взрыва",
        "друзья",
        "папины дочки")
for show in coms:
    print(show)
    

people = {"Джим Персонс":
        "Теория большого взрыва",
        "Брайн Ккрэнтсон":
        "Во все тяжкие",
        "Екаткрина Старшова":
        "Папины дочки"}
for film in people :
    print(film)
    

    
    
    tv = ["во все тяжкие", "секретные материалы", "фарго"]
for i, show in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new 
    
print(tv)
    

tv = ["во все тяжкие", "секретные материалы", "фарго"]
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

    print(tv)
    
    
tv = ["во все тяжкие", "секретные материалы", "фарго"]
coms = ["теория большого взрыва",
        "друзья",
        "папины дочки"]
allShows = []
for show in tv:
    show = show.upper()
    allShows.append(show)
for show in coms:
    show = show.upper()
    allShows.append(show)
print(allShows)


for i in range(1,11):
    print(i)
    
    
x = 10 
while x > 0:
    print ('{}'.format(x))
    x -= 1
print("с новым годом !")
    
    
for i in range(0,100):
    print(i)
    break


qs = ["как тебя зовут?",
      "твой любимый цвет?",
      "что ты делаешь?"]
n = 0
while True:
    print("введи X для выхода")
    a = input(qs[n])
    if a == "X":
        break
    n = (n + 1) % 3
    
