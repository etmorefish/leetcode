# python 统计字符串每个单词出现的次数

# sentence = "I can because i think i can"
# result = {word: sentence.split().count(word) for word in set(sentence.split())}
# print(result)


# from collections import Counter

# str = 'I can because i think i can'
# counts = Counter(str.split())
# print(counts, type(counts), help(counts))

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
