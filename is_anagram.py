def is_anagram(word):
    if type(word[0]) is str and type(word[1]) is str:
        # แปลงเป็น list
        a = list(word[0])
        b = list(word[1])
        #_sort_##################################
        a.sort()
        b.sort()
        #_remove_duplicate_######################
        a = set(a)
        b = set(b)
        #_filtered_only_alphabet_################
        a_filtered = []
        b_filtered = []
        for i in a:
            if i.isalpha() and type(i) is str:
                a_filtered.append(i)
        for i in b:
            if i.isalpha() and type(i) is str:
                b_filtered.append(i)
        #########################################
        # for i in a_filtered:
        #     print(i, end= "")
        # print()
        # for i in b_filtered:
        #     print(i, end= "")
        # print()
        return a_filtered == b_filtered
                
if __name__ == "__main__":
    print(is_anagram(["listen","silent"]))
    print(is_anagram(["television"," it's one evil."]))
    print(is_anagram(["listen", "silentness"]))
    print(is_anagram(["hello", "hola"]))