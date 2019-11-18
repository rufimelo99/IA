from tree_search import *
import numpy as np
#Rui Melo, NMEC 88889
#colegas com quem discuti o problema: 89337(LEI), 89241(ECT), 89179(ECT)

class MyProblem(SearchProblem):
    def __init__(self, domain, initial, goal):
        self.domain = domain
        self.initial = initial
        self.goal = goal
    def goal_test(self, state):
        return self.domain.satisfies(state,self.goal)
    

class MyNode(SearchNode):
    def __init__(self,state,parent, depth=0, cost=0, heuristic=0, evalfunc=0): 
        self.state = state
        self.parent = parent
        

        self.depth = depth
        self.cost = cost
        self.evalfunc = heuristic+cost
        self.children = []
        self.heuristic = heuristic
    
    def __str__(self):
        return "no(" + str(self.state) + "," + str(self.parent) + ")"
    def __repr__(self):
        return str(self)
    
    def in_parent(self, state):
        if self.parent == None:
            return False
        return self.parent.state == state or self.parent.in_parent(state)


class MyTree(SearchTree):

    def __init__(self,problem, strategy='breadth',max_nodes=None): 
        #IMPLEMENT HERE
        self.problem = problem
        self.root = MyNode(problem.initial, None, 0, 0, self.problem.domain.heuristic(problem.initial, self.problem.goal))
        self.open_nodes = [self.root]
        self.strategy = strategy

        self.max_nodes=max_nodes
        self.solution_cost = 0
        self.solution_length = 0
        self.total_nodes = 1

        self.terminal_nodes = 1
        self.non_terminal_nodes = 0

        #self.terminal_nodes_list=[self.root] #para comecar com a root 
        #self.non_terminal_nodes_list=[]
        #self.discarded=[]

    def edit_open_nodes(self, lista=[]):
        self.open_nodes = lista

    def astar_add_to_open(self,lnewnodes):
        if self.strategy == 'breadth':
            self.open_nodes.extend(lnewnodes)
        elif self.strategy == 'astar':
            self.open_nodes = sorted(self.open_nodes + lnewnodes, key= lambda node : node.cost + node.heuristic)

    def effective_branching_factor(self):
        #http://ozark.hendrix.edu/~ferrer/courses/335/f11/lectures/effective-branching.html?fbclid=IwAR09in_z_-9J2ckS9e57rmo57UCvEr-xLzhe0MjFUJR_S9kJNLwlA5_l5-0
        poly=[]
        for i in range (self.solution_length):
            poly.append(1)
        poly.append(-self.total_nodes + 1)
        roots = np.roots(poly)
        result = roots.real[abs(roots.imag) < 0.000001]
        
        return result[-1]
        
    def update_ancestors(self,node):
        if node.children != []:
            node.evalfunc=node.children[0].evalfunc
            for n in node.children:
                if n.evalfunc<node.evalfunc:
                    node.evalfunc=n.evalfunc
        if(node.parent!=None):
            self.update_ancestors(node.parent)

    def discard_worse(self):
        if self.open_nodes != []:
            array_pais=list({node.parent for node in self.open_nodes if node.parent != None})
            
            worse_node=array_pais[0]
            for node in array_pais:
                if node.evalfunc > worse_node.evalfunc:
                    worse_node = node

            tamanho_inicial = len(self.open_nodes)
            self.open_nodes = [node for node in self.open_nodes if node.parent != worse_node]

            tamanho_final = len(self.open_nodes)
            self.open_nodes.append(worse_node)
            self.terminal_nodes -= (tamanho_inicial-tamanho_final)
            self.non_terminal_nodes -= 1



    def search2(self):
        #IMPLEMENT HERE
        while self.open_nodes != []:
            node = self.open_nodes.pop(0)
            self.solution_cost += node.cost
            self.solution_length = node.depth
            
            
            if self.problem.goal_test(node.state):
                self.solution_cost = node.cost 
                #self.solution_length = len(self.get_path(node))-1

                return self.get_path(node)

            lnewnodes = []
             
            for a in self.problem.domain.actions(node.state):
               
                newstate = self.problem.domain.result(node.state,a)
                
                if not node.in_parent(newstate) :
                    
                    newnode = MyNode(newstate,
                                        node, 
                                        node.depth + 1,
                                        node.cost + self.problem.domain.cost(node.state, a),
                                        self.problem.domain.heuristic(newstate, self.problem.goal))
                    

                    lnewnodes.append(newnode)
                    node.children.append(newnode)
                    self.total_nodes += 1
            
            
            if(self.max_nodes!=None):
                while (self.non_terminal_nodes+self.terminal_nodes+len(lnewnodes) > self.max_nodes): 
                    self.discard_worse()
                  
                
            self.add_to_open(lnewnodes)
            if len(lnewnodes):
                self.terminal_nodes += len(lnewnodes)
                self.non_terminal_nodes += 1
            self.terminal_nodes -= 1
            
            
            self.update_ancestors(node)
        return None

    # shows the search tree in the form of a listing
    def show(self,heuristic=False,node=None,indent=''):
        if node==None:
            self.show(heuristic,self.root)
            print('\n')
        else:
            line = indent+node.state
            if heuristic:
                line += (' [' + str(node.evalfunc) + ']')
            print(line)


            if node.children==[]:
                return
            
            for n in node.children:
                self.show(heuristic,n,indent+'  ')


