# tdmat

## What does "tdmat" stand for?
tdmat stands for Thermal Demand Model Adapted from Tabula.

## What is it?
tdmat is a non-GUI tool that implements a simple thermal demand prediction model for european residential buildings.  
tdmat follows an approach similar to the one of the Tabula-Episcope research project [^1].  
It covers the space heating and space cooling demands and presents additional tools regarding domestic hot water demand.

[^1]: https://episcope.eu/building-typology/tabula-webtool/

## How does it work? 
The typical procedure is as follow:
1. tdmat reads buildings properties from the Tabula-Episcope database [^2]
[^2]: https://webtool.building-typology.eu/#bm
2. tdmat computes solar, transmission and ventilation contributions based on indoor setpoint temperature and weather data
3. tdmat put contributions together to create hourly profile of thermal demands

## When will it be available?
Both source code and Python 3 packages will be available by the end of 2022.
