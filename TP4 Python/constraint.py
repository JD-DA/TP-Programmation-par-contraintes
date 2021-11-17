from abc import ABC, abstractmethod
from typing import Dict, List, Optional

#Var = TypeVar('Var') # type pour variable
Var = 'str'
#Value = TypeVar('Value') # type pour domaine
Value = 'int'

# classe pour les contraintes
class Constraint(ABC):
    # constructeur initie les variables
    def __init__(self, variables: List[Var]) -> None:
        self.variables = variables

    # fonctions à redéfinir pour chaque contrainte
    # tester si les domaines sont en conflit la contrainte
    @abstractmethod
    def unsat(self, domains: Dict[Var, List[Value]]) -> bool:
        ...

    # tester si la valeur "value" de la variable "var" a un support
    @abstractmethod
    def checkSupport(self, var: Var, value: Value, domains: Dict[Var, List[Value]]) -> bool:
        ...
        
    # enlever les valeurs sans support de la variable "revisedVar"
    # retourner True si ces valeurs existent
    def propagate(self, revisedVar, domains: Dict[Var, List[Value]]) -> bool:
        listRem = []
        for val in domains[revisedVar]:
            if self.checkSupport(revisedVar, val, domains) == False:
                listRem.append(val)
        for val in listRem:
            domains[revisedVar].remove(val)
        if len(listRem)==0:
            return False
        return True
    
class Different(Constraint):
    def __init__(self, v1, v2) -> None:
        super().__init__([v1, v2])
        self.v1 = v1
        self.v2 = v2

    def unsat(self, domains: Dict[str, List[int]]) -> bool:
        pass
    
    def checkSupport(self, var, value, domains) -> bool:
        pass
    
class Superieur(Constraint):
    def __init__(self, v1: str, v2:str):
        pass
    
    def unsat(self, domains: Dict[str, List[int]]) -> bool:
        pass
    
    def checkSupport(self, var, value, domains) -> bool:
        pass

class Table(Constraint):
    def __init__(self, varList, tupleTable):
        super().__init__(varList)
        self.table = tupleTable
        
    def unsat(self, domains: Dict[str, List[int]]) -> bool:
        pass
    
    def checkSupport(self, var, value, domains) -> bool:
        pass

