def calculatingAverage():
    average_list = []
    while True:
        user_no = int(input("Enter the numbers: "))
        if user_no == -1:
            break
        average_list.append(user_no)
    taking_average = sum(average_list) / len(average_list)
    return taking_average

print("Average: ",calculatingAverage())