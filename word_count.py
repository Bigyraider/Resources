s = "This is an example string 234"

vowels = "aeiouAEIOU"
count = 0

for w in s.split():
    if len(w) < 3:
        continue
    if not w.isalnum():
        continue
    if not any(c in vowels for c in w):
        continue
    if not any(c.isalpha() and c not in vowels for c in w):
        continue
    count+=1
print(count)