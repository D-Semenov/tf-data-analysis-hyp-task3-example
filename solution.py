import pandas as pd
import numpy as np


chat_id = 1474426447 # Ваш chat ID, не меняйте название переменной

def solution(x) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    import scipy.stats as sts
    alpha = 0.06 
    t_value, p_value = sts.ttest_1samp(a = x, popmean = 300)
    answer = p_value < alpha 
    # Не меняйте название функции и её аргументы
    return answer # Ваш ответ, True или False
