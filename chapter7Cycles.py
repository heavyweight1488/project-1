name = "Тед"
for character in name:
    print(character)
  
shows = ["Во все тяжкие","Секретные материалы","Фарго"]  
for shows in shows:
    print(shows)
    

coms = ("Теория большого взрыва",
        "Друзья","Папины дочки")
for shows in coms:
    print(shows)


people = {"Джим Парсонс": "Теория большого взрыва",
          "Брайн Крэнтсон": "Во все тяжкие",
          "Екатерина Старшова": "Папины дочки"}
for character in people:
    print(character)
    

tv = ["Во все тяжкие", 
      "Секретные материалы",
      "Фарго"]
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1
print(tv)


tv = ["Во все тяжкие", 
      "Секретные материалы",
      "Фарго"]
for i, show in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new
print(tv)


tv = ["Во все тяжкие", 
      "Секретные материалы",
      "Фарго"]
coms = ("Теория большого взрыва",
        "Друзья","Папины дочки")
allShows = []
for show in tv:
    show = show.upper()
    allShows.append(show)
for show in coms:
    show = show.upper()
    allShows.append(show)
print(allShows)


for i in range(1,9):
    print(i)
    
    
x = 10
while x > 0 :
    print('{}'.format(x))
    x -= 1
print("С Новым годом !")


for i in range (0,100):
    print(i)
    break

qs = ["What is your name?",
      "Your favorite color?",
      "What are you doing?"]
n = 0
while True:
    print("Введи X для выхода")
    a = input(qs[n])
    if a == "X":
        break
    n = (n + 1) % 3
    
    
for i in range(1,6):
    if i == 3:
        continue
    print(i)
    
    
i = 1
while i<=5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
    
    
for i in range(1,4):
    print(i)
    for letter in ["a", "b", "v"]:
        print(letter)



list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)
print(added)


while input ('д или н?') != 'н':
    for i in range(1,6):
        print(i)
    

    

    
