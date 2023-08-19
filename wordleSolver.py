import english_words as ew

def main():
    is_playing = True
    while(is_playing):
        guessed = False
        words_list = ew.get_english_words_set(['web2'], lower=True)
        lenght = input("Enter word lenght: ")
        if lenght.isnumeric():
            print("you can start with:")
            words_list = get_words_by_lenght(words_list, lenght)
            ##TODO print as table
            print_words_list(words_list)
            count = 0
            while(guessed == False):
                word = input("Enter a word: ").lower()
                if word not in words_list:
                    print("word not in list")
                count += 1
                characters_weight_list = []
                for character in word:
                    characters_weight_list.append( int(input("enter the weight of character: 0 not present, 1 present but wrong position, 2 present and correct position "+ character.upper() + ": ")))

                characters_utility =create_characters_utility_dict(characters_weight_list,word)
                words_list = remove_not_useful_words(words_list,word,characters_utility)
                guessed =check_win(words_list,count)
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

def create_characters_utility_dict(characters_weight_list,word:str):
    characters_utility = dict()
    for index,character in enumerate(word):
        if character not in characters_utility:
            characters_utility[character] = [characters_weight_list[index]]
        else:
            characters_utility[character].append(characters_weight_list[index])
    convert_missing_to_wrong_position(characters_utility)
    return characters_utility

def convert_missing_to_wrong_position(characters_utility:dict):
    for character in characters_utility:
        for index,weight in enumerate(characters_utility[character]):
            if weight == 0 and len(characters_utility[character])>1 and index != 0:
                characters_utility[character][index] = 3
    return characters_utility

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

def get_words_without_present_character_in_index_position(word_list:set[str],character:str,position:int):
    new_word_list = set[str]()
    for word in word_list:
        if word[position]!=character:
            new_word_list.add(word)
    return new_word_list 

def remove_not_useful_words(word_list:set[str],word:str,character_utility:dict):
    new_word_list =word_list.copy()
    for character_index,character in enumerate(word):
        weight =character_utility[character][0]
        print(weight,character_utility)
        character_utility[character].pop(0)
        if weight == 0:
            new_word_list = get_words_without_present_characters(new_word_list,character)
        if weight == 1:
            new_word_list = get_words_with_present_character_but_wrong_position(new_word_list,character,character_index)
        if weight == 2:
            new_word_list = get_words_with_present_character_and_correct_position(new_word_list,character,character_index)
        if weight == 3:
            new_word_list = get_words_without_present_character_in_index_position(new_word_list,character,character_index)
    return new_word_list

def check_win(word_list:set[str],count):
    max_tries = 6 - count
    if max_tries == 0 and len(word_list) > 1:
        print("you lost")
        return False
    if len(word_list) == 1:
        print("you won after " + str(count) + " tries")
        print("the word is: " + word_list.pop())
        return True
    else:
        print_words_list(word_list)
        print("you have " + str(max_tries) + " tries left")
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