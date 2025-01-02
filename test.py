def find_local_maximums(matrix):
    if not matrix or not matrix[0]:
        return []
    
    rows, cols = len(matrix), len(matrix[0])
    result = []
    
    for i in range(rows):
        for j in range(cols):
            val = matrix[i][j]
            if val == 0:
                continue
            
            r = val
            if r == 0:
                continue
            
            inner_r = r - 1
            if inner_r < 1:
                # If no inner layer possible (r=1), check if we have a single cell matrix
                # If single cell matrix, trivially a local max
                if rows == 1 and cols == 1:
                    result.append([i,j])
                # Else no inner region, not a max
                continue
            
            # Compute inner region bounds
            inner_row_start = max(i - inner_r, 0)
            inner_row_end = min(i + inner_r, rows - 1)
            inner_col_start = max(j - inner_r, 0)
            inner_col_end = min(j + inner_r, cols - 1)
            
            # If after clipping, we get no cells other than maybe center, check if any exist:
            if inner_row_end < inner_row_start or inner_col_end < inner_col_start:
                # No inner region at all
                # If it's a single cell or no other reason to disqualify, consider it local max
                if rows == 1 and cols == 1:
                    result.append([i, j])
                continue
            
            is_local_max = True
            for x in range(inner_row_start, inner_row_end + 1):
                for y in range(inner_col_start, inner_col_end + 1):
                    if (x, y) == (i, j):
                        continue
                    if matrix[x][y] >= val:
                        is_local_max = False
                        break
                if not is_local_max:
                    break
            
            if is_local_max:
                result.append([i, j])
    
    return result

# Test cases
if __name__ == "__main__":
    test_cases = [
        (
            [
                [3, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 2, 0],
                [0, 0, 0, 0],
                [0, 3, 0, 3],
            ],
            [[0, 0], [2, 2]],
        ),
        (
            [
                [5, 0, 0],
                [0, 2, 0],
                [0, 0, 1],
            ],
            [[0, 0]],
        ),
        (
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ],
            [],
        ),
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            [[2, 2]],
        ),
    ]

    for i, (matrix, expected) in enumerate(test_cases):
        output = find_local_maximums(matrix)
        print(f"Test Case {i+1}: {'Passed' if output == expected else 'Failed'}")
        print(f"Output: {output}")
        print(f"Expected: {expected}\n")
