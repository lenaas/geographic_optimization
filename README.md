# Geographic Optimization

1. Distance Calculation:
  WHAT WAS DONE:
 - Loading csv into Dataframes.
 - Usage of ´´´pgeocode´´´to derive coordinates from zip code.
 - Usage of ´´haversine´´´to calculate the (angular) distances between the coordinates.

WHY WAS IT DONE THIS WAY:
 - Usage of Haversine metric to provide more exact results than using Euklidean distance as Haversine takes in account that the Earth is not flat. 
 (Overview over the reasons here: https://towardsdatascience.com/calculating-distance-between-two-geolocations-in-python-26ad3afe287b).
- The calculated distance is not the driving distance between compound and customer. 

WHAT COULD BE BETTER IN FUTURE IMPLEMENTATIONS:
- The calculated distance is not the driving distance between compound and customer. Ex: A distance of 40 km as the crow flies can, if covered by car, result in a driven distance of 45km or similar. A driving distance could also be calculated (see https://towardsdatascience.com/driving-distance-between-two-or-more-places-in-python-89779d691def#1c17). For this, API calls are necessary. Apparently there are next to costly GoogleMapsAPI also open source alternatives which work quite well. The free alternatives just don't offer Real-Time-Traffic-Warnings, but as this is not needed, OpenStreetMap or OSMR could be used.

COSTS FOR CURRENT IMPLEMENTATION:
- No direct costs. 

PERFORMANCE FOR CURRENT IMPLEMENTATION:
- Fast calculation of distances due to usage of pandas functions. Results can be expected within less than 5 minutes.

