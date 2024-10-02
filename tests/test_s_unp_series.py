import unittest

from coefficients.interference_coefficients.unpolarized.unpolarized_Spp1 import calculate_s_1_plus_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_Spp1V import calculate_s_1_plus_plus_unpolarized_V

_TEST_LEPTON_POLARIZATION = 1.0
_TEST_TARGET_POLARIZATION = 1.0
_TEST_SQUARED_Q_MOMENTUM_TRANSFER = 1.8200000524520876
_TEST_X_BJORKEN = 0.3429999947547912
_TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER = -0.1720000058412552
_TEST_EPSILON = 0.477109
_TEST_LEPTON_ENERGY_FRACTION = 0.491757
_TEST_K_TILDE = 0.157396
_TEST_SHORTHAND_K = 0.0842939
_TEST_T_PRIME = -0.0337889

_TEST_VERBOSE = False

class TestSUnpolarizedSeriesCoefficients(unittest.TestCase):

    def test_calculate_s_1_plus_plus_unpolarized(self):
        """
        # Title: `tests/test_c_unp_series.py`

        ## Description: Test the function `calculate_s_1_plus_plus_unpolarized`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{++}^{unp}(n = 1)$.
        We call it "SunpPP0" for S (series) unp (unpolarized [target]) PP (++) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_1_plus_plus_unpolarized(
                _TEST_LEPTON_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            0.40303674720775)
        
    def test_calculate_s_1_plus_plus_unpolarized_V(self):
        """
        # Title: `test_calculate_s_1_plus_plus_unpolarized_V`

        ## Description: Test the function `calculate_s_1_plus_plus_unpolarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{++}^{unp, V}(n = 1)$.
        We call it "SunpVPP0" for S (series) unp (unpolarized [target]) V (vector) PP (++) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_1_plus_plus_unpolarized_V(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            -0.00028400148536359)
        
    def test_calculate_c_0_plus_plus_unpolarized_A(self):
        """
        # Title: `test_calculate_c_0_plus_plus_unpolarized_A`

        ## Description: Test the function `calculate_c_0_plus_plus_unpolarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{unp}(n = 0)$.
        We call it "CunpVPP0" for C (series) unp (unpolarized [target]) A (axial vector) PP (++) 0 (n = 0).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_0_plus_plus_unpolarized_A(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            -0.66566222115038)