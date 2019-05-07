"""
Task. Implement a data structure that stores a set 𝑆 of integers with the following allowed operations:

∙ add(𝑖) — add integer 𝑖 into the set 𝑆 (if it was there already, the set doesn’t change).
∙ del(𝑖) — remove integer 𝑖 from the set 𝑆 (if there was no such element, nothing happens).
∙ find(𝑖) — check whether 𝑖 is in the set 𝑆 or not.
∙ sum(𝑙, 𝑟) — output the sum of all elements 𝑣 in 𝑆 such that 𝑙 ≤ 𝑣 ≤ 𝑟.

Input Format. Initially the set 𝑆 is empty. The first line contains 𝑛 — the number of operations. The next
𝑛 lines contain operations. Each operation is one of the following:
∙ “+ i" — which means add some integer (not 𝑖, see below) to 𝑆,
∙ “- i" — which means del some integer (not 𝑖, see below)from 𝑆,
∙ “? i" — which means find some integer (not 𝑖, see below)in 𝑆,
∙ “s l r" — which means compute the sum of all elements of 𝑆 within some range of values (not
from 𝑙 to 𝑟, see below).
However, to make sure that your solution can work in an online fashion, each request will actually
depend on the result of the last sum request. Denote 𝑀 = 1 000 000 001. At any moment, let 𝑥 be
the result of the last sum operation, or just 0 if there were no sum operations before. Then
∙ “+ i" means add((𝑖 + 𝑥) mod 𝑀),
∙ “- i" means del((𝑖 + 𝑥) mod 𝑀),
∙ “? i" means find((𝑖 + 𝑥) mod 𝑀),
∙ “s l r" means sum((𝑙 + 𝑥) mod 𝑀,(𝑟 + 𝑥) mod 𝑀).

Constraints. 1 ≤ 𝑛 ≤ 100 000; 0 ≤ 𝑖 ≤ 109.

Output Format. For each find request, just output “Found" or “Not found" (without quotes; note that the
first letter is capital) depending on whether (𝑖 + 𝑥) mod 𝑀 is in 𝑆 or not. For each sum query, output
the sum of all the values 𝑣 in 𝑆 such that ((𝑙+𝑥) mod 𝑀) ≤ 𝑣 ≤ ((𝑟+𝑥) mod 𝑀) (it is guaranteed that
in all the tests ((𝑙 + 𝑥) mod 𝑀) ≤ ((𝑟 + 𝑥) mod 𝑀)), where 𝑥 is the result of the last sum operation
or 0 if there was no previous sum operation
"""

from sys import stdin


# Splay tree implementation
# Vertex of a splay tree
class Vertex:
    def __init__(self, key, sum, left, right, parent):
        (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)


def update(v):
    if v is None:
        return
    v.sum = v.key + (v.left.sum if v.left is not None else 0) + (v.right.sum if v.right is not None else 0)
    if v.left is not None:
        v.left.parent = v
    if v.right is not None:
        v.right.parent = v


def small_rotation(v):
    parent = v.parent
    if parent is None:
        return
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent is not None:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v


def big_rotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
        # Zig-zig
        small_rotation(v.parent)
        small_rotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        # Zig-zig
        small_rotation(v.parent)
        small_rotation(v)
    else:
        # Zig-zag
        small_rotation(v)
        small_rotation(v)


# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
    if v is None:
        return None
    while v.parent is not None:
        if v.parent.parent is None:
            small_rotation(v)
            break
        big_rotation(v)
    return v


# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key):
    v = root
    last = root
    next = None
    while v is not None:
        if v.key >= key and (next is None or v.key < next.key):
            next = v
        last = v
        if v.key == key:
            break
        if v.key < key:
            v = v.right
        else:
            v = v.left
    root = splay(last)
    return next, root


def split(root, key):
    (result, root) = find(root, key)
    if result is None:
        return root, None
    right = splay(result)
    left = right.left
    right.left = None
    if left is not None:
        left.parent = None
    update(left)
    update(right)
    return left, right


def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    while right.left is not None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right


# Code that uses splay tree to solve the problem

root = None


def insert(x):
    global root
    (left, right) = split(root, x)
    new_vertex = None
    if right is None or right.key != x:
        new_vertex = Vertex(x, x, None, None, None)
    root = merge(merge(left, new_vertex), right)


def next_node(node):
    if node.right:
        return left_descendant(node.right)
    else:
        return right_ancestor(node)


def left_descendant(n):
    if n.left:
        return left_descendant(n.left)
    return n


def right_ancestor(n):
    if n:
        if n.parent is None:
            return None
        if n.key < n.parent.key:
            return n.parent
        return right_ancestor(n.parent)
    return None


def erase(x):
    global root
    ne, root = find(root, x)
    if ne and ne.key == x:
        splay(next_node(ne))
        splay(ne)
        l = ne.left
        r = ne.right
        if r:
            r.left = l
            if l:
                l.parent = r
            r.parent = None
            root = r
        elif l:
            l.parent = None
            root = l
        else:
            root = None


def search(x):
    global root
    if root:
        ne, root = find(root, x)
        if ne:
            return ne.key == x
        else:
            return False
    else:
        return False


def sum(fr, to):
    global root
    (left, middle) = split(root, fr)
    (middle, right) = split(middle, to + 1)
    if middle:
        ans = middle.sum
    else:
        ans = 0
    root = merge(merge(left, middle), right)
    return ans


if __name__ == '__main__':
    MODULO = 1000000001
    n = int(stdin.readline())
    last_sum_result = 0
    for i in range(n):
        line = stdin.readline().split()
        if line[0] == '+':
            x = int(line[1])
            insert((x + last_sum_result) % MODULO)
        elif line[0] == '-':
            x = int(line[1])
            erase((x + last_sum_result) % MODULO)
        elif line[0] == '?':
            x = int(line[1])
            print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
        elif line[0] == 's':
            l = int(line[1])
            r = int(line[2])
            res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
            print(res)
            last_sum_result = res % MODULO
