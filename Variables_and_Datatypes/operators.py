"""
+ ,addition
-, subtraction
*, multiplication
/, division
//, integer division (gives whole number as output always)
%, modulus (for remainder)
**, exponentiation (for power)


Logical operators:
and, returns True if both conditions are True
or, returns True if at least one condition is True
not, reverses the result of a condition

Relational/Comparison operators:
==, equal to
!=, not equal to
>, greater than
<, less than
>=, greater than or equal to
<=, less than or equal to

Assignment operators:
=, assigns a value
+=, adds and assigns a value
-=, subtracts and assigns a value
*=, multiplies and assigns a value
/=, divides and assigns a value
//=, integer divides and assigns a value
%=, takes the remainder and assigns a value
**=, raises to a power and assigns a value


"""

# EXAMPLE:
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Integer division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)


# LOGICAL OPERATORS:
x = 10
y = 5

print("Logical AND:", x > 0 and y > 0)
print("Logical OR:", x < 0 or y > 0)
print("Logical NOT:", not (x < y))


# RELATIONAL/COMPARISON OPERATORS:
print("Equal to:", x == y)
print("Not equal to:", x != y)
print("Greater than:", x > y)
print("Less than:", x < y)
print("Greater than or equal to:", x >= y)
print("Less than or equal to:", x <= y)


# ASSIGNMENT OPERATORS:
number = 10
print("Assignment:", number)

number += 5
print("Addition assignment:", number)
number -= 3
print("Subtraction assignment:", number)
number *= 2
print("Multiplication assignment:", number)
number /= 4
print("Division assignment:", number)
number //= 2
print("Integer division assignment:", number)
number %= 3
print("Modulus assignment:", number)
number **= 2
print("Exponentiation assignment:", number)

"""OPERATOR PRECEDENCE
NOT>AND>OR"""

"""not True and False or True

#in this case, the NOT operator will be evaluated first, then the AND operator and finally the OR operator

#therefore it then becomes:
(not True) and False or True
= False and False or True
= False or True
= True"""  #since the OR operator is used, the final result will be True if any of the two operands is True