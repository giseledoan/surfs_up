# Surfs_up Statistical Analysis

## A. Overview of the Analysis

### This project is to analyze temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round. 

## B. Results
From the hawaii.sqlite file, the analysit writes a query that filters the date columns in the Measurement table retrieve all the temperatures for the month of June and December. 

### B.1 Summary statistics for June temperature
![alt text](https://github.com/giseledoan/surfs_up/blob/main/Resources/June_temps.png?raw=true)
### B.2 Summary statistics for December temperature
![alt text](https://github.com/giseledoan/surfs_up/blob/main/Resources/Dec_temps.png?raw=true) 
### B.3 Three key differences in weather between June and December.
- The average temperatures in June and December do not have much different: mean 74.94 June vs. mean 71.04 Dec.
- The minimum temperature in December is much lower than that of June: 64 in June vs 56 in December. 
- The maximum temperatures in December and June do vary much: 85 in June vs 83 in December. 
## C. Summary
- The temperatures in June (summer) and December (winter) in Oahu demonstrate very little difference. That the temperature in Dec is as high as that of summer is a signal of warm weather during the year. This is good for ice cream sales. 
- Since we query temperatures in June and Decembers for all years since 2010, the result may not accurate as temperatures change year by year. We can improve that by filter temperatures in June and December in the last year starting from the last data point in the database. 
`prev_year = dt.date(2017, 8, 23)`
- Calculate the date one year from the last date in data set.
`prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)`
- Extracts all of the results from our query and put them in a list
`results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()`