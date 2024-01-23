"""Estimate the value of Pi with Monte Carlo simulation.
Author:  Steven Sanchez-Jimenez
Credits:  TBD
"""

import random
import doctest
import points_plot

GOOD_PI = 3.141592653589793  # A very good estimate, from math.pi
SAMPLES = 1_000  # More => more precise, but slower


def in_unit_circle(x: float, y: float) -> bool:
    """Returns True if and only if (x,y) lies within the circle with origin (0,0) and radius (1,0)
    >>>in_unit_circle(0,0)
    True
    >>>in_unit_circle(1.0,1.0)
    False

    #you were wondering, weren't you?
    >>>in_unit_circle(0,-0.5)
    True
    >>>in_unit_circle(-0.9,-0.5)
    False

    """


def rand_point_unit_sq() -> tuple[float, float]:
    """Returns random x,y in 0..1.0, 0..1.0"""
    x = random.random()
    y = random.random()
    return x, y


a, b = rand_point_unit_sq()


def plot_random_points(n_points: int = 500):
    """Generate and plot n_points points in interval (0,0) to (1,1).
    Creates a window and prompts the user before closing it"""
    points_plot.init()
    for i in range(n_points):
        x, y = rand_point_unit_sq()
        points_plot.plot(x, y, color_rgb=(255, 10, 10))  ## Red
        points_plot.plot(x, y, color_rgb=(240, 240, 240))  ## Grey
    points_plot.wait_to_close()


def relative_error(est: float, expected: float) -> float:
    """Relative error of estimate (est) is a non-negative fraction of the actual value.
     Note estimate and expected are NOT interchangeable(see test cases).
     For example, if expected value is 5.0 but estimate is 3.0, the
     absolute error is -2.0, but the relative error is 2.0/5.0 = 0.4.
     If the expected value is 3.0 but the estimate is 5.0, the
     absolute error is 2.0, but the relative error is 2.0/3.0 = 0.66.
     >>>round(relative_error(3.0,5.0), 2)
     0.4
     >>>round(relative_error(5.0,3.0), 2)
     0.67
     """
    abs_error = est - expected
    rel_error = abs(abs_error / expected)
    return rel_error


def pi_approx() -> float:
    """Return the estimate of pi by sampling random points
    >>>relative_error(pi_approx(), GOOD_PI) <= 0.01 #within 1%
    True
    >>>relative_error(pi_approx(), GOOD_PI) <= 0.01 #within 1%
    True
    >>>relative_error(pi_approx(), GOOD_PI) <= 0.01 #within 1%
    True"""


def main():
    doctest.testmod()
    # eyeball test of scattering points
    points_plot.init()
    estimate = pi_approx()
    print(f"Pi is approximately{estimate}")
    points_plot.wait_to_close()


if __name__ == "__main__":
    main()



