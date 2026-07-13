def f(x, y):
    return 1 + x*y

x0, y0, h = 0, 2, 0.1
x1 = x0 + h
y1 = y0 + h*f(x0, y0)  

print("Iterations:")
for i in range(1, 6):
    y_new = y0 + (h/2)*(f(x0, y0) + f(x1, y1))
    print(f"  {i}: y = {y_new:.10f}")
    if abs(y_new - y1) < 1e-10:
        break
    y1 = y_new

print(f"\nFinal: y(0.1) = {y_new:.10f}") 