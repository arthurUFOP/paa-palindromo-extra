the_string = "1s2u3b4i5no7n8i9b-u4s"
m = [["" for _ in the_string] for _ in the_string]

def reset_m(size):
    global m
    m = [["" for _ in range(size)] for _ in range(size)]

def max_length_string(a, b):
    if len(a) > len(b):
        return a
    return b

def rec_palindrome(x, i, j):
    if i>=j:
        return x[i]
    
    if x[i] == x[j]:
        return x[i] + rec_palindrome(x, i+1, j-1) + x[j]
    
    return max_length_string(rec_palindrome(x, i+1, j), rec_palindrome(x, i, j-1))

def memo_palindrome(x, i, j):
    if i>=j:
        return x[i]
    
    if x[i] == x[j]:
        if m[i+1][j-1] != "":
            return x[i] + m[i+1][j-1] + x[j]
        else:
            m[i+1][j-1] = memo_palindrome(x, i+1, j-1)
            return x[i] + m[i+1][j-1] + x[j]
    
    if m[i+1][j] == "":
        m[i+1][j] = memo_palindrome(x, i+1, j)
    
    if m[i][j-1] == "":
        m[i][j-1] = memo_palindrome(x, i, j-1)
    
    return max_length_string(m[i+1][j], m[i][j-1])

def din_palindrome(x):
    n = len(x)

    M = [["" for _ in x] for _ in x]
    for i in range(1, n):
        M[i][i] = x[i]

    for i in range(1, n):
        for j in range(n-i):
            if x[j] == x[i+j]:
                M[j][i+j] = x[j] + M[j+1][i+j-1] + x[i+j]
            else:
                M[j][i+j] = max_length_string(M[j+1][i+j], M[j][i+j-1])
    
    return M[0][len(x)-1]

if __name__ == "__main__":
    print(rec_palindrome(the_string, 0, len(the_string) - 1))
    print(memo_palindrome(the_string, 0, len(the_string) - 1))
    print(din_palindrome(the_string))