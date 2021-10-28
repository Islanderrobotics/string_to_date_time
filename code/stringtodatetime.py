import pandas as pd
import datetime

class StringToDateTime:
    ''' this class is designed to make converting strings to datetime more accessable
    this is done by creating an instance of the class StringToDateTime(df, column_names)
    df is where you will define the pandas dataframe that you will work with
    column_names is when you have a column names for columns you wish have converted to datetime
    that is not not ["date","dates","starttime","start_time","start time"], to use this input argument
    successfully you must pass in a list'''

    def __init__(self,df, column_names = []):
        if isinstance(column_names,list) is False:
            raise AttributeError("column_names needs to be a list")
        self.df = df
        self.copy_df = df.copy()
        self.time_spot = {}
        self.time_list = ["date","dates","starttime","start_time","start time"]
        self.possible = [" " ,",","/","-", ":"]
        self.greates = [i*0 for i in range(len(self.possible))]
        if (len(column_names)>0):
            for i in column_names:
                self.time_list.append(i)

    def _finding_the_columns(self):
        count = 0
        # time_spot = {}
        for i in self.df.columns:
            if i.lower() in set(self.time_list):
                self.time_spot[i] = count
            count+=1

    def _making_the_changes(self):
        for j in self.time_spot.keys():
            for i in self.df[j]:
                self.greates[0] = self.greates[0]+i.count(self.possible[0])
                self.greates[1] = self.greates[1]+i.count(self.possible[1])
                self.greates[2] = self.greates[2]+i.count(self.possible[2])
                self.greates[3] = self.greates[3]+i.count(self.possible[3])
                self.greates[4] = self.greates[4]+i.count(self.possible[4])
            for i in range(len(self.greates)):
                if self.greates[i] == max(self.greates):
                    most_used_char = self.possible[i]
            for w in self.df[j]:
                rep = ""
                for l in w:
                    try:
                        int(l)
                        rep = rep+l
                    except ValueError:
                        rep =rep+most_used_char

                self.df[j].replace(to_replace={w:rep}, inplace=True)
        # data["Date"] = pd.to_datetime(data["Date"],infer_datetime_format=True)
            self.df[j] = pd.to_datetime(self.df[j],infer_datetime_format=True)
            self.greates = [i*0 for i in range(len(self.possible))]
    def check(self):
        self._finding_the_columns()
        self._making_the_changes()
        return self.df
    def resource(self):
        links ={}
        links["youtube"] = ""
        links["github"] = ""
        for i in links.keys():
            print(f"the link for {i} is {links[i]}") 

if __name__ =="__main__":
    import pandas as pd
    import datetime
    from stringtodatetime import StringToDateTime
    data = pd.read_csv("landslide_data3.csv")
# data = pd.read_csv('https://raw.githubusercontent.com/jldbc/coffee-quality-database/master/data/arabica_data_cleaned.csv')
# data = pd.read_csv("travel_times.csv"

    stringtodate = StringToDateTime(df = data)
    data = stringtodate.check()