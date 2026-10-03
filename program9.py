def is_anagram(word1: str, word2: str) -> bool:
    
    
    clean_word1 = word1.lower().replace(" ", "")
    clean_word2 = word2.lower().replace(" ", "")

   
    return sorted(clean_word1) == sorted(clean_word2)


def main():
    
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")

    
    if is_anagram(word1, word2):
        print("Output: Yes")
    else:
        print("Output: No")


if __name__ == "__main__":
    main()
