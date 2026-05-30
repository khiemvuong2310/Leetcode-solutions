public class Solution {
    public bool IsPalindrome(int x) {
         if(x<0) return false;
        var s = x.ToString();
        for(int i=0; i < s.Length / 2; i++)
        {
            if(s[i] != s[s.Length - 1 - i]) return false;
        }
        return true;
    }
}