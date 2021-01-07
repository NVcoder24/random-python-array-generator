# random-python-array-generator
generates random python arrays
## libraries
###### you need pyperclip only if you using full version (random array generator.py)
```
pip install random
pip install pyperclip
```
## using
###### rag_min.py must be in folder with your main python script!
```python
import rag_min # Random Array Generator MINimum

print(rag_min.get_rand_array(10, 1, 10)) # get_rand_array(amount of elements in array, minimum simbols in string, maximum symbols in string)
```
also you can get random string or symbol
```python
import rag_min # Random Array Generator MINimum

print(f"random string: {rag_min.get_rand_str(1, 10)}") # get_rand_array(minimum simbols in string, maximum symbols in string)
print(f"random symbol: {rag_min.get_rand_char()}")
```
you can convert array you get to string too
```python
import rag_min # Random Array Generator MINimum

some_array = rag_min.get_rand_array(10, 1, 10)
my_string_array = rag_min.convert_array_to_string(some_array) # convert_array_to_string(array)

print(f"my random array: {my_string_array}")
```
```python
import rag_min

my_array = [1,2,3,4,5]
my_string_array = rag_min.convert_array_to_string(my_array)

print(f"my array: {my_string_array}")
```
idk but you can get symbols that uses in rag
```python
import rag_min # Random Array Generator MINimum

my_simbols = rag_min.chars

print(f"my symbols collection: {my_simbols}")
```
