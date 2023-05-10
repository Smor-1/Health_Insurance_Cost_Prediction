# Predicting Health Insurance Costs

## Roles & Responsibilities
|  Name  | Role Week 1 | Role Week 2 |  Role Week 3 |
|:--------:|:--------:|:--------:|:--------:|
| Massimo | Data Engineer  |  Data Exploration / Presentation |  TBD  |
| Roza | Data Scientist  |  Readme Management / Project Description Write Up  |  TBD  |
| Mark | Project Manager / GitHub Cleanup  |  Presentation / Tabeleau |  TBD  |
| Sandy | Readme Management / Project Description Write Up  |  Data Scientist |  TBD  |

## Background & Rationale

It is well known that how much an individual pays for insurance policies are very case dependent. One person may be paying a lot more than another due to seemingly unknown factors. In the case of health insurance, various lifestyle situations such as being a smoker, having more than one child or even the region you live in has an impact on how much you are charged. 

Therefore, in this project, we set out to create a machine learning algorithm to predict health insurance charges. This knowledge would benefit both insurers and beneficiaries. 

## Research Questions

There are two main questions we wanted to answer in this endeavour: 
1) What model is most predictive of how much someone is charged for health insurance? 
2) What factors in this dataset are most influential of how much someone is charged for health insurance? 

## Dataset 

There are seven columns and 1338 non-null rows in this dataset, columns include: 
* Age: Age of the primary beneficiary
* Sex: Male or Female
* BMI: Body Mass Index of the primary beneficiary
* Children: Number of children covered by health insurance / number of dependents
* Smoker: Smoking status, either Yes or No 
* Region: The US resedential area: Northeast, Northwest, Southeast or Southwest
* Charges: Individual medical costs billed by health insurance 

![Image](Insurance.png)

The source for the dataset is https://www.kaggle.com/datasets/mirichoi0218/insurance

## Database
To hold our data we are using a postgres relational database with two tables. Each patient is assigned a unique Identifier which relates our tables, "info" contains information on each patient and "charges" cointain their insurance charges as well as their location. The Schema is provided in schema.sql as well as a join statement to bring the tables together in joins_queries.sql.

### ERD

![Image](Resources/Database_ERD.png)

## Data Exploration
To explore the data histogram of the columns will show how our data looks like. The age distribution is shown in the next graph

![age distribution](Resources/histo_age.png)

It is looks like that we have data for all ages which is a good start. Now lets take a look at the BMI distribution.

![BMI distribution](Resources/histo_BMI.png)

BMI has fairly normal distribution and it should work for our data analysis. Next number of the childeren

![childeren distribution](Resources/histo_childeren.png)

This is what we expected, but it should be noted that there is not enough information for higher than 4 childeren in the dataset. Next let's explore our target in machin learning section which is the cost of the health insurance.

![charges distribution](Resources/histo_charges.png)

It seems that our data is right skewed which means that we will have to deal with it somehow. For now lets explore more and find out if there is relation between sex of the individual to the charges they pay by getting a mean. 

![mean sex](Resources/mean_sex.png)

It seems that male individual are paying a bit more than female individuals. Next lets take a look at the regions.

![mean region](Resources/mean_region.png)

Simlarly they are close to each other but we can say that south east region is paying more but at the same time it has a higher BMI so we need to dig deeper. Now lets check if the number of childeren has an effect on our data.

![mean childeren](Resources/mean_childeren.png)

It seems that individual with 3 childeren has to pay more, but still this is early to predict this. Now lets take a look at the average of charges for each age group.

![mean age plot](Resources/mean_age_plot.png)

There is an obvious trend here. As it can be seen the older an individual gets, he or she has to pay more for the insurance. lastly let's take a look at the effect of being smoker on the amount of the payment in insurance.

![mean smoker](Resources/mean_smoker.png)

The differnece is huge. It seems that being an smoker is bad for both your health and finances. Lets go deeper and seprate the charges for smoker and non smokers.

![charges smoker vs non-smoker](Resources/charges_smoker_non_smoker.png)

It can be seen that where the non-smoker charges nearly ends (15000) smoker charges just starts and goes higher. Next lets plot them sepratly with age to see if still age is effective parameters compare to being smoker.

![smoker vs charge](Resources/smoker_charge.png) ![non-smoker vs charge](Resources/non_smoker_charge.png)

As it can be seen, in the data there is 2 catagory in each plot e.g. high paying smokers, low paying smoker, high paying non-smoker and low paying non-smokers. Most of our data is low paying non-smokers that we should be aware of. The difference between high paying and low paying is still under investigation as well.

## Machine learning method 
In this study we have continuous data for charges, therefore regression method should be used. Generating seaborn heatmap confirms that the charges are very dependent on being smoker or not as we found out in the data exploration phase.

![Heat map](Resources/heatmap.png)

According to this heatmap, smoker, age and BMI are the main contributer and have a strong contribution to the charges column.
Machin learning models that are used are LinearRegression, DecisionTreeRegressor, RandomForestRegressor and Nural Network (not completed yet). The results are summarized in the next table:

|  Model  | Mean Squared | R Squared |
|:--------:|:--------:|:--------:|
| LinearRegression |  37068872  |  TBD  |
| DecisionTreeRegressor |  41378968  |  TBD  |
| RandomForestRegressor |  29639376  |  TBD  |
| Nural Network |  TBD  |  TBD  |


Up to now the best result that we got is from Random Forest Regressor. The following pictures are showing predicted model versus actual data for age and bmi. The input for our model are age, sex, BMI, number of children, Being smoker or not and the region. The out put of our model is the individual medical costs billed by the health insurance.

![age vs charge](Resources/RandomForestRegressor_age_charges.png)

![age vs charge](Resources/RandomForestRegressor_bmi_charges.png)

## Dashboard Design
The presentation of the data will be structured in columns across the display. The dashboard features visualizations that represent the main data points prominently on the left side, along with written details which explain the data and the application of this information. The dashboard will feature a large area that will have a space for viewers to input different data points of their own, and these will generate visualizations that correspond to those point. This may be one single chart or several to adequately represent the infomation being called.

![Dashboard_Draft_1](https://user-images.githubusercontent.com/119453505/236359817-37a3d8b3-70d5-4e41-b40a-748b537c2a4f.png)



## Conclusion and Ansewring Research Questions

1) What model is most predictive of how much someone is charged for health insurance? 

Currently Random Forest Regressor but we are suspecting that nural network will have a better results.

3) What factors in this dataset are most influential of how much someone is charged for health insurance? 

Being smoker is one of the main influential parameters for determining health insurance. The next parameters are age and BMI. Parameters such as sex, number of childeren and region are not as important as the rest of parameters  

## Technologies, languages, tools, and algorithms
<p align="center">
<img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" alt="Python" height="40" style="vertical-align:top; margin:4px">
<img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/visual-studio-code/visual-studio-code.png" alt="VS Code" height="40" style="vertical-align:top; margin:4px">
<img src="https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original.svg" alt="PostgreSQL" height="40" style="vertical-align:top; margin:4px">
<img src="https://github.com/devicons/devicon/blob/master/icons/jupyter/jupyter-original.svg" alt="Jupyter" height="40" style="vertical-align:top; margin:4px">
<img src="https://financeandbusiness.ucdavis.edu/sites/g/files/dgvnsk4871/files/styles/sf_landscape_16x9/public/images/article/tableau_logo_2.png?h=c673cd1c&itok=Xie5DAhG" alt="Tableau" height="40" style="vertical-align:top; margin:4px">
<img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/javascript/javascript.png" alt="Javascript" height="40" style="vertical-align:top; margin:4px">
<img src="https://github.com/devicons/devicon/blob/master/icons/html5/html5-original.svg" alt="HTML" height="40" style="vertical-align:top; margin:4px">
<img src="https://github.com/devicons/devicon/blob/master/icons/css3/css3-original.svg" alt="CSS" height="40" style="vertical-align:top; margin:4px">
</p>
Liberaries that are used : Pandas, numpy, Matplotlib, hvplot, plotly, random, string, pickle, seaborn and sklearn 
Machin learning models used: PCA, LinearRegression, DecisionTreeRegressor, RandomForestRegressor and Nural Network
