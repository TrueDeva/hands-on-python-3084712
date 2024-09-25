NAMES = ["John", "Paul", "George", "Ringo", "Jones", "Baker", "Sully"]
AGES = [20, 21, 22, 23]

JOHN = NAMES[0]
PAUL = NAMES[1]

# [:] means trim from! Such Trim from 0 and 4
JOHN_PAUL = NAMES[1:3]
# trim the first 2 and leave the rest
GEORGE_RINGO = NAMES[2:]
REVERSE = NAMES[::-1]
# reverse names and display display every second one
REVERSE = NAMES[::-2]

EVERY_OTHER = NAMES[::2]

print(sum(AGES))
print(min(AGES))
print(max(AGES))

print(JOHN_PAUL)
print(GEORGE_RINGO)
print(REVERSE)
