"""Elevator level"""
import numpy as np


def elevator_algo(new_lvl, elevators):
    """

    :param new_lvl:
    :param elevators:
    :returns elevators_updated:
    """
    # Calculate distance between new level and the current
    # elevator levels
    dist_vec = np.abs(np.subtract(new_lvl, elevators))

    # Find out which is the closest one
    elevator_idx = np.argmin(dist_vec)

    # Create new positions after movement
    elevators_new = np.copy(elevators)
    elevators[elevator_idx] = new_lvl

    return elevators

