total = float(input("Please enter the total: $ "))


num_people = int(input("Please enter the amount of people you would like to split the bill with: ")) ## totally couldve used a float here but apparently its better for other people reading tge code to have it using the right value.

tip_percentage = float(input("please enter the % you would like to tip: % "))

def split_bill(total, num_people, tip_percentage):
    result = total * (tip_percentage / 100) / num_people
    return(result)
answer = split_bill(total, num_people, tip_percentage)
print(f"${answer:.2f}")

