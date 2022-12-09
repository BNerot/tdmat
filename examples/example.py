from pathlib import Path
from sys import path
from pandas import read_csv, date_range, concat
from numpy import full, sin

from tdmat import read_PVGIS_TMY, get_weather, Weather, Building, Demand

buildings_list = list(Building._TD1.index.unique().dropna())[2:]

"""
READ ME
This file presents a simple example of thermal demands calculation for a building in Belgium, according to the new model.
"""



def basic_example():
    """
    This corresponds to:
    # multi-family house (MFH)
    # in Belgium (BE)
    # energy data from Tabula are given for national climate (N) (but our own climate is used here)
    # retrofitting level is advanced (003) (tabs 'charts 3' and 'calculation PDF 3' in Tabula webtool)
    """
    """
    i) pick a building on https://webtool.building-typology.eu or in buildings_list.
    It is described by the 'name' variable.
    """
    name = "BE.N.MFH.06.Gen.ReEx.001.003"

    """
    ii) create a Building object
    """
    building = Building(name)
    # print(building)

    """
    iii) create a Weather object
    """
    city = "Brussels"
    weather = get_weather(f"TMY_{city}_2005-2020.csv", f"SP_{city}.csv")

    """
    iv) create a Demand object
    """
    demand = Demand(building, weather, DHW_profile_draw_off=sin(range(8760))+2)

    """
    v) access the newly created demand profiles and show their main properties
    """
    print(f"The thermal demand of building\n{name}\nhas the following properties:\n", demand)
    df = demand.df.set_index(date_range("01/01/2019", freq="h", periods=8760))
    df.groupby(df.index.month).sum() \
        .plot.bar(title="Monthly demand (kWh/(m².month)", grid=True, figsize=(16, 9))

    return building, demand


building, demand = basic_example()
