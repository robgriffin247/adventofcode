from santas_little_helpers.scraper_elf import scrape

raw = scrape(1)

data = str(raw).replace("b'","").split("\\n")[0:-1]

def part1(data):

    left = [int(i.split("   ")[0]) for i in data]
    right = [int(i.split("   ")[1]) for i in data]

    left.sort()
    right.sort()

    total = 0

    for i, _ in enumerate(left):
        total += abs(left[i] - right[i])
        
    print(f"Distance: {total}")

def part2(data):

    left = set([int(i.split("   ")[0]) for i in data])
    right = [int(i.split("   ")[1]) for i in data]

    total = 0

    for l in left:
        count = 0
        for r in right:
            if r==l:
                count += 1
        total += (count*l)
    
    print(f"Similarity: {total}")

part1(data)
part2(data)