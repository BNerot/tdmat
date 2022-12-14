# tdmat

## What does "tdmat" stand for?
"tdmat" stands for Thermal Demand Model Adapted from Tabula.

## What is it?
`tdmat` is a non-GUI tool that implements a simple thermal demand prediction model for european residential buildings.
`tdmat` follows an approach similar to the one of the Tabula-Episcope research project [^1].
It covers the space heating and space cooling demands and presents additional tools regarding domestic hot water demand. Load profiles follow an hourly time step.

[^1]: https://episcope.eu/building-typology/tabula-webtool/

## How does it work? 
The typical procedure is as follow:
1. `tdmat` reads buildings properties from the Tabula-Episcope database [^2]. Data is stored locally, no internet connection needed.

[^2]: https://webtool.building-typology.eu/#bm

2. `tdmat` computes solar, transmission and ventilation contributions based on indoor setpoint temperature and weather data
3. `tdmat` put contributions together to create hourly profile of thermal demands

##  Installation notes
The packaged version of `tdmat`is available on PyPi. Please run:
`pip install tdmat`


## Where is the project hosted?
Sources are managed on GitHub: https://github.com/BNerot/tdmat


## Is it difficult to use?
Please follow the example in `examples` as a quick start guide. 
You can also find a web version of the documentation in `docs/build/html`. Once this directory is downloaded, please open 'index.html'. 

## Copyright
The code is distributed under an Apache-2.0 license. 
Most of the development work was done in the context of a PhD thesis. 
This thesis was funded by two French institutions:
- Commissariat à l'Energie Atomique: https://www.cea.fr/english
- Agence de la transition écologique: https://www.ademe.fr/en/frontpage/



