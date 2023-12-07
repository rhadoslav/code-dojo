/*
The series, $1^1 + 2^2 + 3^3 + \cdots + 10^{10} = 10405071317$.

Find the last ten digits of the series, $1^1 + 2^2 + 3^3 + \cdots + 1000^{1000}$.

---

- last 10 digits means (sum mod 10^10).
*/
#include <iostream>
#include <cmath>
#include <iomanip>

int main() {
    int target = 1000;
    double result = 0;
    double cut = pow(10, 10);
    double temp = 1;

    for (int i = 1; i <= target; i++) {
        temp = 1;
        for (int j = 0; j < i; j++) {
            temp = fmod(temp * i, cut);
        }
        result = fmod(result + temp, cut);
    }
    std::cout << std::setprecision(100) << result << std::endl;
}
