import random

# write a hello function that prints hello world
# invoke hello function

# write decorator function that logs input and outputs and times it to a function
def log(func):
    def wrapper(*args, **kwargs):
        print("Input: {} {}".format(args, kwargs))
        result = func(*args, **kwargs)
        print("Output: {}".format(result))
        return result
    return wrapper


# invoke decorator function
def hello(x):
    print(f"Hello, World! {x}")
    return(f"Hello, World! {x}")


hello(3)

# write a function that yields a generator that randomly picks 3 types of fruits
def fruit_generator():
    fruits = ["apple", "orange", "banana"]
    while True:
        yield random.choice(fruits)


# invoke fruit generator
for i in range(5):
    print(next(fruit_generator()))
