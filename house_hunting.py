annual_salary   = float(input("What is your annual salary? "))
portion_saved   = float(input("What percent of your salary can you save? "))
total_cost      = float(input("How much does your dream home cost? "))
portion_down_pmt= float(input("What portion of the home price do you need to save? "))
r               = float(input("What is the annual return on your savings? "))  

# defaults:
default_portion_down_pmt    = 0.25
default_r                   = 0.04
current_savings             = 0
num_months                  = 0


# steps to add: If portion, r not given-> assign default. If given, but not decimal, divide by 100

if r == '':
    r = default_r
    print("No value given, default rate of 0.04 applied")

elif r >= 1.0:
    r = r/100        


if portion_down_pmt == '':
    portion_down_pmt = default_portion_down_pmt
    print("No value given, default portion of 25% applied")
elif portion_down_pmt >= 1.0:
    portion_down_pmt = portion_down_pmt/100        


if portion_saved >=1:
    portion_saved = portion_saved/100

#amount you need to get: 
goal_amt        = portion_down_pmt*total_cost
saved_monthly   = (portion_saved*annual_salary)/12


while current_savings < goal_amt:
    current_savings = ((saved_monthly) + (current_savings*(1+(r/12))))
    # print(current_savings)
    num_months += 1

print("You will need to save for ", num_months , " months to buy this house.")




