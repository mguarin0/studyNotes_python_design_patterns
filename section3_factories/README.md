# Factories
combines factory method and abstract factory

Factory: A component responsible solely for the wholesale (not piecewise) creation of objects.

Factory Method: is any method that creates an object

# Motivation
* Object creation logic becomes too convoluted
* Initializer is not descriptive
  * Name is always
  * Cannot overload with same sets of arguments with different names
  * Can turn into 'optional parameter hell'
* Wholesale object creation (non-piecewise, unlike Builder) can be outsourced to
  * A separate method (Factory Method) That may exist in a separate class (Factory)
  * Can create hierarchy of factories with Abstract Factory

# Summary
* A factory method is a static method that creates objects
* A factory is any entity that can take care of object creation
* A faccory can be external or reside inside the object as an inner class
* Hierarchies of factories can be used to create related objects
