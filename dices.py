#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

import random


def dice_cast(dice_faces):
    """Функция броска кубика с заданным количеством граней
    Параметры:
    dice_faces - количество граней кубика
    Возвращаемое значение: возвращает значение в виде целого числа в диапазоне от 1 до максимального
    количества граней кубика
    """
    rnd = random.randint(1, dice_faces)
    return rnd


def dice_casts(dice_faces, casts):
    """Функция броска сериии кубиков с заданным количеством граней
    Параметры:
    dice_faces - количество граней кубика
    casts      - количество бросков кубика
    Возвращаемое значение:    Возвращает значение в виде коллеции целых чисел в
    диапазоне от 1 до максимального количества граней кубика
    """
    rolls = []
    for _ in range(casts):
        rolls.append(dice_cast(dice_faces))
    return rolls


def remove_inferior_casts(dice_faces, casts, remove_casts):
    """Функция броска сериии кубиков с заданным количеством граней и удаления лишьних выпавших значений.
    Данная комбинация используется для наброса параметров персонажа.
    Параметры:
    dice_faces   - количество граней кубика
    casts        - количество бросков кубика
    remove_casts - количество удаляемых значений бросков
    Возвращаемое значение:    Возвращает значение в виде суммы выпавших кубиков
    """
    rolls = dice_casts(dice_faces, casts)
    rolls.sort()
    for _ in range(remove_casts):
        del rolls[0]
    return sum(rolls)


def remove_minimal_casts(casts, remove_casts, rolls):
    """Функция удаления из сериии бросков кубиков заданного количества бросков с минимальными значениями
    Параметры:
    casts      - список значений бросков кубика
    remove_casts - количество удаляемых значений бросков
    Возвращаемое значение:    Возвращает значение в виде коллеции целых чисел
    """
    casts.sort()
    for _ in range(remove_casts):
        del rolls[0]
    return casts


def shots_series_and_remove_casts(dice_faces, casts, remove_casts, shots):
    """Функция накидки серии бросков серии кубиков.
    Данная комбинация используется для наброса всех параметров персонажа за единственную итерацию.
    Параметры:
    dice_faces   - количество граней кубика
    casts        - количество бросков кубика
    remove_casts - количество удаляемых значений бросков
    shots        - Количество набросок
    Возвращаемое значение:    Возвращает значение в виде колекции параметров """
    rolls = []
    for _ in range(shots):
        rolls.append(remove_inferior_casts(dice_faces, casts, remove_casts))
    return rolls


class Dice:
    def __init__(self):
        pass


if __name__ == '__main__':
    print("Серия 6 набросов по 4ре кубика D6, с удалением 1 минимального: ", shots_series_and_remove_casts(6, 4, 1, 6))
    print("Наброс по 4ре кубика D6, с удалением 1 минимального и суммированием результата: ",
          remove_inferior_casts(6, 4, 1))
    print('Наброс по 4ре кубика D6: ', dice_casts(6, 4))
    print("Бросок кубика D6: ", dice_cast(6))
