# Triangle Functions

This project provides several functions to validate and classify a triangle based on its sides.

## Functions

`valid_triangle(sides: List[int]) -> bool`:
This function takes a list of sides of the triangle and returns a boolean value indicating whether the triangle is valid or not. A shape is considered a triangle if all sides have a length greater than 0, and the sum of the lengths of any two sides is greater than or equal to the length of the third side.

`is_equilateral(sides: List[int]) -> bool`:
This function takes a list of sides of the triangle and returns a boolean value indicating whether the triangle is equilateral or not. An equilateral triangle has all three sides the same length.

`is_isosceles(sides: List[int]) -> bool`:
This function takes a list of sides of the triangle and returns a boolean value indicating whether the triangle is isosceles or not. An isosceles triangle has at least two sides the same length.

`is_scalene(sides: List[int]) -> bool`:
This function takes a list of sides of the triangle and returns a boolean value indicating whether the triangle is scalene or not. A scalene triangle has all sides of different lengths.

## Example
```python
sides = [3, 4, 5]
print(valid_triangle(sides))  # Output: True
print(is_equilateral(sides))  # Output: False
print(is_isosceles(sides))  # Output: False
print(is_scalene(sides))  # Output: True
```

## Contributing

If you find any bugs or have any suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
