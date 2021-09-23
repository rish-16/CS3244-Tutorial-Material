# Tutorial 3 Week 5: Linear Models

In T3W5, I cover the Linear Models. Find the tutorial slides [here](https://www.figma.com/file/jqyuC4tzHUu84NaXc28zPI/Tutorial-Slides?node-id=0%3A1).

This repo contains Python implementations of `LinearRegressionClassifier`, `LogisticRegressionClassifier`, and `SupportVectorClassifier`. You can call them in a similar fashion to related models from `sklearn`. I train them on the popular *Iris Type Classification Dataset* found in `data/iris.csv`, as well as the *Breast Cancer Classification Dataset* from `sklearn.datasets`. 

> You can find the SVM implementation in `Intro_to_Support_Vector_Machines.ipynb`. It has some more in-depth comments inside.

## Contents
This repo contains the code used to answer Questions 1, 2, and 5.

### Question 1
You cannot use **Mean Squared Error**.

MSE is mainly used in the case of regression problems, not classification tasks (which is when Logistic Regression is used). 

- `Accuracy` shows us how "good" our model is on unseen data
- `AUC-ROC` shows us the model's ability to tell apart positive and negative instances
- `Log Loss` is used as the cost function for Logistic Regression. The aim is to minimise this over training.

---

### Question 2
The **Normal Equation** from the lecture:

```bash
ø = (1/(X.T * X)) * X.T * Y
  = [4    -5.5    -7    7].T

y_hat = 4 - 5.5x1 - 7x2 + 7x3
```

---

### Question 3
> Check the slides for annotated solutions for all the equations here.

---

### Question 4
> Check the slides for diagrams and answers to these questions.

---

### Question 5a
A symmetric matrix is one that's equal to its transpose. 

> Look at the slides for an annotated proof.

### Question 5b
You have to use induction for this. Consider the base case and then move on to the inductive step.

> Look at the slides for an annotated proof.

### Question 5c
Similar to `5b`, we have to use induction. We use the concept of **Idempotency** again.

> Look at the slides for an annotated proof.

### Question 5d
We know that `trace(AB) = trace(BA)`. For symmetric and idempotent matrices, `rank(A) = trace(A)`.

> Look at the slides for an annotated proof.