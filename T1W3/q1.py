import math
from pprint import pprint

class Point:
    def __init__(self, x, y, label=None):
        self.x = x
        self.y = y
        self.label = label
        
    def euclidean_distance(self, pt):
        '''
        Calculates Euclidean Distance
        [(x1 - x2)^2 + (y1 - y2)^2] ** 0.5
        '''
        return math.sqrt(
            (self.x - pt.x)**2 + (self.y - pt.y)**2
        )
        
points = [
    Point(-1, 1, 0),
    Point(0, 1, 1),
    Point(0, 2, 0),
    Point(1, -1, 0),
    Point(1, 0, 1),
    Point(1, 2, 1),
    Point(2, 2, 0),
    Point(2, 3, 1)
]

new = Point(1, 1)
k = 7

# k-NN algorithm
distances = list(map(
    lambda pt : [pt.euclidean_distance(new), pt.x, pt.y, pt.label],
    points
))

sorted_distances = sorted(distances, key=lambda pt : pt[0])

print ('{:<10}{:<10}{:<15}{:<5}'.format("Rank", "Point", "Distance", "Label"))

for i, rec in enumerate(sorted_distances, 0):
    print ('{:<10}{:<10}{:<15.3f}{:<5}'.format(
        i+1, 
        "(" + str(rec[1]) + ", " + str(rec[2])+ ")", 
        rec[0], 
        rec[3]
        ))

print ()
print ('{:<10}{:<10}{:<15}{:<5}'.format("Rank", "Point", "Distance", "Label"))

for rec in sorted_distances[:k]:
    print ('{:<10}{:<10}{:<15.3f}{:<5}'.format(
        i+1, 
        "(" + str(rec[1]) + ", " + str(rec[2])+ ")", 
        rec[0], 
        rec[3]
        ))
    
print ("\nThe new point (1, 1) belongs to class 1.")