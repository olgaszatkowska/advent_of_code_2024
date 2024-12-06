NEXT_DIRECTIONS = {
    "up": "right",
    "right": "down",
    "down": "left",
    "left": "up",
    
}

class LoopFound(Exception):
    pass

def get_lab_map():
    lab_map = []
    with open("inputs/6.txt") as file:
        for line in file:
            lab_map.append(list(line.replace("\n", "")))
            
    return lab_map

def find_guard_position(lab_map):
    height = len(lab_map)
    width = len(lab_map[0])
    
    for i in range(height):
        for j in range(width):
            if lab_map[i][j] == "^":
                return i,j
            
    raise Exception

def find_guard_next_position(position: tuple, direction):
    x, y = position
    
    if direction == "up":
        return x-1, y
    if direction == "right":
        return x, y+1
    if direction == "down":
        return x+1, y
    if direction == "left":
        return x, y-1
    
    raise Exception

def move_guard(lab_map, start_position, obstacle):
    height = len(lab_map)
    width = len(lab_map[0])

    direction = "up"
    possible_positions = [start_position]
    position = start_position
    
    path: dict[tuple,list[tuple]] = {}
    
    while True:
        x, y = find_guard_next_position(position, direction)
        
        if x < 0 or y < 0:
            break
            
        if x >= height or y >= width:
            break
        
        if lab_map[x][y] == "#":
            direction = NEXT_DIRECTIONS[direction]
            continue
        
        next_position = (x,y)

        next_taken_positions = path.get(position)
        
        if next_taken_positions and next_position in next_taken_positions:
            raise LoopFound
        
        if next_taken_positions:            
            next_taken_positions.append(next_position)
            path[position] = next_taken_positions
        else:
            path[position] = [next_position]
        
        possible_positions.append(next_position)
        position = next_position

    return possible_positions

def count_possible_loops():
    lab_map = get_lab_map()
    start_position = find_guard_position(lab_map)

    total_loops = 0
    
    height = len(lab_map)
    width = len(lab_map[0])
    
    for i in range(height):
        for j in range(width):
            position_value = lab_map[i][j]
            if position_value == "^" or position_value == "#":
                continue

            lab_map[i][j] = "#"

            try:
                move_guard(lab_map, start_position, (i,j))
            except LoopFound:
                total_loops+=1

            lab_map[i][j] = "."
            
         
    print(total_loops)

def find_total_unique_positions():
    lab_map = get_lab_map()
    position = find_guard_position(lab_map)
    positions = move_guard(lab_map, position)
    unique_positions = set(positions)
    print(len(unique_positions))
    
# find_total_unique_positions()
count_possible_loops()