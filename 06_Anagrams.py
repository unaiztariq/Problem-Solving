# Problem 3: Group Anagrams
# Given a list of strings, group the strings that are anagrams of each other.
# Example:
# Input: ["eat","tea","tan","ate","nat","bat"]
# Output:
# [
#   ["eat","tea","ate"],
#   ["tan","nat"],
#   ["bat"]
# ]

def group_anagrams_dict(anagrams):
    dictt={}
    for i in anagrams:
        key = ''.join(sorted(list(i)))
        if key in dictt:
            dictt[key].append(i)
        else:
            dictt[key] = [i]
    sorted_anagrams = []
    for j in dictt.values():
        sorted_anagrams.append(j)
    return sorted_anagrams


def group_anagrams_brute_force(anagrams):
    same_list = []
    end_list = []
    for words in anagrams:
        allowed = True
        if words in same_list:
            continue
        else:
            same_list = []
            for i in end_list:
                    if words in i:
                        allowed = False
                        break
        if allowed == True:
            for i in anagrams:
                for letter in words:
                    if letter not in i:
                        break
                else:
                    same_list.append(i)
            end_list.append(same_list)
    return end_list


def anagram(word1,word2):
    key1 = "".join(sorted(word1.lower()))
    key2 = "".join(sorted(word2.lower())) 

    if  key1 == key2:
        return True
    else:
        return False

print(group_anagrams_brute_force(["eat","tea","tan","ate","nat","bat"]))
print(anagram("Listen","Silent"))
