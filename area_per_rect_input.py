#!/usr/bin/env python3
# Author: Mikhail Ibrahim
# Date: Feb 25, 2025
# Description: A Python program that calculates the area and perimeter of a rectangle based on user input.


def main():
    length = float(input("Enter the length of the rectangle (cm): "))
    width = float(input("Enter the width of the rectangle (cm): "))

    area = length * width
    perimeter = 2 * (length + width)

    print("\nFor a rectangle with length {} cm and width {} cm:".format(length, width))
    print("The area is {} square centimeters.".format(area))
    print("The perimeter is {} centimeters.".format(perimeter))


if __name__ == "__main__":
    main()
