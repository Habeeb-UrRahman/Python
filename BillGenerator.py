fruits=['Banana','Oranges','Apple','Pear']
# stock = {"Banana": 600,"Apple": 1000,"Oranges": 3020,"Pear": 1500}
stock = {"Banana" : 600, "Apple" : 1000, "Oranges" : 3000, "Pear" : 1600}
prices = {"Banana": 18,"Apple": 37,"Oranges": 15,"Pear": 10}

print("Welcome to our online fruit market ")
print("\nThe fruits  available in our marketplace are: ")
def compute_bill():
    total=0
    for k in range(50):
        print("\nFruits: ", "\t","Fruit code: ")
        print("\nBanana \t-->\t 1001\nApple \t-->\t 1002\nOranges -->\t 1003\nPear \t-->\t 1004\n")
        a=int((input("Enter code of the fruit you're looking for: ")))
        quantity=int(input("Enter quantity required for selected fruit: "))
        if a==1001:
            b='Banana'
        elif a==1002:
            b='Apple'
        elif a==1003:
            b='Oranges'
        elif a==1004:
             b='Pear'
        else:
            print("\n Please enter a valid choice ")
            return
        if quantity>stock[b]:
            print("Sorry, we do not have the requested quantity for the selected fruit")
            break
        if stock[b]>0:
            print("-----------------------BILL-------------------------")
            print("Fruit: ",b,quantity,"No.s","\nTotal Price: ",prices[b]*quantity)
            total+=prices[b]
            stock[b]-=quantity
        else:
            print("\nSorry the fruits are out of stock ")       
        b=(input("Press 'next' to continue or 'cancel' to exit : ")) 
        if b==next:
            continue
        else:
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            print("Your total bill is: ", u'\u20B9',total*quantity) # Here u\u20B9 print the rupee symbol
            print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
            print("Stocks remianing after bill: ")
            for i in stock:
                print(i,"\t",stock[i])
            return

compute_bill()


