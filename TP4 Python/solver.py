# fonctionnement d'un solveur CSP
import copy
from queue import Queue

from constraint import Constraint, Var, Value
from csp import CSP
from typing import Dict, List, Optional

class Solver:
    def __init__(self):
        # la variable nbNodes contiendra le nombre de noeuds créés dans
        # l'arbre de recherche
        self.nbNodes = 0

    # fonction qui réalise l'algorithme backtracking
    # lorsqu'on arrive à une solution on affiche la solution
    # puis continuer pour trouver toutes les solutions
    def backtracking_search(self, csp):
        self.nbNodes = self.nbNodes+1
        print(csp.domains)
        # vérifier si le domaine de toutes les variables est singleton
        # si oui, vérifier si le csp est satisfait, retourner true/false
        # sinon, prendre une variable non affectée, instancier la variable
        # avec les valeurs du domaine, où pour chaque valeur on crée
        # une copy du CSP pour travailler dessus
        if (csp.singleton()):
            if (csp.satisfied()):
                print(csp.solution())
                return
            else:
                return
        var = csp.unassignedVar()
        for i in csp.domains[var]:
                csp_res = CSP(csp.variables, csp.domainsCopy())
                csp_res.ctrList = csp.ctrList
                csp_res.vcList = csp.vcList
                csp_res.domains[var] = [i]
                if(csp_res.consistent(var)):
                    self.backtracking_search(csp_res)



    # fonction qui réalise l'algorithme backtracking avec forward checking
    # lorsqu'on arrive à une solution on affiche la solution
    # puis continuer pour trouver toutes les solutions
    def bt_forward(self, csp):
        self.nbNodes = self.nbNodes + 1
        print(csp.domains)
        if (csp.singleton()):
            if (csp.satisfied()):
                print(csp.solution())
                return
            else:
                return
        var = csp.unassignedVar()

        for i in csp.domains[var]:
            if(var=="x" and i==2):
                test = True
            csp_res = CSP(csp.variables, csp.domainsCopy())
            csp_res.ctrList = csp.ctrList
            csp_res.vcList = csp.vcList
            csp_res.domains[var] = [i]
            # on va réduire le domaine de chaque domaine
            self.fw_check(csp_res, var)
            if (not(csp_res.emptyDomain()) and csp_res.consistent(var)):
                self.bt_forward(csp_res)

    # forward checking du CSP avec la variable var qui vient d'être instanciée
    def fw_check(self, csp, var):
        for constraint in csp.ctrList:
            (i,j)=constraint.variables
            if i==var:
                varTest = j
            elif j==var:
                varTest = i
            else:
                continue
            self.revise(varTest,csp,constraint)

            """for index in range(len(csp.domains[varTest])):
                newDomaine = copy.deepcopy(csp.domains[varTest])
                if not(constraint.checkSupport(varTest,csp.domains[varTest][index],csp.domains)):
                    newDomaine.pop(index)
            csp.domains[varTest] = newDomaine"""


    # supprimer les valeurs inconsistantes dans le domaine de revisedVar
    # par rapport à la contrainte constr
    def revise(self, revisedVar, csp, constr):
        dom_copy = {}
        for var in constr.variables:
            dom_copy[var] = csp.domains[var].copy()
        listVal = csp.domains[revisedVar].copy()
        for val in listVal:
            dom_copy[revisedVar] = [val]
            if constr.unsat(dom_copy):
                csp.domains[revisedVar].remove(val)

    # fonction qui réalise l'algorithme backtracking avec propagation de
    # contraintes, la propagation est effectuée par choixAC (AC-1 ou AC3)
    # lorsqu'on arrive à une solution on affiche la solution
    # puis continuer pour trouver toutes les solutions
    def bt_propagation(self, csp, choixAC):
        self.nbNodes = self.nbNodes + 1
        choixAC(csp)
        print(csp.domains)
        if (csp.singleton()):
                print(csp.solution())
        else:
            #var=csp.unassignedVar()
            #var = csp.unassigned_var_spec("croissantDegréDyn")
            #var = csp.unassigned_var_spec("decroissantSupport")
            var = csp.unassigned_var_spec("croissantSupport")

            for i in csp.domains[var]:
                csp_res = CSP(csp.variables, csp.domainsCopy())
                csp_res.ctrList = csp.ctrList
                csp_res.vcList = csp.vcList
                csp_res.domains[var] = [i]
                self.bt_propagation(csp_res,choixAC)


    def reviseNotify(self, revisedVar, csp, constr):
        dom_copy = {}
        notify = False
        for var in constr.variables:
            dom_copy[var] = csp.domains[var].copy()
        listVal = csp.domains[revisedVar].copy()
        for val in listVal:
            dom_copy[revisedVar] = [val]
            if constr.unsat(dom_copy):
                csp.domains[revisedVar].remove(val)
                notify = True
        return notify

    # le CSP a seulement des contraintes binaires
    def propagate_AC1(self, csp):
        reviseVal = True
        while (reviseVal):
            reviseVal = False
            for constr in csp.ctrList:
                reviseVal = reviseVal or self.reviseNotify(constr.variables[0], csp, constr)
                reviseVal = reviseVal or self.reviseNotify(constr.variables[1], csp, constr)

    
    # le CSP a seulement des contraintes binaires
    def propagate_AC3(self, csp):
        queue = Queue()
        for constr in csp.ctrList:
            queue.put((constr,0))
            queue.put((constr,1))
        reviseVal = True
        while (not(queue.empty())):
            (constr,i) = queue.get()
            reviseVal = self.reviseNotify(constr.variables[i], csp, constr)
            if(reviseVal):
                for constr1 in csp.ctrList:
                    if(constr1!=constr):
                        if(constr1.variables[0]==constr.variables[i]):
                            queue.put((constr1,1))
                        elif(constr1.variables[1]==constr.variables[i]):
                            queue.put((constr1,0))
