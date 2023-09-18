[Python Typing](https://realpython.com/python-type-checking/)

## Type Systems

**Dynamic typing** - Python interpreter does type checking only as code runs.
```
if False:
    1 + "two"  # This line never runs, so no TypeError is raised
else:
    1 + 2
```

**Python** is **dynamically** typed language.
[PEP 484](https://peps.python.org/pep-0484/) introduces **type hints**

```
def greeting(name: str) -> str:
    return 'Hello ' + name
```

**Static typing**
Static type checks are performed without running the program.
Typescript code will throw an error: `Type 'number' is not assignable to type 'string'.`

```
let myString: string
myString = "kami"
console.log(myString);
myString = 2
```

**Duck typing**
“if it walks like a duck and it quacks like a duck, then it must be a duck”
Using duck typing you do not check types at all. Instead you check for the presence of a given method or attribute.

```
class TheHobbit:
    def __len__(self):
        return 95022

the_hobbit = TheHobbit()
len(the_hobbit)
```
**Solution**
pydantic enforces type hints at runtime and provides user-friendly errors when data is invalid. Unlike the type hints introduced above which may seem cosmetic, the models introduced by pydantic are productive and would change your data.

Check:
```
python -i task_validator.py
User(**{"id":2, "name":"VERYLONGNAMEPERSON"})
```

## Task 1 Input validation
Create a pydantic class, that inherits from `BaseModel` and validates .

## Hello Types
## Pros and Cons
## Annotations
## Playing With Python Types, Part 1
## Type Theory
## Playing With Python Types, Part 2
## Static Type Checking
## Conclusion
## MYPY