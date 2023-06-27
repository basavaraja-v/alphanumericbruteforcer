# Alphanumeric Code Decoding Script
This script decodes an alphanumeric code through a brute-force approach. It generates all possible codes of the specified length and checks them sequentially until the target code is found.

# Usage
1. Run the script using a Python interpreter.
2. Enter the alphanumeric code to decode when prompted.
3. The script will start decoding, providing progress updates periodically.
4. If the target code is found, it will be displayed along with the elapsed time.
5. If the target code is not found, a "Code not found" message will be displayed.

## Optimizations

- The script utilizes multiprocessing to parallelize the code checking process, improving performance by checking codes in batches.
- You can adjust the batch size to optimize the balance between parallelism and resource usage.
- Additional optimizations can be implemented based on specific code constraints, patterns, or pruning techniques.
- Remember to consider the trade-off between optimization and complexity.

## Note
- Large code lengths or search spaces may require significant time and resources.
- Resource limitations can terminate the script prematurely.
- The script serves as a basic demonstration and may not be suitable for complex decoding scenarios.

# Test Case 1:
```
Enter the alphanumeric code to decode: AB
Decoding in progress...
Code found: AB
Elapsed time: 0.04 seconds
```

# Test Case 2:
```
Enter the alphanumeric code to decode: A!B
Decoding in progress...
Code not found.
```