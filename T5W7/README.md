# Tutorial 5 Week 7: Regularisation and Validation

> Hope you had a productive Recess Week! Let's try getting that 'A' for midterms :D

In T5W7, I cover the Regularisation and Validation. Find the tutorial slides [here](https://docs.google.com/presentation/d/1eE1In5ZS19YKgN3DN9VjNhBavHQoMaKB9NjZ-hreTG0/edit?usp=sharing).

## Contents
This repo contains the code used to answer Questions 1, 2, and 3.

---

### Question 1a
Training time : `m^2 * log(m)`

In **LOO-CV**, one fold is one sample. There are `m-1` training samples and `1` testing sample, each performed `m` times for each sample. That means every sample gets its chance of being the testing sample. This is for _one_ model.

Number of models: `30` <br>
Number of training samples: `m-1` <br>
Number of testing samples: `1` <br>
<br>
Total time: `30 * m * (m-1)^2 * log(m-1)`

### Question 1b

In **10-FCV**, each fold has `m/10` samples inside. There are 9 training folds and 1 testing fold. Each `m/10`-sized fold gets its chance of being the testing fold. This is for _one_ model.

Number of models: `30` <br>
Number of training samples: `9` <br>
Number of testing samples: `1` <br>
Training time for entire dataset of `m` samples : `m^2 * log(m)` <br>
<br>
Total time: `[30 * 10 * (9m/10)^2 * log(9m/10)] + [m^2 * log(m)]`

---

## How to read contour plots
Before we get into Question 2, let's understand the figures given to us.
<br><br>
The ellipses are contour plots that represent the altitudes of the function. Think of it as the graph surface coming out of the paper in 3 dimensions (like a volcano on paper). The lower the number next to a circle, the lower the altitude, and vice versa.

1. Find the minimum value of `Reg. Penalty + MSE term`
2. Return the corresponding values of `(Theta0, Theta1)`

> It's OKAY to guess here! The values are rough _guesstimates_. Just eyeball it.

### Question 2a
No regularisation means we only look at the MSE term. Find the values of `(Theta0, Theta1)` such that the value of the MSE term is minimum. This occurs at the circle at altitude `0.2` on either graph. The center of that circle corresponds to `Theta0 = ~0.9` and `Theta1 = 0.5`. It's alright if the value fluctuates `± 0.5` from the correct answer.

### Question 2b
Look at graph 1. There are possible sums to consider:

1. Minimum MSE + Flexible Reg Penalty = `0.1 + 4.0 = 4.1` (NOPE)
2. Flexible MSE + Minimum Reg Penalty = `0.4 + 5.0 = 5.4` (NOPE)
3. Middle ground = `0.5 + 2.6 = 3.1` (CORRECT)

> The minimum sum corresponds to the pair `(0.2, 0.25)`

### Question 2c
Look at graph 2. There are possible sums to consider:

1. Minimum MSE + Flexible Reg Penalty = `0.1 + 9.0 = 9.1` (NOPE)
2. Flexible MSE + Minimum Reg Penalty = `0.0 + 4.4 = 4.4` (NOPE)
3. Middle ground = `2.5 + 2.2 = 4.7` (CORRECT)

> The minimum sum corresponds to the pair `(0.0, 0.55)`

---

### Question 3a
Time Series data is dependent on time. Breaking that natural order of time makes your data worthless. The best possible scenario is breaking the dataset without abrupt breakages in between. For example, you can store the past few days worth of temporal data points for training, and the future points for testing.

> The value is in the time. Respect it.

### Question 3b
Break your data into training, validation, and testing without switching the order of the samples or shuffling them. For example, suppose we have the following dataset with time going from `T1` to `T20`:

```
Dataset = [T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20]

Training = [T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11]
Validation = [T12, T13, T14, T15]
Testing = [T16, T17, T18, T19, T20]
```

> Again, please respect the time component for temporal data.

### Question 3c
Take adjacent pairs of data points for training and validation.

```
Dataset = [1, 2, 3, 4]

Training = [1] | Validation = [2]
Training = [2] | Validation = [3]
Training = [3] | Validation = [4]
```

There are less-preferred alternatives:

1. `Training = [1] | Validation = [3]` -> decent model
2. `Training = [1, 2] | Validation = [3]` -> predicting too far into the future after limited training
3. `Training = [1, 2, 3] | Validation = [4]` -> better model but can't really compare to training fold in **1.**

> The key is to break the dataset into comparable folds for training and testing that result in models that are not too different from one another.