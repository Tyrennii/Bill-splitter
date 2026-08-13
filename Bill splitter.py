total = float(input("Please enter the total: $"))


num_people = int(input("Please enter the amount of people you would like to split the bill with: ")) ## totally couldve used a float here but apparently its better for other people reading tge code to have it using the right value.

def split_bill(total, num_people):
    result = total / num_people
    return(result)
answer = split_bill(total, num_people)
print(f"${answer:.2f}")

