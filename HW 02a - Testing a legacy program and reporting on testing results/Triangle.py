def classify_triangle(side_a,side_b,side_c):
    """
    Parameters:
            Side_a, side_b, and side_c are the lengths of the triangle's sides.
        
    Returns:
            A string describing the type of triangle.
    """
    # require that the input values be >= 0 and <= 200
    if side_a > 200 or side_b > 200 or side_c > 200:
        return 'InvalidInput'
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return 'InvalidInput'
    if not (isinstance(side_a, int) and isinstance(side_b, int) and isinstance(side_c, int)):
        return 'InvalidInput'
    # Verify that the given sides satisfy the triangle inequality theorem, which states that
    # the sum of the lengths of any two sides must be greater than the length of the remaining side.
    if side_a >= (side_b + side_c) or side_b >= (side_a + side_c) or side_c >= (side_a + side_b):
        return 'NotATriangle'
    # Classifying the triangle
    if side_a == side_b == side_c:
        return 'Equilateral'
    sides_squared = sorted([side_a ** 2, side_b ** 2, side_c ** 2])
    if sides_squared[0] + sides_squared[1] == sides_squared[2]:
        return 'Right'
    if side_a != side_b and side_b != side_c and side_a != side_c:
        return 'Scalene'
    return 'Isosceles'
