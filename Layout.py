"""
Created on Sat Nov 16 20:54:24 2019

@author: Fernando
@author: Hermann

Esta classe implementa de Abstract Base Classes (ABCs).
Também define 2 métodos abstratos: do_diario e do_nomeacao.
"""


import sys
from abc import ABC, abstractmethod


class Layout(ABC):

    def template_method(self):
        """Skeleton of operations to perform. DON'T override me.

        The Template Method defines a skeleton of an algorithm in an operation,
        and defers some steps to subclasses.
        """
        self.__do_absolutely_this()
        self.do_diario()
        self.do_anything()


    def __do_absolutely_this(self):
        """Protected operation. DON'T override me."""
        this_method_name = sys._getframe().f_code.co_name
        print('{}.{}'.format(self.__class__.__name__, this_method_name))

    @abstractmethod
    def do_diario(buffer, arquivo):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass


    @abstractmethod
    def do_nomeacao(buffer, arquivo):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass