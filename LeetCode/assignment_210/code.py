from typing import Optional
from collections import defaultdict, deque

def course_schedule_II(numCourses, prerequisites): 
    """
    Main Idea 
        - Mỗi môn học là một đỉnh (node) trong đồ thị 
        - Mỗi quan hệ [a, b] (phải học b trước a) là một cạnh có hướng từ b đến a. 
        - Bài toán trở thành: liệt kê thứ tự topo (topological ordering) của các đỉnh trong đồ thị. 
        - Nếu có chu trình, thì không thể hoàn thành tất cả các môn học, trả về []. 

    Cách giải: 
        B1: Xây dựng đồ thị & đếm số bậc vào (indegree)
        B2: BFS - Topological Sort (Kahn's Algorithm)
            - Tạo một hàng đợi (queue) chứa các môn có indegree = 0 (không có môn nào cần học trước).
            - Lặp: 
                + Lấy môn ra khỏi queue, thêm vào kết quả 
                + Với mỗi môn học phụ thuộc vào nó: giảm indegree, nếu bằng 0 thì cho vào queue. 
            - Cuối cùng, nếu kết quả đủ numCourses, trả về thứ tự đó. Nếu không -> có chu trình -> trả về []
         
    """
    graph = defaultdict(list)
    indegree = [0] * numCourses

    # Build graph & indegree 
    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1 
    
    # Start with nodes with no prerequisites 
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    order = []

    while queue: 
        course = queue.popleft()
        order.append(course)

        for neighbor in graph[course]: 
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0: 
                queue.append(neighbor)
    return order if len(order) == numCourses else []
