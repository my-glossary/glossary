"""Decorator guide_typing with mypy.

Not completed guide.

.. seealso::

    `Declaring decorators <https://mypy.readthedocs.io/en/stable/generics.html#declaring-decorators>`_

"""

from typing import Any, Callable, TypeVar, cast

from typing_extensions import reveal_type

F = TypeVar('F', bound=Callable[..., Any])


def printing_decorator(func: F) -> F:
    """"""
    def wrapper(*args, **kwargs):
        print('Calling', func)
        return func(*args, **kwargs)
    return cast(F, wrapper)


def add_forty_two(value: int) -> int:
    return 42 + value


a = add_forty_two(3)
reveal_type(a)
a = add_forty_two('foo')
