a = int(input())
b = int(input())

if a > b:
    a, b = b, a

perfect_numbers = []
abundant_count = 0

for number in range(a, b + 1):
    divisor_sum = 0

    for divisor in range(1, number):
        if number % divisor == 0:
            divisor_sum += divisor

    if divisor_sum == number:
        perfect_numbers.append(number)
    elif divisor_sum > number:
        abundant_count += 1

if perfect_numbers:
    print(*perfect_numbers)
else:
    print("Няма")

print(f"Изобилни: {abundant_count}")
