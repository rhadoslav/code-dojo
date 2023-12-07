"""
If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.

Find the sum of all the multiples of $3$ or $5$ below $1000$.

---

30
3 5 6 9 10 12 15 18 20 21 24 25
"""

if __name__ == "__main__":
    upper_bound = 1000
    n_3: int = upper_bound // 3 if upper_bound % 3 != 0 else upper_bound // 3 - 1
    n_5: int = upper_bound // 5 if upper_bound % 5 != 0 else upper_bound // 5 - 1
    n_15: int = upper_bound // 15 if upper_bound % 15 != 0 else upper_bound // 15 - 1
    print(f"{n_3} {n_5}")

    s_3: int = n_3 * (n_3 + 1) // 2 * 3
    s_5: int = n_5 * (n_5 + 1) // 2 * 5
    s_15: int = n_15 * (n_15 + 1) // 2 * 15
    print(f"{s_3} + {s_5} = {s_3 + s_5 - s_15}")
