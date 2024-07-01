def main():
    result = []
    while True:
        start = input('Enter the starting letter: ')
        end = input('Enter the starting letter: ')
        if ord(start)>ord(end) or start.isalpha() == False or end.isalpha() == False:
            print("Please make the end letter after the start letter, and both are valid letters")
        else:
            break
    for i in range(ord(start),ord(end)+1):
        result.append(chr(i))
        
    
    

    """
    ########################################
    Code Your Program here
    ########################################
    """

    print(*result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
