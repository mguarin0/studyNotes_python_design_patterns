"""
singleton by allocator

singleton implementation rewrite allocator

"""
import random

class Database:
    initialized = False

    def __init__(self):
        # self.id = random.randint(1,101)
        # print('Generated an id of ', self.id)
        # print('Loading database from file')
        pass

    # static instance
    _instance = None

    # allocator
    # note __new__ called before __init__
    # initializer will always be called
    # this is a downside of this type of singleton implementation
    def __new__(cls, *args, **kwargs):
        # check if instance has been initialized
        # if not then initialize
        if not cls._instance:
            cls._instance = super(Database, cls)\
                .__new__(cls, *args, **kwargs)

        return cls._instance


database = Database()

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()

    print(d1.id, d2.id)
    print(d1 == d2)
    print(database == d1)
