## Solution Explanation

The array is divided into two equal halves:
- First half: `[x1, x2, ..., xn]`
- Second half: `[y1, y2, ..., yn]`

We iterate from index `0` to `n - 1` and:
- Pick one element from the first half
- Pick one element from the second half
- Append both to the result array

This produces the required shuffled order.

---

## Python Solution

```python
class Solution(object):
    def shuffle(self, nums, n):
        first = nums[:n]
        second = nums[n:]
        result = []

        for i in range(n):
            result += [first[i], second[i]]

        return result
