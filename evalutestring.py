# Get user input for the range

range_input = input("Enter the range (e.g. 'a-z'): ")


# Remove quotes from the user input

range_input = range_input.strip('"')


# Split the range into start and end characters

start_letter, end_letter = range_input.split('-')


# Convert start and end characters to ASCII codes using `ord`

start_ascii = ord(start_letter)

end_ascii = ord(end_letter)


# Generate the string of characters in the range using `chr` and list comprehension

char_range = [chr(i) for i in range(start_ascii, end_ascii+1)]


# Join the characters in the range into a single string

result_string = ''.join(char_range)


# Print the resulting string

print(result_string)



































