#Stage A - Arithmetic operators
"""a =17
b=5

print("a+b=",a+b)   #Addition
print("a-b=",a-b)   #Subtraction
print("a*b=",a*b)   #Multiplication
print("a/b=",a/b)   #Division
print("a//b=",a//b) #floor Divsion. Do division then drop the decimal
print("a%b=",a%b)   #Modulus
print("a**b=",a**b) #Exponet

print("-"*40)
balance = 10000   
balance += 2500  #augment - add 2500 to whatever balace its(10000)
print(balance)
balance -= 4000   #substract 4000 from waht the new balance is. 
print(balance)
balance *= 2     #multiply the new balance by 2
print(balance)     
balance //= 3       
print(balance)

#A standard Lagos plot is 36 m by 18 m. Calculate its area and the length of fencing needed to go all the way round.
plot_length = 36
plot_breadth = 18

area =plot_breadth*plot_length

fencing = 2 *(plot_length+plot_breadth)
print(f'{"Area: "}{area }{" Square meters"}')
print(F'Fence Lenghth:{fencing} Meters')

#A rectangular water tank is 2 m long, 1.5 m wide and 1.2 m high. Print its volume in cubic metres and its capacity in litres (1 m³ = 1,000 litres). Look closely at the volume. Can you explain the strange digits? (Stage C explains.)
tank_length =2
tank_width =1.5
tank_height = 1.2
#Volume = length × width × height
volume =tank_height*tank_width*tank_length

print(f'The volume of the rectangular tank is: {volume:.2f}m³')
#Litres = volume (m³) × 1,000

liter = volume * 1000
print(F'Tank Liters: {liter:,.0f} liters')

# Stage B — Floor division and modulus in real life
total_naira =25000
people =3

each = total_naira//people
left_over =total_naira%people
print(f'Each Person get N{each}')
print(f'Leftover: N{left_over}')

#when you convert a small unit into a bigger one eg minuite to hours, you usually get a whole number of the big unit plus some left over.
minutes = 135
print(f'{minutes}minuites = {minutes//60}hrs:{minutes%60}min')"""

'''print("-")
#Even or odd
#Every whole number divided by 2 leaves a remainder of either 0 or 1:
user_number =int(input(" Enter your number:"))
if user_number % 2 == 0:
    print("You enterd an Even Number")
else:
    print("You entered an Odd Number")

#▪	Last digit: number % 10 gives the last digit; number // 10 removes it.
number =168
print(number%10)  #number value % 10 give the last digit of the number
print(number//10) #number value // 10 removes the last digit of the number

#Divisibility
#If the remainder is 0, the number divides exactly:

print(100 % 4 == 0)    # if a % b == 0, then a divides exactly by b.

#For example, you can check whether 100 eggs fill 25 trays of 4 with none left over.
number_of_eggs=100
number_of_tray =4 #how many eggs fit in one tray (4)

print(number_of_eggs%number_of_tray ==0) # if I divive 100 by 4 will I get zero- no ramainder.

print(10 % 2, 7 % 2) #Check for even and odd number
print(2026 % 10)     #A number %10 gives the last digit
print(2026 // 10)    #A number // 10 throws away the last unit
print(100 % 7 == 2)  #checks if 100%7 gives remainder 2

#A farm collected 1,000 eggs. A crate holds 30. How many full crates are there, and how many loose eggs are left?
eggs_collected =1000
crates_holds =30
full_Crates=(eggs_collected//crates_holds)
print(f'Full crates are:{full_Crates}')
loose_eggs=(eggs_collected%crates_holds)
print(f'Loose eggs are:{loose_eggs}')

#A video is 500 seconds long. Print its length in minutes and seconds using // and %.
video_length = 500
length_min =video_length//60
length_sec=video_length%60
print(f"Video Length in minuite: {length_min}min:{length_sec}sec")

#Convert 5,000 seconds into hours, minutes and seconds. (Hint: you will need both // and % twice.)
total_seconds =5000
total_minute=total_seconds//60
seconds=total_seconds%60
print(total_minute)
print(seconds)

hour = total_minute//60
minute =total_minute%60

print(f'we have: {hour}hr:{minute}min:{seconds}sec')


print("="*60)
#Stage C  —  Precedence, Floats and Rounding
print(2 + 3 * 4) #Multiplication goes before addition:
print((2 + 3) * 4) #Brackets go first, so they change the answer:
print(2 ** 3 ** 2)  #Most operators work left to right, but ** works right to left: so 2 ** 9 -3 ** 2 first
print(10 / 2, type(10 / 2)) #/ always give a float even if the number is a whole number. if you want it to return whole number use //
print(0.1 + 0.2)
print(round(0.1 + 0.2, 2)) #round()function always round down to the nearest number so our output would be 0.3 not 0.30
#When in doubt, add brackets. They cost nothing and make your intention obvious to the next reader.
print(round(2.5), round(3.5))
print(round(7.456, 1)) #round to one decimal place
print(abs(-12))        #abs removes the sign at the front to give just the number
print(divmod(17, 5))   #divmod gives the // and % value together
print(pow(2, 8))       #pow is same as **

print(10 - 4 / 2)
print((10 - 4) / 2)
print(7 // 2 * 2 + 7 % 2) #By precedence // then * Then% before +
print(-7 // 2)       #// and % round down so -4

#Predict, then check: what do int(7 / 2), round(7 / 2) and 7 // 2 each produce?
print(int(7/2)) #int division the number before the decimal so output 3
print(round(7/2)) # round at an excalt half round to the nearest even number so output 4
print(7//2)       #// round down and 3


# Stage D — Smart CLI Calculator (full build)
print("=" * 36)
print(f"{'AIRS SMART CALCULATOR':^36}")
print("=" * 36)
print("Operators:  +  -  *  /  //  %  **")

result = None  # No answer yet
message = ""
a = float(input("First number: "))
op = input("Operator: ")
b = float(input("Second number: "))
if op in ("/", "//", "%") and b == 0:  #This help manage the calculator validations
    message = "Cannot divide by zero."
elif op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    result = a / b
elif op == "//":
    result = a // b
elif op == "%":
    result = a % b
elif op == "**":
    result = a ** b
else:
    message = f"'{op}' is not a supported operator."
 
print("-" * 36)
if result is None:
    print("Error:", message)
else:
    print(f"{a:g} {op} {b:g} = {round(result, 4):,}")

#Comparison operators
op = "*"
print(op == "*", op != "+")
print(op in ("+", "-", "*", "/"))
print(5 >= 5, 3 < 2)
result = None
print(result is None)

#= stores value. == compares values

#Ask the user for a whole number and print whether it is even or odd, using % and if / else.
whole_number = int(input("Enter a whole number: "))
if whole_number %2 == 0:
    print(f'{whole_number} is an even number')
else:
    print(f"{whole_number} is an odd number")

#VAT Calculator
#Nigeria's VAT rate is 7.5%. Ask for a subtotal and print the subtotal, the VAT amount and the total as a neatly aligned three-line receipt. Store the rate in a constant.

VAT_RATE = 0.075 #7.5 stored as a fraction
                #Why 0.075, not 7.5? To find 7.5% of something, you multiply by 7.5 ÷ 100 = 0.075. Multiplying by 7.5 would charge 750% VAT!

subtotal = float(input("Enter subtotal (N): "))
vat =subtotal *VAT_RATE
total = subtotal + vat

vat_label = f"VAT {VAT_RATE:.1%}:"

print("-"*28)
print(f"{'Subtotal:':<12}N{subtotal:>15,.2f}")
print(f"{vat_label:<12}N{vat:>15,.2f}")
print(f"{'Total:':<12}N{total:>15,.2f}")
print("-"*28)


#APPLIED   Simple Interest Calculator

#Ask for an amount saved, a yearly interest rate (%) and a number of years. Use the formula interest = principal × rate × years ÷ 100 and print the interest and final amount as money.

amount_saved = float(input("Enter amount saved: "))
yearly_interest = float(input("Enter your yearly interest rate (%): "))
number_of_years = float(input("Enter number of year(s): "))

interest = (amount_saved*yearly_interest*number_of_years )/100
final_Amount = amount_saved+interest

print("*"*36)
print (f"{'Amount Saved: ':<18}N{amount_saved:>15,.2F}")
print (f"{'Yearly Interest: ':<18}N{yearly_interest:>15g}%")
print (f"{'Number of Years: ':<18}{number_of_years:>15g}")
print (f"{'Interest Earned: ':<18}N{interest :>15,.2F}")
print (f"{'Total Amount: ':<18}N{final_Amount:>15,.2F}")'''


#An ATM pays out ₦1000, ₦500, ₦200 and ₦100 notes. Ask for an amount and print how many of each note to give, using the fewest notes, plus any amount that cannot be paid. Use only // and %. No if statements needed!


amount = int(input("Enter amount (N): "))

n1000 = amount // 1000          # how many N1000 notes
remaining = amount % 1000       # what's left

n500 = remaining // 500
remaining = remaining % 500

n200 = remaining // 200
remaining = remaining % 200

n100 = remaining // 100
remaining = remaining % 100     # what no note can pay

print(f"N1000 notes: {n1000}")
print(f"N500 notes:  {n500}")
print(f"N200 notes:  {n200}")
print(f"N100 notes:  {n100}")
print(f"Cannot pay:  N{remaining}")

#Add a currency-conversion mode: ask for today's Naira-to-Dollar rate and an amount in Naira, and print the Dollar value formatted as money.
dollar_rate = float(input("Todays dollar rate (Naira per 1$): "))
amount= float(input("Naira amount: "))
dollar_conversion = amount/dollar_rate
print(f'The dolar value is ${dollar_conversion:,.2f}')
















