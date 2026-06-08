from typing import Optional
from collections import defaultdict, deque



def can_finish(numCourses, prerequisites):
    """Quy về bài toán đồ thị.
    - Nếu đồ thị có chu trình thì bạn không thể hoàn thành khóa học -> False
    - Nếu đồ thị không có chun trình thì bạn có thể hoàn thành khóa học -> True
    """
    # Build graph: edges from b -> a (b must be before a)
    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[b].append(a)

    visited = [0] * numCourses

    def dfs(course):
        if visited[course] == 1:
            return False
        if visited[course] == 2:  # already visited
            return True

        visited[course] = 1  # mark as visiting
        for neighbor in graph[course]:
            if not dfs(neighbor):
                return False
        visited[course] = 2  # mask as visited
        return True

    for course in range(numCourses):
        if not dfs(course):
            return False
    return True
