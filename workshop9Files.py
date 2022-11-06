file = open(r"D:\учебный процесс\project-1\pisun\files9.txt")
print(file.read())
file.close()

question = input("what is your name?")
with open("st.txt", "w") as q:
    q.write(question)
    
    
import csv 

with open("cs.csv", "w", encoding='utf-8') as f:
    w = csv.writer(f, delimiter=",")
    
    
    w.writerow(["звездные войны",
                "терминатор",
                "исскуственный интелект"])
    
    w.writerow(["дурак",
                "матильда",
                "левиафан"])
    
    w.writerow(["я-робот",
                "люди в черном",
                "эволюция"])