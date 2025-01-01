
'''Problem 9: Check Prime Number'''

n = int(input("Enter a number: "))
if n > 1:
    for i in range(2, int(n**0.5) + 1):  # Checking up to the square root of the number
        if n % i == 0:
            print(f"{n} is not a prime number.")
            break
    else:
        print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
