import unittest

from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_Spp import calculate_curly_S_plus_plus_longitudinally_polarized_interference
from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_S0p import calculate_curly_S_zero_plus_longitudinally_polarized_interference

from form_factors.effective_cffs import compute_cff_effective

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

_TEST_SKEWNESS = 0.20115437410625

_TEST_ELECTRIC_FORM_FACTOR_FE = 0.648238
_TEST_MAGNETIC_FORM_FACTOR_FG = 1.81043
_TEST_DIRAC_FORM_FACTOR_F1 = -21.9835
_TEST_PAULI_FORM_FACTOR_F2 = 23.794
_TEST_CFF_REAL_H = -0.897
_TEST_CFF_REAL_H_TILDE = 2.444
_TEST_CFF_REAL_E = -0.541
_TEST_CFF_REAL_E_TILDE = 2.207
_TEST_CFF_IMAGINARY_H = 2.421
_TEST_CFF_IMAGINARY_H_TILDE = 1.131
_TEST_CFF_IMAGINARY_E = 0.903
_TEST_CFF_IMAGINARY_E_TILDE = 5.383

_TEST_VERBOSE = False

class TestCurlyCLongitudinallyPolarizedSeriesCoefficients(unittest.TestCase):

    def test_calculate_curly_S_plus_plus_longitudinally_polarized_interference(self):
        """
        # Title: `test_calculate_curly_S_plus_plus_longitudinally_polarized_interference`

        ## Description: Test the function `calculate_curly_S_plus_plus_longitudinally_polarized_interference`.
        These Curly Cs don't rely on the helicity flip of the lepton or not, so they
        are easy to test.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_curly_S_plus_plus_longitudinally_polarized_interference(
                3,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_K_TILDE,
                _TEST_SHORTHAND_K,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                _TEST_CFF_IMAGINARY_H,
                _TEST_CFF_IMAGINARY_H_TILDE,
                _TEST_CFF_IMAGINARY_E,
                _TEST_CFF_IMAGINARY_E_TILDE,
                _TEST_VERBOSE), 
            -19.766743031335)
        
    def test_calculate_curly_S_zero_plus_longitudinally_polarized_interference(self):
        """
        # Title: `test_calculate_curly_S_zero_plus_longitudinally_polarized_interference`

        ## Description: Test the function `calculate_curly_S_zero_plus_longitudinally_polarized_interference`.
        These Curly Cs don't rely on the helicity flip of the lepton or not, so they
        are easy to test.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_curly_S_zero_plus_longitudinally_polarized_interference(
                2,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_K_TILDE,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                compute_cff_effective(_TEST_SKEWNESS,_TEST_CFF_IMAGINARY_H),
                compute_cff_effective(_TEST_SKEWNESS,_TEST_CFF_IMAGINARY_H_TILDE),
                compute_cff_effective(_TEST_SKEWNESS,_TEST_CFF_IMAGINARY_E),
                compute_cff_effective(_TEST_SKEWNESS,_TEST_CFF_IMAGINARY_E_TILDE),
                _TEST_VERBOSE), 
            0.66250804420337)