def factorial(n):
    if (n == 0):
        return (1)

    return n * factorial(n - 1)


def pascal_triangle(n):
    pascal_list = []
    if (n <= 0):
        return pascal_list

    for i in range(n):
        row = []
        for x in range(i + 1):
            num = factorial(i)
            denom = factorial(x) * factorial(i - x)
            row.append(num // denom)

        pascal_list.append(row)

    return(pascal_list)
