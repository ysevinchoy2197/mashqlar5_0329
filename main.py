#9-misol
s9 = lambda x: 100 if x > 100 else x
print(s9(110))

#10-misol
s10 = lambda x: abs(x) if x < 0 else x
print(s10(-11))

#11-misol
f11 = lambda a, b: 0 if a == b else (1 if a > b else -1)
print(f11(5, 5))

#12-misol
f12 = lambda x: "Fizz" if x % 3 == 0 else x
print(f12(6))
