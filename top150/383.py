class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ran_lst = list(ransomNote)
        mag_lst = list(magazine)
        for i in range(len(ransomNote)):
            if ran_lst[i] in mag_lst:
                mag_lst.remove(ran_lst[i])
            else:
                return False
        return True
        # print(ransomNote, magazine)
        # ransomNote = sorted(ransomNote)
        # magazine = sorted(magazine)
        # print(ransomNote, magazine)

        # print(ransomNote in magazine)

if __name__ == "__main__":
    ransomNote = "aab"
    magazine = "baa"
    a = Solution()
    ans = a.canConstruct(ransomNote, magazine)
    print(ans)