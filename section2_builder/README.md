# Gamma Categorization
* Design Patterns are typically split into three categories
* This is called Gamma Categorization after Erich Gamma, one of GoF authors

* Creational Patterns
  * Deal with the creation (construction) of objects
  * Explicit (constructor) vs. implicit (DI, reflection, etc.)
  * Wholesale (single statement) vs. piecewise (step-by-step)
* Structural Patterns
  * Concerned with the structure (e.g., class members)
  * Many patterns are wrappers that mimic the underlying class' interface
  * Stress the importance of good API design
* Behavioral Patterns
  * They are all different; no central theme

# Builder
## Motivation
* Some objects are simple and can be created in a single initializer call
* Other objects require a lot of ceremony to create
* Having an object with 10 initalizer arguments is not productive
* Instead, opt for piecewise construction
* Builder provides an API for constructing an object step-by-step
## Def
Builder: when piecewise object construction is complicated, provide an API for doing it succinctly.

# Summary
* A builder is a separate component for building an object
* Can either give builder an initializer or return it via a static function
* To make builder fluent, return self
* Different facets of an object can be built with different builders working in tandem via a base class
