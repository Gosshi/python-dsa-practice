# 新しい問題: 幅優先探索（BFS）を使った最短経路探索
# 問題文
# 2次元グリッド（迷路）が与えられたとき、開始地点から終了地点までの最短経路の長さを求める関数を実装してください。
# 移動可能なセルは 0 で表され、障害物は 1 で表されます。開始地点と終了地点は必ず 0 です。

# 制約
# グリッドのサイズは m×n で、1≤m,n≤100
# 開始地点と終了地点は常に 0（移動可能セル）であると仮定します。
# 経路が存在しない場合は -1 を返します。
from typing import List, Tuple


def shortest_path(grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> int:
    """
    2次元グリッド上での最短経路の長さを計算する関数。

    Args:
    grid (list[list[int]]): 迷路を表す2次元リスト（0: 移動可能, 1: 障害物）
    start (tuple[int, int]): 開始地点の座標 (row, col)
    end (tuple[int, int]): 終了地点の座標 (row, col)

    Returns:
    int: 最短経路の長さ。経路が存在しない場合は -1 を返す。
    """

    grid_size_m = len(grid)
    grid_size_n = len(grid[0])

    # キューを初期化し、スタート地点と距離0を格納
    queue = [(start[0], start[1], 0)]

    # 訪問済みリストを初期化
    visited = set()
    visited.add((start[0], start[1]))

    while queue:
        current_row, current_col, current_distance = queue.pop(0)

        if (current_row, current_col) == end:
            return current_distance

        # 上下左右の方向に移動（移動方向は固定）
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            next_row = current_row + dr
            next_col = current_col + dc

            # gridの範囲内かつ、移動先が0かつ、移動先が未訪問の場合
            if 0 <= next_row < grid_size_m and 0 <= next_col < grid_size_n \
                    and grid[next_row][next_col] == 0 and (next_row, next_col) not in visited:
                # 探索の順序を管理
                #
                # キューに探索するべきノードを順番に追加します。
                # 追加された順に取り出して処理するため、開始地点に近い順番で探索が行われます。
                #
                # キューに追加することで、「今処理している層の次に探索すべき層」を管理できます。
                # これにより、開始地点からの距離が近い順に探索されます。
                queue.append((next_row, next_col, current_distance + 1))

                # 訪問済みリストに追加することで、後戻りを防ぐ
                visited.add((next_row, next_col))

    return -1


if __name__ == "__main__":
    grid = [
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]
    ]
    start = (0, 0)
    end = (3, 3)

    print(shortest_path(grid, start, end))
