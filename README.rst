RequireType
===========

What
----

Decorator that allows you to specify the valid types of the parameters in a
function or method.

In case of that a call don't match the required type will fail with a
``TypeError`` exception.


Why?
----

There are some cases (TODO: add some examples) where you want/need to specify a
specific type to use and since python does not have type checks for parameters
here's where this is useful.

All the existing solutions that I've found had some problem or does not have a
feature that I'd like to have, so I've made my own.


How to use?
-----------

First, install the ``RequireType`` package, you can do that using ``pip``::

    pip install requiretype

In your code you just need to import and use the ``require`` decorator.

Example::

    from requiretype import require

    @require(name=str, age=(int, float, long))
    def greet_person(name, age):
        print "Hello {0} ({1})".format(name, age)

    >>> greet_person("John", 42)
    Hello John (42)

    >>> greet_person("John", "Doe")
    [...traceback...]
    TypeError: Doe is not a valid type.
    Valid types: <type 'int'>, <type 'float'>, <type 'long'>

    >>> greet_person(42, 43)
    [...traceback...]
    TypeError: 42 is not a <type 'str'> type




Some notes
----------

Here are some details about this library. Most of them was found in one or
more packages that helps you to enforce/check/require types and IMO are not
good things to have and motivated me to write this.

RequireType:

    * does not modify ``args`` or ``kwargs``
    * does not move arguments from one place to another
    * support both ``args`` and ``kwargs``
    * allows you to use all the python 2.x supported parameters usage (if not, please report a bug)
    * use named arguments type definition
    * allows you to enforce a subset of all the available arguments
    * raise a standard ``TypeError`` if the arguments type are wrong
