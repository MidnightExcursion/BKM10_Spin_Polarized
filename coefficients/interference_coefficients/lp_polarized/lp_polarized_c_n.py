from coefficients.interference_coefficients.lp_polarized.pl_polarized_Cpp0 import calculate_c_0_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_C0p0 import calculate_c_0_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_Cpp1 import calculate_c_1_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_C0p1 import calculate_c_1_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_Cpp2 import calculate_c_2_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_C0p2 import calculate_c_2_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_Cpp import calculate_curly_C_plus_plus_longitudinally_polarized_interference

from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_C0p import calculate_curly_C_zero_plus_longitudinally_polarized_interference

from form_factors.effective_cffs import compute_cff_effective

def calculate_c_interference_coefficient(
    n_number: int,
    lepton_polarization: float,
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float,
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float,
    skewness_parameter: float,
    t_prime: float,
    k_tilde: float,
    shorthand_k: float,
    Dirac_form_factor_F1: float,
    Pauli_form_factor_F2: float,
    compton_form_factor_h_real_part: float,
    compton_form_factor_h_tilde_real_part: float,
    compton_form_factor_e_real_part: float,
    compton_form_factor_e_tilde_real_part: float,
    verbose: bool = True) -> float:
    """
    """

    print(f"> The number is C_{n_number}! FUCKER BIGG")

    c_plus_plus = 0.
    curly_c_plus_plus = 0.
    c_zero_plus_n = 0.
    curly_c_zero_plus = 0.
    c_minus_plus_n = 0.
    curly_c_minus_plus = 0.

    try:

        if n_number == 0:

            # (1): We compute the first part of the term: C++, n = 0
            c_plus_plus = calculate_c_0_plus_plus_longitudinally_polarized(
                lepton_polarization,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)

            # (2): The second part of the term is C0+, n = 0
            c_zero_plus_n = calculate_c_0_zero_plus_longitudinally_polarized(
                lepton_polarization,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
        elif n_number == 1:

            # (1): We compute the first part of the term: C++, n = 1
            c_plus_plus = calculate_c_1_plus_plus_longitudinally_polarized(
                lepton_polarization,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            # (2): The second part of the term is C0+, n = 1
            c_zero_plus_n = calculate_c_1_zero_plus_longitudinally_polarized(
                lepton_polarization,
                target_polarization,
                squared_Q_momentum_transfer,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                shorthand_k,
                verbose)
            
        elif n_number == 2:

            # (1): We compute the first part of the term: C++, n = 2
            c_plus_plus = calculate_c_2_plus_plus_longitudinally_polarized(
                lepton_polarization,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                verbose)

            # (2): The second part of the term is C0+, n = 2
            c_zero_plus_n = calculate_c_2_zero_plus_longitudinally_polarized(
                lepton_polarization,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

        elif n_number == 3:

            # (1): We compute the first part of the term: C++, n = 3
            c_plus_plus = 0.

            # (2): The second part of the term is C0+, n = 3
            c_zero_plus_n = 0.

        # (3): Calculate the curly C_{++} contribution - requires both n and the CFFs:
        curly_c_plus_plus = calculate_curly_C_plus_plus_longitudinally_polarized_interference(
            n_number,
            lepton_polarization,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            t_prime,
            k_tilde,
            shorthand_k,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h_real_part,
            compton_form_factor_h_tilde_real_part,
            compton_form_factor_e_real_part,
            compton_form_factor_e_tilde_real_part,
            verbose)


        # (4): Calculate the curly C_{+0} contribution - requires both n and the CFFs:
        curly_c_zero_plus = calculate_curly_C_zero_plus_longitudinally_polarized_interference(
            n_number,
            lepton_polarization,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            k_tilde,
            shorthand_k,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compute_cff_effective(skewness_parameter, compton_form_factor_h_real_part),
            compute_cff_effective(skewness_parameter, compton_form_factor_h_tilde_real_part),
            compute_cff_effective(skewness_parameter, compton_form_factor_e_real_part),
            compute_cff_effective(skewness_parameter, compton_form_factor_e_tilde_real_part),
            verbose)
        
        # (5): Calculate the entire thing:
        print(c_plus_plus)
        print(curly_c_plus_plus)
        print(c_zero_plus_n)
        print(curly_c_zero_plus)
        print(c_minus_plus_n)
        print(curly_c_minus_plus)
        c_n_interference_coefficient = c_plus_plus * curly_c_plus_plus + c_zero_plus_n * curly_c_zero_plus + c_minus_plus_n * curly_c_minus_plus
        print(f"c_n_interference_coefficient: {c_n_interference_coefficient}")
        
        # (): If verbose, print the output:
        if verbose:
            print(f"> Calculated c_{n_number} interference coefficient to be:\n{c_n_interference_coefficient}")

        # (): Return the coefficient:
        return c_n_interference_coefficient
    
    except Exception as ERROR:
        print(f"> Error in c_{n_number} contribution to the interference term: \n> {ERROR}")
        return 0