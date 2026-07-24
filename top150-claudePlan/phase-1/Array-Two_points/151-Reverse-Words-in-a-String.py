s = "the sky is blue"

l = list(s)
def reverse_str(left, right):
    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1

reverse_str(0, len(l) - 1)
s = ''.join(l)
print(s)