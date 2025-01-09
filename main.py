def print_report(filepath):
	with open(filepath) as f:
		file_contents = f.read()

		wordcount = count_words(file_contents)
		charcount = count_characters(file_contents)

		print(f"--- Begin report of {filepath} ---")
		print(f"{wordcount} words found in the document\n")
		for char in charcount:
			print(f"The '{char}' character was found {charcount[char]} times")
		print("--- End report ---")

def count_words(text):
	words = text.split()
	return len(words)

def count_characters(text):
	characters = {}

	for char in text.lower():
		if char.isalpha():
			if char not in characters: characters[char] = 1
			else: characters[char] += 1

	return dict(sorted(characters.items(), key=lambda x: x[1], reverse=True))

print_report("books/frankenstein.txt")