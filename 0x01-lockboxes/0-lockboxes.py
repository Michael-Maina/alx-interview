#!/usr/bin/python3
"""Lockboxes Interview Question"""


def canUnlockAll(boxes):
    """
    Function to determine if all boxes can be open with the keys available
    """
    given_keys = boxes[0]
    all_keys = []
    for count, key in enumerate(given_keys, 1):
        # print(f"Initial {given_keys}")
        # print(f"Key {key}")
        all_keys = given_keys.copy()
        all_keys.extend(boxes[key])

        # Removing duplicate keys
        for i in all_keys:
            if i not in given_keys:
                given_keys.append(i)

        print(f"After {given_keys} Count:{count} Boxes:{len(boxes)}")

        if (count == len(boxes)):
            return True

    return False
