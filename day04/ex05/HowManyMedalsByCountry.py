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