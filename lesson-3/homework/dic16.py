nested_dict = {'a': 1, 'b': {'c': 2}}
has_nested = any(isinstance(v, dict) for v in nested_dict.values())
print("16. Check for Nested Dictionaries:", has_nested)