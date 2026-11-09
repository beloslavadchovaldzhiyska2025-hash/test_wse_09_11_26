def is_prime(number):
    if number < 2:
        return False

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


n = int(input())
while n < 5:
    n = int(input())

twin_pairs = []
for p in range(2, n - 1):
    if p + 2 <= n and is_prime(p) and is_prime(p + 2):
        twin_pairs.append((p, p + 2))
        print(p, p + 2)

print(f"Брой двойки: {len(twin_pairs)}")
big_twin = twin_pairs[-1]
print(f"Най-голяма двойка: {big_twin[0]} {big_twin[1]}")
