class SpatioTemporalData:
    """
    • when(location) : This method takes a location as an argument and returns a list
    containing the years where games were held in the given location.
    • where(date) : This method takes a date as an argument and returns the location where
    the Olympics took place in the given year
    """
    def __init__(self, df):
        self.df = df

    def when(self, location):
        """
         This method takes a location as an argument and returns a list
        containing the years where games were held in the given location.
        :param location:
        :return: a list containing the years where games were held in the given location.
        """
        sel_city = self.df["City"] == location
        return self.df[sel_city]["Year"].unique()

    def where(self, date):
        sel_year = self.df["Year"] == date
        return self.df[sel_year]["City"].unique()
