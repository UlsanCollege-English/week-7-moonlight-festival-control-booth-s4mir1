# Week 7 – Moonlight Festival Control Booth

## Overview

This project implements a priority-queue–based alert dispatcher for a festival control booth using Python's built-in `heapq` module.

---

## Functions

| Function | Description |
|---|---|
| `order_festival_alerts` | Returns all alert titles sorted by priority (lowest number first). |
| `order_festival_alerts_stable` | Same as above, but ties are broken by original insertion order. |
| `top_k_festival_alerts` | Returns the titles of the *k* most urgent alerts. |
| `peek_next_festival_alert` | Returns the most urgent title without modifying the input. |

---

## Running the tests

```bash
pytest -q
```

All edge cases (empty input, `k ≤ 0`, `k > len`, duplicate priorities, mutation checks) are covered in `tests/test_challenges.py`.

---

## Complexity Analysis

### `order_festival_alerts`

| | Complexity | Explanation |
|---|---|---|
| Time | **O(n log n)** | `heapify` runs in O(n). Each of the *n* `heappop` calls costs O(log n), giving O(n log n) total. |
| Space | **O(n)** | A full copy of the input list is stored as the heap. The result list is also O(n). |

### `order_festival_alerts_stable`

| | Complexity | Explanation |
|---|---|---|
| Time | **O(n log n)** | Same heap mechanics as above. Building the enriched `(priority, index, title)` tuples is O(n). |
| Space | **O(n)** | The heap stores one three-tuple per alert. |

The insertion index acts as a guaranteed unique tiebreaker, so Python never needs to compare title strings — this also avoids potential `TypeError` if two titles were non-comparable objects.

### `top_k_festival_alerts`

| | Complexity | Explanation |
|---|---|---|
| Time | **O(n log k)** | `heapq.nsmallest(k, alerts)` maintains an internal min-heap of size *k*. Each of the *n* elements is pushed/compared against this heap in O(log k). |
| Space | **O(k)** | Only the top-k heap is kept in memory; the input is read once. |

When `k` is much smaller than `n` this is significantly better than a full sort (O(n log n)). When `k ≈ n`, Python's implementation falls back to a full sort automatically.

### `peek_next_festival_alert`

| | Complexity | Explanation |
|---|---|---|
| Time | **O(n)** | Copying the list is O(n); `heapify` is O(n). Reading `heap[0]` is O(1). |
| Space | **O(n)** | A full copy is needed to avoid mutating the caller's list. |

---

## Why a heap is the right data structure here

A festival control booth receives alerts continuously and needs to **always serve the highest-priority item next**. This is the canonical use case for a **priority queue**:

* **Insertion of a new alert** costs O(log n) — fast enough to keep up with a live stream of events.
* **Extracting the most urgent alert** also costs O(log n) — much cheaper than re-sorting the full list (O(n log n)) on every new arrival.
* **A plain sorted list** would require O(n) shifts on every insertion to maintain order, making it unsuitable for a high-throughput booth.
* **Python's `heapq`** is a min-heap, which maps directly to "smallest priority number = most urgent", so no transformation is needed.

In short: heaps give O(log n) insert *and* O(log n) extract-min, which is optimal for a dynamic priority queue where alerts arrive and are resolved in real time.