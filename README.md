# String to Datetime

  Good AI morning, Islanders. Today, I will show you how to take a string and convert it to DateTime so that your artificial intelligence models can probably understand the column.So sit back, relax with your favorite snack and let's get started!

  Welcome to another excellent tutorial, where today I will be showing you all this fantastic dataset. I believe this dataset is incredible due to two of the columns. These two columns have two different types of potential date-time columns. Making these necessary corrections will seem intimidating at first, but don't worry. This tutorial will help create artificial intelligence more accessible. For you Islanders who are new, my name is William Mckeon. I started my college carer as an electrical engineer student who struggled a lot in my electrical engineering courses. Somehow during that struggle, I managed to teach myself how to program in python and eventually develop Artificial intelligence models. Inevitably I changed majors turning to the dark side of computer science.

## The packages and dataset we will be using

Before we can start converting strings to DateTime formate, we will need to import a couple of python packages and the dataset we will be using.

```python
import pandas as pd
import irdatacleaning
data = pd.read_csv("travel_times.csv")

```

One of the packages we will be using is a channel's favorite, the panda's python package. The other package is the communities python package irdatacleaning. The excellent dataset I have been talking so highly about is the travel_time.csv dataset. Now that we have the dataset loaded, we now needed to look at what this dataset is all about.

## Starting to get into the data

For starters, like always, before we start to make a model, we will need to make some data discovery, like using

```python
data.head()

```

This method will show you the first few rows of all the columns of the dataset. You can see that this dataset has two columns that we humans can tell are supposed to represent time. That is not to say that our models will as well. The easiest way to tell is to call

```
data.info()

```

By calling this method, we will see what data type our model will view each column. in our case, our model will not consider the Date and StartTime columns to have time data within them, but instead, these two columns are considered objects columns. To change this, we will need two lines of code.

## creating an instance of the string to DateTime class

To make the corrections to those two columns, we will need to create a new instance of irdatacleaning. We will need to create a new instance of the StringToDateTime module within irdatacleaning. The line below will show you exactly how to create this new instance.

```
datetime = irdatacleaning.StringToDateTime(data)

```

The input argument you will enter will be the dataset you are working on; in our case, our dataset is set equal to the data variable. It would be best if you, Islanders, kept in mind while using this module is that there is a list of strings being used to identify which columns need to have the DateTime formate corrections applied to them. You can view the values within that list by calling the line you see below.

```
datetime.time_list

```

This module is not restricted to only using datasets with DateTime formate corrections needed that only have those names. You do have the power to add to this list, and you can do this by,

```
datetime = irdatacleaning.StringToDateTime(data,["starting the day"])

```

By adding the input argument of that string within that list, the string starting the day is now added to the list time_list. You can check this by running

```python
datetime.time_list

```

## check

to initiate the process of correcting those columns, you have to enter.

```python
data = datetime.check()

```

By calling the check method, you tell the module that you want to have the needed changes applied to the dataset. Once the method is done with the required changes, it will then return the corrected dataset. We can check how well the module did by calling.

```python
data.info()

```

## More Resources

we did it. We made the necessary corrections to our dataset so that our model will now view those two columns as time instead of objects. Don't worry about remembering everything that we just went over. You can always call the line you see below.

```
datetime.resource()

```

This method will print to the screen the link to the youtube video and the GitHub repository, allowing you to refer back to those two links whenever you run into trouble.
You can install irdatacleaning by entering either the pip or conda command below for those who don't have the python package. As always, happy coding, and I will see you in the next one.

```python
Pip command: pip install irdatacleaning
```

```python
conda install -c islander_robotics irdatacleaning
```
