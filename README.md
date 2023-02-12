# Geographic Optimization

## 1. *Distance Calculation*:

### GOAL:
- Calculation of the distances between every German zip code and every compound for further analysis purposes.

### REQUIREMENTS:
- Easy to maintain and to understand for business users.

### WHAT WAS DONE:
 - Loading csv into Dataframes.
 - Usage of ´pgeocode´ to derive coordinates from zip code.
 - Usage of ´haversine´ to calculate the (angular) distances between the coordinates.

### WHY WAS IT DONE THIS WAY:
 - Usage of Haversine metric to provide more exact results than using Euklidean distance as Haversine takes in account that the Earth is not flat. 
 (Overview over the reasons here: https://towardsdatascience.com/calculating-distance-between-two-geolocations-in-python-26ad3afe287b).
- The calculated distance is not the driving distance between compound and customer. 

### COSTS:
- No direct costs. 

### PERFORMANCE:
- Fast calculation of distances due to usage of pandas functions. Results can be expected within less than 5 minutes.

### MAINTENANCE:
- Low maintenance. Whenever new data arises, just export as csv (use the same file name as in the code) and rerun the notebook.

### TO KEEP IN MIND FOR FUTURE IMPLEMENTATION / RECOMMENDATIONS:
- The calculated distance is not the driving distance between compound and customer. Ex: A distance of 40 km as the crow flies can, if covered by car, result in a driven distance of 45km or similar. A driving distance could also be calculated (see https://towardsdatascience.com/driving-distance-between-two-or-more-places-in-python-89779d691def#1c17). For this, API calls are necessary. Apparently there are next to costly GoogleMapsAPI also open source alternatives which are supposed to work quite well (like OpenStreetMap).


## 2. *Driving Distance Calculation with OpenStreetMap*:

### GOAL:
- Calculation of the driving distances between every German zip code and every compound for further analysis purposes.

### REQUIREMENTS:
- Easy to maintain and to understand for business users.

### WHAT WAS DONE:
- Usage of Dataframes from Distance Calculation (Dataframes with coordinates calculated by ´pgeocode´).
- Usage of OpenStreetMap to get driving distance by car via API requests. For this, also using ´json´ to store the responses temporary in a readable way and to access properly.

### WHY WAS IT DONE THIS WAY:
- Usage of OpenStreetMap instead of Google Maps API as OpenStreetMap is free..

### COSTS:
- No direct costs associated due to usage of free OpenStreetMap.

### PERFORMANCE:
- Bad performance due to 130k needed API calls (took roughly 18h). 
The reasons for this bad performance could be:
  - Calculations took place on a 'normal' MacBook.
  - The bottleneck could be on the side of OpenStreetMap. As it's an open-source tool, there are probably not that many servers to process the API 
    calls etc. 
  - Bad choice of the API call // need for restructuring the API call itself. 

### MAINTENANCE:
- Low maintenance. Whenever new data arises, just export as csv (use the same file name as in the code) and rerun the notebook.

### TO KEEP IN MIND FOR FUTURE IMPLEMENTATIONS / RECOMMENDATIONS:
- Usage of Google Maps API.
The driving distances are calculated between every possible German zipcode and every current compound. Therefore, a rerun is only necessary whenever new data is added to the input (new compound). Assuming this only happens max. twice per year, the costs of using Google's Distance Matrix API twice per year aren't too high as it's pay-as-you-go (currently 5$ per 1000 data elements) (https://mapsplatform.google.com/pricing/?hl=de&_gl=1%2A1puhgn4%2A_ga%2ANTUzOTcwOTMxLjE2NzYyMDk3ODk.%2A_ga_NRWSTWS78N%2AMTY3NjIwOTc4OS4xLjEuMTY3NjIwOTgzNy4wLjAuMA..#pricing-grid). This could not only lead to improved performance of the calculation itself, but is also a more 'elegant' way. It's not well seen if for commercial purposes with a lot of data open-source tools like OpenStreetMap are being used. Reason: Not much server capacity on their side. Calculation with Google Distance Matrix API could look like this:
https://www.geeksforgeeks.org/python-calculate-distance-duration-two-places-using-google-distance-matrix-api/ . As seen, the conversion in coordinates wouldn't even be necessary in this case which would make the notebook more accessible even for non-coders.


## 3. *Heatmap*

### GOAL:
- Getting a visual representation of which cars are demanded by which customers in which regions of Germany.

### REQUIREMENTS:
- Easy to get the information the business users are looking for.
- Possibilities to filter.


