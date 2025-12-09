def ft_count_harvest_iterative():
    inp = int(input("Days until harvest: "))
    i = 1
    if (inp >= 0):
        while (i <= inp):
            print("Day", i)
            i += 1
        print("Harvest time!")
