"""
Reversing the List: The slice b[::-1] creates a new list that is the reverse of b. 
The [:] notation is used to assign this reversed list back to b, effectively modifying b in place.
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:

        s[:] = s[::-1]
