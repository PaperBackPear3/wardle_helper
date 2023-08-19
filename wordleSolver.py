import english_words as ew

def main():
    words_list = ew.get_english_words_set(['web2'], lower=True)
    is_playing = True
    while(is_playing):
        guessed = False
        lenght = input("Enter word lenght: ")
        if lenght.isnumeric():
            print("you can start with:")
            words_list = get_words_by_lenght(words_list, lenght)
            ##TODO print as table
            print_words_list(words_list)
            while(guessed == False):
                word = input("Enter a word: ").lower()
                characters_utility = tuple(int)
                for character in word:
                    characters_utility += (int(input("enter the utility of character: 0 not present, 1 present but wrong position, 2 present and correct position "+ character.upper() + ": ")))
                words_list = remove_not_useful_words(words_list,word,characters_utility)
                guessed =check_win(words_list)
                print_words_list(words_list)
        else:
            print("Not a number")
        if guessed == True:
            is_playing = keep_playing()

def get_words_by_lenght(word_list, lenght):
    possible_words_list = set[str]()
    for word in word_list:
        if len(word) == int(lenght):
            possible_words_list.add(word)
    return possible_words_list

def get_words_without_present_characters(word_list:set[str],character:str):
    new_word_list = set[str]()
    for word in word_list:
        if character not in word:
            new_word_list.add(word)
    return new_word_list

def get_words_with_present_character_but_wrong_position(word_list:set[str],character:str,position:int):
    new_word_list = set[str]()
    for word in word_list:
        if word[position]!=character and character in word:
            new_word_list.add(word)
    return new_word_list

def get_words_with_present_character_and_correct_position(word_list:set[str],character:str,position:int):
    new_word_list = set[str]()
    for word in word_list:
        if word[position]==character:
            new_word_list.add(word)
    return new_word_list

def remove_not_useful_words(word_list:set[str],word:str,character_utility:tuple):

    for index,character in enumerate(word):
        if character_utility[index] == 0:
            word_list = get_words_without_present_characters(word_list,character)
        if character_utility[index] == 1:
            word_list = get_words_with_present_character_but_wrong_position(word_list,character)
        if character_utility[index] == 2:
            word_list = get_words_with_present_character_and_correct_position(word_list,character)
    return word_list

def check_win(word_list:set[str]):
    if len(word_list) == 1:
        print("You win")
        return True
    else:
        return False

def print_words_list(word_list):
    for word in word_list:
        print(word)

#check quit game
def keep_playing():
    choice =input("Want to keep playing? (y/n)")
    if choice.lower() == "y":
        return True
    else:
        print("Bye")
        return False

##staring
if __name__ == "__main__":
    main()