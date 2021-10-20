"""Elevator level algorithm"""
import numpy as np


def elevator_algo(new_lvl, elevators):
    """Elevator algorithm for moving one elevator

    :param new_lvl: Which is the level choosen from dropdown
    :param elevators: Array with current elevator levels
    :returns elevators_updated: Array with updated elevator levels
    :returns lvl_diff: Difference between the old elevator and new lvl
    """
    # Calculate distance between new level and the current
    # elevator levels
    dist_vec = np.abs(np.subtract(new_lvl, elevators))

    # Find out which is the closest one
    elevator_idx = np.argmin(dist_vec)
    lvl_diff = np.min(dist_vec)  # How many levels diff

    # Update position
    elevators[elevator_idx] = new_lvl

    return elevators, lvl_diff
