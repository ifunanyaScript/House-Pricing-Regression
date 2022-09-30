# House-Pricing-Regression
![housie](https://user-images.githubusercontent.com/91638505/193146858-d1ff7db2-a6ca-4311-b63d-d923f159e815.png)

This is regression project on house price prediction.
The dataset I used to work on this project can be found [here.](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data) <br>
I hosted the regression web app on AWS and the link is [here](http://ec2-44-204-3-215.compute-1.amazonaws.com/) <br>
This project features:
### Data cleaning
As a data scientist, one will always come accross ___rogue data___. Data most time is inconsistent, inaccurate or incomplete. As a result, one has to address these issues in the dataset. Sometimes, this is a rather complicated process. Check out the [data_cleaning](https://github.com/ifunanyaScript/House-Pricing-Regression/blob/main/notebooks/data_cleaning.ipynb) notebook in the __notebooks directory__ of this repo.

### Outlier filtering
Their are always outliers in every dataset. When building a prototype that is intended for a general population it will be irresponsible to take outliers into account as that could skew the whole representation. In this case of real estate(house prices) a typical outlier can be a house of 9000sqft, with 2 bedrooms and 2 bathrooms; now that's a typical outlier. The essence of data cleaning is two remove such absurd datapoints from the dataset. Find out more in the [outlier_filering](https://github.com/ifunanyaScript/House-Pricing-Regression/blob/main/notebooks/outlier_filtering.ipynb) notebook

### Regression model
Linear regression model. Achieved __89% accuracy__.  
The model was saved as a pickle file and is available [here](https://github.com/ifunanyaScript/House-Pricing-Regression/blob/main/tokens/house_price_model.pickle)
Notebook available [here](https://github.com/ifunanyaScript/House-Pricing-Regression/blob/main/notebooks/regression_modelling.ipynb).  _Statistical modelling_ 

### Python Flask server
A flask server that serves as a backend through which one can access the pretrained model. Available [here](https://github.com/ifunanyaScript/House-Pricing-Regression/blob/main/server/server.py).

### A web app development
A web app where a user can make a few tangible inputs for the kind of house they want to buy and readily get an estimated cost.  
All the source codes and files used to build the website is available [here](https://github.com/ifunanyaScript/House-Pricing-Regression/tree/main/client).

### Prototype deployment to AWS
The complete package was deployed to AWS EC2 instance. The link is just at the top of this README.

<br>
The notebooks and source codes of the entire project are all available in this repo.  
Feel free to fork this repo and drop a star on your way out. Thanks! 😀.
