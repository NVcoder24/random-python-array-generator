# random-python-array-generator
generates random python arrays
## libraries
###### you need pyperclip only if you using full version (random array generator.py)
```
pip install random
pip install pyperclip
```
## using in other project
###### rag_min.py must be in folder with your main python file!
```python
import rag_min # Random Array Generator MINimum

print(f"some random array: " + get_rand_array(10, 1, 10)) # get_rand_array(amount of elements in array, minimum simbols in string, maximum symbols in string)
```
