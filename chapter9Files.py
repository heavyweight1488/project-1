st = open("st.txt", "w")
st.write("hello pythin!")
st.close()

with open("st.txt", "r") as f:
    print(f.read())
    
    
my_list = list()

with open("st.txt", "r") as f:
    my_list.append(f.read())
    
print(my_list)


import csv

with open("st.csv", "w") as f:
    w = csv.writer(f,
                   delimiter=",")
    
    w.writerow(["one",
                "two",
                "three"])
    
    w.writerow(["four",
                "five",
                "six"])
    