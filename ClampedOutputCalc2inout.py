v_free1 = 2.04
v_free2 = 2.12
n = 0.1
# v_desired1 = float(input("Desired Output: "))
# v_desired2 = float(input("Desired Output: "))
# v_desired3 = float(input("Desired Output: "))
v_desired1 = 1.7
v_desired2 = 1.7
for i in range(int(1/n)):
    n = round(n, 1)
    vOut_clamped1 = (1-n) * v_free1 + n * v_desired1
    vOut_clamped2 = (1-n) * v_free2 + n * v_desired2
    # vOut_clamped1 = round(vOut_clamped1, 4)
    # vOut_clamped2 = round(vOut_clamped2, 4)
    print(str(vOut_clamped1), ",", str(vOut_clamped2))
    n += 0.1
