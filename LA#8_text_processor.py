print("===Text Processor===\n")

sentence = input("Enter a sentence: ").strip()
print()

print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")
print(f"Titlecase: {sentence.title()}")
print(f"\nNumber of 'a' or 'A': {sentence.count('a') + sentence.count('A')}")
print(f"\nSentence with underscore/s: {sentence.replace(' ', '_')}")
print(f"\nSplit sentence: {sentence.split()}")
print(f"\nWords in your sentence: \n{'\n'.join(sentence.split())}")