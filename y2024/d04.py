from santas_little_helpers.scraper_elf import scrape
import numpy as np

raw = scrape(4)
data = str(raw).replace("b'","").replace("'","")[:-1]

def part1(data=data):

    split_data = data.replace('\\', "").split("n")
    letters = [list(i) for i in split_data]
    matrix = np.matrix(letters)

    count = 0

    for x in range(matrix.shape[0]-3):
        for y in range(matrix.shape[1]-3):
            sub_matrix = matrix[np.ix_([x,x+1,x+2,x+3], [y,y+1,y+2,y+3])]
            lines = [
                sub_matrix[np.ix_([0], [0,1,2,3])].tostring().decode().replace("\x00", ""), 
                sub_matrix[np.ix_([0], [0,1,2,3])].tostring().decode().replace("\x00", "")[::-1],
                sub_matrix[np.ix_([0,1,2,3], [0])].tostring().decode().replace("\x00", ""),
                sub_matrix[np.ix_([0,1,2,3], [0])].tostring().decode().replace("\x00", "")[::-1],
                np.diag(sub_matrix).tostring().decode().replace("\x00", ""),
                np.diag(np.rot90(sub_matrix, 1)).tostring().decode().replace("\x00", ""),
                np.diag(np.rot90(sub_matrix, 2)).tostring().decode().replace("\x00", ""),
                np.diag(np.rot90(sub_matrix, 3)).tostring().decode().replace("\x00", ""),
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

    split_data = data.replace('\\', "").split("n")
    letters = [list(i) for i in split_data]
    matrix = np.matrix(letters)

    count = 0

    for x in range(matrix.shape[0]-2):
        for y in range(matrix.shape[1]-2):
            sub_matrix = matrix[np.ix_([x,x+1,x+2], [y,y+1,y+2])]
            lines = [
                np.diag(sub_matrix),
                np.diag(np.rot90(sub_matrix, 1)),
                np.diag(np.rot90(sub_matrix, 2)),
                np.diag(np.rot90(sub_matrix, 3)),
                ]
            count += sum([l.tostring().decode().replace("\x00", "")=="MAS" for l in lines])==2
    return count
