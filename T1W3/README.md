# Tutorial 1 Week 3: k-Nearest Neighbours

In T1W3, I cover the k-Nearest Neighbours (k-NN) algorithm. 

## Contents
This repo contains the code used to answer Question 2.

### Question 2a
Here's the ranking table used to classify the new point `(1, 1)` using 3-NN: 
```
Rank      Point     Distance       Label
1         (0, 1)    1.000          1    
2         (1, 0)    1.000          1    
3         (1, 2)    1.000          1    
4         (0, 2)    1.414          0    
5         (2, 2)    1.414          0    
6         (-1, 1)   2.000          0    
7         (1, -1)   2.000          0    
8         (2, 3)    2.236          1    

Rank      Point     Distance       Label
8         (0, 1)    1.000          1    
8         (1, 0)    1.000          1    
8         (1, 2)    1.000          1    

The new point (1, 1) belongs to class 1 using 3-NN.
```

Here's the ranking table used to classify the new point `(1, 1)` using 7-NN:
```
Rank      Point     Distance       Label
1         (0, 1)    1.000          1    
2         (1, 0)    1.000          1    
3         (1, 2)    1.000          1    
4         (0, 2)    1.414          0    
5         (2, 2)    1.414          0    
6         (-1, 1)   2.000          0    
7         (1, -1)   2.000          0    
8         (2, 3)    2.236          1    

Rank      Point     Distance       Label
8         (0, 1)    1.000          1    
8         (1, 0)    1.000          1    
8         (1, 2)    1.000          1    
8         (0, 2)    1.414          0    
8         (2, 2)    1.414          0    
8         (-1, 1)   2.000          0    
8         (1, -1)   2.000          0    

The new point (1, 1) belongs to class 0 using 7-NN.
```

### Question 2b
Larger values of `k` will lead to smoother decision boundaries. This leads to lower chances of overfitting (Covered in `T3W5`). So, the order is:

```
k_l < k_c < k_r
```

### Question 2c
Time takento run inference on test dataset for vanilla `k-NN` is indepedent of `k`. Altogether, we'll still be taking `m * t` time given a dataset of `m` samples.

--- 

### Question 3a
Both algorithms are correct. The algorithm of Alibe runs in `O(n(d+k))` while that of Bob runs in `O(ndk)`. Alice's algorithm is much faster.

### Question 3b
Maintain a BST with `k` nodes where the BST tracks the top `k` smallest distances. This would reduce the running time to `O(n(d + logk))`. 

--- 

### Question 4
No. The difference between the two ranges give `0.4` and `10º Celcius`. This means the `Temperature` variable will dominate the k-NN when calculating the Euclidean Distance, minimising the impact or effect of the `Humidity` variable.

We can minimise the effect of this disproportion by normalising or standardising the inputs to a suitable range that won't affect the distance metric immensely. This will be covered in future classes.

--- 

### Question 5
