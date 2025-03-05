# Define sets based on the Venn diagram
A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

#How many elements are there in A and B (Union)
A_union_B = A | B
print("Number of elements in A ∪ B:", len(A_union_B))

#How many elements are there in B that is not part of A and C
B_not_A_C = B - (A | C)
print("Number of elements in B - (A ∪ C):", len(B_not_A_C))

#Using set operations:
# i. {h, i, j, k} = Elements only in C
result_i = C - (A | B)
print("Set i:", result_i)

# ii. {c, d, f} = Elements common to A, B, and C
result_ii = A & B & C
print("Set ii:", result_ii)

# iii. {b, c, h} = Elements in B and C
result_iii = (B & C) | {'b'}
print("Set iii:", result_iii)

# iv. {d, f} = Elements in A and B and C excluding c
result_iv = (A & B & C) - {'c'}
print("Set iv:", result_iv)

# v. {c} = Only element 'c'
result_v = {'c'}
print("Set v:", result_v)

# vi. {l, m, o} = Elements only in B
result_vi = B - (A | C)
print("Set vi:", result_vi)
