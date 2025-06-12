def Amstring():
    print("Armstrong numbers between 0 and 999 are:")

    for num in range(1000):
        digits = []  # Clear digits list for each number
        sum_of_cubes = 0  # Reset the sum for each number

        # Extract digits
        for d in str(num):
            digits.append(int(d))  # Convert digit to int before storing

        # Compute sum of cubes of digits
        for d in digits:
            sum_of_cubes += d ** 3

        # Check Armstrong condition
        if sum_of_cubes == num:
            print(num)

# Call the function
Amstring()
