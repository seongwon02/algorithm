def solution(orders, course):
    answer = []

    def dfs(order, target, idx, path):
        if len(path) == target:
            menu = "".join(path)
            menu_count[menu] = menu_count.get(menu, 0) + 1
            return

        for i in range(idx, len(order)):
            path.append(order[i])
            dfs(order, target, i + 1, path)
            path.pop()

    for target in course:
        menu_count = {}

        for order in orders:
            order = sorted(order)
            dfs(order, target, 0, [])

        max_count = 0
        for cnt in menu_count.values():
            if cnt >= 2:
                max_count = max(max_count, cnt)

        if max_count >= 2:
            for menu, cnt in menu_count.items():
                if cnt == max_count:
                    answer.append(menu)

    answer.sort()
    return answer