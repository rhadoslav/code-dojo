"""
The series, $1^1 + 2^2 + 3^3 + \cdots + 10^{10} = 10405071317$.

Find the last ten digits of the series, $1^1 + 2^2 + 3^3 + \cdots + 1000^{1000}$.

---

- last 10 digits means (sum mod 10^10).

"""

if __name__ == "__main__":
    target = 1000
    result = 0
    cut = 10**10
    for i in range(1, target + 1):
        result += (i**i) % cut
    print(result % cut)
