#19.Write a Program to Create a Class in which
#One Method Accepts a String from the User and Another Prints it



class PrintString:

    def __init__(self):
        pass

    def get_msg(self):
        print ("%s"%self.msg)

    def set_msg(self):
        msg = raw_input("Enter String to set :-")
        self.msg = msg



p = PrintString()
p.set_msg()
p.get_msg()
