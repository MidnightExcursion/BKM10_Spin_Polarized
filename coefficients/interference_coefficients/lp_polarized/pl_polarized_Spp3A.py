try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

def calculate_s_3_plus_plus_longitudinally_polarized_A(
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float,
    t_prime: float,
    shorthand_k: float,
    verbose: bool = True) -> float:
    """
    """

    try:

        # (1): Calculate the recurrent quantity sqrt(1 + epsilon^2):
        root_one_plus_epsilon_squared = np.sqrt(1. + epsilon**2)

        # (2): Calculate the main contribution:
        multiplicative_contribution = squared_hadronic_momentum_transfer_t * t_prime * (1. + root_one_plus_epsilon_squared - 2. * x_Bjorken) / squared_Q_momentum_transfer**2

        # (3): Calculate the coefficient
        prefactor = -8. * target_polarization * shorthand_k * (1. - lepton_energy_fraction_y - lepton_energy_fraction_y**2 * epsilon**2 / 4.) / root_one_plus_epsilon_squared**6

        # (4): Calculate the coefficient:
        s_3_plus_plus_A_LP = prefactor * multiplicative_contribution

        # (4.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated s_3_plus_plus_A_LP to be: {s_3_plus_plus_A_LP}")

        # (5): Return the coefficient:
        return s_3_plus_plus_A_LP

    except Exception as ERROR:
        print(f"> Error in calculating s_3_plus_plus_A_LP for Interference Term:\n> {ERROR}")
        return 0