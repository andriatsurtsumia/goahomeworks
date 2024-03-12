# შექმენით ორი ცვლადი name - password სადაც მომხარებელს შემოატანიებთ სახელს და პაროლს და ასევე შექმენით მესამე ცვლადი repeat_password 
# სადაც თუ მომხმარებელის შეყვანილი პაროლი არ დაემთხვევა პირველად შეყვანილ პაროლს დაუწერეთ რომ პაროლი არასწორია 
# თუარადა დაუწერეთ "თქვენ წარმატებით გაიარეთ რეგისტრაცია" - გამოიყენეთ if - else


name1 = input("please enter your name: ")
name2 = input("please enter your password ") 

print(name1 + name2) 

repeat_password = 12345

if repeat_password >= 12345:
  print("sworia") 
else:
  print("arasworia") 