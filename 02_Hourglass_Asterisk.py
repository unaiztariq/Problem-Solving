def hourglass_steric(hourglass:int):

    def odd_allowed(hourglass):
        try:
            if hourglass%2 == 0:
                print("Input should be odd.")
                return False
            return True
        except Exception as e :
            print(str(e) +". It should be an integer.")

    if not all([isinstance(hourglass,int),odd_allowed(hourglass)]):
        return

    outerspace=1
    innerspace=hourglass-4
    steric= "*"

    for i in range(hourglass):
        if i ==0 or i == hourglass-1:
            pattern = "*"*hourglass
            
        elif i==(hourglass//2):
            pattern= (" "*outerspace)+steric
            outerspace -=1
            innerspace +=2
            
        elif i<hourglass//2:
            pattern= (" "*outerspace)+steric+ (" "*innerspace)+steric
            outerspace +=1
            innerspace -=2
            
        elif i>hourglass//2:
            pattern= (" "*outerspace)+steric+ (" "*innerspace)+steric
            outerspace -=1
            innerspace +=2

        print(pattern)


hourglass_steric(19)
