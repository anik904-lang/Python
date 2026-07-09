x0 = 0
y0 = 0
h = 0.1

x1 = x0 + h  
y1 = y0 + h * (1 - y0)  

x2 = x1 + h  
y2 = y1 + h * (1 - y1)  

import math
exact_y1 = 1 - math.exp(-0.1)  
exact_y2 = 1 - math.exp(-0.2)  

print("=" * 60)
print("EULER'S METHOD RESULTS")
print("=" * 60)
print(f"At x = 0.1:")
print(f"  Euler's method: y = {y1:.6f}")
print(f"  Exact solution: y = {exact_y1:.6f}")
print(f"  Error: {abs(exact_y1 - y1):.6f}")
print()
print(f"At x = 0.2:")
print(f"  Euler's method: y = {y2:.6f}")
print(f"  Exact solution: y = {exact_y2:.6f}")
print(f"  Error: {abs(exact_y2 - y2):.6f}")
print("=" * 60)

print("\nSTEP-BY-STEP CALCULATIONS:")
print("-" * 60)
print(f"Step 1: x₁ = {x0} + {h} = {x1}")
print(f"        y₁ = {y0} + {h}(1 - {y0})")
print(f"        y₁ = {y0} + {h}({1-y0})")
print(f"        y₁ = {y1}")
print()
print(f"Step 2: x₂ = {x1} + {h} = {x2}")
print(f"        y₂ = {y1} + {h}(1 - {y1})")
print(f"        y₂ = {y1} + {h}({1-y1:.6f})")
print(f"        y₂ = {y2:.6f}")
print("-" * 60)