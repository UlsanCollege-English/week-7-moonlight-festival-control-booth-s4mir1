"""
Week 7: Moonlight Festival Control Booth

Use Python's heapq module to solve priority queue problems.
"""

from __future__ import annotations

import heapq


def order_festival_alerts(alerts: list[tuple[int, str]]) -> list[str]:
    heap = alerts.copy()
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(len(heap))]


def order_festival_alerts_stable(alerts: list[tuple[int, str]]) -> list[str]:
    heap = [(priority, i, title) for i, (priority, title) in enumerate(alerts)]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[2] for _ in range(len(heap))]


def top_k_festival_alerts(alerts: list[tuple[int, str]], k: int) -> list[str]:
    if k <= 0:
        return []
    return [title for _, title in heapq.nsmallest(k, alerts)]


def peek_next_festival_alert(alerts: list[tuple[int, str]]) -> str | None:
    if not alerts:
        return None
    heap = alerts.copy()
    heapq.heapify(heap)
    return heap[0][1]