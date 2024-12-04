from santas_little_helpers.scraper_elf import scrape
import re

raw = scrape(3)

data = str(raw).replace("b'","").split("\\n")[0:-1]

def part1(data=data):
    
    valid_expressions = re.findall(r"mul\([0-9]*,[0-9]*\)", str(data))
    
    value_pairs = [v.replace("mul(", "").replace(")", "").split(",") for v in valid_expressions]
    
    scores = [int(v[0]) * int(v[1]) for v in value_pairs]
    
    total = sum(scores)

    print(total)
    
part1()