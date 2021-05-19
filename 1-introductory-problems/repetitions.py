word = input() + '@'

max_substr_len = 1
current_substr_start = 0
i = 1
while i < len(word):
    if word[i] != word[current_substr_start]:
        max_substr_len = max(max_substr_len, i - current_substr_start)
        current_substr_start = i
    else:
        i += 1

print(max_substr_len)
