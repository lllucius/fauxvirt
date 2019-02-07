#!/usr/bin/python3

import javalang
import sys

print()
print("from enum import Enum")
print()

for arg in sys.argv[1:]:
    
    f = open(arg, "r").read()
    tree = javalang.parse.parse(f)
    enums = list(tree.filter(javalang.tree.EnumConstantDeclaration))
    if enums:
        print("class %s(Enum):" % tree.types[0].name)
        for path, node in enums:
            print("    %s = '%s'" % (node.name, node.name.lower()))
        print()
