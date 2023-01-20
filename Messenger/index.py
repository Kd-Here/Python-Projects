#!/usr/bin/env python
# -*- coding: latin-1 -*-



with open('WhatsApp_Chat_project.txt','r',encoding='utf8') as f:
    for i in f:
        print(i)
        break


# Python program to replace text in a file
x = input("enter text to be replaced:")
y = input("enter text that will replace:")

# file.txt should be replaced with
# the actual text file name
f = open("file.txt", "r+")

# each sentence becomes an element in the list l
l = f.readlines()

# acts as a counter to know the
# index of the element to be replaced
c = 0
for i in l:
	if x in i:

		# Replacement carries the value
		# of the text to be replaced
		Replacement = i.replace(x, y)

		# changes are made in the list
		l = Replacement
	c += 1

# The pre existing text in the file is erased
f.truncate(0)

# the modified list is written into
# the file thereby replacing the old text
f.writelines(l)
f.close()
print("Text successfully replaced")

