

def restore_ip_address(s):
    result = []
    if len(s) < 3 or len(s) > 12:
        return result

    def backtrack(start, path):
        # if enough 4 part or reach the length s
        if len(path) == 4 and start == len(s):
            result.append(".".join(path))
            return

        if len(path) == 4 or start == len(s):
            return

        for length in range(1, 4):
            if start + length > len(s):  # Tránh lỗi IndexError
                break
            part = s[start : start + length]

            # check condition
            if (part.startswith("0") and len(part) > 1) or int(part) > 255:
                continue
            backtrack(start + length, path + [part])

    backtrack(0, [])
    return result
