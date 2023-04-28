#!/usr/bin/python3


"""
alx interview on lockboxes

"""


def box_object(boxes):
    """This function turns the boxes to objects"""

    output = []
    for box in boxes:
        output.append({
                      'box': box,
                      'unlocked': False
                      })
    output[0]['unlocked'] = True
    return output

# function that checks if the boxes are unlocked
def canUnlockAll(boxes):
    """function that tries to unlock all boxes"""


    inputs = box_object(boxes)
    for idx in range(len(inputs)):
        box = inputs[idx]['box']
        unlocked = inputs[idx]['unlocked']
        for lists in box:
            if not unlocked:
                for elements in boxes:
                    if unlocked:
                        break
                    for element in elements:
                        if element == idx:
                            unlocked = True
                            break
            else:
                break

    return unlocked
