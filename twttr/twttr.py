def main():
    text = 'Input: '
    user_input = str(input(text))
    convert(user_input)


def convert(user_input):
    s = list(user_input)
    outcome = ''
    list_of_vowels = ['e', 'u', 'i', 'o', 'a']
    for i in s:
        if i.lower() in list_of_vowels:
            outcome = outcome
        elif i.lower() not in list_of_vowels:
            outcome += i
    print(outcome)


main()
