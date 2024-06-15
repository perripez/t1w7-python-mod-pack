from text_processing import count_words, unique_words, count_characters, count_unique_characters, reverse_string

# Test String
test_string = "Hello world hello"

# Using the word count module
print("Word count: ", count_words(test_string))
print("Unique words: ", unique_words(test_string))

# Using car_count module
print("Character count: ", count_characters(test_string))
print("Unique characters: ", count_unique_characters(test_string))

# Using  reverse module
print("Reversed string: ", reverse_string(test_string))