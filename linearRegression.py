import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import make_scorer
from sklearn.model_selection import RepeatedKFold, GridSearchCV
from sklearn.preprocessing import MinMaxScaler

from svm_crossvalidate import cal_pearson


def declined(x, y):
    print(x)
    print(y)
    declined = []
    for i in range(0, len(x)):
        declined.append(int((y[i] - x[i]) <= -3))
    return np.array(declined)


def lr_CN():
    print('*** CN regression ***')
    CN = pd.read_csv('./data/reg_CN.csv')
    y_CN = CN.pop('deltaMMSE')
    X_CN = MinMaxScaler().fit_transform(CN.values)
    lr = LinearRegression()
    cv = RepeatedKFold(n_splits=10, n_repeats=5, random_state=0)
    scoring = make_scorer(cal_pearson)
    grid = GridSearchCV(lr, {}, scoring=scoring, cv=cv, return_train_score=False, iid=True)
    grid.fit(X_CN, y_CN)
    cn = grid.best_estimator_
    print('best score:', grid.best_score_)
    # print('best params:', cn.get_params())


def lr_MCI():
    print('*** MCI regression ***')
    MCI = pd.read_csv('./data/reg_MCI.csv')
    y_MCI = MCI.pop('deltaMMSE')
    X_MCI = MinMaxScaler().fit_transform(MCI.values)
    lr = LinearRegression()
    cv = RepeatedKFold(n_splits=10, n_repeats=5, random_state=0)
    scoring = make_scorer(cal_pearson)
    grid = GridSearchCV(lr, {}, scoring=scoring, cv=cv, return_train_score=False, iid=True)
    grid.fit(X_MCI, y_MCI)
    mci = grid.best_estimator_
    print('best score:', grid.best_score_)
    # print('best params:', mci.get_params())


def lr_AD():
    print('*** AD regression ***')
    AD = pd.read_csv('./data/reg_AD.csv')
    y_AD = AD.pop('deltaMMSE')
    X_AD = MinMaxScaler().fit_transform(AD.values)
    lr = LinearRegression()
    cv = RepeatedKFold(n_splits=10, n_repeats=5, random_state=0)
    scoring = make_scorer(cal_pearson)
    grid = GridSearchCV(lr, {}, scoring=scoring, cv=cv, return_train_score=False, iid=True)
    grid.fit(X_AD, y_AD)
    ad = grid.best_estimator_
    print('best score:', grid.best_score_)
    # print('best params:', ad.get_params())


def lr_CN_extra_data():
    print('*** CN regression ***')
    CN = pd.read_csv('./data/reg_CN_extra_data.csv')
    y_CN = CN.pop('deltaMMSE')
    X_CN = MinMaxScaler().fit_transform(CN.values)
    lr = LinearRegression()
    cv = RepeatedKFold(n_splits=10, n_repeats=5, random_state=0)
    scoring = make_scorer(cal_pearson)
    grid = GridSearchCV(lr, {}, scoring=scoring, cv=cv, return_train_score=False, iid=True)
    grid.fit(X_CN, y_CN)
    cn = grid.best_estimator_
    print('best score:', grid.best_score_)
    # print('best params:', cn.get_params())


def lr_MCI_extra_data():
    print('*** MCI regression ***')
    MCI = pd.read_csv('./data/reg_MCI_extra_data.csv')
    y_MCI = MCI.pop('deltaMMSE')
    X_MCI = MinMaxScaler().fit_transform(MCI.values)
    lr = LinearRegression()
    cv = RepeatedKFold(n_splits=10, n_repeats=5, random_state=0)
    scoring = make_scorer(cal_pearson)
    grid = GridSearchCV(lr, {}, scoring=scoring, cv=cv, return_train_score=False, iid=True)
    grid.fit(X_MCI, y_MCI)
    mci = grid.best_estimator_
    print('best score:', grid.best_score_)
    # print('best params:', mci.get_params())


def lr_AD_extra_data():
    print('*** AD regression ***')
    AD = pd.read_csv('./data/reg_AD_extra_data.csv')
    y_AD = AD.pop('deltaMMSE')
    X_AD = MinMaxScaler().fit_transform(AD.values)
    lr = LinearRegression()
    cv = RepeatedKFold(n_splits=10, n_repeats=5, random_state=0)
    scoring = make_scorer(cal_pearson)
    grid = GridSearchCV(lr, {}, scoring=scoring, cv=cv, return_train_score=False, iid=True)
    grid.fit(X_AD, y_AD)
    ad = grid.best_estimator_
    print('best score:', grid.best_score_)
    # print('best params:', ad.get_params())


if __name__ == "__main__":
    print('#### without ADNI-MEM ADNI-EF data ####')
    lr_CN()
    lr_MCI()
    lr_AD()
    print('#### with ADNI-MEM ADNI-EF data ####')
    lr_CN_extra_data()
    lr_MCI_extra_data()
    lr_AD_extra_data()
