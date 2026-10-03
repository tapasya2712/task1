def is_hill_number(n: int) -> bool:
    
    s = str(abs(n))
    length = len(s)

   
    if length < 3:
        return False

    i = 0

   
    while i < length - 1 and s[i] < s[i + 1]:
        i += 1

   
    if i == 0 or i == length - 1:
        return False

   
    while i < length - 1 and s[i] > s[i + 1]:
        i += 1

        return i == length - 1


def main():
    try:
        user_input = int(input("Enter a number: "))
        if is_hill_number(user_input):
            print("Output: Yes")
        else:
            print("Output: No")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()
