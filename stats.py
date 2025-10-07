def count_words(file_content):
    return len(file_content.split());

def count_chars(file_content):
    map_of_chars = {};
    
    for char in file_content:
        char_lower = char.lower();
        if char_lower not in map_of_chars:
            map_of_chars[char_lower] = 0;
        map_of_chars[char_lower] += 1;
    
    return map_of_chars;

def sort_on(items):
    return items["num"];

def build_report(count_words, map_of_chars):
    list_of_chars_to_sort = [];
    for char in map_of_chars:
        list_of_chars_to_sort.append({"char": char, "num": map_of_chars[char]});
    
    list_of_chars_to_sort.sort(reverse=True, key=sort_on);
    
    print("============ BOOKBOT ============");
    print("Analyzing book found at books/frankenstein.txt...");
    print("----------- Word Count ----------")
    print(f"Found {count_words} total words");
    print("--------- Character Count -------");
    
    for char_dict in list_of_chars_to_sort:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}");
    print("============= END ===============");