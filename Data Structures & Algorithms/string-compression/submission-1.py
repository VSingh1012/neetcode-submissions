class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i, k = 0, 0 # i is read, k is write

        while i < n:
            chars[k] = chars[i]
            k += 1
            j = i + 1
            while j < n and chars[j] == chars[i]:
                j += 1

            count = j - i
            
            if count > 1:
                string = str(count)
                for x in range(len(string)):
                    chars[k] = string[x] 
                    k += 1

            i = j 
        
        return k

            
            

            



