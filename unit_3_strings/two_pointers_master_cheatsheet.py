"""
TWO POINTERS TECHNIQUE - COMPLETE CHEATSHEET
============================================

What is Two Pointers?
- Algorithmic technique using two pointers/indices to traverse data structures
- Pointers move toward each other or in same direction
- Usually reduces O(n²) to O(n) time complexity with O(1) space

When to Use:
- Sorted arrays
- Finding pairs/triplets with specific sums
- Palindrome checking
- Removing duplicates
- Sliding window problems
- Merging sorted arrays

Key Patterns:
1. Opposite Direction (Convergent) - pointers start at ends, move toward center
2. Same Direction (Fast & Slow) - both pointers move same direction, different speeds
3. Sliding Window - maintain window of elements

Time Complexity: Usually O(n)
Space Complexity: O(1)
"""

# ===== PATTERN 1: OPPOSITE DIRECTION (CONVERGENT) =====

def two_sum_sorted(arr, target):
    """
    Find two numbers in sorted array that sum to target.
    Pattern: Opposite direction pointers
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum
    
    return [-1, -1]


def three_sum(nums):
    """
    Find all unique triplets that sum to zero.
    Pattern: Fixed element + two pointers
    Time: O(n²), Space: O(1)
    """
    nums.sort()  # Must sort first!
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates for first element
        if i > 0 and nums[i] == nums[i-1]:
            continue
            
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for second and third elements
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result


def is_palindrome(s):
    """
    Check if string is palindrome (ignoring non-alphanumeric).
    Pattern: Opposite direction with filtering
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1
            
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
    
    return True


def max_area(height):
    """
    Container with most water problem.
    Pattern: Opposite direction, move pointer with smaller height
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        width = right - left
        water = width * min(height[left], height[right])
        max_water = max(max_water, water)
        
        # Always move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water


def trap_rain_water(height):
    """
    Trapping rain water problem.
    Pattern: Opposite direction with max tracking
    Time: O(n), Space: O(1)
    """
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    
    return water


# ===== PATTERN 2: SAME DIRECTION (FAST & SLOW) =====

def remove_duplicates(arr):
    """
    Remove duplicates from sorted array in-place.
    Pattern: Slow pointer for unique elements, fast for scanning
    Time: O(n), Space: O(1)
    """
    if not arr:
        return 0
    
    slow = 0  # Points to last unique element
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    
    return slow + 1  # Length of unique array


def move_zeros(nums):
    """
    Move all zeros to end while maintaining relative order.
    Pattern: Slow for non-zero position, fast for scanning
    Time: O(n), Space: O(1)
    """
    slow = 0  # Position for next non-zero element
    
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


def remove_element(nums, val):
    """
    Remove all instances of val in-place.
    Pattern: Slow for keeping elements, fast for scanning
    Time: O(n), Space: O(1)
    """
    slow = 0
    
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    
    return slow


def merge_sorted_arrays(nums1, m, nums2, n):
    """
    Merge nums2 into nums1 (nums1 has enough space).
    Pattern: Two pointers from end to avoid overwriting
    Time: O(m+n), Space: O(1)
    """
    p1, p2 = m - 1, n - 1  # Last elements in original arrays
    p = m + n - 1  # Last position in nums1
    
    # Merge from end to beginning
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    # Add remaining elements from nums2
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1


# ===== PATTERN 3: SLIDING WINDOW =====

def max_sum_subarray_fixed_size(arr, k):
    """
    Find maximum sum of subarray of size k.
    Pattern: Fixed size sliding window
    Time: O(n), Space: O(1)
    """
    if len(arr) < k:
        return 0
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide window: remove first, add new
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum


def longest_substring_without_repeating(s):
    """
    Find length of longest substring without repeating characters.
    Pattern: Variable size sliding window with set
    Time: O(n), Space: O(min(m,n)) where m is charset size
    """
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Shrink window until no repeating character
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length


def min_window_substring(s, t):
    """
    Find minimum window substring containing all characters of t.
    Pattern: Variable sliding window with frequency map
    Time: O(|s| + |t|), Space: O(|s| + |t|)
    """
    if not s or not t:
        return ""
    
    # Count characters in t
    dict_t = {}
    for char in t:
        dict_t[char] = dict_t.get(char, 0) + 1
    
    required = len(dict_t)  # Unique characters in t
    left = right = 0
    formed = 0  # How many unique chars in current window have desired frequency
    
    window_counts = {}
    ans = float("inf"), None, None  # (window length, left, right)
    
    while right < len(s):
        # Add character from right
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1
        
        # Contract window until it ceases to be 'desirable'
        while left <= right and formed == required:
            char = s[left]
            
            # Save smallest window
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            # Remove from left
            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1
            
            left += 1
        
        right += 1
    
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]


# ===== TEMPLATES FOR DIFFERENT PATTERNS =====

def opposite_direction_template(arr):
    """Template for opposite direction problems."""
    left, right = 0, len(arr) - 1
    
    while left < right:
        # Process current state
        if True:  # Replace with your condition
            return "result"
        elif True:  # Replace with condition for moving left
            left += 1
        else:
            right -= 1
    
    return "default_result"


def same_direction_template(arr):
    """Template for same direction problems."""
    slow = 0
    
    for fast in range(len(arr)):
        if True:  # Replace with your condition
            # Process arr[fast]
            arr[slow] = arr[fast]
            slow += 1
    
    return slow


def sliding_window_template(arr, k):
    """Template for fixed size sliding window."""
    if len(arr) < k:
        return 0
    
    # Initialize window
    window_sum = sum(arr[:k])
    result = window_sum
    
    # Slide window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        result = max(result, window_sum)  # Replace with your optimization
    
    return result


# ===== UTILITY FUNCTIONS FOR TESTING =====

def test_two_pointers():
    """Test all two pointer functions with example inputs."""
    
    print("=== TESTING TWO POINTERS FUNCTIONS ===\n")
    
    # Test two_sum_sorted
    arr = [2, 7, 11, 15]
    target = 9
    result = two_sum_sorted(arr, target)
    print(f"Two Sum: {arr}, target={target} -> {result}")
    
    # Test three_sum
    nums = [-1, 0, 1, 2, -1, -4]
    result = three_sum(nums)
    print(f"Three Sum: {nums} -> {result}")
    
    # Test palindrome
    s = "A man a plan a canal Panama"
    result = is_palindrome(s)
    print(f"Is Palindrome: '{s}' -> {result}")
    
    # Test max area
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = max_area(height)
    print(f"Max Area: {height} -> {result}")
    
    # Test remove duplicates
    arr = [1, 1, 2, 2, 3, 4, 4, 5]
    original = arr.copy()
    length = remove_duplicates(arr)
    print(f"Remove Duplicates: {original} -> {arr[:length]}")
    
    # Test move zeros
    nums = [0, 1, 0, 3, 12]
    original = nums.copy()
    move_zeros(nums)
    print(f"Move Zeros: {original} -> {nums}")
    
    # Test sliding window
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    result = max_sum_subarray_fixed_size(arr, k)
    print(f"Max Sum Subarray (k={k}): {arr} -> {result}")
    
    # Test longest substring
    s = "abcabcbb"
    result = longest_substring_without_repeating(s)
    print(f"Longest Substring: '{s}' -> {result}")


# ===== DECISION TREE COMMENTS =====
"""
DECISION TREE: When to Use Which Pattern

Is the array sorted?
├── Yes
│   ├── Looking for a pair/sum? → Opposite Direction
│   ├── Removing duplicates? → Same Direction (Fast/Slow)
│   └── Merging arrays? → Opposite Direction (from ends)
└── No
    ├── Need a window of elements? → Sliding Window
    ├── Fast/slow traversal needed? → Same Direction
    └── Checking palindrome? → Opposite Direction

COMMON PITFALLS:
- Forgetting to handle duplicates in sum problems
- Not checking bounds before accessing array elements
- Moving wrong pointer in opposite direction problems
- Infinite loops when pointers don't move

TIPS:
- Always sort array first for sum problems
- Use while loops for skipping duplicates
- Consider edge cases (empty array, single element)
- Draw diagrams to visualize pointer movement
- Test with simple examples first

COMPLEXITY ANALYSIS:
Pattern              | Time | Space | Use Case
--------------------|------|-------|----------
Opposite Direction  | O(n) | O(1)  | Two Sum, Palindrome
Same Direction      | O(n) | O(1)  | Remove Duplicates, Move Zeros
Sliding Window      | O(n) | O(1)  | Subarray Problems

PRACTICE PROBLEMS BY DIFFICULTY:

Easy:
- Two Sum II (sorted array)
- Valid Palindrome
- Remove Duplicates from Sorted Array
- Move Zeros

Medium:
- 3Sum
- Container With Most Water
- Longest Substring Without Repeating Characters
- Sort Colors

Hard:
- Trapping Rain Water
- Minimum Window Substring
- Sliding Window Maximum
"""

if __name__ == "__main__":
    test_two_pointers()