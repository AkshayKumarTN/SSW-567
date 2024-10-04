#Before fix
| Test ID                   | Input      | Expected Results | Actual Result | Pass or Fail |
|---------------------------|------------|------------------|---------------|--------------|
| testRightTriangleA         | 3, 4, 5    | Right            | InvalidInput  | Fail         |
| testRightTriangleB         | 5, 3, 4    | Right            | InvalidInput  | Fail         |
| testEquilateralTriangles   | 1, 1, 1    | Equilateral      | InvalidInput  | Fail         |

#After fix
| Test ID                   | Input      | Expected Results | Actual Result | Pass or Fail |
|---------------------------|------------|------------------|---------------|--------------|
| testRightTriangleA         | 3, 4, 5    | Right            | Right         | Pass         |
| testRightTriangleB         | 5, 3, 4    | Right            | Right         | Pass         |
| testEquilateralTriangles   | 1, 1, 1    | Equilateral      | Equilateral   | Pass         |