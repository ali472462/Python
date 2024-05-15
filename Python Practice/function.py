"""""
def area_cal (base,height):
    t_area=(1/2)*base*height
    r_area=height*base
    shape=input("Tell Shape of which u want area :")
    if shape == "triangle":
        print(f"Area Of triangle is", t_area)
    elif shape == "rectangle":
        print(f"Area Of Rectangle is", r_area)
    else:
        print(f"Area Of triangle is", t_area)

area=area_cal(55,65)
"""
def print_pattern(numb):
    for i in range(1):
        x=""
        for j in range(numb):
            y="*"
            x=x+y
            print(f"({j+1}){x}")


