# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

print("Вычеслить число с заданной точность d")
print("*" * 40)

from math import pi

d = int(input("Введите число для заданной точности числа Пи:\n"))
print(f"Число Пи с заданной точностью {d} равно {round(pi, d)}")