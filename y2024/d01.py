from santas_little_helpers.scraper_elf import scrape


raw = scrape(1)
data = str(raw).replace("b'","")


def part1(data=data):

    split_data = data.split("\\n")[0:-1]
    
    left = [int(i.split("   ")[0]) for i in split_data]
    right = [int(i.split("   ")[1]) for i in split_data]

    left.sort()
    right.sort()

    total = 0

    for i, _ in enumerate(left):
        total += abs(left[i] - right[i])
        
    return total


def part2(data=data):

    split_data = data.split("\\n")[0:-1]

    left = set([int(i.split("   ")[0]) for i in split_data])
    right = [int(i.split("   ")[1]) for i in split_data]

    total = 0

    for l in left:
        count = 0
        for r in right:
            if r==l:
                count += 1
        total += (count*l)
    
    return total
