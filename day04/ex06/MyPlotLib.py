#!/usr/bin/env python3
# -*-coding:utf-8 -*

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class MyPlotLib:
    def histogram(self, data, features):
        """
        plots one histogram for each numerical feature in the list
        :param data:
        :param features:
        :return:
        """
        fig, ax = plt.subplots()
        for feature in features:
            # if empDfObj.dtypes['Name'] == np.object:
            if data.dtypes[feature] != np.object:
                ax.hist(data[feature], range=(0, 5))
                plt.show()

    def density(self, data, features):
        """
        plots the density curve of each numerical feature in the list
        :param data:
        :param features:
        :return:
        """
        sns.set_style('whitegrid')
        for feature in features:
            if data.dtypes[feature] != np.object:
                sns.kdeplot(data[feature])

    def pair_plot(self, data, features):
        """
        plots a matrix of subplots (also called scatter plot
        matrix). On each subplot shows a scatter plot of one numerical variable against another one.
        The main diagonal of this matrix shows simple histograms.
        :param data:
        :param features:
        :return:
        """
        sns.pairplot(data[features])

    def box_plot(self, data, features):
        """
        displays a box plot for each numerical variable in the
        dataset.
        :param data:
        :param features:
        :return:
        """
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.boxplot(data[features].values)
        ax.set_xticklabels(features, rotation=90)
        # plt.xticks(rotation=90)
        ax.set_ylim(0, 5)
        plt.show()