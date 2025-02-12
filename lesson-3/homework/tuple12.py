def second_largest(tpl):
    unique_sorted = sorted(set(tpl), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None

print(second_largest((65,15,24,13,37)))