import numpy as np
import pandas as pd

'''
Decision Trees are greedy algorithms
that maximise the current Information Gain
without backtracking or going back up to the root.

Future splits are based on the current splits:
split(t+1) = f(split(t))

At every level, the impurity of the dataset
decreases. The entropy (randomness) decreases
with the level.
'''

class DTNode():
    def __init__(self, feat_idx=None, bounds=None, left=None, right=None, info_gain=None, value=None):
       self.feat_idx = feat_idx
       self.bounds = bounds
       self.left = left
       self.right = right 
       self.info_gain = info_gain
       self.value = value

class DecisionTreeClassifier():
    def __init__(self, depth=2, min_split=2):
        self.root = None
        self.depth = depth
        self.min_split = min_split
        
    def build_tree(self, dataset, cur_depth=0):
        x, y = dataset[:, :-1], dataset[:, -1]
        n, n_dim = x.shape
        
        # recursively build the subtrees
        if n >= self.min_split and cur_depth <= self.depth:
            best_split = self.get_best_split(dataset, n, n_dim)
            
            if best_split['info_gain'] > 0:
                left_tree = self.build_tree(best_split['left'], cur_depth+1)
                right_tree = self.build_tree(best_split['right'], cur_depth+1)
                
                return DTNode(best_split['feat_idx'], best_split['bounds'], left_tree, right_tree, best_split['info_gain'])
            
        y = list(y)
        value = max(y, key=y.count) # class label = majority count at leaves
        
        return DTNode(value=value)
    
    def get_best_split(self, dataset, n, n_dim):
        best_split = {}
        max_info_gain = -float('inf')
        
        for idx in range(n_dim):
            feat_val = dataset[:, idx]
            possible_boundss = np.unique(feat_val)
            
            for thresh in possible_boundss:
                # data_left, data_right = self.split(dataset, idx, thresh)
                data_left = np.array([row for row in dataset if row[idx] <= thresh])
                data_right = np.array([row for row in dataset if row[idx] > thresh])
                
                if len(data_left) > 0 and len(data_right) > 0:
                    y, left_y, right_y = dataset[:, -1], data_left[:, -1], data_right[:, -1]
                    cur_info_gain = self.get_info_gain(y, left_y, right_y)
                    
                    if cur_info_gain > max_info_gain:
                       best_split['feat_idx'] = idx
                       best_split['bounds'] = thresh
                       best_split['left'] = data_left
                       best_split['right'] = data_right
                       best_split['info_gain'] = cur_info_gain
                       max_info_gain = cur_info_gain
                       
        return best_split
    
    def get_info_gain(self, parent, left, right):
        weight_left = len(left) / len(parent)
        weight_right = len(right) / len(parent)
        
        info_gain = self.get_entropy(parent) - (weight_left * self.get_entropy(left) + weight_right * self.get_entropy(right))
        
        return info_gain
    
    def get_entropy(self, y):
        labels = np.unique(y)
        entropy = 0
        for cls in labels:
            p_cls = len(y[y == cls]) / len(y)
            entropy += -p_cls * np.log2(p_cls)
            
        return entropy
    
    def fit(self, x, y):
        dataset = np.concatenate((x, y), axis=1)
        self.root = self.build_tree(dataset)
        
    def make_pred(self, x, root):
        if root.value != None:
            return root.value
        
        feat_val = x[root.feat_idx]
        
        if feat_val <= root.bounds:
            return self.make_pred(x, root.left)
        else:
            return self.make_pred(x, root.right)
            
    def predict(self, x):
        return [self.make_pred(i, self.root) for i in x]

cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv('./data/iris.csv', skiprows=1, header=0, names=cols)

# replace class strings with integer indices
df['class'] = df['class'].str.replace('Iris-setosa', '0')
df['class'] = df['class'].str.replace('Iris-versicolor', '1')
df['class'] = df['class'].str.replace('Iris-virginica', '2')
df['class'] = df['class'].map(lambda x : int(x))

X = df.iloc[:, :-1].values
Y = df.iloc[:, -1].values.reshape(-1, 1)
X = np.array(X)
Y = np.array(Y)
        
clf = DecisionTreeClassifier()
clf.fit(X, Y) # split this into training and testing datasets

def print_tree(root=None, indent="  "):
    if root.value != None:
        print (root.value)
    else:
        print ("x_" + str(root.feat_idx), '<=', root.bounds, ":", format(root.info_gain, '0.4f'))
        print (indent + "left: ", end="")
        print_tree(root.left, indent + indent)
        print (indent + "right: ", end="")
        print_tree(root.right, indent + indent)
        
print_tree(clf.root)