#!/usr/bin/env python3
# -*-coding:utf-8 -*

from vector import Vector

v_1 = Vector(5)
v_2 = Vector((0, 5))

somme_vec = v_1 + v_2
somme_scalar = v_1 + 4
rsomme_scalar = 4 + v_1

print(f"sum of {v_1.values} + {v_2.values} = {somme_vec.values}")
print(f"sum of {v_1.values} + 4 = {somme_scalar.values}")
print(f"sum of 4 + {v_1.values}  = {rsomme_scalar.values}")

diff_vec = v_1 - v_2
diff_scalar = v_1 - 4
rdiff_scalar = 4 - v_1

minus_v_1 = v_1.__neg__()
minus_v_1_bis = -v_1
print(f"-{v_1.values} = {minus_v_1.values}")
print(f"-{v_1.values} = {minus_v_1_bis.values}")

print(f"{v_1.values} - {v_2.values} = {diff_vec.values}")
print(f"{v_1.values} - 4 = {diff_scalar.values}")
print(f"4 - {v_1.values}  = {rdiff_scalar.values}")

produit_vec = v_1 * v_2
produit_scalar = v_1 * 4
rproduit_scalar = 4 * v_1

print(f"produit of {v_1.values} * {v_2.values} = {produit_vec}")
print(f"produit of {v_1.values} * 4 = {produit_scalar.values}")
print(f"produit of 4 * {v_1.values}  = {rproduit_scalar.values}")
