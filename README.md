# House-Pricing-Regression
This is regression project on house price prediction.
The dataset I used to work on this project can be found [here.](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data) <br>
I hosted the regression web app on AWS and the link is [here](http://ec2-44-204-3-215.compute-1.amazonaws.com/) <br>
This project features:
### Data cleaning
As a data scientist, one will always come accross ___rogue data___. Data most time is inconsistent, inaccurate or incomplete. As a result, one has to address these issues in the dataset. Sometimes, this is a rather complicated process.

### Outlier filtering
Their are always outliers in every dataset. When building a prototype that is intended for a general population it will be irresponsible to take outliers into account as that could skew the whole representation. In this case of real estate(house prices) a typical outlier can be a house of 4000sqft, with 2 bedrooms and 2 bhk that is overly expensive; now that's a typical outlier. The essence of data cleaning is two remove such absurd datapoints from the dataset. 

### Regression model
Logistic regression. _Statistical modelling_

### Python Flask server
A flask server that serves as a backend through which one can access the pretrained model.

### A web app development
A web app where a user can make a few tangible inputs for the kind of house they want to buy and readily get an estimated cost.

### Prototype deployment to AWS
The complete package will be deployed to AWS EC2 instance. The link is just at the top of this README.

<br>
The notebooks and source codes of the entire project are all available in this repo.  
Feel free to fork this repo 😀.
