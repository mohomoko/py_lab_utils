import numpy as np


def round_to_n(x, n=1, rounding_number_out=False, debug=False):
    """
    round a number (an array) into its meaningful digits

    Args:
        x: float number.
        n: number of meaningful numbers. (default is 1.)
        rounding_number_out: if is True, rounding_number will be returned.
    Returns:
        rounded number (array)
        rounding_number (int): number for use in round() or np.round() module must be used for same result.
    """
    if x < 1e-6:
        print("Tiny input considered as '1e-6' !")
        x = 1e-6
    rounding_number = n - 1 - int(np.floor(np.log10(abs(x))))
    if debug:
        print('rounding_number:', rounding_number)
    if rounding_number_out:
        if rounding_number > 0:
            return np.round(x, rounding_number), rounding_number
        else:
            return np.round(x, rounding_number).astype(int), rounding_number
    else:
        if rounding_number > 0:
            return np.round(x, rounding_number)
        else:
            return np.round(x, rounding_number).astype(int)