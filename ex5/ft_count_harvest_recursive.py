def ft_count_harvest_recursive(days=-1, total=-1):
    if days == -1:
        days = int(input("Days until harvest: "))
        total = days
    if days == 0:
        return
    else:
        ft_count_harvest_recursive(days=days-1)
        print(f"Day {days}")
    if (days == total):
        print("Harvest time!")
