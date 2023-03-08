from FindRoute import FindRoute

# calls the agent and ensures valid-type arguments.
def main(map:dict,op=''):
    FindRoute(op,map)
    pass

# generating test scenario : 
map = {"A":{"C":6,"B":3},
       "B":{"A":3,"H":3,"K":3},
       "C":{"P":2,"G":2,"O":2,"D":3},
       "D":{"F":1,"E":1,"C":3},
       "E":{"F":1,"D":1,"M":14},
       "F":{"G":1,"E":1,"D":1},
       "G":{"H":2,"F":1,"C":2},
       "H":{"I":2,"G":2,"B":3,"K":4},
       "I":{"H":2,"E":2},

       "L":{"K":1},
       "K":{"B":3,"H":4,"N":3,"L":1},
       "O":{"C":2},
       "P":{"C":2},
       "N":{"M":2,"K":3},
       "M":{"X":1,"N":2,"E":14},
       "X":{"M":1}
       }

# quick tests below;

# print(main(map))
# print(main(map))
# print(main(map))