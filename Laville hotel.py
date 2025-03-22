name = input("What is your name: ")
print(f"Hello {name} welcome to Laville hotel!!!!!")
print(f"{name} , what would you like to have today? \n Here is our menu")

food = ["ugali", "kuku", "spaghetti", "fish", "mokimo", "rice"]
for x in food:
    print (x)

drinks = ["soda","juice","lemonade","cocktail","mocktail","whiskey","gin"]
for x in drinks:
    print (x)

print("Place your order")
total = 0
quantity = 0


while True:
    answer = input("My order is :")
    


    if answer == "food":
        preference = input(":")

        if preference == "ugali":
            print("It is available")
            total += 10
            print(f"Your bill is {total}")
            
    
    
        elif preference == "spaghetti":
            print("It is available")
            total += 9
            print(f"Your bill is {total}")
            

        elif preference == "kuku":
            print("It is available")
            total += 15
            print(f"Your bill is {total}")

        elif preference == "fish":
            print("It is available")
            total += 8
            print(f"Your bill is {total}")

        elif preference == "mokimo":
            print("It is available")
            total += 7
            print(f"Your bill is {total}")

        elif preference == "rice":
            print("It is available")
            total += 11
            print(f"Your bill is {total}")

            

        


    elif answer == "drinks":
        preference = input(":")

        if preference == "soda":
            print("It is available,we have \ncoke\nfanta\nsprite\nkrest\nstoney")
            choice = input("Enter your choice: ")
            if choice == "coke":
                print("It is available")
                total += 2
                quantity = int(input("How many do you want?"))
                print(f"Your bill is {total * quantity}")
            elif choice == "fanta":
                print("It is available")
                total += 3
                quantity = int(input("How many do you want?"))
                print(f"Your bill is {total * quantity}")
            elif choice == "sprite":
                print("It is available")
                total += 3
                quantity = int(input("How many do you want?"))
                print(f"Your bill is {total * quantity}")
            elif choice == "krest":
                print("It is available")
                total += 2
                quantity = int(input("How many do you want?"))
                print(f"Your bill is {total * quantity}")
            elif choice == "stoney":
                print("It is available")
                total += 3
                quantity = int(input("How many do you want?"))
                print(f"Your bill is {total * quantity}")
            


            
            
    
    
        elif preference == "juice":
            print("It is available,we have \nmango\norange\npineapple\navocado\napple")
            choice = input("Enter your choice: ")
            if choice == "mango":
                print("It is available")
                total += 2
                quantity = int(input("How many do you want?"))
                print(f"Your bill is {total * quantity}")
            elif choice == "orange":
                print("It is available")
                total += 3
                quantity = int(input("How many do you want?"))
                print(f"Your bill is {total * quantity}")
            elif choice == "pineapple":
                print("It is available")
                total += 3
                quantity = int(input("How many do you want?"))
                print(f"Your bill is {total * quantity}")
               
            elif choice == "avocado":
                print("It is available")
                total += 2
                quantity = int(input("How many do you want?"))
                print(f"Your bill is {total * quantity}")
                
            elif choice == "apple":
                print("It is available")
                total += 3
                quantity = int(input("How many do you want?"))
                print(f"Your bill is {total * quantity}")
                

            

        elif preference == "lemonade":
            print("It is available")
            total += 5
            quantity = int(input("How many do you want?"))
            print(f"Your bill is {total * quantity}")
            
        
        
        elif preference == "cocktail":
            print("It is available")
            total += 6
            quantity = int(input("How many do you want?"))
            print(f"Your bill is {total * quantity}")
           
        elif preference == "mocktail":
            print("It is available")
            total += 6
            quantity = int(input("How many do you want?"))
            print(f"Your bill is {total * quantity}")
           
       
        elif preference == "whiskey":
            print("It is available,we have \nsingleton\njack daniels\nred label\nblack label\nhunters choice")
            choice = input("Enter your choice: ")
            if choice == "singleton":
                print("It is available")
                total += 4
                quantity = int(input("How many do you want?"))
                print(f"Your bill is {total * quantity}")
                
            elif choice == "jack daniels":
                print("It is available")
                total += 5
                quantity = int(input("How many do you want?"))
                print(f"Your bill is {total * quantity}")
                
            elif choice == "red label":
                print("It is available")
                total += 3
                quantity = int(input("How many do you want?"))
                print(f"Your bill is {total * quantity}")
               
            elif choice == "black label":
                print("It is available")
                total += 2
                quantity = int(input("How many do you want?"))
                print(f"Your bill is {total * quantity}")
                
            elif choice == "hunters choice":
                print("It is available")
                total += 3
                quantity = int(input("How many do you want?"))
                print(f"Your bill is {total * quantity}")
                


        elif preference == "gin":
            print("It is available,we have \ntanqueray\ngilbeys\nhendrick's\nlondon dry gin\ngordon's")
            choice = input("Enter your choice: ")
            if choice == "tanqueray":
                print("It is available")
                total += 4
                quantity = int(input("How many do you want?"))
                print(f"Your bill is {total * quantity}")
                
            elif choice == "gilbeys":
                print("It is available")
                total += 5
                quantity = int(input("How many do you want?"))
                print(f"Your bill is {total * quantity}")
                
            elif choice == "hendrick's":
                print("It is available")
                total += 3
                quantity = int(input("How many do you want?"))
                print(f"Your bill is {total * quantity}")
                
            elif choice == "london dry gin":
                print("It is available")
                total += 2
                quantity = int(input("How many do you want?"))
                print(f"Your bill is {total * quantity}")
                
            elif choice == "gordon's":
                print("It is available")
                total += 3
                quantity = int(input("How many do you want?"))
                print(f"Your bill is {total * quantity}")
         
           

    
    else :
        break

print("Your bill is",total)   
print("Welcome back again later !!!")                

    



