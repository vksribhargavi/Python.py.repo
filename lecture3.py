"""import math

# Rounding Functions
print(math.ceil(4.2))
print(math.floor(4.8))
print(math.trunc(4.9))

# Combinatorics
print(math.comb(5, 2))
print(math.perm(5, 2))
print(math.factorial(5))

# Sign & Absolute Functions
print(math.copysign(5, -3))
print(math.fabs(-10.5))

# Distance Functions
print(math.dist([0, 0], [3, 4]))
print(math.hypot(3, 4))

# Exponential & Logarithmic Functions
print(math.exp(2))
print(math.expm1(2))
print(math.log(8, 2))
print(math.log10(1000))
print(math.log2(8))
print(math.log1p(1))

# Fraction & Remainder Functions
print(math.fmod(10, 3))
print(math.remainder(10, 3))
print(math.modf(3.75))

# Floating Point Utilities
print(math.frexp(8))
print(math.ldexp(0.5, 4))
print(math.nextafter(1.0, 2.0))
print(math.ulp(1.0))

# Sum & Product
print(math.fsum([0.1, 0.2, 0.3]))
print(math.prod([2, 3, 4]))

# Number Theory
print(math.gcd(12, 18))
print(math.lcm(12, 18))
print(math.isqrt(10))

# Gamma Functions
print(math.gamma(5))
print(math.lgamma(5))

# Checking Functions
print(math.isclose(0.1 + 0.2, 0.3))
print(math.isfinite(100))
print(math.isinf(math.inf))
print(math.isnan(math.nan))

# Angle Conversion
print(math.radians(180))
print(math.degrees(math.pi))

# Trigonometric Functions
print(math.sin(math.radians(90)))
print(math.cos(math.radians(0)))
print(math.tan(math.radians(45)))

# Inverse Trigonometric Functions
print(math.asin(1))
print(math.acos(1))
print(math.atan(1))
print(math.atan2(1, 1))

# Hyperbolic Functions
print(math.sinh(1))
print(math.cosh(1))
print(math.tanh(1))

# Inverse Hyperbolic Functions
print(math.asinh(1))
print(math.acosh(2))
print(math.atanh(0.5))

# Square Root
print(math.sqrt(144))"""


import random
 # Random float between 0.0 and 1.0
print(random.random())                 
# Random integer between 1 and 10
print(random.randint(1, 10))           
# Random odd number between 1 and 19
print(random.randrange(1, 20, 2))   
# Random float between 1.5 and 5.5
print(random.uniform(1.5, 5.5))        
# Random item from the list
print(random.choice(["Red", "Blue", "Green"]))  
# Shuffle the list items randomly
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)                
print(numbers)
# Random 3 unique items
print(random.sample([10, 20, 30, 40, 50], 3))  
# Random 5 items with replacement
print(random.choices(["A", "B", "C"], k=5))     
# Random 4-bit integer
print(random.getrandbits(4))           
# Random float using triangular distribution
print(random.triangular(1, 10, 5))   
# Random float using beta distribution
print(random.betavariate(2, 5))       
# Random float using exponential distribution
print(random.expovariate(1.5))        
# Random float using gamma distribution
print(random.gammavariate(2, 3))      
# Random float using Gaussian distribution
print(random.gauss(0, 1))             
# Random float using log-normal distribution
print(random.lognormvariate(0, 1))    
# Random float using normal distribution
print(random.normalvariate(0, 1))     
# Random float using Pareto distribution
print(random.paretovariate(3))        
# Random float using Von Mises distribution
print(random.vonmisesvariate(0, 1))   
# Random float using Weibull distribution
print(random.weibullvariate(1, 2))    
# Set seed value for same random results
random.seed(10)                      
# Same random integer every time with same seed
print(random.randint(1, 100))         