"""
Rotate 2D matrix by 90, 180, or 270 degrees counterclockwise
Discussion reference: https://stackoverflow.com/questions/42519/how-do-you-rotate-a-two-dimensional-array
"""

from __future__ import annotations


def make_matrix(row_size: int = 4) -> list[list[int]]:
    """
    Create a matrix with sequential integers
    >>> make_matrix()
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    >>> make_matrix(1)
    [[1]]
    >>> make_matrix(-2)
    [[1, 2], [3, 4]]
    >>> make_matrix(3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    # Use absolute value and default to 4 if input is 0
    row_size = abs(row_size) or 4
    return [[1 + x + y * row_size for x in range(row_size)] for y in range(row_size)]


def rotate_90(matrix: list[list[int]]) -> list[list[int]]:
    """
    Rotate matrix 90° counterclockwise
    >>> rotate_90(make_matrix())
    [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]]
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> rotate_90(matrix)
    [[3, 6], [2, 5], [1, 4]]
    """
    # Transpose then reverse rows = 90° rotation
    return reverse_row(transpose(matrix))


def rotate_180(matrix: list[list[int]]) -> list[list[int]]:
    """
    Rotate matrix 180° counterclockwise
    >>> rotate_180(make_matrix())
    [[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> rotate_180(matrix)
    [[6, 5, 4], [3, 2, 1]]
    """
    # Reverse rows and columns = 180° rotation
    return reverse_row(reverse_column(matrix))


def rotate_270(matrix: list[list[int]]) -> list[list[int]]:
    """
    Rotate matrix 270° counterclockwise
    >>> rotate_270(make_matrix())
    [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> rotate_270(matrix)
    [[4, 1], [5, 2], [6, 3]]
    """
    # Transpose then reverse columns = 270° rotation
    return reverse_column(transpose(matrix))


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """
    Create transposed matrix (swap rows and columns)
    >>> transpose([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]
    """
    return [list(x) for x in zip(*matrix)]


def reverse_row(matrix: list[list[int]]) -> list[list[int]]:
    """
    Reverse row order (vertical flip)
    >>> reverse_row([[1, 2], [3, 4]])
    [[3, 4], [1, 2]]
    """
    return matrix[::-1]


def reverse_column(matrix: list[list[int]]) -> list[list[int]]:
    """
    Reverse each row's elements (horizontal flip)
    >>> reverse_column([[1, 2], [3, 4]])
    [[2, 1], [4, 3]]
    """
    return [x[::-1] for x in matrix]


def print_matrix(matrix: list[list[int]]) -> None:
    """Print matrix in readable format"""
    for row in matrix:
        print(*row)


if __name__ == "__main__":
    # Create and rotate a 4x4 matrix
    matrix = make_matrix()
    print("Original matrix:")
    print_matrix(matrix)
    
    rotations = [
        ("90° counterclockwise", rotate_90),
        ("180°", rotate_180),
        ("270° counterclockwise", rotate_270)
    ]
    
    for description, func in rotations:
        print(f"\nRotated {description}:")
        print_matrix(func(matrix))
        # Create fresh matrix for next rotation
        matrix = make_matrix()
    
    # Demonstrate with non-square matrix
    non_square = [[1, 2, 3], [4, 5, 6]]
    print("\nOriginal non-square matrix (2x3):")
    print_matrix(non_square)
    
    for description, func in rotations:
        print(f"\nRotated {description}:")
        print_matrix(func(non_square))