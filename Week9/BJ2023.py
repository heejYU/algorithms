def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime(digit, length, N):
    if length == N:
        print(digit)
        return
    
    for i in range(1, 10, 2):
        new_digit = digit * 10 + i
        if is_prime(new_digit):
            find_prime(new_digit, length + 1, N)

N = int(input())

for prime in [2, 3, 5, 7]:
    find_prime(prime, 1, N)