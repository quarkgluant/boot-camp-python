#!/usr/bin/env python3
# -*-coding:utf-8 -*

import pandas as pd

def proportionBySport(df, year, sport, gender):
    """
    The function returns a float corresponding to the proportion (percentage) of participants who
    played the given sport among the participants of the given gender.
    The function answers questions like the following : "What was the percentage of female
    basketball players among all the female participants of the 2016 Olympics?"
    Hint: here and further, if needed, drop duplicated sportspeople to count only unique ones.
    Beware to call the dropping function at the right moment and with the right parameters, in
    order not to omit any individuals.
    :param df: Pandas dataset
    :param year: olympic year
    :param sport: sport
    :param gender: M or F
    :return: percentage (float)
    """
    sel_gender = df["Sex"] == gender
    sel_year = df["Year"] == year
    sel_sport = df["Sport"] == sport
    players = df[sel_gender & sel_year & sel_sport]["Name"].nunique()
    total = df[sel_gender & sel_year]["Name"].nunique()
    return players / total
