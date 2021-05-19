word = input()
letter_counter = [0] * (ord('Z') - ord('A') + 1)
for letter in word:
    letter_counter[ord(letter) - ord('A')] += 1

palindrome_half = []
middle_letter = ''
total_odd_counts = 0
for letter_code in range(ord('Z') - ord('A') + 1):
    letter = chr(ord('A') + letter_code)
    if letter_counter[letter_code] % 2 == 1:
        middle_letter = letter
        total_odd_counts += 1
        if total_odd_counts > 1:
            break
    
    while letter_counter[letter_code] > 1:
        palindrome_half.append(letter)
        letter_counter[letter_code] -= 2

if total_odd_counts <= 1:
    print(''.join(palindrome_half + [middle_letter] + palindrome_half[::-1]))
else:
    print('NO SOLUTION')


# from collections import Counter
 
# word = input()
# letter_counter = Counter(word)
 
# palindrome_half = []
# middle_letter = ''
# total_odd_counts = 0
# for letter, count in letter_counter.items():
#     if count % 2 == 1:
#         middle_letter = letter
#         total_odd_counts += 1
#         if total_odd_counts > 1:
#             break

#     while count > 1:
#         palindrome_half.append(letter)
#         count -= 2
 
# if total_odd_counts <= 1:
#     print(''.join(palindrome_half + [middle_letter] + palindrome_half[::-1]))
# else:
#     print('NO SOLUTION')
