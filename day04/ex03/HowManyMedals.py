#!/usr/bin/env python3
# -*-coding:utf-8 -*

import pandas as pd

def howManyMedals(df, name):
    """
    The function returns a dictionary of dictionaries giving the number and type of medals for each
    year during which the participant won medals.
    The keys of the main dictionary are the Olympic games years. In each year's dictionary, the
    keys are 'G', 'S', 'B' corresponding to the type of medals won (gold, silver, bronze). The
    innermost values correspond to the number of medals of a given type won for a given year.
    :param df: Pandas dataframe
    :param name: Participant Name
    :return: a dictionary of dictionaries giving the number and type of medals for each
        year during which the participant won medals
    """
    # for year in df["Year"].values:
    #     print(year)
    sel_name = df["Name"] == name
    df_result = df[sel_name]
    count = {}
    for year in df_result["Year"]:
        sel_year = df_result["Year"] == year
        count[year] = dict(df_result[sel_year]["Medal"].value_counts())
    # count = {1992: {'Bronze': 1, 'Gold': 1}, 1994: {'Silver': 2, 'Bronze': 1}, 1998: {}, 2002: {'Gold': 2}, 2006: {'Gold': 1}}
    result = {}
    for year in count:
        try:
            gold = count[year]["Gold"]
        except KeyError:
            gold = 0
        try:
            silver = count[year]["Silver"]
        except KeyError:
            silver = 0
        try:
            bronze = count[year]["Bronze"]
        except KeyError:
            bronze = 0

        result[year] = dict(G=gold, S=silver, B=bronze)
    return result
