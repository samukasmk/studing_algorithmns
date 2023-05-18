"""
Develop a function that searches and matches groups of anagrams as well as the expected result:

>>> words_list = ["abc", "bca", "aaa", "mmm", "door", "rood", "rod", "orod"]

>>> matching_anagram_groups(words_list)
[
  ["abc", "bca"], ["aaa"], ["mmm"], ["door", "rood", "orod"], ["rod"]
]
"""


def counting_anagrams_dict(phrase):
    anagram_characters_counf = {}
    for char in phrase:
        anagram_characters_counf[char] = anagram_characters_counf.get(char, 0) + 1
    return anagram_characters_counf


def matching_anagram_groups(words_list):
    group_matched = {}

    # iterate each phrase
    for word in words_list:
        # normalize word sorting it
        sorted_word = ''.join(sorted(word))

        # check if it has an anagram matched
        if sorted_word in group_matched:
            # put other in group
            group_matched[sorted_word].append(word)
        else:
            # start a new group to match
            group_matched[sorted_word] = [word]

    return list(group_matched.values())


class TestMatchingAnagramGroups():
    def test_match_anagram_groups(self):
        words_list = ["abc", "bca", "aaa", "mmm", "door", "rood", "rod", "orod"]
        expected_groups = [["abc", "bca"], ["aaa"], ["mmm"], ["door", "rood", "orod"], ["rod"]]
        print(type(matching_anagram_groups(words_list)))
        assert matching_anagram_groups(words_list) == expected_groups

if __name__ == "__main__":
    import os
    import pytest

    current_file = os.path.abspath(__file__)
    pytest.main([current_file])