def solution(name):
    n = len(name)

    # 상하 이동 비용
    vertical = 0
    for c in name:
        diff = ord(c) - ord('A')
        vertical += min(diff, 26 - diff)

    # 좌우 이동 비용
    horizontal = n - 1

    for i in range(n):
        next_idx = i + 1

        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1

        horizontal = min(
            horizontal,
            2 * i + n - next_idx,
            i + 2 * (n - next_idx)
        )

    return vertical + horizontal