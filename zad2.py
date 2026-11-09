numbers = []

while True:
    number = int(input())
    if number == 0:
        break
    numbers.append(number)

if not numbers:
    print("Няма данни")
else:
    increases = 0
    negative_count = 0

    for index, number in enumerate(numbers):
        if number < 0:
            negative_count += 1
        if index > 0 and number > numbers[index - 1]:
            increases += 1

    negative_percentage = (negative_count * 100 * 2 + len(numbers)) // (2 * len(numbers))

    print(f"Най-малко: {min(numbers)}")
    print(f"Нараствания: {increases}")
    print(f"Отрицателни: {negative_percentage}%")
