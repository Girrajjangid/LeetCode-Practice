class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        # Initialize frequency arrays for s1 and for the window in s2
        s1_freq = [0] * 26
        window_freq = [0] * 26
        # Populate the frequency array for s1
        for char in s1:
            s1_freq[ord(char) - ord('a')] += 1
        # Sliding window to check frequencies in s2
        for i in range(len(s2)):
            # Add the current character in s2 to the window frequency
            window_freq[ord(s2[i]) - ord('a')] += 1
            # If the window size exceeds the size of s1, remove the character that is sliding out
            if i >= len(s1):
                window_freq[ord(s2[i - len(s1)]) - ord('a')] -= 1
                # Compare the frequency arrays of the current window and s1
            if s1_freq == window_freq:
                return True
        return False