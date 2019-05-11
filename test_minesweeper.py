import minesweeper

class TestMinesweeper:

	def test_read_grid_size(self):
		input = "4,4"
		assert minesweeper.read_grid_size(input) == [4,4]

	def test_empty_grid(self):
		input = "0,0"
		assert minesweeper.read_grid_size(input) == []

	def test_empty_mine_list(self):
		mines = ""
		assert minesweeper.read_mines_from_string(mines, [0,0]) == []

	def test_empty_mine_list_with_grid(self):
		mines = ""
		grid = [2, 3]
		assert minesweeper.read_mines_from_string(mines, grid) == [[".", "."], [".", "."], [".", "."]]

	def test_read_mines_from_string(self):
		mines = """*.."""
		assert minesweeper.read_mines_from_string(mines, [3, 1]) == [["*", ".", "."]]

	def test_read_multiline_mines(self):
		mines = """*..
		..."""
		assert minesweeper.read_mines_from_string(mines, [3, 2]) == [["*", ".", "."],[".", ".", "."]]

	def test_solve(self):
		grid = [["*", ".", "."],[".", "*", "."],[".", ".", "."]]
		assert minesweeper.solve(grid) == [["*", "2", "1"],["2", "*", "1"],["1", "1", "1"]]

	def test_check_and_increment(self):
		grid = [[".", ".", "."],[".", "*", "."],[".", ".", "."]]
		assert minesweeper.check_and_increment(2, 2, grid) == [[".", ".", "."],[".", "*", "."],[".", ".", "1"]]

	def test_check_and_increment_with_existing_number(self):
		grid = [["1", ".", "."],[".", "*", "."],[".", ".", "."]]
		assert minesweeper.check_and_increment(0, 0, grid) == [["2", ".", "."],[".", "*", "."],[".", ".", "."]]

	def test_check_and_increment_with_existing_number(self):
		grid = [["*", ".", "."],[".", "*", "."],[".", ".", "."]]
		assert minesweeper.check_and_increment(0, 0, grid) == [["*", ".", "."],[".", "*", "."],[".", ".", "."]]

	def test_end_to_end(self):
		grid_size_str = "3,3"
		mines_str = """*..
		.*.
		..."""

		grid_size =  minesweeper.read_grid_size(grid_size_str)
		grid = minesweeper.read_mines_from_string(mines_str, grid_size)


		assert minesweeper.solve(grid) == [["*", "2", "1"],["2", "*", "1"],["1", "1", "1"]]
