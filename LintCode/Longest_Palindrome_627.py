def longestPalindrome(s):
    # write your code here
    if len(s) == 1:
        return 1
    
    length = 0
    my_hash_table = {}
    for c in s:
        if c in my_hash_table:
            my_hash_table[c] += 1
        else:
            my_hash_table[c] = 1
    
    for k, v in my_hash_table.items():
        if v % 2 == 0: 
            length += v
            my_hash_table[k] -= v
        elif v // 2 > 0:
            length += (v // 2) * 2
            my_hash_table[k] -= (v // 2) * 2
    
    for v in my_hash_table.values():
        if v == 1:
            length += 1
            break

    print(my_hash_table)
    return length

print(longestPalindrome('abccccdddd'))

