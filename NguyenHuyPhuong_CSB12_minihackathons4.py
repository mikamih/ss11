# #Bài 1:
# dict5={'HP': 20,
#        'DELL': 50,
#        'MACBOOK': 12,
#        'ASUS': 305}
# print('The number of macbook left: ',dict5.get('MACBOOK'))
# a= input('please choose a product: ')
# print('Available',a,":",dict5.get(a))

# #Bài 2:
# dict5.update({'Toshiba':10})
# print (dict5)
# brand= input('input a brand: ')
# amount= int(input('input amount: '))
# dict5[brand] = amount
# print(dict5)
# dict5['DELL']+=10
# dict5['MACBOOK']-=10
# print(dict5)

# #Bài 3
# pricegobrrrrr={'HP': 600, 
#                'DELL': 650,
#                'MACBOOK':1200,
#                'ASUS':400}
# print('price of ASUS:',pricegobrrrrr.get('ASUS'))
# brandsearch=input('input a brand: ')
# print('Price of',brandsearch,':', pricegobrrrrr.get(brandsearch))

# orderbrand = "ASUS"
# orderquantity = 5
# orderprice = pricegobrrrrr[orderbrand] * orderquantity
# print("Total price:", orderprice)

# order_brand = input("Input a brand: ")
# order_quantity = int(input("Input amount to buy: "))
# order_price = pricegobrrrrr[order_brand] * order_quantity
# print("Total price:", order_price)


#Bài 6
dict6={'Name': 'Light',
        'Age': 17,
        'Strength': 8,
        'Defense': 10,
        'HP': 100,
        'Backpack': ['Shield', 'Bread Loaf'],
        'Gold': 100,
        'Level': 2}
dict6.get('Backpack').append('Flint stone')
dict6['Gold'] += 50
print (dict6)

#Bài 7
skills=[{"Name": "Tackle",
        "Minimum level:": 1,
        "Damage": 5,
        "Hit rate": 0.3},
        {"Name": "Quick Attack",
        "Minimum level:": 2,
        "Damage": 3,
        "Hit rate": 0.5},
        {"Name": "Strong Kick",
        "Minimum level:": 4,
        "Damage": 9,
        "Hit rate": 0.2}]

for i, skill in enumerate(skills, start=1):
    print(f"skill {i}: {skill['Name']}" )

chosen_skill = int(input("Choose skill by number: ")) -1
if chosen_skill < len(skills):
    skill = skills[chosen_skill]
    if dict6["Level"] >= skill ["Minimum level"]:
        print(f"You Chose {skill['Name']}.")
        print(f"Damage: {skill['Damage']}")
    else:
        print("Cannot deploy. Required level",skill['Minimum level'])
else:
   print("Invalid skill choice")