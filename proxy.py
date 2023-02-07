
class Printer(object):

    def print(self):
        print('printer is now printing')
        return True

class PrinterProxy(object):

    def __init__(self, user, password):
        self.printer = Printer()
        self.user = user 
        self.password = password

    def print(self):
        if self.user !=  'admin' or self.password != '123456':
            print('You have no permission')
            return None
        return self.printer.print() 


if __name__ == '__main__':
    printer = PrinterProxy('admin', '123456')
    printer.print()
    printer = PrinterProxy('guest', '123456')
    printer.print()
    

