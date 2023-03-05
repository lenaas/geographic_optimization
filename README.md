# Geographic Optimization

## General Structure of the project
- driving_distance_calc.ipynb : Notebook to calculate the driving distance between compounds and every possible German zipcode.
  Whenever new compounds are added, just execute the notebook inserting the right csv file 
  (the csv file with the new data needs to be in the same directory!)
  
## *Driving Distance Calculation with OpenStreetMap*:

### GOAL:
- Calculation of the driving distances between every German zip code and every compound for further analysis purposes.

### REQUIREMENTS:
- Easy to maintain and to understand for business users.

### WHAT WAS DONE:
- Usage of Dataframes from Distance Calculation (Dataframes with coordinates calculated by ´pgeocode´).
- Usage of OpenStreetMap to get driving distance by car via API requests. For this, also using ´json´ to store the responses temporary in a readable way and to access properly. Please be aware that the calculated distances are in meters. To get kilometers, conversion is needed.

### WHY WAS IT DONE THIS WAY:
- Usage of OpenStreetMap instead of Google Maps API as OpenStreetMap is free.

### COSTS:
- No direct costs associated due to usage of free OpenStreetMap.

### MAINTENANCE:
- Low maintenance. Whenever new data arises, just export as csv (use the same file name as in the code) and rerun the notebook.



## *Heatmap*

### GOAL:
- Getting a visual representation of which cars are demanded by which customers in which regions of Germany.

### REQUIREMENTS:
- Easy to get the information the business users are looking for.
- Possibilities to filter.

### WHAT WAS DONE:
- Usage of ´bokeh´ as this provides interactive maps which can be downloaded and seen as html file.
- Usage of ´plotly´ for comparison.

### WHY WAS IT DONE THIS WAY:
- Bokeh is one of the new rising visualization libraries. The opportunity to zoom in etc. makes it more attractive than the standard libraries. 
Also, as the plots can be filtered etc. in html, it shields the business user from the code. There are also many ways to actually visualize the data. In the project, only the standard was used due to a tight schedule.(Reference project : https://towardsdatascience.com/level-up-your-visualizations-make-interactive-maps-with-python-and-bokeh-7a8c1da911fd / https://colab.research.google.com/drive/1G2QGZO78CRMRNTXqcct48pBaSLLLhpK_?usp=sharing#scrollTo=j1blTDkc0nta).

### COSTS:
- No direct costs associated.

### PERFORMANCE:
- Fast results. 

### MAINTENANCE:
- Code has to be adapted whenever new data arises (minor changes). Also, for every possible column in the Dataframe, another heatmap is needed. 

### TO KEEP IN MIND FOR FUTURE IMPLEMENTATIONS / RECOMMENDATIONS:
- Usage of better geospatial data (https://www.igismap.com/download-germany-administrative-boundary-shapefiles-states-districts-postal-codes/). Would be $19 (one time pay). It's a different approach than used right now (way less code needed). 
- Stumbled across the opportunity to create dashboards in Python. Could be a great way to have all the different heatmaps in one place but further investigation is needed therefore. 


