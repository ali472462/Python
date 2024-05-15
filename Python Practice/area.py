def ar(base, height):
    area = 0.5 * (base * height)
    print(__name__ == '__main__')

def calculate_area(dimension1, dimension2, shape="triangle"):
    '''
    Calculate the area of a shape.

    :param dimension1: In case of triangle it is "base". For rectangle it is "length".
    :param dimension2: In case of triangle it is "height". For rectangle it is "width".
    :param shape: Either "triangle" or "rectangle" (default is "triangle")
    :return: Area of a shape
    '''
    if shape == "triangle":
        area = 0.5 * (dimension1 * dimension2)  # Triangle area is : 0.5(Base*Height)
    elif shape == "rectangle":
        area = dimension1 * dimension2  # Rectangle area is: Length*Width
    else:
        print("Error: Input shape is neither triangle nor rectangle.")
        area = None  # If user didn't supply "triangle" or "rectangle" as shape then return None
    return area

if __name__ == '__main__':
    print(ar(5, 9))
    print("I am in Are.py")
    print(calculate_area(30, 40, "rectangle"))
    triangle_area = calculate_area(30, 60)  # Here third argument is missing
    print("Area of triangle with no shape supplied: ", triangle_area)