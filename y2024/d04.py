from santas_little_helpers.scraper_elf import scrape
import re
import pprint as pp
import numpy as np

raw = scrape(4)
data = str(raw).replace("b'","").replace("'","")[:-1]

def part1(data=data):

    split_data = data.replace('\\', "").split("n")
    letters = [list(i) for i in split_data]
    matrix = np.matrix(letters)

    count = 0

    for x in range(matrix.shape[0]-3):#range(137):
        for y in range(matrix.shape[1]-3):# range(137):
            sub_matrix = matrix[np.ix_([x,x+1,x+2,x+3], [y,y+1,y+2,y+3])]
            lines = [
                sub_matrix[np.ix_([0], [0,1,2,3])].tostring().decode().replace("\x00", ""), # left line
                sub_matrix[np.ix_([0], [0,1,2,3])].tostring().decode().replace("\x00", "")[::-1], # left line rev
                sub_matrix[np.ix_([0,1,2,3], [0])].tostring().decode().replace("\x00", ""), # top line
                sub_matrix[np.ix_([0,1,2,3], [0])].tostring().decode().replace("\x00", "")[::-1], # top line rev
                np.diag(sub_matrix).tostring().decode().replace("\x00", ""), # 0,0 to 3,3
                np.diag(np.rot90(sub_matrix, 1)).tostring().decode().replace("\x00", ""), # 0,3 to 3,0
                np.diag(np.rot90(sub_matrix, 2)).tostring().decode().replace("\x00", ""), # 0,3 to 3,0
                np.diag(np.rot90(sub_matrix, 3)).tostring().decode().replace("\x00", ""), # 0,3 to 3,0
                ]
            
            if x+4==matrix.shape[0]:
                    lines.append(sub_matrix[np.ix_([1], [0,1,2,3])].tostring().decode().replace("\x00", ""))
                    lines.append(sub_matrix[np.ix_([1], [0,1,2,3])].tostring().decode().replace("\x00", "")[::-1])
                    lines.append(sub_matrix[np.ix_([2], [0,1,2,3])].tostring().decode().replace("\x00", ""))
                    lines.append(sub_matrix[np.ix_([2], [0,1,2,3])].tostring().decode().replace("\x00", "")[::-1])
                    lines.append(sub_matrix[np.ix_([3], [0,1,2,3])].tostring().decode().replace("\x00", ""))
                    lines.append(sub_matrix[np.ix_([3], [0,1,2,3])].tostring().decode().replace("\x00", "")[::-1])

            if y+4==matrix.shape[1]:
                lines.append(sub_matrix[np.ix_([0,1,2,3], [1])].tostring().decode().replace("\x00", ""))
                lines.append(sub_matrix[np.ix_([0,1,2,3], [1])].tostring().decode().replace("\x00", "")[::-1])
                lines.append(sub_matrix[np.ix_([0,1,2,3], [2])].tostring().decode().replace("\x00", ""))
                lines.append(sub_matrix[np.ix_([0,1,2,3], [2])].tostring().decode().replace("\x00", "")[::-1])
                lines.append(sub_matrix[np.ix_([0,1,2,3], [3])].tostring().decode().replace("\x00", ""))
                lines.append(sub_matrix[np.ix_([0,1,2,3], [3])].tostring().decode().replace("\x00", "")[::-1])

            count += sum([l=="XMAS" for l in lines])
    return count

def part2(data=data):
    return "incomplete"
