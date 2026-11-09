n = int(input())

if n <= 0:
    print("Error")
else:
    multiples_of_three = 0
    positive_sum = 0
    positive_count = 0

    for _ in range(n):
        number = int(input())

        if number % 3 == 0:
            multiples_of_three += 1

        if number > 0:
            positive_sum += number
            positive_count += 1

    print(multiples_of_three)

    if positive_count == 0:
        print("Няма положителни")
    else:
        print(f"{positive_sum / positive_count:.2f}")
