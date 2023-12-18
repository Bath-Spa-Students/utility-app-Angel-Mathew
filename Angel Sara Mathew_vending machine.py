# introduction to my  vending machine
print("Hello")
print("Welcome to Legna pastries and bakery vending machine")
print("----------------------------------------------------")
print("Welcome for drinks as well from Legna vending machine")
print("what would like? here is the menu")

# items in Legna vending machine
Legna={"A01":{"Name":"Zaatar Crossiant","Code":"A01","Price":"$3.27","Stock":15},
       "A02":{"Name":"Plain Crossiant","Code":"A02","Price":"$2.38","Stock":10},
       "A03":{"Name":"Chocolate Crossiant","Code":"A03","Price":"$0.37","Stock":10},
       "A04":{"Name":"Chicken Sandwich","Code":"A04","Price":"$4.58","Stock":7},
       "A05":{"Name":"Veg Sandwich","Code":"A05","Price":"$2.14","stock":7},
       "A06":{"Name":"Chicken Puff","Code":"A06","Price":"$0.54","Stock":9},
       "A07":{"Name":"Veg Puff","Code":"A07","Price":"$0.54","Stock":9},
       "A08":{"Name":"Egg Puff","Code":"A08","Price":"$0.82","Stock":8},
       "A09":{"Name":"Sweet Puff","Code":"A09","Price":"$2.72","Stock":9},
       "A10":{"Name":"Baklava","Code":"A10","Price":"$16.34","Stock":14},
       "A11":{"Name":"Kunafa","Code":"A11","Price":"$3.53","Stock":11},
       "A12":{"Name":"Cream Bun","Code":"A12","Price":"$1.75","Stock":12},
       "A13":{"Name":"Strawberry Tart","Code":"A13","Price":"$7.35","Stock":10},
       "A14":{"Name":"Borrachuelos","Code":"A14","Price":"$13.91","Stock":15},
       "A15":{"Name":"Eccles Cake","Code":"A15","Price":"$5.00","Stock":5},
       "A16":{"Name":"Vanilla Cupcake","Code":"A16","Price":"$6.81","Stock":13},
       "A17":{"Name":"Milk Cake","Code":"A17","Price":"$6.00","Stock":7},
       "A18":{"Name":"Whole Wheat jaggery cake","Code":"A18","Price":"$6.81","Stock":6},
       "A19":{"Name":"Marble Cake","Code":"A19","Price":"$2.41","Stock":10},
       "A20":{"Name":"Dream Cake","Code":"A20","Price":"$1.26","Stock":9},
       "...":{"....":"..........","....":"...",".....":".....",".....":"."},
       "B01":{"Drinks":"Soya Milk","Code":"B01","Price":"$2.53","Stock":2},
        "B02":{"Drinks":"Cold Water","Code":"B02","Price":"$1.00","Stock":5},
        "B03":{"Drinks":"Hot Water","Code":"B03","Price":"$1.00","Stock":5},
        "B04":{"Drinks":"Mountain Dew","Code":"B04","Price":"$2.75","Stock":6},
        "B05":{"Drinks":"Tea","Code":"B05","Price":"$1.36","Stock":5},
        "B06":{"Drinks":"Coffee","Code":"B06","Price":"$1.36","Stock":5}}

#Creating headers for the table:
headers = ['Name','Code','Price','Stock']
headers=['Drinks and snacks','Code','Price','Stock',]

#Displays the menu for customer: 
print("--------")
print(f"{headers[0]: <30} | {headers[1]: <30} | {headers[2]: <30} | {headers[3]: <30} | ")
for product_key,product_details in Legna.items():
    print("")
    for keys,value in product_details.items():
        print(f"{value: <30} |", end=" ")

#taking order from the customer:
print("-----------------")
print("\n your order please")
print("-------------------")
Order=input("\n\nEnter the code:")
if Order in Legna:
    item_choice = Legna[Order]
    print (f"Choice: {item_choice}")

#check if the selected item is valid and finding the price:
if Order in Legna:
    Ordered_Legna=Legna[Order]

#check if it is a pastry:
if 'Name' in Ordered_Legna:
   print(f"You have ordered {Ordered_Legna['Name']} : ", end="")

# convert price string to float 
   Price=float(Ordered_Legna["Price"].replace('$',""))
   print(Price)

# check if it is a Drink:
elif 'Drinks' in Ordered_Legna:
    print(f"You have ordered {Ordered_Legna['Drinks']} : ", end="")

# convert price string to float  
    Price=float(Ordered_Legna["Price"].replace('$',""))
    print(Price)

#insert money into Legna vending machine by customer:
print("--------------------------------")
print("insert money")
print(".............")

Total_cost=float(input("enter the cost:"))
Balance=Total_cost-Price
print("\n\n--------------------------------")
print("Balance : ",Balance,"\n")
print("\n...................................")

print("Thank you for purchasing", "\n Have a busy day enjoy the delicious food from Legna")
print("If any feedback please leave it on the counter,if possible we will try to solve the problem",
      "\n making it comfortable and tasty according to your wish")
print("<:) Bye")
print("\n******************************************************************************************")

