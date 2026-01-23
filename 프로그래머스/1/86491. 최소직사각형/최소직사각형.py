def solution(sizes):
    row, col = 0, 0
    for card in sizes:
        
        row = max(min(card[0], card[1]), row)
        col = max(max(card[0], card[1]), col)
    return row*col
