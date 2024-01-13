# importing "keyword" for keyword operations
import keyword
# initializing strings for testing while putting them in an array
keys = ["for", "geeksforgeeks", "elif", "elseif", "nikhil",
		"assert", "shambhavi", "True", "False", "akshat", 
		"akash", "break", "ashty", "lambda", "suman",
		"try", "vaishnavi"]

for i in range(len(keys)):
	# checking which are keywords
	if keyword.iskeyword(keys[i]):
		print(keys[i] + " is python keyword")
	else:
		print(keys[i] + " is not a python keyword")
