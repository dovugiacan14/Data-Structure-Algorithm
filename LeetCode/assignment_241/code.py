def diffways_to_compute(expression):
    memo = {}

    def compute(expr):
        if expr in memo:
            return memo[expr]
        
        results = []
        for i, char in enumerate(expr):
            if char in '+-*':
                left = compute(expr[:i])
                right = compute(expr[i+1:])

                for l in left:
                    for r in right:
                        if char == "+": 
                            results.append(l + r)
                        elif char == "-":
                            results.append(l - r)
                        elif char == "*":
                            results.append(l * r)
        if not results:
            results = [int(expr)]
        memo[expr] = results
    return compute(expression)
