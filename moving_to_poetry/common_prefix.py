def longestCommonPrefix(strs: list) -> str:
        """
        Find the longest common prefix string among an array of strings
        
        Parameters :
        - strs : array of strings (list)
        
        Return 
        - prefix : longest common prefix (str)
        """
        if len(strs) == 0 :
             return None 
        for element in strs :
            if element == '' :
                raise IndexError("Please remove the empty string from the list")
        n = min(map(lambda x : len(x), strs))
        index = 0
        prefix = ""
        for index in range(n) :
            prefix_temp = set()
            for element in strs :
                    prefix_temp.add(element[index])
            if len(prefix_temp) != 1 :
                return prefix 
            prefix += ''.join(prefix_temp)
        return prefix