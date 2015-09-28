#!/usr/bin/env python
# encoding: utf-8

"""
Decorator that allows you to define the valid types of the parameters in a
function.
All the existing solutions that I've found had some problem, so I've made my
own.
This helper:
    - doesn't modify `args` or `kwargs`
    - doesn't move arguments from one place to another
    - support both `args` and `kwargs`
    - allows you to use all the python 2.x supported parameters usage
    - use named arguments type definition
    - allows you to enforce a subset of all the available arguments
    - rise a standard TypeError if the arguments type are wrong
"""

import functools
import inspect


def decorator_with_args(decorator):
    """
    Helper to decorate a decorator and be able to use arguments in a 'simple'
    decorator without too much hassle.
    """
    def new(*args, **kwargs):
        def new2(func):
            return decorator(func, *args, **kwargs)
        return new2
    return new


def check_type(arg, valid):
    """
    Check that the `arg` corresponds with type/types of `valid`.

    :param arg: the arg to check
    :type arg: any object
    :param valid: the type/types that is/are valid for `arg`
    :type valid: type or tuple(type, type, ...)
    """
    if isinstance(valid, tuple):
        if sum(isinstance(arg, type_) for type_ in valid) == 0:
            msg = "{0} is not a valid type.\nValid types: {1}"
            msg = msg.format(arg, ', '.join(str(x) for x in valid))
            raise TypeError(msg)

    if not isinstance(arg, valid):
        raise TypeError('%s is not a %s type' % (arg, valid))


@decorator_with_args
def require(fn, **argument_types):
    """
    Return a decorator function that requires specified types.

    :param argument_types: each element of which is a type or class or a tuple
                           of several types or classes.
    :type argument_types: tuple (type or tuple of types)

    Example to require a string then a numeric argument

    @require(str, (int, long, float))
    def (a, b): ...
    """
    argnames, _, keywords_arg, _ = inspect.getargspec(fn)

    @functools.wraps(fn)
    def check_call(*args, **kwargs):
        """
        This wrapper check the defined types and call the `fn` callable if the
        types are ok.
        """
        callargs = inspect.getcallargs(fn, *args, **kwargs)

        # XXX: I've commented this since we may be overwritting kwargs in here!
        # add the kwargs to the named list
        # kwargs = callargs.get('kwargs', {})
        # callargs.update(kwargs)

        # not named args are not checked
        callargs.pop('args', None)

        for name, type_ in argument_types.iteritems():
            check_type(callargs[name], type_)

        # types are ok, do the call
        fn(*args, **kwargs)

    return check_call
