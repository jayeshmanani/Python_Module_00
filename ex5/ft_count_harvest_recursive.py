def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    count_print(1, days)


def count_print(current, total):
    print(f"Day {current}")
    if current == total:
        print("Harvest time!")
        return
    count_print(current + 1, total)
