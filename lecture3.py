import math

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
print(math.sqrt(144))