n = int(input("Enter n (odd, >= 5): "))

if n < 5 or n % 2 == 0:
    print("Invalid input: n must be an odd integer >= 5.")
else:
    mid = n // 2 

    for i in range(n):
        if i == mid:
            print("*" * (2 * n - 1))          
        else:
            stars = mid - abs(i - mid) + 1    
            print("*" + " " * n + "*" * stars)