# Node structure

class node:
	
	def __init__(self, parent, grid, empty_tile_pos, cost, level, direction):
		self.parent = parent
		self.grid = grid
		self.empty_tile_pos = empty_tile_pos
		self.cost = cost
		self.level = level
		self.direction = direction
		
	def __lt__(self, nxt):
		return self.cost < nxt.cost