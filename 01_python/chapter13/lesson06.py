def fizzbuzz(start, end):
    fizzbuzz_list = []
    for i in range(start, end):
        if (i % 3 == 0) and (i % 5 == 0):
            fizzbuzz_list.append("fizzbuzz")
        elif (i % 5 == 0):
            fizzbuzz_list.append("buzz")
        elif (i % 3 == 0):
            fizzbuzz_list.append("fizz")
        else:
            fizzbuzz_list.append(i)
    return fizzbuzz_list
