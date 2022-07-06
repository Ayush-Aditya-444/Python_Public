for i in range ( int ( input () ) ) :
    arr , ind = [] , -1
    exp , res = input () , ""
    for el in range ( len ( exp ) ) :
        if exp [ el ].isalpha () :
            res += exp [ el ]
        elif exp [ el ] == ')' :
            while arr [ ind ] != '(' :
                top = arr.pop ( ind )
                res += top
                ind -= 1
            arr.pop ( ind )
            ind -= 1
        else :
            arr.append ( exp [ el ] )
            ind += 1
    print ( res )