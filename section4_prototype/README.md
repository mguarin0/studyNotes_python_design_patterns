
# Def
Prototype = a partially or full initalized object that you copy (clone) and make use of.

# Motivation
* Complicated objects (e.g., cars) aren't designed from scratch
  * They reiterate existing designs
* An existing (partially or fully constructed) design is a Prototype
* We make a copy (clone) the prototype and customize it
  * Requires 'deep copy' support
* We make the cloning convenient (e.g., via a Factory)

# Summary
* To implement a prototype, partially construct an object and store it somewhere
* Deep sopy the prototype Customize the resulting instance
* A factory provides a convenient API for using prototypes
