try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

from form_factors.effective_cffs import compute_cff_effective

from coefficients.dvcs_coefficients.unpolarized.bkm10.unpolarized_curlyC_dvcs import calculate_curly_c_unpolarized_dvcs

def calculate_c_1_unpolarized_dvcs(
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float, 
    skewness_parameter: float,
    shorthand_k: float,
    compton_form_factor_h: complex,
    compton_form_factor_h_tilde: complex,
    compton_form_factor_e: complex,
    compton_form_factor_e_tilde: complex,
    verbose: bool = False) -> float:
    """
    """

    try:

        # (1): Calculate the first term's prefactor:
        prefactor = 8. * shorthand_k * (2. - lepton_energy_fraction_y) / ((2. - x_Bjorken) * (1. + epsilon**2))
        
        # (2): Calculate the second terms' Curly C contribution:
        curlyC_unp_DVCS = calculate_curly_c_unpolarized_dvcs(
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            compute_cff_effective(skewness_parameter, compton_form_factor_h),
            compute_cff_effective(skewness_parameter, compton_form_factor_h_tilde),
            compute_cff_effective(skewness_parameter, compton_form_factor_e),
            compute_cff_effective(skewness_parameter, compton_form_factor_e_tilde),
            compton_form_factor_h.conjugate(),
            compton_form_factor_h_tilde.conjugate(),
            compton_form_factor_e.conjugate(),
            compton_form_factor_e_tilde.conjugate(),
        ).real

        # (3): Calculate the entire coefficient:
        c1_dvcs_unpolarized_coefficient = prefactor * curlyC_unp_DVCS
        
        if verbose:
            print(f"> Calculated c1_dvcs_unpolarized_coefficient to be: {c1_dvcs_unpolarized_coefficient}")

        return c1_dvcs_unpolarized_coefficient
    
    except Exception as E:
        print(f"> Error in computing c1_dvcs_unpolarized_coefficient:\n> {E}")
        return 0.