This is one of the exercises I resolved to apply for an amazon SDE job.

## Instructions
In Amazon's expansive distribution network, there are `n` unique inventory processes, each supported by `robots[i]` robots. These processes are competitive, resulting in clash events every minute between two randomly chosen processes.

The task is to identify which inventory processes have a possibility of surviving until the end in at least one scenario. Return the indices of these processes (in ascending order, 1-indexed) that could potentially emerge as the last surviving process.

### Clash Rules:
- The process with more robots overtakes the one with fewer robots, gaining its robots.
- If both processes have the same number of robots, one process randomly wins and gains the other's robots.

This process repeats until only one inventory process remains.

**Note:** The indices of the inventory processes that need to be returned are **1-based indexed**.

### Example

#### **Input:**
```
n = 5
robots = [1, 6, 2, 7, 2]
```

### **Explanation:**
Assuming **1-based indexing** of the `robots` array:

The robot at index `2` may survive after the following clashes (where `robots[i] = 0` indicates that its robots have been acquired by some other robot):
1. The **2nd** robot acquires the **1st** increasing its total to `6 + 1 = 7`. `robots = [0, 7, 2, 7, 2]`
2. It eliminates the **3rd**, raising its total count of robots to `7 + 2 = 9`. `robots = [0, 9, 0, 7, 2]`
3. It defeats the **4th**, enhancing its total count of robots to `9 + 7 = 16`. `robots = [0, 16, 0, 0, 2]`
4. Finally, it conquers the **5th**, increasing its total robots to `16 + 2 = 18`. `robots = [0, 18, 0, 0, 0]`

The robot at index **4** can also endure after the following clashes:
1. The **4th** robot acquires the **1st** taking its total number of robots to `7 + 1 = 8`. `robots = [0, 6, 2, 8, 2]`
2. Then it surpasses the **3rd**, with its total number of robots ascending to `8 + 2 = 10`. `robots = [0, 6, 0, 10, 2]`
3. Next, it takes over the **2nd**, raising the total number of robots to `10 + 6 = 16`. `robots = [0, 0, 0, 16, 2]`
4. Finally, it overcomes the **5th**, and its total robot count strengthens to `16 + 2 = 18`. `robots = [0, 0, 0, 18, 0]`

Thus, the inventory processes that may continue to operate following the clashes are `[2, 4]`.  
All other processes will be eliminated at some point under all possible scenarios.

#### **Output:**
```
[2, 4]
```

### **Function Description**
Complete the function `fetchProcessIndices`

```python
def fetchProcessIndices(robots: List[int]) -> List[int]:
    pass
```

### **Parameters:**
- `int robots[n]`: an array of integers depicting the number of robots each inventory process controls.

### **Returns:**
- `int[]`: the identifiers of inventory processes in **ascending order** that could endure post clashes in at least one probable scenario.

### **Constraints**
- `1 ≤ n ≤ 2 × 10^5`
- `1 ≤ robots[i] ≤ 10^9`
