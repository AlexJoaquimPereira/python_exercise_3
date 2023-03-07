question1 = ["1) Which of the following ingredients is not normally used to brew beer?", "A) Hops", "B)Yeast", "C) Malt", "D) Vinegar", "D"]
question2 = ["2) What is the most densely populated U.S. state?", "A) Connecticut", "B) New Jersey", "C) Rhode Island", "D) Maryland", "B"]
question3 = ["3) King Philip II of Macedonia was assassinated in 336 B.C. and was succeeded by his son. Who was he?", "A) Alexander the Great","B) Philip III", "C) Diadochi", "D) Antigonus II", "A"]
question4 = ["4) What group did Stephen Stills leave to form Crosby, Stills & Nash?", "A) The Yardbirds", "B) The Spencer Davis Band", "C) Buffalo Springfield", "D) Blind Faith", "C"]

prize = 0

print("After each question appears, enter the option\n")

while True:
    i = 0
    while i<5:
        print (question1[i])
        i = i+1
    ans = input()
    if (ans == question1[5]):
        prize = 1000
    else: break

    i = 0
    while i<5:
        print (question2[i])
        i = i+1
    ans = input()
    if (ans == question2[5]):
        prize = 2000
    else: break
        
    i = 0
    while i<5:
        print (question3[i])
        i = i+1
    ans = input()
    if (ans == question3[5]):
        prize = 5000
    else: break
    
    i = 0
    while i<5:
        print (question4[i])
        i = i+1
    ans = input()
    if (ans == question4[5]):
        prize = 10000
        break
    else: break

print("You won ", prize)