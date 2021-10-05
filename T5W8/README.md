# Tutorial 5 Week 8: Evaluation Metrics

In T5W8, I cover Evaluation Metrics. Find the tutorial slides [here](https://docs.google.com/presentation/d/19QigHWaB3GTnhyNfWkbXYpcfvUT2wPq1Zi2ft40GATM/edit?usp=sharing).

> This chapter is very important to you as ML practitioner. It gives us tools to analyse how our model is doing after training. These methods give us an indication of which direction to head in when stuck. 

## Contents
This repo contains answers for Questions 1 and 2.

### Question 1a
| Sample | Prediction | Label   |
|--------|------------|---------|
| x1     | 0 (NEG)    | 0 (NEG) |
| x2     | 0 (NEG)    | 1 (POS) |
| x3     | 0 (NEG)    | 1 (POS) |
| x4     | 0 (NEG)    | 0 (NEG) |
| x5     | 0 (NEG)    | 0 (NEG) |
| x6     | 1 (POS)    | 1 (POS) |
| x7     | 1 (POS)    | 1 (POS) |
| x8     | 1 (POS)    | 0 (NEG) |
| x9     | 1 (POS)    | 1 (POS) |
| x10    | 1 (POS)    | 1 (POS) |

| Submetric | (Pred, Actual) | Score |
|-----------|----------------|-------|
| TP        | (POS, POS)     | 4     |
| FP        | (POS, NEG)     | 1     |
| TN        | (NEG, NEG)     | 3     |
| FN        | (NEG, POS)     | 2     |

```
Precision = TP / (TP + FP)  = 4/5 = 0.8

Recall = TP / (TP + FN) = 4/6 = 0.67

F1 = 2/(1/P + 1/R) = 2/(1/0.67 + 1/0.8) = 0.73
```

### Question 1b
Brute force method of calculating F1 scores for all model outputs as thresholds will take `O(m^2)`. <br><br>

1. Sort all samples – `O(m logm)`
2. For the first threshold, find TP, FN, FP, FN and calculate F1 Score – `O(m)`
3. Next threshold will take `O(1)` since we can change the 4 values in 2.
4. After the first computation, it'll take `O(m-1) ~ O(m)` for remaining `m-1` samples

Total optimised run time is `O(m logm)`.

### Question 1c
Here, the number of thresholds are increased beyond number of samples in the dataset.

1. Sort all samples – `O(m logm)`
2. If we pick a threshold between two samples (in sorted order), they'll give the same F1 score
3. This means there can only be `(m+1)` possible F1 scores to consider
4. We can binary search for the best F1 score peak – O(logm)

---

### Question 2a – Micro
| _Dog_        | POS_act | NEG_act |
|--------------|---------|---------|
| **POS_pred** | 10      | 3       |
| **NEG_pred** | 6       | 26      |

| _Cat_        | POS_act | NEG_act |
|--------------|---------|---------|
| **POS_pred** | 13      | 5       |
| **NEG_pred** | 6       | 21      |

| _Pig_        | POS_act | NEG_act |
|--------------|---------|---------|
| **POS_pred** | 7       | 7       |
| **NEG_pred** | 3       | 28      |

### Question 2b
| _Combined_   | POS_act | NEG_act |
|--------------|---------|---------|
| **POS_pred** | 30      | 15      |
| **NEG_pred** | 15      | 75      |

```
Accuracy_micro = (TP + TN) / (TP + TN + FP + FN) = (30 + 75)/(30 + 75 + 15 + 15) = 0.778

Precision_micro = TP / (TP + FP) = 30 / (30 + 15) = 0.667

Recall_micro = TP / (TP + FN) = 30 / (30 + 15) = 0.667

F1_micro = 2/(1/P + 1/R) = 2/(1/0.667 + 1/0.667) = 0.667
```

### Question 2c – Macro
| _Dog_        | POS_act | NEG_act |
|--------------|---------|---------|
| **POS_pred** | 10      | 3       |
| **NEG_pred** | 6       | 26      |

Precision_Dog = 10 / (10 + 3) = 0.769 <br>
Recall_Dog = 10 / (10 + 6) = 0.625

| _Cat_        | POS_act | NEG_act |
|--------------|---------|---------|
| **POS_pred** | 13      | 5       |
| **NEG_pred** | 6       | 21      |

Precision_Cat = 13 / (13 + 5) = 0.722 <br>
Recall_Cat = 13 / (13 + 6) = 0.684

| _Pig_        | POS_act | NEG_act |
|--------------|---------|---------|
| **POS_pred** | 7       | 7       |
| **NEG_pred** | 3       | 28      |

Precision_Pig = 7 / (7 + 7) = 0.5 <br>
Recall_Pig = 7 / (7 + 3) = 0.7

```
Precision_micro = (P_Dog + P_Cat + P_Pig) / 3 = 0.664
Recall_micro = (R_Dog + R_Cat + R_Pig) / 3 = 0.664
```

### Question 2d
| Class | TP  | FP  |
|-------|-----|-----|
| A     | 9   | 1   |
| B     | 100 | 900 |
| C     | 9   | 1   |
| D     | 9   | 1   |

```
Precision_micro = (TP1 + TP2 + TP3) / [(TP1 + FP1) + (TP2 + FP2) + (TP3 + FP3)] 
                = (9 + 100 + 9 + 9) / (10 + 1000 + 10 + 10) 
                = 0.137
```

```
Precision_A = Precision_C = Precision_D = 9 / 10 = 0.9
Precision_B = 100 / 1000 = 0.1

Precision_macro = (P1 + P2 + P3) / 4
                = (0.9 + 0.1 + 0.9 + 0.9) / 4
                = 0.7
```

We can see that `Precision_macro` >>> `Precision_micro`. <br><br>

- The model has high Precision for classes A, C, and D, with low Precision for class B
- `Precision_macro` takes the average of all individual Precision values, treating each class equally
    - It does not consider the heavy imbalance in class B
    - `Precision_macro` is relatively higher as a result
- `Precision_micro` doesn't treat classes equally
    - The imbalances are factored into the calculation
    - Class B has low Precision and makes up the majority of the dataset
    - `Precision_micro` is relatively lower as a result
