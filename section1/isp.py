"""
interface segregation principle

don't want to stick too many elements into an interface
because forcing clients to implement too many methods
that they do not need


Programming Notes:
Abstract classes are classes that contain one or more abstract methods.
An abstract method is a method that is declared, but contains no implementation.
Abstract classes cannot be instantiated, and require
subclasses to provide implementations for the abstract methods.
"""
from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError()

    def fax(self, document):
        raise NotImplementedError()

    def scan(self, document):
        raise NotImplementedError()


# ok if you need a multifunction device
class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):
    def print(self, document):
        # ok - print stuff
        pass

    def fax(self, document):
        pass  # do-nothing
        # apporach 1 do-nothing
        # this is problematic because using of the
        # becomes problematic

    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan!')
        # apporach 2 raise error
        # this becomes a problem because can introduce bugs
        # if a dev class this scan method in api




# solution is to segregation your inferface
class Printer:
    @abstractmethod
    def print(self, document): pass


class Scanner:
    @abstractmethod
    def scan(self, document): pass


# Now just inherite what you need
# same for Fax, etc.
class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        pass  # something meaningful


class MultiFunctionDevice(Printer, Scanner):  # , Fax, etc
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)


printer = OldFashionedPrinter()
printer.fax(123)  # nothing happens
printer.scan(123)  # oops!
