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

## Task 1
Create an abstract class Shape that will enforce that any child class will need to implement the filed method.

But why is Abstract Class not by default in Python like Java or other **Object Oriented Language**?
Duck Typing relies on the concept of dynamically typed. As in Python, the variable type is assigned to object on run-time, thus in duck typing, you do not check type. Rather the presence of method is checked.

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

Check the len of integer.

```
x = 123
print(len(x))
```

# Task 2
Implement the `IntLike` class that will define the `__len__` method.


The output above explains the duck typing clearly, as in above code it was not searching for the variable type rather it finds the particular method (in this case __len__).
## Hello Types
In this section you’ll see how to add type hints to a function.
Create a function that will add headline as role description, it should have an `bool` type argument `upper`, that convert text to upper case letter.

```
def headline(text, upper):
    if upper:
        return f"{text.upper()}\n{'-' * len(text)}"
    else:
        return f"{text}\n{'-' * len(text)}"

```

Evaluate the function with your role description:
```
print(headline("Implement clean and scalable code.", upper = True))
```


## Pros and Cons
**Pros**:

Type hints help document your code.

Type hints improve IDEs and linters. (Check function).

Type hints help you build and maintain a cleaner architecture.


**Cons**:

Type hints take developer time and effort to add.

## Annotations

When running the code, you can also inspect the annotations. They are stored in a special .__annotations__ attribute on the function:

```
python -i headline.py
headline.__annotations__
```

## Static Type Checking
Refactor funtion to add type hints:

```
def headline(text: str, upper: bool = False) -> str:
```
Install `mypy`:
```
pip install mypy
```

Run `Mypy` on this code:

```
mypy headline.py

```


## Dynamic Type Checking
Pydantic enforces type hints at **runtime** and provides user-friendly errors when data is invalid. Unlike the type hints introduced above which may seem cosmetic, the models introduced by pydantic are productive and would change your data.

The file `user_model.py` implements the class with `dynamic type checking`.
```
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
```

It can additionaly specify the `custom_validator`.
How to fix the following errors:
```
python -i user_model.py
u = User(id="2", name="VERYLONGNAMEPERSON", surname = "K")
u = User(id=[1], name="VERYLONGNAMEPERSON",surname = "K")
```

Check the type of the attribute `id`:
```
u = User(id="2", name="kamila", surname = "kazimierska")
type(u.id)
```
## Task 3 Type Checking
Write the function with type checking that takes the user argument and
print it in `title` format.

## Task 4 Input validation
Create a [pydantic class](https://docs.pydantic.dev/latest/usage/models/),
that inherits from `BaseModel`
has the name `Employee`,
fields `name`, `surname`, `role`.

## Task 5 Extend the employee
Create a child subclass of `Employee`, add the fileld `techonologies` make sure it can take one of the available choices: ['Python', 'Angular', 'Docker', '.Net'].
So, I can evaluate the following:

```
Developer(
    name="K", surname="K", role="full-stack",
    technologies = ["Python", "Angular"]
)
```



## Reference
[Python Typing](https://realpython.com/python-type-checking/)

[PEP 484](https://peps.python.org/pep-0484/)

[Pydatnic](https://docs.pydantic.dev/latest/)
[Abstract](https://medium.com/@vidipmalhotra/abstract-method-in-python-vs-duck-typing-6ef77fb816c)