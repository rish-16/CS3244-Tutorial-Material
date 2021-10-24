# Tutorial 4 Week 6: Bias Variance Tradeoff

In T4W6, I cover Bias-Variance Tradeoff. Find the tutorial slides [here](https://www.figma.com/file/jqyuC4tzHUu84NaXc28zPI/Tutorial-Slides?node-id=0%3A1).

> This tutorial was pretty difficult. I've attached a `FAQ.pdf` file that seeks to clarify certain details on this week's topics.

## Contents
This repo contains answers for Questions 1 and 2.

### Question 1a
Number of data points: Yes
Amount of Noise: No
Complexity of Target: No

### Question 1b
Determinstic noise will increase as it gets harder for `H` to model `f`. Stochastic noise remains the same as it is independent of `H` and `f`. There is a greater chance of overfitting.

### Question 1c
Determinstic noise will decrease as it gets eaier for `H` to model `f`. Stochastic noise remains the same as it is independent of `H` and `f`. There is a greater chance of overfitting.

---

### Question 2a
Each blue point is the average training accuracy for an arbitrary value of `C`. It's the average of all the `10` accuracies for the 10-FCV. 

Each green point is the average validation accuracy for an arbitrary value of `C`. It's the average of all the `10` validation accuracies for the 10-FCV.

### Question 2b
Each blue region represents the **variance** of the training accuracy for a value of `C`. It is calculated by getting the variance of all `10` accuracies for the 10-FCV. 

Similarly, the green region is the **variance** of the validation accuracy for a value of `C`. It's the variance of all `10` accuracies for the 10-FCV.

### Question 2c
The best validation accuracy is reached when `C = 1`. 

> High training accuracy DOES NOT indicate high validation/testing accuracies. Always perform your train-test process to see if the model has generalised well to the unseen data before doing anything with the model (like deploying to production or using it IRL).

---

### Question 3a

> The annotated proofs for this question can be found on the slides.

### Question 3b
1. Smaller `k` values with everything else constant, will increase the variance.
2. As `k` increases, bias increases. As the number of instances increases, we will be considering points further away from `x0` (closeness decreases) and the resulting predictions will move away from `f(x0)`. 

> Bias = Closeness to Truth

---

### Question 4

> The annotated proofs for this question can be found on the slides.