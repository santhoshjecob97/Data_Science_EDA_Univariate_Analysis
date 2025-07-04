class Univariate():
    
    def quanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            #print(columnName)
            if(dataset[columnName].dtype=='O'):
                #print("qual")
                qual.append(columnName)
            else:
                #print("quan")
                quan.append(columnName)
        return quan,qual

    def Univariate(dataset,quan):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%",
                                   "Q3:75%","99%","Q4:100%","IQR","1.5rule","Lesser","Greater","Min","Max"],columns=quan)
        for columnName in quan:
            descriptive[columnName]["Mean"]=dataset[columnName].mean()
            descriptive[columnName]["Median"]=dataset[columnName].median()
            descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]
            descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
            descriptive[columnName]["99%"]=np.percentile(dataset[columnName],99)
            descriptive[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]
            descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75%"]-descriptive[columnName]["Q1:25%"]
            descriptive[columnName]["1.5rule"]=1.5*descriptive[columnName]["IQR"]
            descriptive[columnName]["Lesser"]=descriptive[columnName]["Q1:25%"]-descriptive[columnName]["1.5rule"]
            descriptive[columnName]["Greater"]=descriptive[columnName]["Q3:75%"]+descriptive[columnName]["1.5rule"]
            descriptive[columnName]["Min"]=dataset[columnName].min()
            descriptive[columnName]["Max"]=dataset[columnName].max()
            descriptive[columnName]["kurtosis"]=dataset[columnName].kurtosis()
            descriptive[columnName]["skew"]=dataset[columnName].skew()
            descriptive[columnName]["Var"]=dataset[columnName].var()
            descriptive[columnName]["Std"]=dataset[columnName].std()
        return descriptive
    
    def freqTable(colunName,dataset):
            freqTable=pd.DataFrame(columns=["Unique_Values","Frequency","Relative_Frequency","Cumsum"])
            freqTable["Unique_Values"]=dataset[columnName].value_counts().index
            freqTable["Frequency"]=dataset[columnName].value_counts().values
            freqTable["Relative_Frequency"]=(freqTable["Frequency"]/103)
            freqTable["Cumsum"]=freqTable["Relative_Frequency"].cumsum()
        return freqTable
    
    
    
    def Replace_Outlier(ColumnName,dataset):
            for lesscolumn in lesser:
                dataset[lesscolumn][dataset[lesscolumn]<descriptive[lesscolumn]["LesserRange"]]=descriptive[lesscolumn]["LesserRange"]
            for greatcolumn in greater:
                dataset[greatcolumn][dataset[greatcolumn]>descriptive[greatcolumn]["GreaterRange"]]=descriptive[greatcolumn]["GreaterRange"]
        return columnName
    
    
    
    
    def Outlier_Column_Names(descriptive,quan):
            lesser=[]
            greater=[]
            for columnName in quan:
                if(descriptive[columnName]["LesserRange"]>descriptive[columnName]["Min"]):
                    lesser.append(columnName)
                if(descriptive[columnName]["GreaterRange"]<descriptive[columnName]["100%"]):
                    greater.append(columnName)
            return lesser,greater
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    