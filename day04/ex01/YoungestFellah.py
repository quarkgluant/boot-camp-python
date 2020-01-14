#!/usr/bin/env python3
# -*-coding:utf-8 -*

import pandas as pd


def youngestFellah(df, year):
    male = df["Sex"] == "M"
    female = df["Sex"] == "F"
    sel_year = df["Year"] == year
    age_male = df[male & sel_year]["Age"].min()
    age_female = df[female & sel_year]["Age"].min()
    return dict(f=age_female, m=age_male)