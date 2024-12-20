from santas_little_helpers.scraper_elf import scrape
import math
import pprint as pp
import numpy as np

raw = scrape(5)
data = str(raw).replace("b'","").replace("'","")[:-1]

def part1(data=data):

    orders = [[int(i) for i in o.split("|")] for o in data.split("\\n\\n")[0].split("\\n")]
    n = (-1+math.sqrt(1+8*len(orders)))/2
    
    
    books = data.split("\\n\\n")[1]
    return orders

def part2(data=data):

    return "incomplete"
