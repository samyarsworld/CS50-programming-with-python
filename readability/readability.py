from cs50 import get_string

# Prompt user for a text
text = get_string("Write your text here: ")

# Word, sentence, and letter count
l_count = s_count = 0
w_count = 1             # Accounting for the last word


for i in text:
    if i in [".", "?", "!"]:
        s_count += 1
    if i.isspace():
        w_count += 1
    if i.isalpha():
        l_count += 1

# Average number of letters per 100 words
L = l_count * 100 / w_count

# Average number of sentences per 100 words
S = s_count * 100 / w_count

# Coleman-Liau index formula
CLI = round(0.0588 * L - 0.296 * S - 15.8)

# Output the grade
if CLI >= 16:
    print("Grade 16+")
elif CLI < 1:
    print("Before Grade 1")
else:
    print(f"Grade {CLI}")
