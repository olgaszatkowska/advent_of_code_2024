import re


with open("inputs/3.txt") as file:
    memory = file.read()


def find_multiplications_sum_result():
    multiplications = re.findall(r"(?<=mul\()\d+,\d+(?=\))", memory)

    result = 0

    for multiplication in multiplications:
        number_1, number_2 = list(map(int, multiplication.split(",")))
        result += number_1 * number_2

    print(result)


def find_do_multiplications_sum_result():
    operations = re.findall(r"(?<=mul\()\d+,\d+(?=\))|don't\(\)|do\(\)", memory)

    result = 0
    count = True

    for operation in operations:
        if operation == "do()":
            count = True
            continue

        if operation == "don't()":
            count = False
            continue

        if count:
            number_1, number_2 = list(map(int, operation.split(",")))
            result += number_1 * number_2

    print(result)


find_multiplications_sum_result()
find_do_multiplications_sum_result()
