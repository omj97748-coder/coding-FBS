for row in range(10):
    start = row * 10 + 1
    end = start + 10

    numbers = list(range(start,end))

    if row % 2 == 1:
        numbers.reverse()

    print(*numbers)