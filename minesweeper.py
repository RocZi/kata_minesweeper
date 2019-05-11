#!/usr/bin/env python3
def read_grid_size(grid_string):
	output = [int(x) for x in grid_string.split(',')]

	if output == [0,0]: 
		return []
	else:
		return output

def read_mines_from_string(mine_string, grid_size):
	if len(mine_string) == 0:
		columns = grid_size[0]
		rows = grid_size[1]
		return [["." for c in range(columns)] for r in range(rows)]
	else:
		lines = mine_string.split('\n')
		stripped_lines = [line.strip() for line in lines]

		grid = []

		for line in stripped_lines:
			grid.append([c for c in line])

		return grid

def solve(grid):
	rows = range(len(grid))
	columns = range(len(grid[0]))

	areas_to_check = [
		lambda r, c: (r - 1, c - 1),
		lambda r, c: (r - 1, c),
		lambda r, c: (r - 1, c + 1),
		lambda r, c: (r, c - 1),
		lambda r, c: (r, c + 1),
		lambda r, c: (r + 1, c - 1),
		lambda r, c: (r + 1, c),
		lambda r, c: (r + 1, c + 1)
	]

	for r in rows:
		for c in columns:
			if grid[r][c] == '*':
				for operation in areas_to_check:
					check_r, check_c = operation(r, c)
					check_and_increment(check_r, check_c, grid)


	return grid


def check_and_increment(row, col, grid):
	max_rows = len(grid)
	max_columns = len(grid[0])

	if row < 0 or row > max_rows:
		return grid
	elif col < 0 or col > max_columns:
		return grid
	elif grid[row][col] == '*':
		return grid
	else:
		symbol = None

		if grid[row][col] == '.':
			symbol = '1'
		else:
			count = int(grid[row][col])
			count += 1
			symbol = str(count)

		grid[row][col] = symbol
		
		return grid