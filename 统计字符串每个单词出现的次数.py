def count(str):
    count_words = str.lower().split()
    count_word = {}
    for word in count_words:
        if word not in count_word.keys():
            count_word[word] = 1
        else:
            count_word[word] += 1
    return count_word

print(count('I can because i think i can'))
# {'i': 3, 'can': 2, 'because': 1, 'think': 1}

# 方法二
# from collections import Counter

# str = 'I can because i think i can'
# counts = Counter(str.lower().split())
# print(counts, type(counts), help(counts))

