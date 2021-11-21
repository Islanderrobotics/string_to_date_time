
<!-- #region pycharm={"name": "#%% md\n"} -->
# String to Datetime
Good AI morning, Islanders today I will be showing u all how to take a string and convert it to DateTime so that our artificial intelligent models can probably understand the column. So sit back relax with your favorite snack and let’s get started!

Hey Islanders, welcome to another awesome tutorial, where today I will be showing you all this really awesome dataset. I believe this dataset is really awesome due to how two of the columns. within these two columns, there are two different types of potential date-time columns. they are going to see intimidating at first but don’t worry this video is going to make ai more accessible. For you Islanders who are new, my name is William Mckeon. I started my college carer as an electrical engineer student who struggled a lot in my electrical engineering courses. Somehow during that struggle, I managed to teach myself how to program in python and eventually how to develop Artificial intelligence models. Inevitably I changed majors turning to the dark side of computer science.

## The packages and dataset we will be using

Before we can actually start converting strings to DateTime formate we will need to import a couple of python packages and the dataset we will be using.
<!-- #endregion -->

```python pycharm={"name": "#%%\n"}
import pandas as pd
import irdatacleaning
data = pd.read_csv("travel_times.csv")
```

<!-- #region pycharm={"name": "#%% md\n"} -->
The packages we will be using will be of course our channels favorite the panda's python package, as well as the communities python package irdatacleaning. The dataset we will be working with today is called the travel_time.csv dataset. This is a really cool dataset to use, before we can do anything with the converting strings to DateTime we need to do a few steps.
<!-- #endregion -->

<!-- #region pycharm={"name": "#%% md\n"} -->
## Starting to get into the data

For starters like always before we start to make a model we will need to do some data discovery, like using
<!-- #endregion -->

```python pycharm={"name": "#%%\n"}
data.head()
```

<!-- #region pycharm={"name": "#%% md\n"} -->
When you call this method it will show you the first few rows of all the columns of the dataset. This method will allow for you to see that this dataset has two columns that we humans can tell are supposed to represent time. That is not to say that our models will as well the easiest way to tell is to call,
<!-- #endregion -->

```python pycharm={"name": "#%%\n"}
data.info()
```

<!-- #region pycharm={"name": "#%% md\n"} -->
when you call this method it will show you that our model will indead, not consider the Date, and StartTime columns to have time data within them. to change this we will only needed two lines of code.
<!-- #endregion -->

<!-- #region pycharm={"name": "#%% md\n"} -->
## creating an instance of the string to DateTime class
To make the corrections to those two columns  we will need create a new instance of irdatacleaning more specificly, we will need to create a new instance of the StringToDateTime module within irdatacleaning, the line below will show you exactly how to create this new instance.
<!-- #endregion -->

```python pycharm={"name": "#%%\n"}
datetime = irdatacleaning.StringToDateTime(data)
```

<!-- #region pycharm={"name": "#%% md\n"} -->
the input argumnet you will enter will the dataset you are working with in our case our dataset is set equal to the data variable. something you Islanders need to keep in mind while using this module is that there is a list of strings being used to identify which columns needed to have the datetime formate corrections applied to them. to be able to view those strings you can call the line you see bellow
<!-- #endregion -->

```python pycharm={"name": "#%%\n"}
datetime.time_list
```

<!-- #region pycharm={"name": "#%% md\n"} -->
this is not to say that you are restricted to only using this module with datasets that have columns that needed to have the datetime formate corrections applied them with only those names. you do have the power to add to this list and you can do this by,
<!-- #endregion -->

```python pycharm={"name": "#%%\n"}
datetime = irdatacleaning.StringToDateTime(data,["starting the day"])
```

<!-- #region pycharm={"name": "#%% md\n"} -->
the input argumnet of adding that string within that list even though the list only has a length of you. starting the day is now added to the list time_list with in the module, you can check this by running,
<!-- #endregion -->

```python pycharm={"name": "#%%\n"}
datetime.time_list
```

<!-- #region pycharm={"name": "#%% md\n"} -->
## check
to tell the class to make the changes to the dataset all you have to do is,
<!-- #endregion -->

```python pycharm={"name": "#%%\n"}
data = datetime.check()
```

<!-- #region pycharm={"name": "#%% md\n"} -->
by calling the check method you are telling the module that you want to now have the needed changes applied to the dataset. once the methof is done with the needed changes it will then return the corrected dataset. once the needed changes have been applied to the dataset we can check how well the module did by calling.
<!-- #endregion -->

```python pycharm={"name": "#%%\n"}
data.info()
```

<!-- #region pycharm={"name": "#%% md\n"} -->
## More Resources
we did it we where able to make the necessary corrections to our dataset so that our model will now vew those two columns as time instead of objects. dont worry about remembering everything that just went on you can always call the line you see bellow.
<!-- #endregion -->

```python pycharm={"name": "#%%\n"}
datetime.resource()
```

<!-- #region pycharm={"name": "#%% md\n"} -->
this method will print to the screen two links the link to the youtube video, as well as the github reposotory. allowing you to be able to reffer back to those two links when ever you run into trouble.
<!-- #endregion -->

<!-- #region pycharm={"name": "#%% md\n"} -->
for those of you who dont have the python package you can install irdatacleaning by entering either the pip or conda command bellow. As always happy coding and I will see you in the next one.
<!-- #endregion -->
