"""
DIVIDE AND CONQUER ALGORITHMS - COMPLETE CHEATSHEET
===================================================

What is Divide and Conquer?
An algorithmic paradigm that solves problems by:
1. DIVIDE: Break problem into smaller subproblems of same type
2. CONQUER: Solve subproblems recursively (base case solves directly)
3. COMBINE: Merge solutions to get final answer

Key Characteristics:
- Recursive structure
- Subproblems are independent
- Often leads to O(n log n) time complexity
- Uses call stack (space complexity consideration)

When to Use Divide and Conquer:
✓ Problem can be broken into similar subproblems
✓ Subproblems are independent (no overlap)
✓ Optimal substructure exists
✓ Want to improve brute force O(n²) to O(n log n)

Common Applications:
- Sorting: Merge Sort, Quick Sort
- Searching: Binary Search
- Tree operations: Tree traversal, height calculation
- Mathematical: Fast exponentiation, matrix multiplication
- Geometric: Closest pair of points, convex hull
- Array problems: Maximum subarray, inversion counting
"""

import math
import random
from typing import List, Tuple, Optional, Any

# ===== FUNDAMENTAL DIVIDE AND CONQUER TEMPLATE =====

def divide_and_conquer_template(problem, threshold=1):
    """
    General template for divide and conquer algorithms.
    
    Args:
        problem: The problem instance to solve
        threshold: Minimum size for direct solution (base case)
    """
    # BASE CASE: If problem is small enough, solve directly
    if len(problem) <= threshold:
        return solve_directly(problem)
    
    # DIVIDE: Split problem into subproblems
    subproblems = divide(problem)
    
    # CONQUER: Recursively solve each subproblem
    sub_solutions = []
    for subproblem in subproblems:
        sub_solutions.append(divide_and_conquer_template(subproblem, threshold))
    
    # COMBINE: Merge solutions to get final answer
    return combine(sub_solutions)


def solve_directly(problem):
    """Base case: solve small problems directly."""
    pass


def divide(problem):
    """Split problem into smaller subproblems."""
    pass


def combine(sub_solutions):
    """Merge subproblem solutions into final answer."""
    pass


# ===== CLASSIC ALGORITHMS =====

# ===== BINARY SEARCH =====

def binary_search(arr, target):
    """
    Classic binary search implementation.
    Time: O(log n), Space: O(log n) - recursive calls
    """
    def binary_search_helper(left, right):
        # BASE CASE: Target not found
        if left > right:
            return -1
        
        # DIVIDE: Find middle point
        mid = left + (right - left) // 2
        
        # Check if we found target
        if arr[mid] == target:
            return mid
        
        # CONQUER: Search in appropriate half
        elif arr[mid] > target:
            return binary_search_helper(left, mid - 1)
        else:
            return binary_search_helper(mid + 1, right)
    
    return binary_search_helper(0, len(arr) - 1)


def binary_search_iterative(arr, target):
    """
    Iterative binary search (more space efficient).
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1


def binary_search_leftmost(arr, target):
    """
    Find leftmost occurrence of target.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return result


def binary_search_rightmost(arr, target):
    """
    Find rightmost occurrence of target.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return result


# ===== MERGE SORT =====

def merge_sort(arr):
    """
    Classic merge sort implementation.
    Time: O(n log n), Space: O(n)
    """
    # BASE CASE: Array of length 1 or empty is already sorted
    if len(arr) <= 1:
        return arr
    
    # DIVIDE: Split array in half
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # CONQUER: Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # COMBINE: Merge sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    Merge two sorted arrays into one sorted array.
    Time: O(n), Space: O(n)
    """
    result = []
    i = j = 0
    
    # Compare elements from both arrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def merge_sort_inplace(arr, left=None, right=None):
    """
    In-place merge sort to reduce space complexity.
    Time: O(n log n), Space: O(log n) - recursive calls only
    """
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    
    # BASE CASE
    if left >= right:
        return
    
    # DIVIDE
    mid = left + (right - left) // 2
    
    # CONQUER
    merge_sort_inplace(arr, left, mid)
    merge_sort_inplace(arr, mid + 1, right)
    
    # COMBINE
    merge_inplace(arr, left, mid, right)


def merge_inplace(arr, left, mid, right):
    """Helper function for in-place merging."""
    # Create temporary arrays
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


# ===== QUICK SORT =====

def quick_sort(arr):
    """
    Quick sort implementation.
    Time: O(n log n) average, O(n²) worst, Space: O(log n)
    """
    # BASE CASE
    if len(arr) <= 1:
        return arr
    
    # DIVIDE: Choose pivot and partition
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # CONQUER & COMBINE: Recursively sort and concatenate
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr, low=0, high=None):
    """
    In-place quick sort implementation.
    Time: O(n log n) average, O(n²) worst, Space: O(log n)
    """
    if high is None:
        high = len(arr) - 1
    
    # BASE CASE
    if low < high:
        # DIVIDE: Partition and get pivot index
        pivot_index = partition(arr, low, high)
        
        # CONQUER: Recursively sort both sides
        quick_sort_inplace(arr, low, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, high)


def partition(arr, low, high):
    """Partition function for quick sort."""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_randomized(arr, low=0, high=None):
    """
    Randomized quick sort to avoid worst case.
    Time: O(n log n) expected, Space: O(log n)
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Randomize pivot choice
        random_index = random.randint(low, high)
        arr[random_index], arr[high] = arr[high], arr[random_index]
        
        pivot_index = partition(arr, low, high)
        quick_sort_randomized(arr, low, pivot_index - 1)
        quick_sort_randomized(arr, pivot_index + 1, high)


# ===== ADVANCED DIVIDE AND CONQUER ALGORITHMS =====

# ===== MAXIMUM SUBARRAY (KADANE'S ALGORITHM ENHANCED) =====

def max_subarray_divide_conquer(arr):
    """
    Find maximum sum subarray using divide and conquer.
    Time: O(n log n), Space: O(log n)
    """
    def max_subarray_helper(arr, left, right):
        # BASE CASE
        if left == right:
            return arr[left]
        
        # DIVIDE
        mid = left + (right - left) // 2
        
        # CONQUER: Find max in left and right halves
        left_max = max_subarray_helper(arr, left, mid)
        right_max = max_subarray_helper(arr, mid + 1, right)
        
        # COMBINE: Find max crossing subarray
        left_sum = float('-inf')
        current_sum = 0
        for i in range(mid, left - 1, -1):
            current_sum += arr[i]
            left_sum = max(left_sum, current_sum)
        
        right_sum = float('-inf')
        current_sum = 0
        for i in range(mid + 1, right + 1):
            current_sum += arr[i]
            right_sum = max(right_sum, current_sum)
        
        cross_sum = left_sum + right_sum
        
        return max(left_max, right_max, cross_sum)
    
    return max_subarray_helper(arr, 0, len(arr) - 1)


# ===== CLOSEST PAIR OF POINTS =====

def closest_pair_points(points):
    """
    Find closest pair of points using divide and conquer.
    Time: O(n log n), Space: O(n)
    """
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
    def closest_pair_rec(px, py):
        n = len(px)
        
        # BASE CASE: Use brute force for small arrays
        if n <= 3:
            min_dist = float('inf')
            for i in range(n):
                for j in range(i + 1, n):
                    min_dist = min(min_dist, distance(px[i], px[j]))
            return min_dist
        
        # DIVIDE
        mid = n // 2
        midpoint = px[mid]
        
        pyl = [point for point in py if point[0] <= midpoint[0]]
        pyr = [point for point in py if point[0] > midpoint[0]]
        
        # CONQUER
        dl = closest_pair_rec(px[:mid], pyl)
        dr = closest_pair_rec(px[mid:], pyr)
        
        # COMBINE
        d = min(dl, dr)
        
        # Check points near the dividing line
        strip = [point for point in py if abs(point[0] - midpoint[0]) < d]
        
        min_strip = d
        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and (strip[j][1] - strip[i][1]) < min_strip:
                min_strip = min(min_strip, distance(strip[i], strip[j]))
                j += 1
        
        return min(d, min_strip)
    
    # Sort points by x and y coordinates
    px = sorted(points, key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])
    
    return closest_pair_rec(px, py)


# ===== MATRIX MULTIPLICATION (STRASSEN'S ALGORITHM) =====

def matrix_multiply_strassen(A, B):
    """
    Matrix multiplication using Strassen's algorithm.
    Time: O(n^2.807), Space: O(n²)
    """
    n = len(A)
    
    # BASE CASE: 1x1 matrix
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    # Ensure matrices are even-sized (pad if necessary)
    if n % 2 == 1:
        A = pad_matrix(A)
        B = pad_matrix(B)
        n += 1
    
    # DIVIDE: Split matrices into quarters
    mid = n // 2
    
    a11 = get_submatrix(A, 0, 0, mid)
    a12 = get_submatrix(A, 0, mid, mid)
    a21 = get_submatrix(A, mid, 0, mid)
    a22 = get_submatrix(A, mid, mid, mid)
    
    b11 = get_submatrix(B, 0, 0, mid)
    b12 = get_submatrix(B, 0, mid, mid)
    b21 = get_submatrix(B, mid, 0, mid)
    b22 = get_submatrix(B, mid, mid, mid)
    
    # CONQUER: Compute 7 products recursively
    m1 = matrix_multiply_strassen(matrix_add(a11, a22), matrix_add(b11, b22))
    m2 = matrix_multiply_strassen(matrix_add(a21, a22), b11)
    m3 = matrix_multiply_strassen(a11, matrix_subtract(b12, b22))
    m4 = matrix_multiply_strassen(a22, matrix_subtract(b21, b11))
    m5 = matrix_multiply_strassen(matrix_add(a11, a12), b22)
    m6 = matrix_multiply_strassen(matrix_subtract(a21, a11), matrix_add(b11, b12))
    m7 = matrix_multiply_strassen(matrix_subtract(a12, a22), matrix_add(b21, b22))
    
    # COMBINE: Compute result quarters
    c11 = matrix_add(matrix_subtract(matrix_add(m1, m4), m5), m7)
    c12 = matrix_add(m3, m5)
    c21 = matrix_add(m2, m4)
    c22 = matrix_add(matrix_subtract(matrix_add(m1, m3), m2), m6)
    
    # Combine quarters into result matrix
    return combine_quarters(c11, c12, c21, c22)


def get_submatrix(matrix, row, col, size):
    """Extract submatrix of given size starting at (row, col)."""
    return [[matrix[row + i][col + j] for j in range(size)] for i in range(size)]


def matrix_add(A, B):
    """Add two matrices."""
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]


def matrix_subtract(A, B):
    """Subtract two matrices."""
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]


def pad_matrix(matrix):
    """Pad matrix to make it even-sized."""
    n = len(matrix)
    padded = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            padded[i][j] = matrix[i][j]
    return padded


def combine_quarters(c11, c12, c21, c22):
    """Combine four quarter matrices into one matrix."""
    n = len(c11)
    result = [[0] * (2 * n) for _ in range(2 * n)]
    
    for i in range(n):
        for j in range(n):
            result[i][j] = c11[i][j]
            result[i][j + n] = c12[i][j]
            result[i + n][j] = c21[i][j]
            result[i + n][j + n] = c22[i][j]
    
    return result


# ===== FAST EXPONENTIATION =====

def fast_power(base, exp):
    """
    Fast exponentiation using divide and conquer.
    Time: O(log n), Space: O(log n)
    """
    # BASE CASE
    if exp == 0:
        return 1
    if exp == 1:
        return base
    
    # DIVIDE: Split exponent in half
    if exp % 2 == 0:
        # Even exponent: base^exp = (base^(exp/2))^2
        half_power = fast_power(base, exp // 2)
        return half_power * half_power
    else:
        # Odd exponent: base^exp = base * base^(exp-1)
        return base * fast_power(base, exp - 1)


def fast_power_iterative(base, exp):
    """
    Iterative fast exponentiation.
    Time: O(log n), Space: O(1)
    """
    result = 1
    current_power = base
    
    while exp > 0:
        if exp % 2 == 1:
            result *= current_power
        current_power *= current_power
        exp //= 2
    
    return result


# ===== COUNTING INVERSIONS =====

def count_inversions(arr):
    """
    Count number of inversions in array using divide and conquer.
    Time: O(n log n), Space: O(n)
    """
    def merge_and_count(arr, temp, left, mid, right):
        i, j, k = left, mid + 1, left
        inv_count = 0
        
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                # All elements from i to mid are greater than arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1
        
        # Copy remaining elements
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
        
        # Copy back to original array
        for i in range(left, right + 1):
            arr[i] = temp[i]
        
        return inv_count
    
    def merge_sort_and_count(arr, temp, left, right):
        inv_count = 0
        if left < right:
            mid = left + (right - left) // 2
            
            inv_count += merge_sort_and_count(arr, temp, left, mid)
            inv_count += merge_sort_and_count(arr, temp, mid + 1, right)
            inv_count += merge_and_count(arr, temp, left, mid, right)
        
        return inv_count
    
    temp = [0] * len(arr)
    return merge_sort_and_count(arr.copy(), temp, 0, len(arr) - 1)


# ===== FINDING KTH LARGEST ELEMENT =====

def find_kth_largest(nums, k):
    """
    Find kth largest element using quickselect (divide and conquer).
    Time: O(n) average, O(n²) worst, Space: O(log n)
    """
    def quickselect(nums, left, right, k):
        if left == right:
            return nums[left]
        
        # Random pivot for better average performance
        pivot_index = random.randint(left, right)
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        
        # Partition around pivot
        pivot_index = partition_desc(nums, left, right)
        
        if k == pivot_index:
            return nums[k]
        elif k < pivot_index:
            return quickselect(nums, left, pivot_index - 1, k)
        else:
            return quickselect(nums, pivot_index + 1, right, k)
    
    return quickselect(nums, 0, len(nums) - 1, k - 1)


def partition_desc(nums, left, right):
    """Partition array in descending order."""
    pivot = nums[right]
    i = left
    
    for j in range(left, right):
        if nums[j] >= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    
    nums[i], nums[right] = nums[right], nums[i]
    return i


# ===== TREE-RELATED DIVIDE AND CONQUER =====

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_height(root):
    """
    Calculate height of binary tree using divide and conquer.
    Time: O(n), Space: O(h) where h is height
    """
    # BASE CASE
    if not root:
        return 0
    
    # DIVIDE & CONQUER
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    
    # COMBINE
    return 1 + max(left_height, right_height)


def count_nodes(root):
    """
    Count nodes in binary tree.
    Time: O(n), Space: O(h)
    """
    # BASE CASE
    if not root:
        return 0
    
    # DIVIDE & CONQUER
    left_count = count_nodes(root.left)
    right_count = count_nodes(root.right)
    
    # COMBINE
    return 1 + left_count + right_count


def tree_sum(root):
    """
    Calculate sum of all values in binary tree.
    Time: O(n), Space: O(h)
    """
    # BASE CASE
    if not root:
        return 0
    
    # DIVIDE & CONQUER
    left_sum = tree_sum(root.left)
    right_sum = tree_sum(root.right)
    
    # COMBINE
    return root.val + left_sum + right_sum


def is_balanced(root):
    """
    Check if binary tree is height-balanced.
    Time: O(n), Space: O(h)
    """
    def check_balance(node):
        if not node:
            return True, 0
        
        left_balanced, left_height = check_balance(node.left)
        if not left_balanced:
            return False, 0
        
        right_balanced, right_height = check_balance(node.right)
        if not right_balanced:
            return False, 0
        
        balanced = abs(left_height - right_height) <= 1
        height = 1 + max(left_height, right_height)
        
        return balanced, height
    
    balanced, _ = check_balance(root)
    return balanced


# ===== UTILITY FUNCTIONS =====

def is_sorted(arr):
    """Check if array is sorted."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def generate_random_array(size, min_val=1, max_val=100):
    """Generate random array for testing."""
    return [random.randint(min_val, max_val) for _ in range(size)]


def benchmark_algorithm(algorithm, *args, iterations=1000):
    """Benchmark an algorithm."""
    import time
    
    start_time = time.time()
    for _ in range(iterations):
        algorithm(*args)
    end_time = time.time()
    
    return (end_time - start_time) / iterations


# ===== TEST FUNCTIONS =====

def test_binary_search():
    """Test binary search implementations."""
    print("=== TESTING BINARY SEARCH ===\n")
    
    arr = [1, 2, 4, 4, 4, 6, 8, 10, 15, 20]
    target = 4
    
    print(f"Array: {arr}")
    print(f"Target: {target}")
    print(f"Binary search: {binary_search(arr, target)}")
    print(f"Leftmost occurrence: {binary_search_leftmost(arr, target)}")
    print(f"Rightmost occurrence: {binary_search_rightmost(arr, target)}")
    print()


def test_sorting_algorithms():
    """Test sorting algorithms."""
    print("=== TESTING SORTING ALGORITHMS ===\n")
    
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {arr}")
    
    # Test merge sort
    merge_sorted = merge_sort(arr.copy())
    print(f"Merge sorted: {merge_sorted}")
    
    # Test quick sort
    quick_sorted = quick_sort(arr.copy())
    print(f"Quick sorted: {quick_sorted}")
    
    # Test in-place versions
    arr_copy = arr.copy()
    merge_sort_inplace(arr_copy)
    print(f"In-place merge sorted: {arr_copy}")
    
    arr_copy = arr.copy()
    quick_sort_inplace(arr_copy)
    print(f"In-place quick sorted: {arr_copy}")
    print()


def test_advanced_algorithms():
    """Test advanced divide and conquer algorithms."""
    print("=== TESTING ADVANCED ALGORITHMS ===\n")
    
    # Test maximum subarray
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = max_subarray_divide_conquer(arr)
    print(f"Array: {arr}")
    print(f"Maximum subarray sum: {max_sum}")
    
    # Test fast exponentiation
    base, exp = 3, 10
    result = fast_power(base, exp)
    print(f"{base}^{exp} = {result}")
    
    # Test counting inversions
    arr = [2, 4, 1, 3, 5]
    inversions = count_inversions(arr.copy())
    print(f"Array: {arr}")
    print(f"Number of inversions: {inversions}")
    
    # Test kth largest
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    kth_largest = find_kth_largest(nums.copy(), k)
    print(f"Array: {nums}")
    print(f"{k}th largest element: {kth_largest}")
    print()


def test_tree_algorithms():
    """Test tree-related divide and conquer algorithms."""
    print("=== TESTING TREE ALGORITHMS ===\n")
    
    # Create a sample tree:      1
    #                          /   \
    #                         2     3
    #                        / \
    #                       4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print(f"Tree height: {tree_height(root)}")
    print(f"Node count: {count_nodes(root)}")
    print(f"Tree sum: {tree_sum(root)}")
    print(f"Is balanced: {is_balanced(root)}")
    print()


# ===== COMPLEXITY ANALYSIS =====
"""
DIVIDE AND CONQUER COMPLEXITY ANALYSIS:

Algorithm               | Time Complexity | Space Complexity | Notes
------------------------|-----------------|------------------|------------------
Binary Search           | O(log n)        | O(log n)         | O(1) iterative
Merge Sort              | O(n log n)      | O(n)             | Stable sort
Quick Sort              | O(n log n)*     | O(log n)         | *O(n²) worst
Fast Exponentiation     | O(log n)        | O(log n)         | O(1) iterative
Maximum Subarray        | O(n log n)      | O(log n)         | D&C approach
Closest Pair Points     | O(n log n)      | O(n)             | Geometric problem
Matrix Multiplication   | O(n^2.807)      | O(n²)            | Strassen's algorithm
Counting Inversions     | O(n log n)      | O(n)             | Modified merge sort
Kth Largest (Quickselect)| O(n)*          | O(log n)         | *O(n²) worst
Tree Height             | O(n)            | O(h)             | h = tree height

RECURRENCE RELATIONS:

1. Binary Search: T(n) = T(n/2) + O(1) → O(log n)
2. Merge Sort: T(n) = 2T(n/2) + O(n) → O(n log n)
3. Quick Sort: T(n) = 2T(n/2) + O(n) average → O(n log n)
4. Strassen's: T(n) = 7T(n/2) + O(n²) → O(n^2.807)

MASTER THEOREM:
For recurrence T(n) = aT(n/b) + f(n):

Case 1: f(n) = O(n^c) where c < log_b(a) → T(n) = O(n^log_b(a))
Case 2: f(n) = O(n^c) where c = log_b(a) → T(n) = O(n^c log n)
Case 3: f(n) = O(n^c) where c > log_b(a) → T(n) = O(f(n))

WHEN TO USE DIVIDE AND CONQUER:

✓ Problem can be broken into similar subproblems
✓ Subproblems are independent (no overlapping)
✓ Combining solutions is efficient
✓ Want to improve from O(n²) to O(n log n)

✗ Subproblems overlap (use dynamic programming instead)
✗ Breaking down is more expensive than direct solution
✗ Cannot efficiently combine subproblem solutions

OPTIMIZATION TECHNIQUES:

1. **Iterative Implementation**: Reduce space complexity
2. **Randomization**: Improve average-case performance (quicksort)
3. **Tail Recursion**: Some compilers can optimize
4. **Memoization**: If subproblems overlap (becomes DP)
5. **Threshold Switching**: Use simpler algorithm for small inputs

COMMON PATTERNS:

1. **Split in Half**: Binary search, merge sort
2. **Choose Pivot**: Quick sort, quickselect
3. **Process All Subproblems**: Tree algorithms
4. **Geometric Divide**: Closest pair, convex hull
5. **Mathematical Decomposition**: Fast exponentiation

INTERVIEW TIPS:

1. **Identify the Pattern**: Look for repeated substructure
2. **Define Recurrence**: Write down the recurrence relation
3. **Handle Base Cases**: Always define stopping conditions
4. **Consider Space**: Recursive calls use stack space
5. **Analyze Complexity**: Use Master Theorem when applicable
6. **Test Edge Cases**: Empty inputs, single elements
"""

if __name__ == "__main__":
    test_binary_search()
    test_sorting_algorithms()
    test_advanced_algorithms()
    test_tree_algorithms()
    
    print("=== DIVIDE AND CONQUER SUMMARY ===")
    print("Key Principle: Divide → Conquer → Combine")
    print("Common Complexity: O(n log n) for many algorithms")
    print("Space Consideration: Recursive calls use O(log n) to O(n) space")
    print("Master Theorem: Use to analyze recurrence relations")
    print("Optimization: Consider iterative versions for better space complexity")