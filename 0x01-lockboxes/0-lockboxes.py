#!/usr/bin/python3
"""A module to tackle the lockboxes problem."""


def checkBoxesForKey(boxes, ignore, key):
    """Checkseach inner box looking for the key needed
    to unlock the current box"""
    keyExists = False
    for idx, box in enumerate(boxes):
        if keyExists:
            break
        if idx is not ignore:
            for elem in box:
                if elem == key:
                    keyExists = True
                    break
    return keyExists


def canUnlockAll(boxes):
    """Unlocking boxes function. Checks if a list of boxes can be unlocked."""
    canUnlock = True
    for idx, box in enumerate(boxes):
        if idx == 0:
            continue
        key = idx
        if not checkBoxesForKey(boxes, idx, key):
            canUnlock = False
    return canUnlock
