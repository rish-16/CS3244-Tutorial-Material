# Tutorial 2 Week 4: Decision Trees

In T2W4, I cover the Decision Tree algorithm. Find the tutorial slides [here](https://www.figma.com/file/jqyuC4tzHUu84NaXc28zPI/Tutorial-Slides?node-id=0%3A1).

I have included the implementation of a Decision Tree classifier in pure Python using `numpy` and `pandas` in `dtc.py`. You can call it in a similar fashion to that in `sklearn` using the `DecisionTreeClassifier` object. I train it on the popular *Iris Type Classification Dataset* found in `data/iris.csv`.

## Contents
This repo contains the code used to answer Questions 1, 2, 3, and 4.

### Question 1a

```
                  S_1
                /     \
              0/       \1
            F=0        S_2
                       / \
                     0/   \1
                   F=1    S_3
                         /   \
                       0/     \1
                      F=1     F=0
```

### Question 1b
Function `F` can be represented as `AND(S_2, S_3)`. We can build as tree that's of depth 2:

```
                  S_2
                /     \
              0/       \1
            S_3         S_3
            / \         / \
          0/   \1     0/   \1
         F=0   F=1   F=1   F=1
```

If your memory of the `AND` gate is fuzzy, here's a tabular summary:

| **A** | **B** | **AND** |
|-------|-------|---------|
| 0     | 0     | 0       |
| 0     | 1     | 0       |
| 1     | 0     | 0       |
| 1     | 1     | 1       |

### Question 1c

If your memory of the `XOR` gate is fuzzy, here's a tabular summary:

| **A** | **B** | **XOR** |
|-------|-------|---------|
| 0     | 0     | 0       |
| 0     | 1     | 1       |
| 1     | 0     | 1       |
| 1     | 1     | 0       |

To implement this `XOR` gate, we'd need `2^d` leaf nodes and `2^d - 1` internal nodes. It grows exponentially with `d`. Using a Decision Tree is not scalable. Pruning is not possible because we need to consider every single input (ie. a feature) – we can't just ignore any of them.

You can, however, implement `AND` and `OR` gates using a DT since pruning is possible. We dont need to consider all our inputs. For example, for an `AND` gate, if any one of our inputs is `0`, the result is `0` regardless of the other inputs. Likewise, if any feature in an `OR` gate is `1`, the result is `1` regardless of the other inputs.

---

### Question 2a
The features are as follows:

- `Income`
- `Credit History`
- `Debt`

The label is `Decision`.

At each level, the main question we will be asking is,


> Which feature to choose such that splitting via that gives us the "greatest purity" ie. the most even split between samples.

The tree would look like so:

```
                   CrHi?
            /        |       \        
        Bad/     Good|        \Unknown
          /          |         \
         Rej        App        Income?
                            /     |     \
                           /      |      \
                      0-5K/  5-10K|       \10K+ 
                       Debt      App      App
                      /   \
                  Low/     \High
                   App     Rej
``` 

*Note: Refer to the slides for more on Information Gain and Entropy. We covered Claude Shannon's Information Theory in this class!*

### Question 2b

Tree 1:
```
           CrHi?
       /     |     \
  Good/   Bad|      \Unknown
     App    Rej     Income?
                 /     |     \
            0-5K/ 5-10K|      \10K+
              App     App     App
```

Tree 2:
```
           CrHi?
       /     |     \
  Good/   Bad|      \Unknown
     App    Rej      Debt?
                    /     \
                Low/       \High
                 App       App
```

Tree 3:
```
                       Income?

          /               |               \
         /                |                \
    0-5K/            5-10K|                 \10K+
     Debt?              Debt?               Debt?
    /     \            /     \             /     \
Low/       \High   Low/       \High    Low/       \High
 App       Rej      App       App       App       App
```

### Question 2c
> Of course, you must convert (encode) these strings like `GOOD`, `BAD`, `HIGH`, `LOW` to numeric values. So `GOOD = 1` and `BAD = 0`, for example. Same goes for the labels. ML Models ***DO NOT*** work with raw strings, only numbers.

`DT($4K, GOOD CH, HIGH debt) = Approve`

> Hint: Just follow path down to the leaf in your DT Classifier from Question 2a.

If we use our 3 DTs, the results will be the following:

```
Tree 1: Approve
Tree 2: Approve
Tree 3: Reject
```

If we use uniform voting (every tree gets equal say ie. majority voting), we `Approve` the application since 2/3 classifiers agree.

--- 

### Question 3a
Debt depends on Income. Person A with income of $5K and a debt of $4K, and Person B with income $15K and a debt of $4K, results in Person A being in `HIGH` debt while Person B is in `LOW` debt. Debt is categorical and Income is a quantifiable, continuous variable. This makes the explainability ambiguous.

### Question 3b
Empirically, Decision Trees are bad performers on datasets with missing values. To calculate metrics like Information Gain and Entropy, it is nice to have all the information in front of us. Missing data makes these measures unreliable, making the DT classifier inaccurate. Replacing missing values with alternatives (`mean`, `max`, `min`, `mode`, etc.) could easily skew your data (think of it as "poisoning your dataset"). Also, dropping the affected rows makes the dataset smaller and non-representative of those specific cases (your model won't know what to do in those cases anymore).

### Question 3c
Decision Trees do not consider temporal (time-related) features. You are introducing heavy class imbalance into your dataset by appending rows of data with a `REJECT` decision. Your model might overfit on this new biased dataset. Always try to maintain a good balance of `positive` and `negative` cases in your dataset to allow for better generalisation.

> More on class imbalance and overfitting in future weeks!

---

### Question 4
Refer to the working covered in class. You can find the official working in the [slides](https://www.figma.com/file/jqyuC4tzHUu84NaXc28zPI/Tutorial-Slides?node-id=0%3A1).