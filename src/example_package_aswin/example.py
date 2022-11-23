def display_symbols():
    print(
        """
    plus : +
    minus : -
    star : *
    slash : /
    percentage : %
    """
    )

class plus:
    def add(a,b):
        assert type(a)==type(b)==int or type(a)==type(b)==float, "your input must be <class int> or <class float>"
        """
        this will add your numbers
        """
        return a+b
    
    def concat(a:str,b:str):
        assert type(a)==type(b)==str, "your input must be <type str>"
        """
        this will concat your string
        """
        return a+b

class minus:
    def sub(a,b):
        """
        this will subtract your numbers
        """
        return a-b

class star:
    def mul(a,b):
        assert type(a)==type(b)==int or type(a)==type(b)==float, "your input must be <class int> or <class float>"
        """
        this will multiply your numbers
        """
        return a*b
    def duplicate(*args):
        """
        this will duplicate your numbers
        """
        assert 0<len(args)<3,"There should be only 2 arguments MAX"
        if(len(args)==1):
            assert type(args[0]==str),"Parameter should be a <class str>"
            return(args[0]*2)

        else:
            assert (type(args[0])==str and type(args[1])==int) or (type(args[0])==int and type(args[1])==str), "one of the parameters must be <class str> and other must be <class int>"
            return args[0]*args[1]

class slash:
    def div(a,b):
        """
        this will divide your numbers
        """
        return a/b

class percentage:
    def mod(a,b):
        """
        This will get the remainder of the two numbers
        """
        return a%b
