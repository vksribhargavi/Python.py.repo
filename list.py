'''#import math
var =10
var1=10.25
var2="vignan"
var3=math.var1
print(var+var3)'''

'''import os
print("Current Working Directory:")
print(os.getcwd())'''
'''
import math
sub1 = int(input("Enter sub1 marks: "))
sub2 = int(input("Enter sub2 marks: "))
if sub1 >= 35 and sub2 >= 35:
    print("Pass")
else:
    print("Fail")'''

'''#import math 
l=[120,121,122,123,124,125,126,127,128,129]
i=int(input())
for i in range(129):
    print("valid")
else:
    print("invalid")'''


#Hello world
#print("Hello world")
'''
#Hello world with a variable
msg="Hello World"
print(msg)'''

'''#make a list
bikes=['trek','duke','enfield']
first_bike=bikes[0]
last_bike=bikes[-1]'''

'''str='Yellow'
print(str[0])
print(str[-1])
print(str[-2])
print(str[1])
print(str[2])
print(str[3])'''
'''
course="python"
print(course[3])
print(course[2:5])
print(course[-4:-1])
print(course[-6:-2])'''

'''course='Revit'
course1='API'
print(course +" "+ course1)
num1=96
num2=65
print(num1+num2)'''

'''str="Bhargavi"
print(len(str))'''

'''for x in range(10):
  print(x)

marks=98;
marks=[98,85,84]
print(marks)

'''
''' studentdetails=("studentid:12","studentname:AA","studentpercentage:98")
print(studentdetails)
tuple2=(89,90,91,91)
print(tuple2)'''

'''set={622,383,372}
print(type(set))'''

'''to print the list without list
numbers = list((1, 2, 3, 4))
print(numbers)
print(type(numbers))'''

'''upper and lower case
course="Bhargavi"
print(course.upper())
print(course.lower())
'''

'''colors = ['blue', 'green', 'yellow']
colors.append('red')
print(colors)

numbers=[1,2,3,4]
numbers.append(5)
print(numbers)
numbers.remove(3)'''

'''pet_type = "fish"
if pet_type == "dog":
     print("You have a dog.")
elif pet_type == "cat":
     print("You have a cat.")
elif pet_type == "fish":
# this is performed
     print("You have a fish")
else:
     print("Not sure!")'''

'''
result=[x**2 for x in range(10) if x%2==0]
print(result)'''


 #fprn loop
'''for x in range (10):
    if x%2==0 :
        print(x**2)
    else:
        print(x)'''

'''num=int(input())
for i in range(1,11):
    result=num*i
    print(num,"x",i,"=",result)'''

'''word=input("enter name:")
count=0
for i in word:
    count=count+1
    print(count)'''
'''
for i in range(10,0,-1):
    print(i)'''

#vowels
'''word=input("enter words:")
words=word.lower()
for i in words:
  if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
      print(i)'''

#largest number
'''num=[10,20,30,40]
largest=num[0]
for i in num:
    if i>largest:
        largest=i
        print(largest)'''

# Names starting with A
'''names = ['Amir', 'Arjun', 'Rush', 'Lohi', 'Swa', 'Deep']
for i in names:
    if i.startswith('A'):
        print(i)'''

#positive and negative numbers count
'''num = [10, 20, 54, 67, -2, -32, -238]
positive = 0
negative = 0
for i in num:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
print("Positive numbers count:", positive)
print("Negative numbers count:", negative)'''

#to print only 3 vowels
'''word=input("enter words:")
words=word.lower()
count=0
for i in words:
  if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
      count=count+1
      if count==3:
         print("3 vowels")
         break'''


#skip Capital letters
'''word = input("Enter a word: ")
for i in word:
    if i.isupper():
        continue
    print(i)'''

#for loop
'''nums = [1,2,3,4,5]
for num in nums:
     print(num)'''

'''for i in range(99):
     print(i)'''

#break loop
'''numbers = [0, 254, 2, -1, 3]
for num in numbers:
    if num < 0:
        print("Negative number detected!")
        break
    print(num)'''

#continue loop
'''big_number_list = [1, 2, -1, 4, -5, 5,2, -9]
for i in big_number_list:
     if i < 0:
      continue
     print(i)'''

#while loop
'''hungry = True
while hungry:
      print("Time to eat!")
      hungry = False'''

#nested loops
'''groups = [["Jobs", "Gates"], ["Newton","Euclid"], ["Einstein", "Feynman"]]
for group in groups:
     for name in group:
        print(name)'''


#List Comprehension
'''result = [x**2 for x in range(10) if x %
2 == 0]
print(result)'''

###########OS#################
import os

print(os.getcwd())                            # Current working directory
print(os.listdir())                           # List files and folders in current directory
print(os.listdir("."))                        # List files and folders from given path
print(os.path.exists("sample.txt"))           # True if file/folder exists
print(os.path.isfile("sample.txt"))           # True if it is a file
print(os.path.isdir("my_folder"))             # True if it is a folder

print(os.path.abspath("sample.txt"))          # Full absolute path
print(os.path.basename("/home/user/file.txt")) # file.txt
print(os.path.dirname("/home/user/file.txt")) # /home/user
print(os.path.join("folder", "file.txt"))     # folder/file.txt
print(os.path.splitext("sample.txt"))         # ('sample', '.txt')

print(os.name)                                # Operating system name
print(os.sep)                                 # Path separator
print(os.linesep)                             # Line separator
print(os.pathsep)                             # Path list separator

print(os.environ)                             # Environment variables
print(os.getenv("PATH"))                      # Get PATH environment variable
print(os.cpu_count())                         # Number of CPU cores

print(os.stat("sample.txt"))                  # File details, if file exists
print(os.path.getsize("sample.txt"))          # File size in bytes, if file exists
print(os.path.getmtime("sample.txt"))         # Last modified timestamp, if file exists

print(os.makedirs("new_folder", exist_ok=True)) # Create folder safely
print(os.rename("old.txt", "new.txt"))        # Rename file, if old.txt exists
print(os.remove("new.txt"))                   # Delete file, if new.txt exists
print(os.rmdir("new_folder"))                 # Delete empty folder

print(os.system("echo Hello Python"))         # Run system command


###########SYS#################
import sys

print(sys.version)                            # Python version information
print(sys.version_info)                       # Version info tuple
print(sys.executable)                         # Path to Python interpreter
print(sys.platform)                           # Operating system platform
print(sys.implementation)                     # Python implementation details

print(sys.argv)                               # Command-line arguments list
print(sys.path)                               # Module search paths
print(sys.modules)                            # Dictionary of loaded modules
print(sys.builtin_module_names)               # Tuple of built-in module names

print(sys.prefix)                             # Python installation directory
print(sys.base_prefix)                        # Base installation directory
print(sys.exec_prefix)                        # Platform-specific installation directory
print(sys.base_exec_prefix)                   # Base platform-specific installation directory

print(sys.maxsize)                            # Maximum integer used for indexing
print(sys.maxunicode)                         # Maximum Unicode code point
print(sys.byteorder)                          # System byte order ('little' or 'big')

print(sys.getdefaultencoding())               # Default string encoding
print(sys.getfilesystemencoding())            # File system encoding
print(sys.getrecursionlimit())                # Current recursion limit

print(sys.getsizeof("Hello"))                 # Memory size of an object in bytes
print(sys.intern("Python"))                   # Interned string object

print(sys.stdin)                              # Standard input stream
print(sys.stdout)                             # Standard output stream
print(sys.stderr)                             # Standard error stream

print(sys.flags)                              # Interpreter startup flags
print(sys.float_info)                         # Floating-point information
print(sys.int_info)                           # Integer implementation information
print(sys.hash_info)                          # Hash algorithm information
print(sys.thread_info)                        # Thread implementation information

print(sys.getswitchinterval())                # Thread switch interval in seconds
print(sys.getprofile())                       # Current profiling function
print(sys.gettrace())                         # Current tracing function

print(sys.api_version)                        # C API version number
print(sys.hexversion)                         # Python version as hexadecimal integer
print(sys.dont_write_bytecode)                # True if .pyc files are disabled
print(sys.warnoptions)                        # Warning options list



###########STATISTICS#################
import statistics

print(statistics.mean([10, 20, 30, 40]))                 # 25
print(statistics.fmean([10, 20, 30, 40]))                # 25.0
print(statistics.geometric_mean([1, 3, 9]))              # 3.0
print(statistics.harmonic_mean([2, 4, 8]))               # 3.4285714285714284

print(statistics.median([10, 20, 30, 40]))               # 25.0
print(statistics.median_low([10, 20, 30, 40]))           # 20
print(statistics.median_high([10, 20, 30, 40]))          # 30
print(statistics.median_grouped([10, 20, 30, 40]))       # 25.0

print(statistics.mode([1, 2, 2, 3]))                     # 2
print(statistics.multimode([1, 1, 2, 2, 3]))             # [1, 2]

print(statistics.pvariance([10, 20, 30, 40]))            # 125
print(statistics.variance([10, 20, 30, 40]))             # 166.66666666666666

print(statistics.pstdev([10, 20, 30, 40]))               # 11.180339887498949
print(statistics.stdev([10, 20, 30, 40]))                # 12.909944487358056

print(statistics.quantiles([10, 20, 30, 40, 50], n=4))   # [15.0, 30.0, 45.0]

print(statistics.covariance([1, 2, 3], [2, 4, 6]))       # 2.0
print(statistics.correlation([1, 2, 3], [2, 4, 6]))      # 1.0
print(statistics.linear_regression([1, 2, 3], [2, 4, 6])) # LinearRegression(slope=2.0, intercept=0.0)

print(statistics.NormalDist(0, 1))                       # NormalDist(mu=0.0, sigma=1.0)
print(statistics.NormalDist(0, 1).pdf(0))                # 0.3989422804014327
print(statistics.NormalDist(0, 1).cdf(0))                # 0.5
print(statistics.NormalDist(0, 1).inv_cdf(0.95))         # 1.6448536269514722

print(statistics.NormalDist.from_samples([10, 20, 30]))  # NormalDist(mu=20.0, sigma=10.0)




###########STRING#################
import string

print(string.ascii_lowercase)                 # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)                 # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_letters)                   # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

print(string.digits)                          # 0123456789
print(string.hexdigits)                       # 0123456789abcdefABCDEF
print(string.octdigits)                       # 01234567

print(string.punctuation)                     # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.whitespace)                      # Space, tab, newline, etc.
print(string.printable)                       # All printable characters

print(string.capwords("hello world"))         # Hello World

print(string.Template("Hello, $name").substitute(name="Rajesh"))      # Hello, Rajesh
print(string.Template("Hello, $name").safe_substitute())              # Hello, $name

print(string.Formatter().format("Value = {}", 100))                   # Value = 100
print(string.Formatter().parse("Name: {0}, Age: {1}"))                # Iterator of parsed fields


###########COLLECTIONS#################
import collections

print(collections.Counter("banana"))                         # Counter({'a': 3, 'n': 2, 'b': 1})
print(collections.Counter([1, 2, 2, 3, 3, 3]))              # Counter({3: 3, 2: 2, 1: 1})

print(collections.defaultdict(int)["missing"])              # 0
print(collections.defaultdict(list)["items"])               # []

print(collections.deque([1, 2, 3]))                         # deque([1, 2, 3])
print(collections.deque([1, 2, 3], maxlen=5))               # deque([1, 2, 3], maxlen=5)

Point = collections.namedtuple("Point", ["x", "y"])
print(Point(10, 20))                                        # Point(x=10, y=20)
print(Point(10, 20).x)                                      # 10

print(collections.OrderedDict([("a", 1), ("b", 2)]))        # OrderedDict({'a': 1, 'b': 2})

print(collections.ChainMap({"a": 1}, {"b": 2}))             # ChainMap({'a': 1}, {'b': 2})
print(collections.ChainMap({"a": 1}, {"b": 2})["b"])        # 2

print(collections.UserDict({"x": 100}))                     # {'x': 100}
print(collections.UserList([10, 20, 30]))                  # [10, 20, 30]
print(collections.UserString("Hello"))                      # Hello

print(collections.Counter("banana").most_common(2))         # [('a', 3), ('n', 2)]

print(collections.deque([1, 2, 3]).pop())                  # 3
print(collections.deque([1, 2, 3]).popleft())              # 1

print(collections.Counter("abc") + collections.Counter("bcd"))  # Counter({'b': 2, 'c': 2, 'a': 1, 'd': 1})


###########ITERTOOLS#################
import itertools

print(next(itertools.count(10)))                          # 10
print(list(itertools.islice(itertools.count(10), 5)))     # [10, 11, 12, 13, 14]

print(list(itertools.islice(itertools.cycle(["A", "B", "C"]), 7)))  # ['A', 'B', 'C', 'A', 'B', 'C', 'A']
print(list(itertools.repeat("Hello", 3)))                 # ['Hello', 'Hello', 'Hello']

print(list(itertools.accumulate([1, 2, 3, 4])))           # [1, 3, 6, 10]
print(list(itertools.chain([1, 2], [3, 4])))             # [1, 2, 3, 4]
print(list(itertools.compress("ABCDE", [1, 0, 1, 0, 1]))) # ['A', 'C', 'E']

print(list(itertools.dropwhile(lambda x: x < 3, [1, 2, 3, 4, 1])))  # [3, 4, 1]
print(list(itertools.takewhile(lambda x: x < 3, [1, 2, 3, 1])))     # [1, 2]

print(list(itertools.filterfalse(lambda x: x % 2 == 0, [1, 2, 3, 4])))  # [1, 3]
print(list(itertools.starmap(pow, [(2, 3), (3, 2)])) )   # [8, 9]

print(list(itertools.groupby("AAABBBCC")))               # Group iterators
print(list(itertools.islice(range(10), 2, 8, 2)))        # [2, 4, 6]

print(list(itertools.pairwise([10, 20, 30, 40])))        # [(10, 20), (20, 30), (30, 40)]

print(list(itertools.product([1, 2], ["A", "B"])))       # [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]
print(list(itertools.permutations([1, 2, 3], 2)))        # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
print(list(itertools.combinations([1, 2, 3], 2)))        # [(1, 2), (1, 3), (2, 3)]
print(list(itertools.combinations_with_replacement([1, 2], 2)))  # [(1, 1), (1, 2), (2, 2)]

print(list(itertools.zip_longest([1, 2], ["A"], fillvalue="X")))  # [(1, 'A'), (2, 'X')]

print(list(itertools.batched([1, 2, 3, 4, 5], 2)))       # [(1, 2), (3, 4), (5,)]


###########FUNCTOOLS#################
import functools

print(functools.reduce(lambda x, y: x + y, [1, 2, 3, 4]))           # 10
print(functools.reduce(lambda x, y: x * y, [1, 2, 3, 4]))           # 24

print(functools.partial(pow, 2)(5))                                 # 32
print(functools.partial(int, base=2)("1010"))                       # 10

print(functools.cmp_to_key(lambda a, b: a - b))                     # Key wrapper object
print(sorted([5, 2, 9, 1], key=functools.cmp_to_key(lambda a, b: a - b)))  # [1, 2, 5, 9]

@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))                                                # 55

class Person:
    @functools.cached_property
    def full_name(self):
        return "Rajesh Kumar"

print(Person().full_name)                                           # Rajesh Kumar

print(functools.total_ordering)                                     # Class decorator
print(functools.wraps(lambda: None))                                # Decorator function

print(functools.singledispatch)                                     # Generic function decorator
print(functools.singledispatchmethod)                               # Generic method decorator


###########OPERATOR#################
import operator

print(operator.add(10, 5))                   # 15
print(operator.sub(10, 5))                   # 5
print(operator.mul(10, 5))                   # 50
print(operator.truediv(10, 5))               # 2.0
print(operator.floordiv(10, 3))              # 3
print(operator.mod(10, 3))                   # 1
print(operator.pow(2, 3))                    # 8

print(operator.neg(10))                      # -10
print(operator.pos(-10))                     # -10
print(operator.abs(-10))                     # 10
print(operator.invert(5))                    # -6

print(operator.eq(10, 10))                   # True
print(operator.ne(10, 5))                    # True
print(operator.gt(10, 5))                    # True
print(operator.ge(10, 10))                   # True
print(operator.lt(5, 10))                    # True
print(operator.le(5, 5))                     # True

print(operator.and_(6, 3))                   # 2
print(operator.or_(6, 3))                    # 7
print(operator.xor(6, 3))                    # 5
print(operator.lshift(5, 1))                 # 10
print(operator.rshift(5, 1))                 # 2

print(operator.concat("Hello ", "Python"))   # Hello Python
print(operator.contains([10, 20, 30], 20))   # True
print(operator.countOf([1, 2, 2, 3], 2))     # 2
print(operator.indexOf([10, 20, 30], 20))    # 1

print(operator.getitem([10, 20, 30], 1))     # 20
print(operator.setitem([1, 2, 3], 1, 99))    # None (modifies list in place)
print(operator.delitem([1, 2, 3], 1))        # None (modifies list in place)

print(operator.itemgetter(1)(["A", "B", "C"]))  # B

person = {"name": "Rajesh", "age": 30}
print(operator.itemgetter("name")(person))   # Rajesh

class Employee:
    def __init__(self):
        self.name = "Rajesh"
        self.salary = 50000

print(operator.attrgetter("name")(Employee()))   # Rajesh
print(operator.attrgetter("salary")(Employee())) # 50000

print(operator.methodcaller("upper")("python"))  # PYTHON

print(operator.truth([1, 2, 3]))             # True
print(operator.not_([]))                     # True

print(operator.is_(None, None))              # True
print(operator.is_not(10, 20))               # True



'''
'''
'''import random
area=random.randint(50,250)
print(area)
if area > 200:
    print("35 people are in the plot")
elif area>150:
    print("25 people are in the plot")
else:
    print("8 people are in plot")'''

'''for i in range(2,15,4):
   print(i)'''

'''n = 2
n1 = (n*n+2)
n2 = (n*n1-2)
n3 = (n2+2)
print(n)
print(n1)
print(n2)
print(n3)'''

'''i = 1
while i <= 100:
    print(i)
    i += 4.5'''
'''
import random
size = int(input())
members = random.sample([1,2,3,4,5,6,7,8,9,10], 4)
for i in range(10):
    print(members)'''
 
'''import random
i=0
while i<11:
    l=random.randint(1,20)
    b=random.randint(1,20)
    print(l,b,l,b)
    i+=1   ''''''