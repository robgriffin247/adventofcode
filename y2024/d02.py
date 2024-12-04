from santas_little_helpers.scraper_elf import scrape
import numpy as np


raw = scrape(2)
data = str(raw).replace("b'","").split("\\n")[0:-1]


def part1(data=data):
    safe = 0
    rows = [[int(v) for v in r.split(" ")] for r in data]
    for row in rows:
        steps = []
        for i, value in enumerate(row):
            if i>0:
                d = row[i-1] - value
                steps.append(d)
            
        if (len(set([int(np.sign(i)) for i in steps]))==1) & (max([abs(step) for step in steps]) in [1,2,3]):
            safe += 1
            
    return safe


def part2(data=data):
    return "incomplete"