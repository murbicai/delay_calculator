from math import log

bpm = int(input("What's the BPM? "))

division = input("What's the division? e.g. 1/4, 5/16 etc.")

dotted = input("Dotted? (y/n) ")

num, denom = division.split('/')

num, denom = int(num), int(denom)

denom = log(denom, 4)

# q = quarter note interval aka number of ms between each 1/4
# 60000 = number of ms per minute
q = 60000 / bpm

result = int(q * num / denom)
if dotted == "y":
    result = int(result*(1.5))
    dotted = "dotted"
else:
    dotted = ""

print(f'For a {dotted}{division} delay at {bpm} BPM, use: \n{result} ms')