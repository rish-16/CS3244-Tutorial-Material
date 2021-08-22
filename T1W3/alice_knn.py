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
    
    def __str__(self):
        return "({}, {}) | {}".format(self.x, self.y, self.label)
    
    def __repr__(self):
        return "({}, {}) | {}".format(self.x, self.y, self.label)
        
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
k = 3

S = [0 for _ in range(len(points))]
D = list(map(lambda pt : pt.euclidean_distance(new), points)) # O(nd)
answers = []

# O(nk)
for i in range(len(points)):
    for j in range(k):
        i_min = min(range(len(D)), key=D.__getitem__)
        min_D = min(D)
        
        if S[i_min] == 0:
            S[i_min] = 1
            D[i_min] = float('inf') # past smallest will not be picked again
            answers.append(i_min)
        
for i in answers[:k]:
    print (points[i])