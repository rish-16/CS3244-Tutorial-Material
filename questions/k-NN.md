<details>
<summary><b>Does <code>k</code> include the new observation itself?</b></summary>

<br>
Nope. The `k` hyperparameter refers purely to the number of *closest* samples from your dataset you want to compare with. Your new observation is not treated as one sample out of `k`. 
</details>

<details>
<summary><b>Can we set <code>k = 0</code>?</b></summary>

<br>
Nope. A k-NN first calculates distance between the new observation and the `m` training points. Next, it finds the `k` closest points to the new observation and classifies it as the majority class within the top `k` points. If `k = 0`, you're basically ignoring and neglecting the dataset completely. You can't even classify the new observation because we aren't able to get a majority of anything – you can't get the labels of `0` closest points. It's a bit absurd and destroys the purpose of using a comparison-based `k-NN` model. <br>

Empirically, `k` values of 3, 5, and 7 are used. This gives some leeway to generalise without overfitting or underfitting. Though, depending on the specific context, you may have to change that. Always test your `k` models in practice such that it gives the best performance on the testing dataset.
</details>

<details>
<summary><b>Can we set <code>k = m</code> where <code>m</code> is the number of samples in the training dataset?</b></summary>

<br>
Nope. Then that just considers all the points as the closest and considers the majority of your dataset's sample labels. For example, if your dataset has 20 `yes` labels and 50 `no` labels, and if we set `k = m`, this is what happens:
<br><br>

1. You calculate the distance between new observation and all `m` training points
2. You consider the labels of all `m` training points
3. By sheer counting, there are *way more* `no` points than `yes` points
4. Your new observation will be classified as `no` even though it could have been `yes`

Why? By simple majority voting, of course.
<br><br>
This situation is called **Class Imbalance** and is covered in this module.
</details>