from __future__ import annotations
from jaclang.plugin.feature import JacFeature as _Jac
from jaclang.plugin.builtin import *
from dataclasses import dataclass as __jac_dataclass__

@_Jac.make_walker(on_entry=[_Jac.DSFunc('return_message', _Jac.RootType)], on_exit=[])
@__jac_dataclass__(eq=False)
class interact(_Jac.Walker):

    def return_message(self, _jac_here_: _Jac.RootType) -> None:
        _Jac.report({'response': 'Hello, world!'})

@_Jac.make_walker(on_entry=[_Jac.DSFunc('return_message', _Jac.RootType)], on_exit=[])
@__jac_dataclass__(eq=False)
class interact_with_body(_Jac.Walker):
    name: str

    def return_message(self, _jac_here_: _Jac.RootType) -> None:
        _Jac.report({'response': 'Hello, ' + self.name + '!'})

@_Jac.make_walker(on_entry=[_Jac.DSFunc('return_message', _Jac.RootType)], on_exit=[])
@__jac_dataclass__(eq=False)
class temperature_converter(_Jac.Walker):
    fahrenheit: float

    def return_message(self, _jac_here_: _Jac.RootType) -> None:
        celsius = (self.fahrenheit - 32) * 5.0 / 9.0
        _Jac.report({'response': 'The temperature ' + str(self.fahrenheit) + 'Â°F is ' + str(celsius) + 'Â°C.'})

@_Jac.make_walker(on_entry=[_Jac.DSFunc('return_message', _Jac.RootType)], on_exit=[])
@__jac_dataclass__(eq=False)
class add(_Jac.Walker):
    a: int
    b: int

    def return_message(self, _jac_here_: _Jac.RootType) -> None:
        _Jac.report({'response': 'The sum of ' + str(self.a) + ' and ' + str(self.b) + ' is ' + str(self.a + self.b) + '.'})