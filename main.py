
def main():

    file_contents = None
    file_path = "books/frankenstein.txt"

    character_dict = {}
    sorted_char_list = []
    
    with open(file_path) as f:
        file_contents = f.read()


    print(f"--- Begin report of {file_path} ---")
    print(f"{get_number_of_words(file_contents)} words found in the document")
    print("\n")

    character_dict = get_number_of_times_character_appears(file_contents)
    sorted_char_list = convert_dict_to_list_of_dicts(character_dict)

    for i in range(len(sorted_char_list)):

        char = sorted_char_list[i]["character"]
        count = sorted_char_list[i]["count"]

        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")





def get_number_of_words(contents):

    word_list = contents.split()

    return len(word_list)

def get_number_of_times_character_appears(file_contents):
    char_dict = {}
    lowercase_string = file_contents.lower()

    for char in lowercase_string:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    return char_dict


def convert_dict_to_list_of_dicts(dict):

    new_list = []

    for key in dict:
        if key.isalpha():
            new_dict = {"character": key, "count" : dict[key]}
            new_list.append(new_dict)

    new_list.sort(reverse = True, key=sort_on)

    return new_list


def sort_on(dict):
    
    return dict["count"]

main()