# Introduction to Search

1 December 2025

## Files, again

Consider the following example file, `data.csv` (the actual YouTube views data is not real):

```csv
Track,Album Name,Artist,YouTube Views,Explicit Track
Not Like Us,Not Like Us,"120,344,203",Kendrick Lamar,1
Flowers,Flowers - Single,"32,344,203",Miley Cyrus,0
I Had Some Help (feat. Morgan Wallen),I Had Some Help,Post Malone,"12,344,203",1
```

We can read the contents of the file line by line like so. You can find more details about this from the previous notes.

```python
with open("data.csv") as f:
	for line in f:
		# split the line into its columns
		info = line.split(",")
		# print the track name
		print(info[0])
```

### Commas in the CSV data?

If there are commas in the data the method above breaks. Instead, we can use the `csv` module to read the file more appropriately. To do this, we can create what's called a `reader` object to read the file. Open the file as usual, but use the reader to iterate over the filestream. An example is below.

```python
import csv

with open("data.csv") as f:
	reader = csv.reader(f)

	for info in reader:
		# the reader splits the line into a list automagically
		# so we can print the track name if we know its index
		print(info[0])
```

## Search Algorithms

Remember that [algorithms](https://en.wikipedia.org/wiki/Algorithm) are simply a sequence of steps to solve a problem.

In computer science and mathematics, it's a relatively big deal to solve problems that involve looking for items. These problems are solved using **search** algorithms. For example, if we have a whole bunch of data and we're looking for one specific item, we can use a **search** algorithm to find what we need. There are different search algorithms for different situations.

Some are really good and efficient, some are not. We can estimate how efficient an algorithm is relative to the amount of data that we're looking through. We always want to use the best algorithm based on the situation.

Computer scientists and mathematicians are always searching (there's a joke in there somewhere) for new ways to search. There are some discovered algorithms that are well known. To start, we're going to implement an algorithm that is relatively simple to understand, **linear search**.

### Linear Search

Linear search is an algorithm that can be used to find things in an unordered list. Note, an unordered list means that the elements in the list are not in any particular order.

The algorithm can be described like this:

1. Start at the beginning of the list
2. If the current thing is the thing we're looking for, stop... **we've found it!**
3. If not, move to the next thing
4. If we've reached the end of the list, stop... **it's not in this list!**
5. Repeat step 2.

![Linear Search](https://www.tutorialspoint.com/data_structures_algorithms/images/linear_search.gif)

If we're using the data above, we can implement linear search like this:

```python
# omitted code above

# we're looking for miley cyrus songs
artist = "miley cyrus"

with open("data.csv") as f:
	reader = csv.reader(f)

	for info in f:
		if info[2].lower() == artist:
			print("We found a Miley Cyrus song!")
					
```


