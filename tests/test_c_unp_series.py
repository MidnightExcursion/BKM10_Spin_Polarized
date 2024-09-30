import unittest

from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp0 import calculate_c_0_plus_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp0V import calculate_c_0_plus_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp0A import calculate_c_0_plus_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp1 import calculate_c_1_plus_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp1V import calculate_c_1_plus_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp1A import calculate_c_1_plus_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp2 import calculate_c_2_plus_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp2V import calculate_c_2_plus_plus_unpolarized_V
# from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp2A import calculate_c_1_plus_plus_unpolarized_A

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

class TestCLPSeriesCoefficients(unittest.TestCase):

    def test_calculate_c_0_plus_plus_unpolarized(self):
        """
        # Title: `test_calculate_c_0_plus_plus_unpolarized`

        ## Description: Test the function `calculate_c_0_plus_plus_unpolarized`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{unp}(n = 0)$.
        We call it "CunpPP0" for C (series) unp (unpolarized [target]) PP (++) 0 (n = 0).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_0_plus_plus_unpolarized(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            0.42395672814361)
        
    def test_calculate_c_0_plus_plus_unpolarized_V(self):
        """
        # Title: `test_calculate_c_0_plus_plus_unpolarized_V`

        ## Description: Test the function `calculate_c_0_plus_plus_unpolarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{unp}(n = 0)$.
        We call it "CunpVPP0" for C (series) unp (unpolarized [target]) V (vector) PP (++) 0 (n = 0).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_0_plus_plus_unpolarized_V(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            -0.12536847747885)
        
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
        
    def test_calculate_c_1_plus_plus_unpolarized(self):
        """
        # Title: `test_calculate_c_1_plus_plus_unpolarized`

        ## Description: Test the function `calculate_c_1_plus_plus_unpolarized`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{unp}(n = 1)$.
        We call it "CunpPP1" for C (series) unp (unpolarized [target]) PP (++) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_1_plus_plus_unpolarized(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.39741815117728)

    def test_calculate_c_1_plus_plus_unpolarized_V(self):
        """
        # Title: `test_calculate_c_1_plus_plus_unpolarized_V`

        ## Description: Test the function `calculate_c_1_plus_plus_unpolarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{unp}(n = 1)$.
        We call it "CunpVPP1" for C (series) unp (unpolarized [target]) V (vector) PP (++) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_1_plus_plus_unpolarized_V(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.061154291210992)
        
    def test_calculate_c_1_plus_plus_unpolarized_A(self):
        """
        # Title: `test_calculate_c_1_plus_plus_unpolarized_A`

        ## Description: Test the function `calculate_c_1_plus_plus_unpolarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{unp, A}(n = 1)$.
        We call it "CunpAPP1" for C (series) unp (unpolarized [target]) A (axial vector) PP (++) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_1_plus_plus_unpolarized_A(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.18956751992963)
        
    def test_calculate_c_2_plus_plus_unpolarized(self):
        """
        # Title: `test_calculate_c_2_plus_plus_unpolarized`

        ## Description: Test the function `calculate_c_2_plus_plus_unpolarized`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{unp}(n = 2)$.
        We call it "CunpPP2" for C (series) unp (unpolarized [target]) PP (++) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_2_plus_plus_unpolarized(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            0.012731207597019)
        
    def test_calculate_c_2_plus_plus_unpolarized_V(self):
        """
        # Title: `test_calculate_c_2_plus_plus_unpolarized_V`

        ## Description: Test the function `calculate_c_2_plus_plus_unpolarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{unp}(n = 2)$.
        We call it "CunpVPP2" for C (series) unp (unpolarized [target]) V (vector) PP (++) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_2_plus_plus_unpolarized_V(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            -0.0047723778335283)