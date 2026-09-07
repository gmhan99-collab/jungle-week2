class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        # if len(prerequisites) == 1: return True
        for u, v in prerequisites:
            graph[v].append(u)

        visited = []
        visiting = []
        def dfs(Node):
            if Node in visiting: return False
            if Node in visited: return True

            visiting.append(Node)
            for i in graph[Node]:
                if not dfs(i):
                    return False
            visiting.remove(Node)
            visited.append(Node)
            return True

        for i in range(numCourses):
            if i not in visited and not dfs(i): # Short - Circuit Evaluation
                return False
                
        return True