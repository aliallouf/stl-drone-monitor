# STL Altitude Monitor with RTAMT

This project demonstrates how to use **Signal Temporal Logic (STL)** to monitor drone flight safety requirements. We use the `RTAMT` library to calculate the **robustness** of a temporal requirement against a discrete-time signal.

## The Requirement
We want to ensure that the drone does not stay at a dangerous altitude for too long:
> "If the altitude exceeds 100m, it must return to 100m or less within a 5-second window."

**STL Formula:**
` (alt > 100) -> eventually[0, 5] (alt <= 100) `

## How Robustness Works
STL doesn't just return True or False; it returns a **Robustness Value**:
* **Positive (> 0):** The requirement is satisfied. The value indicates the "distance" to violation.
* **Negative (< 0):** The requirement is violated. The value indicates how far the signal is from being safe.



## Example Results
In our test case, the drone climbs to 110m at $T=4$ and stays there. Because it never returns to $\le 100$ within the 5s window, a violation is triggered.

| Time | Altitude | Robustness | Status |
|------|----------|------------|-----------|
| 0s   | 50.0     | 50.00      | ✅ Safe   |
| 4s   | 110.0    | -10.00     | ❌ VIOLATION |

## Installation
```bash
pip install rtamt
