"""
[위상 정렬 - Topological Sort]

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]

힌트:
- 진입 차수(in-degree) 사용
- 진입 차수가 0인 정점부터 시작
- 큐 사용
"""

from collections import deque

def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
    
    Returns:
        위상 정렬 순서
    """
    # TODO: 그래프와 진입 차수 초기화
    in_degree = 0
    graph_for_degree = { x : 0 for edge in edges for x in edge}
    graph = { x : [] for edge in edges for x in edge}
    queue = deque()
    # TODO: 그래프 구성 및 진입 차수 계산
    for u, v in edges : 
        graph_for_degree[v] += 1
        graph[u].append(v)
    # TODO: 진입 차수가 0인 정점들을 큐에 추가
    for i in graph_for_degree.keys():
        if graph_for_degree[i] == 0: 
            queue.append(i)
    # print("queue before while :", queue)

    result = []

    
    # TODO: 큐가 빌 때까지 반복

    while (len(queue)):
        cursor = queue.popleft()
        # print("queue in while: ", queue)
        result.append(cursor)
        for i in graph[cursor] :
            if graph_for_degree[i] > 0: graph_for_degree[i] -= 1
        for i in graph_for_degree.keys():
            if graph_for_degree[i] == 0 and i not in result and i not in queue: # 탐색했고, 탐색중인 것 제외
                queue.append(i)

    return result

# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]
    
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    # topological_sort(vertices, edges)
    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")

    vertices = 7
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
        (2, 3),  # 2 → 3
        (2, 4),  # 2 → 4
        (3, 5),  # 3 → 5
        (4, 5),  # 4 → 5
        (5, 6),  # 5 → 6
    ]

    # print("=== 위상 정렬 테스트 1 ===")
    # print("과목 관계:")
    # print("  0 → 1 → 3 → 5 → 6")
    # print("  0 → 2 → 3")
    # print("       ↘ 4 → 5")
    print()

    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")

    vertices = 8
    edges = [
        (0, 3),
        (1, 3),
        (1, 4),
        (2, 4),
        (2, 5),
        (3, 6),
        (4, 6),
        (4, 7),
        (5, 7),
    ]

    # print("=== 위상 정렬 테스트 2 ===")
    # print("과목 관계:")
    # print("  0 → 3 → 6")
    # print("  1 → 3 → 6")
    # print("  1 → 4 → 6")
    # print("       ↘ 7")
    # print("  2 → 4 → 6")
    # print("       ↘ 5 → 7")
    print()

    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")

    vertices = 10
    edges = [
        (0, 1),
        (0, 2),
        (1, 3),
        (1, 4),
        (2, 4),
        (2, 5),
        (3, 6),
        (4, 6),
        (4, 7),
        (5, 7),
        (6, 8),
        (7, 8),
        (8, 9),
    ]
    print()

    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")

    vertices = 8
    edges = [
        (0, 1),
        (0, 2),
        (1, 3),
        (2, 4),
        (3, 5),
    ]
    print()

    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")