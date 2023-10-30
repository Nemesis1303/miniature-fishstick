# miniature-fishstick

Example 1:

```bash
curl -X POST 'http://kumo01:8080/topiclabeller/getLabel/' \
-H 'accept: application/json' \
--data-urlencode "chemical_description=water, wastewater, pollution, groundwater, exposure, contaminant, contamination, treatment, drinking_water, remediation, heavy_metal, waste, chemical, pesticide, drink_water"
```

Example 2:

```bash
curl -X POST 'http://kumo01:8080/topiclabeller/getLabels/' \
-H 'accept: application/json' \
--data-urlencode "chemical_description=['water, wastewater, pollution, groundwater, exposure, contaminant, contamination, treatment, drinking_water, remediation, heavy_metal, waste, chemical, pesticide, drink_water',
 'forest, climate, climate_change, adaptation, tree, flood, mitigation, drought, wood, hazard, vulnerability, land, forestry, resilient, carbon',
 'food, milk, meat, wine, food_safety, ingredient, nutritional, agri_food, diet, nutrition, health, waste, consumption, chain, olive_oil',
 'farming, agriculture, crop, soil, food, organic, plant, irrigation, fertilizer, pesticide, fertiliser, multi_actor, pest, yield, nutrient',
 'climate, internal_combustion_engine, arctic, electro_optical, climate_change, atmospheric, satellite, copernicus, earth_observation, observation, sea_ice, earth, remote_sensing, ice_sheet, forecast',
 'soil, carbon, carbon_dioxide, atmospheric, air_quality, flux, emission, atmosphere, microbial, aerosol, air_pollution, climate, plant, atmospheric_carbon, carbon_cycle',
 'biodiversity, ecological, ecosystem, climate_change, landscape, habitat, restoration, biodiversity_ecosystem, ecology, coral_reef, es, tropical_forest, tropical, coral, specie',
 'mineral, earth, isotope, geological, sediment, rock, proxy, reconstruct, stable_isotope, deposit, past, isotopic, mining, record, reconstruction',
 'ocean, marine, sea, coastal, microplastic, phytoplankton, deep_sea, marine_ecosystem, southern_ocean, oceanic, coast, plastic, diatom, atlantic, underwater',
 'aquaculture, fish, microalgae, fishery, algae, seaweed, farming, seafood, marine, fishing, salmon, feed, food, biomass, catch']"
```