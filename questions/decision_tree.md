<details>
<summary><b>Can Decision Trees take in temporal data?</b></summary>

<br>

Nope. You could ask "why don't we add in a new feature called `time` and call it a day?". 

### Your headaches
Imagine Decision Trees *could* learn temporal information. If you added a feature for `time`, you're okay for the most part if your time is discrete ie. `t = 1, 2, 3, ..., T`. You are absolutely screwed if your time is continuous which is the case for most real-life applications. Your rows, and hence, your dataset, will blow up exponentially for each sample/instance.

IRL, temporal data consists of sequential samples `x_i` with `T` timesteps. Each timestep is represented by a vector in `R^n` that encompasses the information at that timestep. So, for a sequence of words (ie. a sentence) like "the horse drank water", the numeric representation would be `x_i = [v_1, v_2, v_3, v_4]` where `v_i` is a *word vector*. You can use a similar technique to encode all kinds of sequential information like pixels in an image (each timestep would be a pixel from left to right, top to bottom) or weekly stock prices (each timestep would be a daily price point). This makes the data 2-dimensional (ie. a matrix) instead of your usual 1-dimensional data (simple vector).

Your discrete time dataset (of words or daily stock prices) would look like this. How would you even make this Decision-Tree-friendly?

| Sample Index   | Token Index | Vector Repr | Label |
| -------------- | ----------- | ----------- | ----- |
| 1              | 1           | w\_1        | 1     |
|                | 2           | w\_2        | 1     |
|                | 3           | w\_3        | 1     |
|                | 4           | w\_4        | 1     |
| 2              | 1           | w\_1        | 0     |
|                | 2           | w\_2        | 0     |
|                | 3           | w\_3        | 0     |
|                | 4           | w\_4        | 0     |
|                | 5           | w\_5        | 0     |
|                | 6           | w\_6        | 0     |
| 3              | 1           | w\_1        | 1     |
|                | 2           | w\_2        | 1     |
|                | 3           | w\_3        | 1     |

### Temporal features
Temporal features indicate a sequential nature to the instances, likely spanning multiple timesteps each. They have a general pattern of `x_i = [v_1, v_2, v_3, ..., v_T]` where `T` is the number of timesteps and `v_t` is some vector representation of each timestep (words, pixels, or daily stock price, for example). 

This brings me to the concept of *Recurrence* where the future timestep depends on what came before. As in, `P(v_{t+1} | [v_1, v_2, ..., v_t])`. To predict data in the future, you need to know data in the past. 

### How Decision Trees learn

As such, purely going by how Decision Trees learn over data, you can't re-feed related data into a Decision Tree. Every single sample you send through a DT is assumed to be independent of all other samples or inputs fed into it. Your task with a DT is *ideal path selection* ie. finding your way to some arbitrary leaf node for the final classification. There is no going back up in any way once you start going down. Once you pass a branch, you will never go back up that branch ever again.

> It's a one way ticket downwards to the leaves.

A Decision Tree takes in inputs and produces a prediction that's either a label (Classification) or numeric real value (Regression Trees). It does not spit out temporal vectors used to encode your dataset samples. There is no way of passing in 2-dimensional inputs into your DT, just 1-dimensional.

## Think harder
Here's a rule of thumb:

> If you can't easily break up a dataset using `if-else` statements, a Decision Tree is the wrong model for that task.

Why? A Decision Tree is essentially a glorified, fancy `if-else` statement generator that comes up with the conditions by itself using stuff like Information Gain and Entropy. If it can't do that, you can't use a DT for the problem at hand. Use something else.
</details>