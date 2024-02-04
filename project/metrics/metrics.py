from typing import List
from objects.eval import PREvalData


def accuracy_score(y_pred: List[str], y_pos: List[str]) -> float:
    if len(y_pred) != len(y_pos):
        raise Exception("both arrays must have the same length")

    if len(y_pred) == 0:
        raise Exception("lists may not be empty")
    tp = 0
    for pred, pos in zip(y_pred, y_pos):
        if pred == pos:
            tp = tp + 1

    return tp / len(y_pred)


def precision_score(y_pred: List[str], y_pos: List[str]) -> PREvalData:
    if len(y_pred) != len(y_pos):
        raise Exception("both arrays must have the same length")

    if len(y_pred) == 0:
        raise Exception("lists may not be empty")

    str_to_int = dict()
    i = 0
    for pos, pred in zip(y_pos, y_pred):
        if pos not in str_to_int:
            str_to_int[pos] = i
            i = i + 1
        if pred not in str_to_int:
            str_to_int[pred] = i
            i = i + 1

    int_to_str = {v: k for k, v in str_to_int.items()}
    y_pos_int = []
    y_pred_int = []
    for pos, pred in zip(y_pos, y_pred):
        y_pos_int.append(str_to_int[pos])
        y_pred_int.append(str_to_int[pred])

    precisions = dict()

    tp_all = 0
    fp_all = 0

    for cl in list(str_to_int.values()):
        tp = 0
        fp = 0
        for pos, pred in zip(y_pos_int, y_pred_int):
            if pred == cl and pred == pos:
                tp = tp + 1
                tp_all = tp_all + 1
            if pred == cl and pred != pos:
                fp = fp + 1
                fp_all = fp_all + 1

        if tp == 0 and fp == 0:
            precision = 0
        else:
            precision = tp / (tp + fp)
        precisions[int_to_str[cl]] = precision

    precision_all = 0
    if tp_all == 0 and fp_all == 0:
        precision_all = 0
    else:
        precision_all = tp_all / (tp_all + fp_all)

    return PREvalData(precision_all, precisions)
