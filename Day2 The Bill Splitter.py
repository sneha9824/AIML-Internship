Total_Bill_amount = float(input("Enter the Total_Bill_amount"))
number_of_people = int(input("Enter the number_of_people"))
share_per_people = (Total_Bill_amount/number_of_people)
print(f"Total Bill{Total_Bill_amount}, Each person pays: {share_per_people}")

print("Type of Total_Bill_amount:",type(Total_Bill_amount))
print("Type of number_of_people:",type(number_of_people))
print("Type of share_per_people:",type(share_per_people))
