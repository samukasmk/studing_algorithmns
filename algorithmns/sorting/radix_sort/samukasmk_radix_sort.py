def radix_sort(numbers):
    len_chars = len(numbers[0])
    operation = 0
    for position in range(-1, -abs(len_chars + 1), -1):
        bucket = {str(digit): [] for digit in range(0, 10)}

        for n in numbers:
            char = n[position]
            bucket[char].append(n)

            operation += 1

        numbers = []
        for values in bucket.values():
            for value in values:
                numbers.append(value)
            operation += 1

    print(operation)
    return numbers


# numbers = [
#     '00120',
#     '00450',
#     '43589',
#     '73141',
#     '31975',
#     '52455',
#     '60443',
#     '21271',
# ]

numbers = ['0008', '0325', '0010', '0009', '0100', '0003', '0005', '0012', '1023', '0020']



# numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
print(f'Initial list: {numbers}')

numbers = radix_sort(numbers)

# sorted = ['00120', '00450', '21271', '31975', '43589', '52455', '60443', '73141']

sorted = ['0003', '0005', '0008', '0009', '0010', '0012', '0020', '0100', '0325', '1023']

if numbers == sorted:
    print(f'Sorted list: {numbers}')
else:
    print(f"Final is not sorted: {numbers}")

n = 23
digits = 5

print(str(n).zfill(digits))