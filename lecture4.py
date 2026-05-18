'''import datetime
print(datetime.date.today())
# Returns the current local date.

print(datetime.datetime.now())
# Returns the current local date and time.

print(datetime.datetime.utcnow())
# Returns the current UTC date and time.
# UTC = Coordinated Universal Time.

print(datetime.time(14, 30, 45))
# Creates a time object with hour, minute, and second.

print(datetime.date(2026, 5, 16))
# Creates a date object with year, month, and day.

print(datetime.datetime(2026, 5, 16, 10, 30, 0))
# Creates a datetime object with date and time.

print(datetime.timedelta(days=5))
# Represents a duration of 5 days.
# Used for date/time calculations.

print(datetime.timedelta(hours=2, minutes=30))
# Represents a duration of 2 hours and 30 minutes.

print(datetime.date.today().year)
# Returns the current year.

print(datetime.date.today().month)
# Returns the current month.

print(datetime.date.today().day)
# Returns the current day.

print(datetime.datetime.now().hour)
# Returns the current hour.

print(datetime.datetime.now().minute)
# Returns the current minute.

print(datetime.datetime.now().second)
# Returns the current second.

print(datetime.datetime.now().strftime("%Y-%m-%d"))
# Formats date/time into a string.
# %Y = year, %m = month, %d = day

print(datetime.datetime.now().strftime("%d/%m/%Y"))
# Formats date as DD/MM/YYYY.

print(datetime.datetime.now().strftime("%I:%M %p"))
# Formats time in 12-hour format.
# %I = hour, %M = minute, %p = AM/PM

print(datetime.datetime.strptime("2026-05-16", "%Y-%m-%d"))
# Converts a string into a datetime object.
# String must match the given format.

print(datetime.date.today() + datetime.timedelta(days=7))
# Adds 7 days to the current date.

print(datetime.date.today() - datetime.timedelta(days=7))
# Subtracts 7 days from the current date.

print(datetime.datetime.now().weekday())
# Returns the weekday number.
# Monday = 0, Sunday = 6

print(datetime.datetime.now().isoweekday())
# Returns the weekday number using ISO format.
# Monday = 1, Sunday = 7

print(datetime.date.today().isoformat())
# Returns date in ISO format (YYYY-MM-DD).

print(datetime.datetime.now().timestamp())
# Returns Unix timestamp.
# Number of seconds since Jan 1, 1970.

print(datetime.datetime.min)
# Smallest supported datetime value.

print(datetime.datetime.max)
# Largest supported datetime value.

print(datetime.date.min)
# Smallest supported date value.

print(datetime.date.max)
# Largest supported date value.

print(datetime.time.min)
# Smallest supported time value.

print(datetime.time.max)
# Largest supported time value.'''


'''import copy
print(copy.copy([1, 2, 3])) # Creates a shallow copy of the list.

print(copy.deepcopy([[1, 2], [3, 4]])) # Creates a deep copy of the nested list.

original = [1, 2, 3]
print(copy.copy(original)) # Creates a shallow copy of the original list.

nested = [[1, 2], [3, 4]]
print(copy.deepcopy(nested))# Creates a deep copy of the nested list and inner lists.

person = {"name": "Rajesh", "age": 30}
print(copy.copy(person))# Creates a shallow copy of the dictionary.

employee = {
    "name": "Rajesh",
    "skills": ["Python", "Revit API"]
}
print(copy.deepcopy(employee))# Creates a deep copy of the dictionary and nested list.

number = 100
print(copy.copy(number))# Copies an integer value.

text = "Hello Python"
print(copy.copy(text)) # Copies a string value.

tuple_data = (1, 2, 3)
print(copy.copy(tuple_data)) # Copies a tuple.

set_data = {10, 20, 30}
print(copy.copy(set_data)) # Creates a shallow copy of the set.'''


'''import time
# Current Unix timestamp
print(time.time())     
# Current date and time as a string                       
print(time.ctime()) 
# Thu Jan  1 05:30:00 1970 (depending on timezone)                          
print(time.ctime(0))  
# Current date and time as a string                        
print(time.asctime()) 
# Current local time as struct_time                        
print(time.localtime())
# Current UTC time as struct_time                       
print(time.gmtime())                          

print(time.localtime().tm_year)    # year
print(time.localtime().tm_mon)     # month
print(time.localtime().tm_mday)    # day
print(time.localtime().tm_hour)    # hour
print(time.localtime().tm_min)     # minute
print(time.localtime().tm_sec)     # second

print(time.strftime("%Y-%m-%d"))        # date in YYYY-MM-DD format
print(time.strftime("%d/%m/%Y"))        # date in DD/MM/YYYY format
print(time.strftime("%I:%M:%S %p"))     #time in 12-hour format
print(time.strftime("%A"))              #weekday name
print(time.strftime("%B"))              #month name

# Convert string to struct_time
print(time.strptime("2026-05-16", "%Y-%m-%d"))  
# Convert tuple to timestamp
print(time.mktime((2026, 5, 16, 10, 30, 0, 0, 0, -1)))  
# High-resolution performance timer
print(time.perf_counter())    
# CPU processing time                
print(time.process_time())    
 # Monotonic clock value                
print(time.monotonic())       
# CPU time used by current thread               
print(time.thread_time())                     

# Information about time()
print(time.get_clock_info("time"))           
# Information about perf_counter()
print(time.get_clock_info("perf_counter"))    

print(time.tzname)         # Local timezone names
print(time.timezone)       # Offset from UTC in seconds
print(time.altzone)        # DST offset from UTC in seconds
print(time.daylight)      # 1 if DST is defined, else 0
print(time.sleep(1)) # Pauses execution for 1 second (returns None)
'''


from pathlib import Path
print(Path("sample.txt"))  
# Creates a path object for the file "sample.txt".
print(Path.cwd())  
# Returns the current working directory.
print(Path.home())  
# Returns the user's home directory.
print(Path("sample.txt").name)  
# Returns the file name.
print(Path("sample.txt").stem)  
# Returns the file name without extension.
print(Path("sample.txt").suffix)  
# Returns the file extension.
print(Path("sample.txt").suffixes)  
# Returns all suffixes/extensions as a list.
print(Path("folder/sample.txt").parent)  
# Returns the parent folder of the file.
print(Path("folder") / "sample.txt")  
# Joins folder and file path using / operator.
print(Path("folder/sample.txt").parts)  
# Returns path parts as a tuple.
print(Path("sample.txt").exists())  
# Checks whether the file exists.
print(Path("sample.txt").is_file())  
# Checks whether the path is a file.
print(Path("my_folder").is_dir())  
# Checks whether the path is a directory.
print(Path("sample.txt").absolute())  
# Returns the absolute path.
print(Path("sample.txt").resolve())  
# Returns the resolved absolute path.
print(Path("sample.txt").with_name("new.txt"))  
# Changes the file name.
print(Path("sample.txt").with_suffix(".csv"))  
# Changes the file extension.
print(Path("folder/sample.txt").relative_to("folder"))  
# Returns the relative path from the given folder.
print(list(Path(".").iterdir()))  
# Lists all items in the current directory.
print(list(Path(".").glob("*.txt")))  
# Finds all .txt files in the current directory.
print(list(Path(".").rglob("*.py")))  
# Finds all .py files recursively.
# Make sure sample.txt exists before reading
Path("sample.txt").touch()
print(Path("sample.txt").read_text())  
# Reads file content as text.
print(Path("sample.txt").read_bytes())  
# Reads file content as bytes.
print(Path("output.txt").write_text("Hello"))  
# Writes text into a file.
print(Path("output.bin").write_bytes(b"ABC"))  
# Writes bytes into a binary file.
Path("new_folder").mkdir(exist_ok=True)
print("Folder created")
# Creates a new directory.
print(Path("output.txt").rename("renamed.txt"))  
# Renames the file.
Path("renamed.txt").unlink(missing_ok=True)
print("File deleted")
# Deletes the file.
Path("new_folder").rmdir()
print("Folder removed")
# Removes an empty directory.
print(Path("sample.txt").stat())  
# Returns file information like size and timestamps.
print(Path("sample.txt").touch())  
# Creates the file if it does not exist.
