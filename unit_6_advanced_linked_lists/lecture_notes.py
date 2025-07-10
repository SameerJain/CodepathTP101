Write a function to find the middle node of a singly linked list. If the list has an even number of nodes, return the second middle node.

Examples:
Input: head = [1, 2, 3, 4, 5]
Output: Node with value 3
Input: head = [1, 2, 3, 4, 5, 6]
Output: Node with value 4

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
Examples:
Input: s = "leetcode"
Output: 0
Input: s = "loveleetcode"
Output: 2
Input: s = "aabb"
Output: -1

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.



Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.