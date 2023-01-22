#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

import random

def dice_cast(dice_faces):
    rnd = random.randint(1, dice_faces)
    return rnd

def dice_casts(dice_faces, casts):
    rolls = []
    for _ in range(casts):
        rolls.append(dice_cast(dice_faces))
    return rolls

def remove_inferior_casts(dice_faces, casts, remove_casts):
    rolls = dice_casts(dice_faces, casts)
    rolls.sort()
    for _ in range(remove_casts):
        del rolls[0]
    return sum(rolls)

def  shots_series_and_remove_casts(dice_faces, casts, remove_casts, shots):
    rolls = []
    for _ in range(shots):
        rolls.append(remove_inferior_casts(dice_faces, casts, remove_casts))
    print("Серия из ", shots, " набросок: ", rolls)

shots_series_and_remove_casts(6, 4, 1, 6)
