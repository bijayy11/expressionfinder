from math import isqrt

def find_expression(input_set, target):
    # Step 1: Check for perfect roots by iterating over possible roots
    remaining = sorted(input_set, reverse=True)
    root = None
    power = None
    for p in range(2, len(remaining) + 2):
        candidate_root = round(target ** (1 / p))
        if candidate_root ** p == target:
            root = candidate_root
            power = p
            break

    if root is None:
        return "Target is not a perfect power."

    # Step 2: Find factors of the root using the remaining numbers
    factors = []
    for num in remaining:
        if root % num == 0:
            quotient = root // num
            if quotient in remaining:
                factors.append(num)
                factors.append(quotient)
                remaining.remove(num)
                if quotient in remaining:
                    remaining.remove(quotient)
                break

    if len(factors) != 2:
        # If factors are not directly found, further decompose
        for num in remaining:
            if root % num == 0:
                quotient = root // num
                for inner_num in remaining:
                    if quotient % inner_num == 0:
                        next_factor = quotient // inner_num
                        if inner_num in remaining and next_factor in remaining:
                            factors.append(num)
                            factors.append(inner_num)
                            factors.append(next_factor)
                            if num in remaining:
                                remaining.remove(num)
                            if inner_num in remaining:
                                remaining.remove(inner_num)
                            if next_factor in remaining:
                                remaining.remove(next_factor)
                            break
                if len(factors) == 3:
                    break

    if not factors:
        return "No valid decomposition found."

    # Step 3: Construct the expression
    factor_expr = f"{factors[0]} * {factors[1]}"
    if len(factors) > 2:
        # Decompose the conflicting digit using addition or subtraction from remaining digits
        for a in remaining:
            for b in remaining:
                if a - b == factors[2] or a + b == factors[2]:
                    operator = "-" if a - b == factors[2] else "+"
                    factor_expr += f" * ({a} {operator} {b})"
                    remaining.remove(a)
                    remaining.remove(b)
                    break
            if len(remaining) < 2:
                break

    expression = f"({factor_expr})^{power}"
    return expression

# Input from user
input_set = set(map(int, input("Enter a set of integers (separated by spaces): ").split()))
target = int(input("Enter the target number: "))

# Run the function
result = find_expression(input_set, target)

# Output the result
print(f"Expression that results to {target} is { result}")