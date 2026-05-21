'''
import functools
# functools.reduce()
# Repeatedly applies a function to combine all items into a single value.
print(functools.reduce(lambda x, y: x + y, [1, 2, 3, 4]))

# functools.partial()
# Creates a new function by fixing some arguments in advance.
print(functools.partial(pow, 2)(5))

# functools.cmp_to_key()
# Converts an old-style comparison function into a key function for sorting.
print(sorted([5, 2, 9, 1], key=functools.cmp_to_key(lambda a, b: a - b)))

# functools.lru_cache()
# Stores previously computed results to improve performance.
@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))

# functools.cached_property
# Computes a value once and stores it for future use.
class Person:
    @functools.cached_property
    def full_name(self):
        return "Rajesh Kumar"
print(Person().full_name)

# functools.total_ordering
# Automatically provides missing comparison methods in a class.
print(functools.total_ordering)

# functools.wraps
# Preserves original function information when using decorators.
print(functools.wraps(lambda: None))

# functools.singledispatch
# Enables function overloading based on argument type.
print(functools.singledispatch)

# functools.singledispatchmethod
# Enables method overloading inside classes based on argument type.
print(functools.singledispatchmethod)'''

############# ITERTOOLS IN PYTHON #############

import itertools
# count() → Creates an infinite sequence of numbers starting from a given value
print(next(itertools.count(10)))  

# islice() → Takes only a specific number of elements from an iterator
print(list(itertools.islice(itertools.count(10), 5)))  

# cycle() → Repeats elements infinitely in a loop
print(list(itertools.islice(itertools.cycle(["A", "B", "C"]), 7)))  

# repeat() → Repeats the same value multiple times
print(list(itertools.repeat("Hello", 3)))  

# accumulate() → Returns cumulative sums
print(list(itertools.accumulate([1, 2, 3, 4])))  

# chain() → Combines multiple iterables into one sequence
print(list(itertools.chain([1, 2], [3, 4])))  

# compress() → Filters data based on selectors (1=True, 0=False)
print(list(itertools.compress("ABCDE", [1, 0, 1, 0, 1])))  

# dropwhile() → Drops elements while condition is True
print(list(itertools.dropwhile(lambda x: x < 3, [1, 2, 3, 4, 1])))  

# takewhile() → Takes elements while condition is True
print(list(itertools.takewhile(lambda x: x < 3, [1, 2, 3, 1])))  

# filterfalse() → Returns elements where condition is False
print(list(itertools.filterfalse(lambda x: x % 2 == 0, [1, 2, 3, 4])))  

# starmap() → Applies a function using tuple arguments
print(list(itertools.starmap(pow, [(2, 3), (3, 2)])))  

# groupby() → Groups consecutive similar elements
print(list(itertools.groupby("AAABBBCC")))  

# islice() → Extracts elements using start, stop, and step
print(list(itertools.islice(range(10), 2, 8, 2)))  

# pairwise() → Creates overlapping pairs
print(list(itertools.pairwise([10, 20, 30, 40])))  

# product() → Returns Cartesian product of iterables
print(list(itertools.product([1, 2], ["A", "B"])))  

# permutations() → Returns ordered arrangements
print(list(itertools.permutations([1, 2, 3], 2)))  

# combinations() → Returns unordered selections
print(list(itertools.combinations([1, 2, 3], 2))) 

# combinations_with_replacement() → Allows repeated values
print(list(itertools.combinations_with_replacement([1, 2], 2)))  

# zip_longest() → Zips iterables of different lengths
print(list(itertools.zip_longest([1, 2], ["A"], fillvalue="X")))  

# batched() → Splits data into fixed-size groups
print(list(itertools.batched([1, 2, 3, 4, 5], 2)))  


