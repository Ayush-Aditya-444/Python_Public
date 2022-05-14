def count_substring(string, sub_string):
    # Find a string in Python - Hacker Rank Solution START
    count = 0
    for i in range(len(string)-len(sub_string)+1):
        if (string[i:i+len(sub_string)] == sub_string):
            count += 1
    return count
    # Find a string in Python - HackerRank Solution END
if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print(count)