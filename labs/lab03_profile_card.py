"""#stagee A - Variable and data type
name = "Amaka Obi"
age =19
height_m = 1.68
is_errolled = True

print(name,age,height_m,is_errolled)

print(name,str(age) + "yr",height_m,is_errolled)
print(type(name))
print(type(age))
print(type(height_m))
print(type(is_errolled))

x,y,z =1,2.5,"three" #declaring several variable

print(x)
print(y)
print(z)

phone="Iphone"
storage_gb=256
price= 800000.0
is_new =False

print(phone, type(phone))
print(storage_gb, type(storage_gb))
print(price,type(price))
print(is_new, type(is_new))

a= "Lagos"
b= "Abuja"

#Store "Lagos" in a and "Abuja" in b. Swap their values in a single line, then print both.
a,b=b,a
print (a)
print(b)

d=7/2
print(d)

## Stage B — Getting input and converting types
CURRENT_YEAR=2026   # To define a contant, that which we dont want to change. We define the variable in capital letters. It is a convention that tells other programmers "do not modify this". If the year changes, you update it in one place and the whole program stays correct.
name=input("What is your name?",)
birth_year=input("Year of birth?",)
print("Year of birth is stored as:", type(birth_year))
birth_year =int(birth_year)
age = current_year -birth_year
print ("hello", name, "your age is", str(age)+"years")

#Ask for an item name, its price and the quantity, then print the total cost. Use float() for the price and int() for the quantity.
UNIT_PRICE = 68500.50
item_bought =input("what are you buying?")
quatity_bought =input("How many are you buying?")
print(quatity_bought)
total_cost = UNIT_PRICE*int(quatity_bought)
print(f"Total amount for {quatity_bought} bag(s) of rice is {quatity}")

#Write a fuel calculator: ask for the number of litres and the price per litre, then print the total to pay
num_liters =input("How many liters do you want? ")
price_per_liter=float(input("what is the price per liter "))
total_amount = float(num_liters)*(price_per_liter)
print(f"Total cost for yu fuel is {total_amount}")

#F string and its specifier
amount =1234567.8915
print(f'{amount:,}')     #thousand seperator

print(F"{amount:,.2f}") #thousand seperator and value in 2 decimal place

print(f"{amount:.1%}") #multiply by 100 and add % at the front

#:05 Zero padding is used when ever number must all have same lenth eg student id.

student = 5
print(f"{student:05}")

hours, minutes = 9, 5
print(f"{hours:02}:{minutes:02}")

print(f'{"left":-<10}|')

print(f"{'Help':*^20}")

print(f"{2+3 = }")
print(f"{2-3 = }")

#Print one receipt line for 2 laptop bags at N18,500 each: the item left-aligned in 15 characters, quantity right-aligned in 5, and the total right-aligned in 12 with commas and 2 decimals.
quantity = 2
cost_per_item=18500
total_cost =quantity*cost_per_item
print (f"{'Laptop bag':<15}{quantity:>5}{total_cost:>12,.2f}")

#A learner scored 72 out of 80. Print a sentence showing the score and the percentage with one decimal place, using the % format specifier.
score=72
total_score =80
percentage =score/total_score
print(f"'You scored'{score}/{total_score}'which is'{percentage:.1%}" )

#Stage D  —  The Complete Profile Card
CURRENT_YEAR =2026
COURSE_WEEKS =8

print("="*40)
print(f"{'AIRS LEARNER PROFILE CARD':^40}")
print("="*40)

name = input("Full name:")
birth_year = int(input("year of birth: "))
city =input("City: ")
track =input ("Diploma track(AI/Robotics): ")
weekly_hours = float(input("study hours per week: "))
age = CURRENT_YEAR -birth_year
total_hours =weekly_hours *COURSE_WEEKS
print() #print() with nothing inside prints an empty line, adding space between the questions and the card.
print("-"*40)
print(f"{'Name:':<15}{name.title()}") #.title change the name in proper case (First letter in name start with capital letter)
print(f"{'age':<15}{age}")
print(f"{'city:':<15}{city.title()}")
print(f"{'Track:':<15}{track.upper()}")
print(f"{'Study plan:':<15}{weekly_hours}hrs/week")
print(f"{'Course total:':<15}{total_hours:.1f}hrs in {COURSE_WEEKS}Weeks")
print("="*40)

city ="  LAGOS state "
print("[" + city +"]") #"[]" is to check if there are hidden space in the test. it can be any special character
print("[" + city.strip() + "]") # Remove starting and ending white space
print(city.strip().title()) # Remove whitespaces and capitalise each word
print(city.strip().upper()) # Remove whitespaces and all letters capitalised
print(city.strip().lower())
print(len(city.strip())) #Remove surrounding white space and tell me the nunber of character in the word
print(city.strip().replace("LAGOS state", "Benin"))

#Ask for a product name, then print it in title case and upper case, and print how many characters it has.
print("-"*50)
product_name =input("What is the product name: ")
print('Product name is ',product_name.strip())
print('Title Case :',product_name.title())
print('Upper Case :',product_name.upper())
print("character :", len(product_name))

#Users often type emails with stray spaces and capital letters. Ask for an email address and print a cleaned version with no surrounding spaces, all in lowercase.

email =input("Enter your email address :")
saved_email=(email.strip().lower())
print(f"{'Saved Email: '}{saved_email}")

#Ask for the price and size (GB) of two mobile data plans, then print the cost per GB of each, formatted as money. Which is better value?
#DATA PLAN ANALYSI
plan_a_price =float(input("What is the price for plan A: "))
plan_a_gb =float(input("How many gB is plan A: "))

plan_b_price =float(input("What is the price for plan B: "))
plan_b_gb =float(input("How many gB is plan B: "))

cost_per_gb_a =(plan_a_price/plan_a_gb)
cost_per_gb_b =(plan_b_price/plan_b_gb)


print(f"Cost per GB for plan A is: N{cost_per_gb_a:,.2f}")
print(f"Cost per GB for plan B is: N{cost_per_gb_b:,.2f}")

if cost_per_gb_a < cost_per_gb_b:
    print("Plan A is better value.")
elif cost_per_gb_b < cost_per_gb_a:
    print("Plan B is better value.") 
else:
    print("Both plans give the same value.")

#Ask for an amount in Naira (it may have kobo, e.g. 1250.75) and print the same amount in kobo as a whole number with thousand separators. Hint: multiply by 100, then round() and int().
withdraw = float(input("How much are you withdrawing: "))
money_received = int(round(withdraw*100)) #Round() here help handle kobo Value by rounding to the nearest whole number
print(f'This is the money dispensed: N{money_received:,}')"""

print("^" *50)
#Ask for a name, role, phone number and email. Print a boxed business card 36 characters wide: the name in capitals and the role in title case, both centred, then left-aligned phone and email 
name =input("What is your name: ").strip().upper()
role=input("Please input your role: ").strip().title()
phone_number =(input("Enter your call line: ")).strip()
email=input("Enter your email address: ").strip().lower()

border=("+" + "-"*34 + "+")
print()
print(border)

print(f'|{name:^34}|')
print(f'|{role:^34}|')
print(f"|{' ':34}|")
print(f"|{'Phone: '+ phone_number:<34}|")
print(f"|{'Email:'+ email:<34}|")

print(border)

