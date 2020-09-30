# gpacalc
Python library for calculating GPA.

## Usage
You can import the calculator like so:
```py 
from gpa import calc


```
`calc` takes a `dict` type as an input, in a structure like so, where the first value is your pertcentage in your class out of 100.0 and the second is the amount of credit-hours that the class is worth:
```py
scores = {
    "Math": [80.1, 2],
    "Chemistry": [92.4, 2.0],
    "History": [68.1, 3.0],
    "English": [32.0, 3]
}
```

For the first value, entering an `int` will get it converted to a `float` and divided by 100. For example, `15` would be interpreted as `15.0`, or 15 percent.
For the second value, an `int`, `str`, or `float` type is accepted.