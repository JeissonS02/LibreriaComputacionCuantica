import LibraryCplx as lc
import unittest


class TestCplxOperations(unittest.TestCase):

    def test_sumacplx(self):
        suma = lc.sumacplx((3, 2), (-5, 5.2))
        self.assertAlmostEqual(suma[0], -2)
        self.assertAlmostEqual(suma[1], 7.2)

    def test_multcplx(self):
        multiplicacion = lc.multcplx((3, 2), (-5, 5.2))
        self.assertAlmostEqual(multiplicacion[0], -25.4)
        self.assertAlmostEqual(multiplicacion[1], 5.6)

    def test_restcplx(self):
        resta = lc.restacplx((3, 2), (-5, 5.2))
        self.assertAlmostEqual(resta[0], 8)
        self.assertAlmostEqual(resta[1], -3.2)

    def test_divclpx(self):
        division = lc.divcplx((2, -4), (4, -2))
        self.assertAlmostEqual(division[0], 0.8)
        self.assertAlmostEqual(division[1], -0.6)

    def test_mod(self):
        modulo = lc.modulocplx((0, 9))
        self.assertAlmostEqual(modulo, 9)

    def test_conj(self):
        conjugado = lc.conjugadocplx((2, 7))
        self.assertAlmostEqual(conjugado[0], 2)
        self.assertAlmostEqual(conjugado[1], -7)

    def polar_cplx(self):
        polar = lc.cartesianToPolarCplx((5, 5))
        self.assertAlmostEqual(polar[0], 7.0710678118654755)
        self.assertAlmostEqual(polar[1], 45)

    def cartesian_cplx(self):
        cartesian = lc.polarToCartesianCplx((5, 5))
        self.assertAlmostEqual(cartesian[0], 4.980973)
        self.assertAlmostEqual(cartesian[1], 0.435779)

    def fase_cplx(self):
        fase = lc.fasecplx((1, 5))
        self.assertAlmostEqual(fase, 1.3)


if __name__ == '__main__':
    unittest.main()
