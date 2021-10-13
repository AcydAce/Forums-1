
import math

numerator = int(input("insert numerator : "))
while numerator <= 0:
    numerator = int(input("numerator cannot be <= 0, insert numerator [>0] : "))

denominator = int(input("insert denominator : "))
while denominator < 0:
    denominator = int(input("denominator cannot be <= 0,insert numerator [>0] : "))

fraction = (f"{numerator} / {denominator}")

if numerator < denominator:

    fraction_type = "proper fraction"
    print(f"[{fraction}] is a proper fraction.")
else:

    fraction_type = "improper fraction"
    print(f"[{fraction}] is an improper fraction.")

gcd      = math.gcd(numerator, denominator)

if gcd == 1:

    print(f"This {fraction_type} cannot be simplified.")

else:

    numerator = numerator // gcd
    denominator = denominator // gcd

    print(f"This {fraction_type} can be simplified into: {numerator} / {denominator}")

WholeNum = numerator // denominator
Remainder = numerator % denominator

if Remainder == 0:
    print(f"{fraction} can be written as the whole number {WholeNum}.")
else:
    print(f"{fraction} can be written as the mixed number {WholeNum} {Remainder} / {Denom}.")
