def simplify_path(path):
    stack = []
    directories = path.split("/")
    for dir in directories: 
        if dir == "." or not dir: 
            continue 
        elif dir == "..": 
            if stack: 
                stack.pop()
        else: 
            stack.append(dir)
    return "/" + "/".join(stack)


# Nghiên cứu lại - Dùng Quy Hoạch Động 
