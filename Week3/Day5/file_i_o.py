with open('./Week3/Day5/nameslist.txt', 'r+') as f:
    # line = f.readlines()
    # names = f.read().splitlines()

    names = [line.strip() for line in f]
    count_darth = names.count("Darth")
    print(count_darth)