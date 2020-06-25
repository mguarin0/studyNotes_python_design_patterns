# Singleton
A component which is instantiated only once.

# Motivation
* For some components it only makes sense to have one in the system
  * Database repository
  * Object factory
* E.g., the initializer call is expensive
  * We only do it once
  * We provide everyone with the same instance
* Want to prevent anyone creating additional copies
* Need to take care of lazy instantiation

# Summary
* Different realizations of singleton: custom allocator, decorator, metaclass
* Laziness is easy, just init on first request Monostate variation
Testability issues
