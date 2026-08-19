class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i, j = 0, 0
        compressed_str = []


        while i < n:
            i += 1
            if i - j == 1: # check if we have a count of 1, so we can add the designated character
                compressed_str.append(chars[j])
            if i == n or chars[i] != chars[j]:
                count = i - j
                if count != 1:
                    if count > 9: # to account for the numbers greater than 10
                        for c in str(count): 
                            compressed_str.append(c)
                    else:
                        compressed_str.append(str(count))
                j = i
        

        k = len(compressed_str)
        for x in range(k):
            chars[x] = compressed_str[x] # modifying the first k elements of chars array (naive approach)

        return k


            


