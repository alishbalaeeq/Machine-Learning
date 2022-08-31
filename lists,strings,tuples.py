# Enumerate

Fruits = ['Apples', 'Bananas', 'Apricot', 'Orange', 'Peach']

for i, value in enumerate(Fruits):
    print(i, value)

Vegetables = ['Spinach', 'Cucumber', 'Broccoli', 'Red Pepper', 'Tomato']

for i, value in enumerate(Vegetables, 5):
    print(i, value)

# Given a list of strings, return the count of the number of strings
# where the string length is 2 or more and the first and last chars of the
# string are the same.

sent = ["My name is Khan and I am not a terrorist", "I ate a banana today but tomorrow I'll eat orange",
        "No, Please go away", "I", "Engine is genuine"]

count = 0
for i in sent:
    length = len(i)
    if length >= 2:
        last = i[length - 1]
        first = i[0]

        if first.lower() == last.lower():
            count = count + 1

print(f"The string count is {count}")

# Given a list of strings, return a list with the strings in sorted order,
# except group all the strings that begin with 'x' first.

sent = ["My name is Khan and I am not a terrorist", "I ate a banana today but tomorrow I'll eat orange",
        "No, Please go away", "I", "Engine is genuine", "X-Men is a really cool movie"]

sent1 = []
sent2 = []
main_sent = []

for i in sent:
    first = i[0]
    if first.lower() == 'x':
        sent1.append(i)
    else:
        sent2.append(i)

sent2.sort()
main_sent.append(sent1)
main_sent.append(sent2)

print(main_sent)

# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.

tuples = [(1, 2, 3), (43, 22, 2), (25, 66, 8, 21)]

list1 = len(tuples) 
for i in range(0, list1): 
    for j in range(0, list1-i-1): 
        if (tuples[j][-1] > tuples[j + 1][-1]): 
            temp = tuples[j]
            tuples[j]= tuples[j + 1] 
            tuples[j + 1]= temp 

print(tuples)

# Given a list of numbers, return a list where all adjacent == elements
# have been reduced to a single element, so [1, 2, 2, 3] returns [1, 2, 3].

list1 = [1, 2, 2, 3, 44, 55, 44]
new_list = []

for i in list1:
    if i not in new_list:
        new_list.append(i)

print(new_list)

# two lists sorted in increasing order, create and return a merged list of
# all the elements in sorted order

list1 = [1, 6, 3, 7, 4, 8, 33, 9, 2, 65]
list2 = [55, 2, 88, 4, 6, 23, 0, 43]

list1.sort()
list2.sort()
final_list = list1 + list2

final_list.sort()

print(final_list)


