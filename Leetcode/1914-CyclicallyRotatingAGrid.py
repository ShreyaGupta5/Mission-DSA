class Solution:
    def rotateGrid(self, grid, k):
        m, n = len(grid), len(grid[0])

        layers = min(m, n) // 2

        for layer in range(layers):

            elements = []

            # top row
            for j in range(layer, n - layer):
                elements.append(grid[layer][j])

            # right column
            for i in range(layer + 1, m - layer - 1):
                elements.append(grid[i][n - layer - 1])

            # bottom row
            for j in range(n - layer - 1, layer - 1, -1):
                elements.append(grid[m - layer - 1][j])

            # left column
            for i in range(m - layer - 2, layer, -1):
                elements.append(grid[i][layer])

            # rotate
            length = len(elements)
            rot = k % length
            rotated = elements[rot:] + elements[:rot]

            idx = 0

            # put back top row
            for j in range(layer, n - layer):
                grid[layer][j] = rotated[idx]
                idx += 1

            # put back right column
            for i in range(layer + 1, m - layer - 1):
                grid[i][n - layer - 1] = rotated[idx]
                idx += 1

            # put back bottom row
            for j in range(n - layer - 1, layer - 1, -1):
                grid[m - layer - 1][j] = rotated[idx]
                idx += 1

            # put back left column
            for i in range(m - layer - 2, layer, -1):
                grid[i][layer] = rotated[idx]
                idx += 1

        return grid
