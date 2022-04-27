""" Compute the area of triangle with vertices (x0, y0), (x1, y1), and (x2, y2) """

def point_distance(x_0, y_0, x_1, y_1):
    """ Return distance between two points (x0,y0) and (x1,y1) """
    x_dist = x_0 - x_1
    y_dist = y_0 - y_1
    return (x_dist ** 2 + y_dist ** 2) ** 0.5


def triangle_area(x_0, y_0, x_1, y_1, x_2, y_2):
    """ Returns the area of a triangle with vertices (x0,y0), (x1,y1), and (x2,y2). """
    
    # Compute the lengths of the three sides.
    len_01 = point_distance(x_0, y_0, x_1, y_1)
    len_02 = point_distance(x_0, y_0, x_2, y_2)
    len_12 = point_distance(x_1, y_1, x_2, y_2)
    
    # Compute the semi-perimeter length, i.e., half of the perimeter length.
    semi_perim = (len_01 + len_02 + len_12) / 2
    
    # Compute the area according to Heron's formula.
    return (semi_perim * (semi_perim - len_01) * (semi_perim - len_02) * (semi_perim - len_12)) ** 0.5


# Compute area of triangle with vertices (10, 0), (0, 0), and (0, 10).
# Since triangle is right trianga, area should be 50.0

x_0, y_0 = 10, 0
x_1, y_1 = 0, 0
x_2, y_2 = 0, 10
print(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2))