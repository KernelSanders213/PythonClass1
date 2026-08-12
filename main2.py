import gc

# 1. Create a circular reference
class Node:
    def __init__(self, name):
        self.name = name
        self.reference = None

# Instantiate two nodes
node_a = Node("A")
node_b = Node("B")

# Make them point to each other (creates a cycle)
node_a.reference = node_b
node_b.reference = node_a

# 2. Remove the pointers to the objects from our scope
# Normal reference counting cannot delete them because they still point to each other!
del node_a
del node_b

# 3. Manually trigger the cyclic garbage collector
# gc.collect() returns the number of unreachable objects found and cleared
unreachable_count = gc.collect()

gc.

print(f"Garbage collector found and freed {unreachable_count} objects.")
