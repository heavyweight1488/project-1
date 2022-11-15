from library import book

def search():    
    author = input("Введите автора: ")

    if author in book:
        writer = book[author] 
    elif author not in book:
        return("Такого автора нет в библиотеке.")
     
    books = input("Введите книгу: ")

    if books in writer:
        for i, show in enumerate(writer):
            if books in writer[i]:
                new = writer[i]
                writer[i] = new
            return author, show
    else:
        return("такой книги нет")

        
print(search()) 


def addedBook():
    
    while True:
        
        addOrNot = input("Может хотите добавить книгу? если да -> да, если нет то -> нет. ")
        
        if addOrNot == "да":
            added = input("Введи автора куда хочешь добавить книгу: ")
        elif addOrNot == "нет":
            break
        #elif addOrNot == "да":
           # added = input("Введи автора куда хочешь добавить книгу: ")
            
        if added in book:
            booking = book[added]
        elif added not in book:
            print("Такого автора нет.")
            continue
        
        
        booksAdd = input("Введи книгу которую хочешь добавить: ")
        
        if booksAdd in booking:
            print("Такая книга уже существует. ")
        elif booksAdd not in booking:
            booking.append(booksAdd)
            print(booking)
            print("Книга добавлена.")
        
        
print(addedBook())


def delete():
    
    while True:
        
        addOrNot = input("Может хотите удалить книгу? если да -> да, если нет то -> нет. ")
        
        if addOrNot == "нет":
            break
        elif addOrNot == "да":
            deleting = input("Введи автора где хочешь удалить книгу: ")
        
        if deleting in book:
            booking = book[deleting]
        elif deleting not in book:
            print("Такого автора нет в библиотеке.")
            continue
            
            
        booksdelete = input("Введи книгу которую хочешь удалить: ")
        if booksdelete not in booking:
            print("Такой книги не существует.")
        elif booksdelete in booking:
            booking.remove(booksdelete)
            print(booking)
            print("Книга удалена.")

print(delete())


def contin():
    while True:
        questFirstF = input("хочешь продолжить?")
        if questFirstF == "да":
            questFirstF = search()
        
        elif questFirstF == "нет":
            break
        
        
print(contin())


               
       


    


    
    
    