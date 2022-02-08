
if __name__ == "__main__":

    numbers = [1,2,3,4,5,6,7]
    evens = [x for x in numbers if x % 2 is 0]
    odds = [y for y in numbers if y not in evens]
    print(f'{numbers=}\n{evens=}, {odds=}')
