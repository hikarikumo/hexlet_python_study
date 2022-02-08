

def modx(x):
    return (x % 2, x)


if __name__ == "__main__":
    list_to_sort = [7, 5, 1, 8, 6, 10]
    list_to_sort.sort(key=modx)
    print(list_to_sort)

