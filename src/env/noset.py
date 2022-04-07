# coding=utf-8
"""
pyrc noset Module
"""
__all__ = (
    "Noset",
    "NOSET",
)


class Noset:
    """
    Marker object for globals not initialized or other objects.

    Examples:
        >>> name = Noset.__name__.lower()
        >>> assert str(NOSET) == f'<{name}>'
        >>> assert repr(NOSET) == f'<{name}>'
        >>> assert repr(Noset("test")) == f'<test>'
    """
    name: str
    __slots__ = ("name",)
    def __init__(self, name: str = ""): self.name = name if name else self.__class__.__name__.lower()
    def __hash__(self): return hash((self.__class__, self.name,))
    def __reduce__(self): return self.__class__, (self.name,)
    def __repr__(self): return self.__str__()
    def __str__(self): return f'<{self.name}>'


NOSET = Noset()
