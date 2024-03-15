#homework.

#მომხმარებელს შემოატანინეთ სახელი, გვარი, ასაკი და საცხოვრებელი ადგილი. თითოეული მათგანი append-ის გამოყენებით დაამატეთ სიაში. slicing-ის გამოყენებით დაბეჭდეთ
#1: სახელი, გვარი, 2: გვარი, ასაკი, 3: სახელი, გვარი, ასაკი 4: გვარი, ასაკი, საცხოვრებელი ადგილი.


name1 = input("please enter your name: ")
name2 = input("please enter your lastname: ")
name3 = input("please eneter your age: ")
name4 = input("please enter your liveplace") 

obj_list = []

obj_list.append("andria")

print(obj_list) 


obj_list.append("tsurtsumia") 

print(obj_list)  


obj_list.append("15") 

print(obj_list) 

obj_list.append("tbilisi") 

print(obj_list) 


obj_list = ["andria", "tsurtsumia", "15", "tbilisi"] 

sliced_obj = obj_list[1:4]

sliced_obj = obj_list[1:4]

print(obj_list)

# მომხმარებელს შემოატანინეთ უარყოფითი რიცხვი. ამ რიცხვიდან 0-მდე არსებული ყველა უარყოფითი რიცხვი დაამატეთ სიაში და საბოლოოდ დაბეჭდეთ სია.


input = ("please enter your number") 

num_list = []

num_list.append(0) 

print(num_list) 

num_list.append(-1) 

print(num_list)  

num_list.append(-2) 

print(num_list) 

num_list.append(-3)

print(num_list) 

num_list.append(-4)

print(num_list) 

num_list.append(-5)

print(num_list)

num_list.append(-6)

print(num_list) 

num_list.append(-7)

print(num_list)

num_list.append(-8)

print(num_list)

num_list.append(-9)

print(num_list)

num_list.append(-10) 

print(num_list) 

num_list = ["0", "-1", "-2", "-3", "-4", "-5", "-6", "-7", "-8", "-9", "-10"] 

print(num_list) 

# ცვლადში შეინახეთ თქვენი სახელი და გვარი. Slicing-ის გამოყენებით ჯერ სახელი, შემდეგ კი გვარი დაბეჭდეთ.


name = "andria tsurtsumia"
sliced_name = name[0:3] 
print(name)   

#სიაში შეინახეთ მინიმუმ 5 საყვარელი ფილმი. გამოიყენეთ Slicing და  დაბეჭდეთ რამდენიმე კომბინაციით. Bonus (არ არის აუცილებელი)


movie_list = ["a bornx tale", "hachiko", "cars 3", "cars 1", "qerchi", "king lion"] 

sliced_movie = movie_list[0:2]

print(movie_list)  

#მომხმარებელს შემოატანინეთ აკადემიის სახელი. თუ ის "G"-თი იწყება, დაუპრინტეთ რომ გოა არის საუკეთესო არჩევანი.სხვა შემთხვევაში დაუპრინტეთ, რომ არასწორი გადაწყვეტილება მიიღო.

name = input("please eneter you academy") 

print(name) 

if academy '=' G:
    print("GREAT decision")
else: 
    print("BAD decision") 
