def second_smallest(tpl):
    unique_sorted = sorted(set(tpl))
    return unique_sorted[1] if len(unique_sorted) > 1 else None

print(second_smallest((51,25,48,76,89))) 