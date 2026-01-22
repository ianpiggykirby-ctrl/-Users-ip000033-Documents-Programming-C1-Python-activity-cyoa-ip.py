# Files and Data

18 November 2025

## Files
For this section, we'll learn how to open and read text files.
When we open up files, we need to consider the location or **path** to the file.
The **path** to the file is the direction we take to get to the file.
including in a path, is the **file's name** and the folder that it lives in.
### Opening Files
To open a file, we use the `open()` function. The `open()` function returns a **file object**.  A **file object** represents a **file stream** which is like a pipe that connects our python file to the external file.
```python
# information.txt is a file that we went to open
file = open("information.txt")
```
### Reading their contents
When reading the contents of a file, you receive the first line of data,
then the second, ... ,all the way to the end.
Use the `.readline()` method to read one line of information.
if you call it again, it will give you the next line of information.
```python
# omitted code above
first_line = file.readline()  # string
second_line = file_readline()
```

If you want to read all lines of the file, **iterate over the file**,
```python
# omitted code above
for line in file:
    # do something with the line
	print(line)         # line is a string
```
### Managing File Streams
When we pen up a file stream, we should always close it after we're finished reading/writing anty info. This helps to lower the risk of corrupting any data in the file. To close a file stream, we use the `.close()` method.
```python
# omitted code above
file.close() # closes the stream safely
```

An alternate way to open/close files is to use the `with`  keyword. `with` helps us create these things described as closures.
```python
# the file is information.txt
with open("information.txt") as file:
    line = file.readline()
	for line in file:
	   print(line)

file.readline()  # this would break
```
## Lists

Lists are type of data that are helpful in strong more than one related piece of information, that is related.  With lists, order matters. To create a list, we use brackets `[]` . 
```python
# create an empty list
some_list = []
```

### Convert a String to a List
There are times where we want to get information from a string.
One use case where this is important is the example of a `.csv` or. comma-separated values file.
```csv
Name, Age, Favourite Character
Ian, 16, Kirby
Kirby, Unknown, Bandana Dee
```

```python
# As a string, the second line would be
info = "Ian,16,Kirby"
# Split the string wherever there's a , 
info_list = info.split(",") #["Ian", "16", "Kirby"]
```
### Accessing Specific Items in a List

To access a specific element inside the list, we use `[]`
bracket notation. We give the **index** of the item, which is like the address of the item. **indices** are always integers.

```python
# omitted code above
# info_list -> ["Ian", "16", "Kirby"]
# Access Ian's age -- index = 1
print(f"Ian's age is {info_list[1]}.")
# Access Ian's favourite character -- index = -1
print(f"Ian's favourite character is {info_list[-1]}")
```