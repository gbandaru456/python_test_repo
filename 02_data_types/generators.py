def generate_numbers(n):
    for i in range(n):
        yield i

def filter_even_num(num):
    for numner in num:
        if numner %2== 0:
            yield numner
for even in filter_even_num(generate_numbers(10)):
    print(even)

