class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        return_list = []
        sorted_word_indices = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            sorted_word_indices[sorted_word] = []
    
        for index, value in enumerate(strs):
            value = "".join(sorted(value))
            list_indices = sorted_word_indices.get(value) 
            list_indices.append(index)

        for key in sorted_word_indices.keys():
            key = "".join(sorted(key))
            unique_word_list = []
            
            for index in sorted_word_indices.get(key, "Error!"):
                unique_word_list.append(strs[index])

            return_list.append(unique_word_list)

        
    
        return return_list



