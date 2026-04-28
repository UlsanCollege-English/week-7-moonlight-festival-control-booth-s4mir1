"""
Week 7: Moonlight Festival Control Booth

Use Python's heapq module to solve priority queue problems.
"""

from __future__ import annotations

import heapq


def order_festival_alerts(alerts: list[tuple[int, str]]) -> list[str]:
    """
    Return alert titles in the order they should be handled.

    Each alert is a tuple:
        (priority, title)

    Smaller priority numbers should be handled first.

    Args:
        alerts: A list of (priority, title) tuples.

    Returns:
        A list of alert titles sorted from most urgent to least urgent.

    Time complexity:  O(n log n) — heapify is O(n), each of the n pops is O(log n).
    Space complexity: O(n) for the copied heap.
    """
    heap = alerts.copy()          # avoid mutating caller's list
    heapq.heapify(heap)           # O(n) in-place min-heap
    result = []
    while heap:
        _, title = heapq.heappop(heap)   # O(log n)
        result.append(title)
    return result


def order_festival_alerts_stable(alerts: list[tuple[int, str]]) -> list[str]:
    """
    Return alert titles in the order they should be handled.

    If two alerts have the same priority, keep the original input order
    (i.e. the sort is stable with respect to insertion position).

    Args:
        alerts: A list of (priority, title) tuples.

    Returns:
        A list of alert titles in stable priority order.

    Time complexity:  O(n log n).
    Space complexity: O(n) for the heap with index entries.
    """
    # Insert a sequential index as a tiebreaker so Python never has to
    # compare the title strings — the index alone breaks every tie.
    heap: list[tuple[int, int, str]] = [
        (priority, i, title) for i, (priority, title) in enumerate(alerts)
    ]
    heapq.heapify(heap)
    result = []
    while heap:
        _, _, title = heapq.heappop(heap)
        result.append(title)
    return result


def top_k_festival_alerts(alerts: list[tuple[int, str]], k: int) -> list[str]:
    """
    Return the titles of the k most urgent alerts.

    Alerts are returned from most urgent (smallest priority number) to
    least urgent within the top-k set.

    Args:
        alerts: A list of (priority, title) tuples.
        k:      Number of alerts to return.

    Returns:
        Up to k alert titles ordered by urgency.
        Returns an empty list when k <= 0 or alerts is empty.

    Time complexity:  O(n log k) — heapq.nsmallest uses a size-k heap internally.
    Space complexity: O(k) for the result heap.
    """
    if k <= 0:
        return []
    # Inject the original index as a tiebreaker so that alerts with the same
    # priority are returned in insertion order (stable).  nsmallest alone does
    # not guarantee this because it may compare title strings arbitrarily when
    # priorities are equal.
    indexed = [(priority, i, title) for i, (priority, title) in enumerate(alerts)]
    return [title for _, _, title in heapq.nsmallest(k, indexed)]


def peek_next_festival_alert(alerts: list[tuple[int, str]]) -> str | None:
    """
    Return the title of the next alert to handle without permanently
    changing the original input.

    Args:
        alerts: A list of (priority, title) tuples.

    Returns:
        The title of the highest-priority alert, or None if the list is empty.

    Time complexity:  O(n) for heapify on the copy.
    Space complexity: O(n) for the copied heap.
    """
    if not alerts:
        return None
    heap = alerts.copy()
    heapq.heapify(heap)
    # After heapify the smallest element is always at index 0 — no pop needed.
    return heap[0][1]