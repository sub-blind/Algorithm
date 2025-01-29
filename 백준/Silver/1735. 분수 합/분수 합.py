import sys
import math

input = sys.stdin.readline

num1, den1 = map(int, input().split())
num2, den2 = map(int, input().split())

numerator = num1 * den2 + num2 * den1
denominator = den1 * den2
gcd = math.gcd(numerator, denominator)

print(numerator // gcd, denominator // gcd)
