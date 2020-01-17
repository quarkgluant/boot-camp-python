#!/usr/bin/env python3
# -*-coding:utf-8 -*

import pandas as pd

def howManyMedalsByCountry(df, country):
    """
    The function returns a dictionary of dictionaries giving the number and type of medal for each
    competition where the country team earned medals.
    The keys of the main dictionary are the Olympic games' years. In each year's dictionary, the
    key are 'G', 'S', 'B' corresponding to the type of medals won.
    Duplicated medals per team games should be handled and not counted twice
    :param df: Pandas dataset which contains dataFrame
    :param country: country name
    :return: a dictionary of dictionaries giving the number and type of medal for each
    competition where the country team earned medals.
    """
    sel_team = df["Team"] == country
    df_result = df[sel_team]
    count = {}
    for year in df_result["Year"]:
        sel_year = df_result["Year"] == year
        count[year] = dict(df_result[sel_year]["Medal"].value_counts())
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

if __name__ == '__main__':
    from FileLoader import FileLoader
    loader = FileLoader()
    data = loader.load('../athlete_events.csv')
    how_many_france = howManyMedalsByCountry(data, 'France')
    print(how_many_france)