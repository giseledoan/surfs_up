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
- 
## C. Summary

### C.1 Pivot table for B.1 analysis (Outcomes vs. Launch Dates)
+ Choosing the right fields to put into the right areas was a bit difficult for new Pivot table user. 
+ The analyst had to try putting the fields around, failed and tried in order to get the right table. 
### C.2 `COUNTIFS()` function for B.2 analysis (Outcomes vs. Goals)
+ This function was confusing when using with 2-number ranges like from 5,000 to 9,999.
+ The analyst added the second number as did with the first number but the formula failed. `=COUNTIFS(Kickstarter!D:D,">=5000"**,**Kickstarter!D:D,"<=9999"...)`
+ Then she realized there must be a space between 2 selections in order for the function operate. `=COUNTIFS(Kickstarter!D:D,">=5000"**, **Kickstarter!D:D,"<=9999"...)`
   
## D. Results

### D.1 Outcomes based on Launch Date

+ ***Ideal months:*** Summer is a good season to create crowdfunding campaign for theater. The ideal months are **May, June and July** because of 3 reasons:
	- They have the highest number of successful campaigns. 
	-  Although these 3 months have relatively high failed campaigns in comparison with the other months, the number of failed campaigns is just about 1/2 of the number of successful campaigns in the same months.
	-  Additionally, **July** has the second lowest cancellation number.

+ ****Bad months*:***
	- Although **October** has 0 cancellation, it is not a good month for crowdfunding because it has high failed number and that failed number is nearly equal the successful number in the same month. *(50 vs 65)*
	- **January** is the next bad month for crowdfunding. It has low successful number *(<60)*, high failed number and cancellation.

### D.2 Outcomes based on Goals
+ Successful campaigns have goals under $5,000. 
+ Higher failed percentage are of campaigns that have high goals from $45,000 to over $50,000

### D.3 Data set limitations
+ ***Outcomes based on launch dates:*** should have the percentage of successful, failed and canceled, not just the number of each outcome for more accurate analysis. 
+ ***Outcomes based on goals:*** Outcomes of the analysis in D.2 makes an impression that lower goals associate with higher successful percentage. However, the third highest failing goals is from $25,000 to $29,000 while one of the third highest successful goals is from $35,000 to $44,999. Apparently, dollar amount of goals is not a determinant in success. We should measure other data such as demographic and income of the participants for more thoughtful  analysis.

### D.4 Other possible tables and graphs

+ From the limitation of outcomes vs. launch date discussed above, we could create another table of program outcomes by percentage and create a chart based on that data.
