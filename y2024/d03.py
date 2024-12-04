from santas_little_helpers.scraper_elf import scrape
import re


raw = scrape(3)
data = str(raw).replace("b'","").split("\\n")[0:-1]


def part1(data=data):
    
    valid_expressions = re.findall(r"mul\([0-9]*,[0-9]*\)", str(data))
    
    value_pairs = [v.replace("mul(", "").replace(")", "").split(",") for v in valid_expressions]
    
    scores = [int(v[0]) * int(v[1]) for v in value_pairs]
    
    total = sum(scores)

    return total
    

def part2(data=data):
    
    expressions = re.findall(r"mul\([0-9]*,[0-9]*\)|do\(\)|don't\(\)", str(data))
    
    valid_expressions = []
    do = True

    for v in expressions:
        if v=="don't()":
            do=False
        elif v=="do()":
            do=True
        elif do:
            valid_expressions.append(v)


    value_pairs = [v.replace("mul(", "").replace(")", "").split(",") for v in valid_expressions]
    
    scores = [int(v[0]) * int(v[1]) for v in value_pairs]
    
    total = sum(scores)

    return 'incomplete'
