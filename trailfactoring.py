import TF

assigment = TF.getassigment()


p = int(assigment[1])

c = TF.floor_pow2_rational(
    int(float(assigment[0]) * 10),
    10
)

d = TF.floor_pow2_rational(
    int(float(assigment[0]) * 10) + 2,
    10
)


TF.factorfromctod(c, d, p)