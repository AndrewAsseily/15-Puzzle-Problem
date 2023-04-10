import copy

from heapq import heappush, heappop

from Queue import priorityQueue
from node import node

# bottom, left, top, right
row = [ 1, 0, -1, 0 ]
col = [ 0, -1, 0, 1 ]
direction = ["D", "L", "U", "R"]
n = 4


#################################################################################################

# calculate goalDict first in input_arrayization

# def calculateGoalDict(output_array):
# 	goalDict = {}
# 	for i in range(4):
# 		for j in range(4):
# 			goalDict[output_array[i][j]] = [i, j]

# 	return goalDict


# Goal Dict: {1:[0,0], 2:[2,3]}
# input Dict: {2:[0,0], 1:[2,3]}



# dict in cost cal
# hn = 0
# gridDict = {}#{5:(0,1), 4:(1,1)}


#return goalDict
#returns fn value params(input, goalDict):

# def calculateCost(grid, goalDict, level, w):
# 	gridDict = {}
# 	hn = 0
# 	for i in range(4):
# 		for j in range(4):
# 			val = grid[i][j]
# 			gridDict[val] = [i,j]
# 	print("griddict:", gridDict)
# 	#print(gridDict)
# 	# compare gridDict and goalDict
# 	for val in range(16): 
# 		gridPosX = gridDict[val][0]
# 		gridPosY = gridDict[val][1]
# 		goalPosX = goalDict[val][0]
# 		goalPosY = goalDict[val][1]
# 		print(gridPosX, gridPosY)
# 		print(goalPosX, goalPosY)
# 		hn += max(abs(gridPosX - goalPosX), abs(gridPosY - goalPosY))
		
# 	cost = hn*w + level
# 	return cost

#################################################################################################


#above is the more efficient implementation of the cost function, using Dictionaies

#calculate the hn value, then the cost
def calculateCost(grid, output_array, level, w):
    hn = 0
    for i in range(4):
        for j in range(4):
            number = grid[i][j]
            for a in range(4):
                for b in range(4):
                    if output_array[a][b] == number:
                        goalX = a
                        goalY = b
                        nodeX = i
                        nodeY = j
                        heuristicx = abs(goalX - nodeX)
                        heuristicy = abs(goalY - nodeY)
                        hn += max(heuristicy, heuristicx)
						# f(n) = g(n) + h(n)
	# cost = level + heuresitc
    cost = hn*w + level
    return cost

#generate a new node with its new tile position and other parameters
def newNode(grid, empty_tile_pos, new_empty_tile_pos, level, parent, output_array, w, direction) -> node:
				
	# Copy data from parent gridrix to current gridrix
	new_grid = copy.deepcopy(grid)

	# Move tile
	x1 = empty_tile_pos[0]
	y1 = empty_tile_pos[1]
	x2 = new_empty_tile_pos[0]
	y2 = new_empty_tile_pos[1]
	new_grid[x1][y1], new_grid[x2][y2] = new_grid[x2][y2], new_grid[x1][y1]

	cost= calculateCost(new_grid, output_array, level, w)

	new_node = node(parent, new_grid, new_empty_tile_pos, cost, level, direction)

	return new_node

# Function to check if (i, j) is within bounds
def inBounds(i, j):

    if i < 4 and i >= 0 and j < 4 and j >= 0:
        return True
    else:
        return False

# Print path from root node to destination node
def followPath(root, solution_As, fn_values):

	if root == None:
		return
	else:
		
		followPath(root.parent, solution_As, fn_values)
		solution_As.append(root.direction)
		fn_values.append(root.cost)
		#printgridrix(root.grid)

	#print()
	
	return solution_As, fn_values

def empty_tile_position(node):
	for i in range(4):
		for j in range(4):
			if node[i][j] == 0:
				return [i, j]


def init():
	input_array = []
	output_array = []
	count = 1
	input_file = input("What file would you like to open? ")
	
	with open(input_file) as f:
		for line in f:
			line = line.strip()
			if count == 1:
				w = float(line)
			elif count == 3 or count == 4 or count == 5 or count == 6:
				line = line.split()
				for i in range(len(line)):
					line[i] = int(line[i])
				input_array.append(line)
			elif count == 8 or count == 9 or count == 10 or count == 11:
				line = line.split()
				for i in range(len(line)):
					line[i] = int(line[i])
				output_array.append(line)

			count+=1
	
	return w, input_array, output_array, input_file


def run(input_array, empty_tile_pos, output_array, w):
	level = 0
	frontier = priorityQueue()
	cost = calculateCost(input_array, output_array, level, w)
	root = node(None, input_array,empty_tile_pos, cost, 0, "")
	solution_As = []
	fn_values = []
	number_of_nodes = 0
	frontier.push(root)
	repeated_states = []
	
	while not frontier.empty():

		#finds node with the lowest cost because the priority queue is formed based on the cost
		smallest = frontier.pop()

		# If smallest is the answer node
		if smallest.cost == smallest.level: 
			#format solution_As and fn_values
			solution_As, fn_values = followPath(smallest, solution_As, fn_values)
			solution_As = " ".join(solution_As)
			for i in range(len(fn_values)):
				fn_values[i] = str(fn_values[i])
			fn_values = " ".join(fn_values)
			#remove the empty string at the beginning of the solution
			solution_As = solution_As[1:]


			return solution_As, number_of_nodes, fn_values

		# Generate all possible children
		for i in range(4):
			new_tile_pos = [smallest.empty_tile_pos[0] + row[i], smallest.empty_tile_pos[1] + col[i]]
			if inBounds(new_tile_pos[0], new_tile_pos[1]): #makes sure the node we want to explore is within the bounds
				child = newNode(smallest.grid, smallest.empty_tile_pos, new_tile_pos, smallest.level + 1, smallest, output_array, w, direction[i])
				frontier.push(child)
				number_of_nodes += 1
				repeated_states.append(child.grid)
	
	return 

#reformats the matrix for the output file
def output_formatter(matrix):
	line = ""
	for i in matrix:
		for j in i:
			line += str(j) + " "
		
		#print(line)
		line += "\n"
	#print()
	return line



def output_file(w, input_array, output_array, solution_As, number_of_nodes, fn_values, input_file):
	input_number = input_file[5]
	output_file_name = "Output" + input_number + ".txt"
	with open(output_file_name, "w") as f:
		print("***************************", file = f)
		print(output_formatter(input_array), file = f)
		print(output_formatter(output_array), file = f)
		print(w, file = f)
		print(len(solution_As.split()), file = f)
		print(number_of_nodes, file = f)
		print(solution_As, file = f)
		print(fn_values, file = f)
	
	return 

def main():
	
	w, input_array, output_array, input_file = init()
	empty_tile_pos = empty_tile_position(input_array)
	solution_As, number_of_nodes, fn_values = run(input_array, empty_tile_pos, output_array, w)
	output_file(w, input_array, output_array, solution_As, number_of_nodes, fn_values, input_file)
	

main()