import math


def sumacplx(c1, c2):
    parteI = (c1[0] + c2[0])
    parteD = (c1[1] + c2[1])

    return parteI, parteD


def multcplx(c1, c2):
    parteA = c1[0] * c2[0]
    parteB = c1[1] * c2[1]
    parteC = c1[0] * c2[1]
    parteD = c1[1] * c2[0]
    parteI = parteA - parteB
    parteD = parteC + parteD

    return parteI, parteD


def restacplx(c1, c2):
    parteI = (c1[0] + c2[0])
    parteD = (c1[1] + c2[1])

    return parteI, parteD


def divcplx(c1, c2):
    parteA = (c1[0] * c2[0]) + (c1[1] * c2[1])
    parteB = (c2[0] ** 2) + (c2[1] ** 2)
    parteC = (c2[0] * c1[1]) - (c1[0] * c2[1])

    parteI = parteA / parteB
    parteD = parteC / parteB

    return parteI, parteD


def modulocplx(c1):
    parteA = c1[0] ** 2 + c1[1] ** 2
    parteB = parteA ** (1 / 2)

    return parteB


def conjugadocplx(c1):
    return c1[0], -c1[1]


def fasecplx(c1):
    parteA = c1[1] / c1[0]
    parteB = math.atan(parteA)

    return parteB


def cartesianToPolarCplx(c1):
    modulo = modulocplx(c1)
    fase = fasecplx(c1)

    return modulo, fase


def polarToCartesianCplx(c1):
    parteA = c1[0] * math.cos(c1[1])
    parteB = c1[0] * math.sin(c1[1])

    return parteA, parteB
