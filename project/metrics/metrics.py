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
        tp = sum(1 for pos, pred in zip(y_pos_int, y_pred_int)
                 if pred == cl and pred == pos)
        fp = sum(1 for pos, pred in zip(y_pos_int, y_pred_int)
                 if pred == cl and pos != cl)
        tp_all += tp
        fp_all += fp

        if tp == 0 and fp == 0:
            precision = 0
        else:
            precision = tp / (tp + fp)
        precisions[int_to_str[cl]] = precision

    precision_all = 0
    if tp_all != 0 or fp_all != 0:
        precision_all = tp_all / (tp_all + fp_all)

    return PREvalData(precision_all, precisions)


def recall_score(y_pred: List[str], y_pos: List[str]) -> PREvalData:
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

    recalls = dict()

    tp_all = 0
    fn_all = 0

    for cl in list(str_to_int.values()):
        tp = sum(1 for pos, pred in zip(y_pos_int, y_pred_int)
                 if pred == cl and pred == pos)
        fn = sum(1 for pos, pred in zip(y_pos_int, y_pred_int)
                 if pred != cl and pos == cl)

        tp_all += tp
        fn_all += fn

        if tp == 0 and fn == 0:
            recall = 0
        else:
            recall = tp / (tp + fn)
        recalls[int_to_str[cl]] = recall

    recall_all = 0
    if tp_all != 0 or fn_all != 0:
        recall_all = tp_all / (tp_all + fn_all)

    return PREvalData(recall_all, recalls)


def f1_score(y_pred: List[str], y_pos: List[str]) -> PREvalData:
    recall: PREvalData = recall_score(y_pred=y_pred, y_pos=y_pos)
    precision: PREvalData = precision_score(y_pred=y_pred, y_pos=y_pos)

    recall_all = recall.all
    precision_all = precision.all

    f1_all = 2 * precision_all * recall_all / (precision_all + recall_all)

    f1_singles = dict()

    for (cl, r), (_, p) in zip(list(recall.singles.items()), list(precision.singles.items())):
        if (p + r > 0):
            f1 = 2 * p * r / (p + r)
        else:
            f1 = 0
        f1_singles[cl] = f1
    return PREvalData(f1_all, f1_singles)
