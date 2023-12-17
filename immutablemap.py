from collections.abc import Mapping

class ImmutableMap(Mapping):
    def __init__(self, *args, **kwargs):
        for arg in args:
            if not isinstance(arg, Mapping):
                raise TypeError(f"Expected Mapping data type, passed {arg.__class__.__name__}")
        self._dict = {}

        for arg in args:
            self._dict.update(arg)

        self._dict.update(kwargs)

    def __len__(self):
        return len(self._dict)

    
    def __contains__(self, key):
        return key in self._dict

    
    def __getitem__(self, key):
        return self._dict[key]

    
    def __delitem__(self, *args):
        raise TypeError("Can't delete items")

    
    def __instance_checker(self, other):
        return isinstance(other, ImmutableMap)

    
    def __eq__(self, other):
        if self.__instance_checker(other):
            return self._dict == other._dict
        raise TypeError(f"Can't check equality for {self.__class__.__name__} and {other.__class__.__name__}")

    def __ge__(self, other):
        if self.__instance_checker(other):
            return self._dict >= other._dict
        raise TypeError(f"Can't check 'greater or equal' for {self.__class__.__name__} and {other.__class__.__name__}")

    def __gt__(self, other):
        if self.__instance_checker(other):
            return self._dict > other._dict
        raise TypeError(f"Can't check 'greater than' for {self.__class__.__name__} and {other.__class__.__name__}")

    def __ior__(self, other):
        raise TypeError("Can't perform in-place OR for ImmutableMapping")

    
    def __iter__(self):
        return iter(self._dict)

    
    def __le__(self, other):
        if self.__instance_checker(other):
            return self._dict <= other._dict
        raise TypeError(f"Can't check 'less or equal' for {self.__class__.__name__} and {other.__class__.__name__}")

    def __lt__(self, other):
        if self.__instance_checker(other):
            return self._dict < other._dict
        raise TypeError(f"Can't check 'less than' for {self.__class__.__name__} and {other.__class__.__name__}")

    def __ne__(self, other):
        if self.__instance_checker(other):
            return self._dict != other._dict
        raise TypeError(f"Can't check 'not equal' for {self.__class__.__name__} and {other.__class__.__name__}")

    
    def __or__(self, other):
        if self.__instance_checker(other):
            return ImmutableMap(**self._dict, **other._dict)
        raise TypeError(f"Can't do | 'not equal' for {self.__class__.__name__} and {other.__class__.__name__}")

    
    def __repr__(self):
        return f"ImmutableMap({self._dict})"

    
    def __sizeof__(self):
        sumall = sum(object.__sizeof__(key) + object.__sizeof__(value) for key, value in self._dict.items())
        return sumall + object.__sizeof__(self)

    
    def items(self):
        return self._dict.items()

    
    def keys(self):
        return self._dict.keys()

    
    def pop(self, key):
        raise TypeError("Can't do pop on ImmutableMap")

    
    def popitem(self):
        raise TypeError("Can't do pop item on ImmutableMap")

    
    def setdefault(self, key, default=None):
        raise TypeError("Can't set something on ImmutableMap")

   
    def update(self, *args, **kwargs):
        raise TypeError("Can't update something on ImmutableMap")
    
    
