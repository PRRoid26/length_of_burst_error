import random


def introduce_error(data, error_probability):
    result = ""
    for bit in data:
        if random.random() < error_probability:
            result += '1' if bit == '0' else '0'  
        else:
            result += bit
    return result

s = input("Enter the bits sent by the sender: ")


error_probability = 0.1
r = introduce_error(s, error_probability)
print("Bits received by the receiver (with errors):", r)

ll = -1
ul = -1


for i in range(len(s)):
  if s[i] != r[i]:
    if ll == -1:
        ll = i
        ul = i
    else:
        ul = i
  if ll == -1:
      flag=1
  else:
      flag=0

if flag==1:
  print("There were no errors during transfer.")
else:
  print("The length of the burst error is:", (ul - ll) + 1)