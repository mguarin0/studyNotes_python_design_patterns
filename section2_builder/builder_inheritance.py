"""
you may have noticed that with builder facets and combining builders
we are directly violating the open-closed principle because anytime
a new sub-builder is introduced we have to modify the base class

an alternative is to use builder inheritance


take away is taht you can use builders as inheritors of other builders and you can do this into infinity
which solves the problem of your original builder the root builder depending on sub-builders
you'll never have to go back and modify the person builder and therefore you are in line with the open-closed principle
"""


# ELEMENT
class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f'{self.name} born on {self.date_of_birth} works as a {self.position}'

    @staticmethod
    def new():
        return PersonBuilder()

# BUILDER
class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


# SUB-BUILDER
class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


# SUB-BUILDER
class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self


# SUB-BUILDER
class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


if __name__ == '__main__':
    pb = PersonBirthDateBuilder()
    me = pb\
        .called('Dmitri')\
        .works_as_a('quant')\
        .born('1/1/1980')\
        .build()  # this does NOT work in C#/C++/Java/...
    print(me)
