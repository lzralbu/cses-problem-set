word = input()

anagrams = set()

def gen_anagrams(word, anagram = ''):
    global anagrams
    if len(word) == 0:
        anagrams.add(anagram)
        return word
    
    for i, letter in enumerate(word):
        gen_anagrams(word[ : i] + word[i + 1 : ], anagram + letter)

gen_anagrams(word)

print(len(anagrams))
print('\n'.join(sorted(anagrams)))

# def fat(n):
#     result = 1
#     while n > 1:
#         result *= n
#         n -= 1
#     return result

# from collections import Counter
# letter_counter = Counter(word)

# total_anagrams = fat(len(word))
# for letter, count in letter_counter.items():
#     total_anagrams //= fat(count)

# print(total_anagrams)

# for i in range(1 << len(word)):
#     letters = []
#     for pos, bit in enumerate(bin(i)[2:].rjust(len(word), '0')):
#         if bit == '1':
#             letters.append(word[pos])
#     anagrams.add(''.join(letters))
