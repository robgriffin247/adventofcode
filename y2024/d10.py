from santas_little_helpers.scraper_elf import scrape
import math
import pprint as pp
import numpy as np

raw = scrape(10)
data = str(raw).replace("b'","").replace("'","")[:-1]

def part1(data=data):

    print(data)
    lines = [line for line in data.split(r"\n")]
    return lines[-1]

def part2(data=data):

    return "incomplete"
