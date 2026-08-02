"""type_casting.py"""

# Integer to float and string
value_int = 42
value_float = float(value_int)
value_str = str(value_int)

print("int -> float:", value_float, type(value_float))
print("int -> str:", value_str, type(value_str))

# Float to int and boolean
value_float = 3.14
value_int = int(value_float)
value_bool = bool(value_float)

print("float -> int:", value_int, type(value_int))
print("float -> bool:", value_bool, type(value_bool))

# String to int and float (when valid)
value_str = "123"
value_int = int(value_str)
value_float = float(value_str)

print("str -> int:", value_int, type(value_int))
print("str -> float:", value_float, type(value_float))

# Sequence conversions
value_list = [1, 2, 3]
value_tuple = tuple(value_list)
value_set = set(value_list)

print("list -> tuple:", value_tuple, type(value_tuple))
print("list -> set:", value_set, type(value_set))

# Boolean casting examples
print("bool(0):", bool(0))
print("bool(1):", bool(1))
print("bool(""):", bool(""))
print("bool('hello'):", bool("hello"))

