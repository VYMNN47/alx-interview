#!/usr/bin/python3
"""Module for canUnlockAll function"""


def canUnlockAll(boxes):
    """a func that determines if all the boxes can be opened."""
    keys = [0]
    opened = set([0])

    while keys:
        current_key = keys.pop(0)

        for key in boxes[current_key]:
            if key < len(boxes) and key not in opened:
                opened.add(key)
                keys.append(key)

    return len(opened) == len(boxes)
