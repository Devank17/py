import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('E:\\project\\G-20 Country.csv')

while(True):
    print('\t\t\t\t\t Main Menu')
    print('1. Fetch Data')
    print('2. Dataframe Attributes')
    print('3. Display Records')
    print('4. Working on Records')
    print('5. Working on Columns')
    print('6. Data Visualization')
    print('7. Data Analytics')
    print('8. Exit')

    m = int(input('Enter Your Choice: '))
    if m==1:
        print('Fetching Data')
        print(data)
    elif m==2:
        print('Dataframe Attribute Menu')
        print('1. Display Transpose of the Dataframe')
        print('2. Column Names of the Dataframe')
        print('3. Indexes of the Dataframe')
        print('4. Shape of the Dataframe')
        print('5. Dimension of the Dataframe')
        print('6. Data Type of the Dataframe')
        print('7. Size of the Dataframe')
        i = int(input('Enter Your Choice: '))
        if i==1:
            print(data.T)
        elif i==2:
            print(data.columns)
        elif i==3:
            print(data.index)
        elif i==4:
            print(data.shape)
        elif i==5:
            print(data.ndim)
        elif i==6:
            print(data.dtypes)
        elif i==7:
            print(data.size)
        else:
            print('Invalid Choice')
            
    elif m==3:
        print('Record Menu')
        print('1. Display Top 5 Records')
        print('2. Display Bottom 5 Records')
        print('3. Display Specific Number of Records from the Top')
        print('4. Display Specific Number of Records from the Bottom')
        print('5. Display Detail of a Specific Country')
        print('6. Display Detail of All the Countries')
        i2=int(input('Enter Your Choice: '))
        if i2==1:
            print(data.head())
        elif i2==2:
            print(data.tail())
        elif i2==3:
            n=int(input('Enter Number of Records to be Displayed from the Top : '))
            print(data.head(n))
        elif i2==4:
            n=int(input('Enter Number of Records to be Displayed from the Bottom : '))
            print(data.tail(n))
        elif i2==5:
            rc=int(input('Enter the Index of Required Country : '))
            print(data.iloc[rc])
        elif i2==6:
            print('The Data is : ')
            print(data)
        else:
            print('Invalid Choice')
    elif m==4:
        print('Working on Record Menu')
        print('1. Insert a Specific Country Detail')
        print('2. Update a Specific Country Detail')
        print('3. Delete a Specific Country Detail')
        
        i3=int(input('Enter Your Choice: '))
        if i3==1:
            z=int(input('Enter Position of New Record : '))
            a = input('Enter the Country Name : ')
            b = input("Enter Data of Women's Literacy Rate : ")
            c = input("Enter Data of Men's Literacy Rate : ")
            d = input("Enter Data of Female Population : ")
            e = input("Enter Data of Male Population : ")
            data.loc[z]=[a,b,c,d,e]
            print('Record Added Successfully')
            print(data)
        elif i3==2:
            z=int(input('Enter Position of Record : '))
            a=input('Enter the Country Name whose Data is to be Updated : ')
            b = input("Enter Data of Women's Literacy Rate : ")
            c = input("Enter Data of Men's Literacy Rate : ")
            d = input("Enter Data of Female Population : ")
            e = input("Enter Data of Male Population : ")
            data.loc[z]=[a,b,c,d,e]
            print('Record Updated Successfully')
            print(data)
        elif i3==3:
            dele=int(input('Enter Index Number : '))
            data.drop(dele,axis=0,inplace=True)
            print('Data Deleted Successfully')
            print(data)
        else:
            print('Inavlid Choice')
    elif m==5:
        print('Working on Columns')
        print('1. Insert a New Column Data')
        print('2. Update a Column')
        print('3. Delete a Specific Column Data')
        
        i4=int(input('Enter Your Choice: '))
        if i4==1:
            x = input('Enter the Name of New Column : ')
            a = input('Enter the Data of India : ')
            b = input('Enter the Data of Australia : ')
            c = input('Enter the Data of Canada : ')
            d = input('Enter the Data of Japan : ')
            e = input('Enter the Data of China : ')
            f = input('Enter the Data of Italy : ')
            g = input('Enter the Data of France : ')
            data[x]=[a,b,c,d,e,f,g]
            print('Column Added Successfully')
            print(data)
            
        elif i4==2:
            x = input('Enter the Name of Column : ')
            a = input('Enter the Data of India : ')
            b = input('Enter the Data of Australia : ')
            c = input('Enter the Data of Canada : ')
            d = input('Enter the Data of Japan : ')
            e = input('Enter the Data of China : ')
            f = input('Enter the Data of Italy : ')
            g = input('Enter the Data of France : ')
            data[x]=[a,b,c,d,e,f,g]
            print('Column Updated Successfully')
            print(data)
        elif i4==3:
            dl = input('Enter Column Name : ')
            del data[dl]
            print('Column Deleted Successfully')
            print(data)
        else:
            print('Invalid Choice')
            
    elif m==6:
        print('Data Visualization')
        print('1. Line Graph')
        print('2. Bar Graph')
        print('3. Horizontal Bar Graph')
        print('4. Histogram')
        i5=int(input('Enter Your Choice: '))
        if i5==1:
            print('Line Chart Menu')
            print('1. Line Graph of All Data')
            print("2. Line Graph of Countries and Women's Literacy Rate")
            print("3. Line Graph of Countries and Men's Literacy Rate")
            print("4. Line Graph of Countries and Female Population")
            print("5. Line Graph of Countries and Male Population")
            
            ii=int(input('Enter Your Choice: '))
            if ii==1:
                data.plot(kind='line')
                plt.xlabel('Countries')
                plt.ylabel('Number of People In Millions')
                plt.title('Line Graph of All Data')
                plt.show()
            elif ii==2:
                plt.plot(data['COUNTRY NAME'],data["WOMEN'S LITERACY RATE"])
                plt.xlabel('Countries')
                plt.ylabel('Number of People In Millions')
                plt.title("Line Graph of Women's Literacy Rate")
                plt.legend()
                plt.show()
            elif ii==3:
                plt.plot(data['COUNTRY NAME'],data["MEN'S LITERACY RATE"])
                plt.xlabel('Countries')
                plt.ylabel('Number of People In Millions')
                plt.title("Line Graph of Men's Literacy Rate")
                plt.legend()
                plt.show()
            elif ii==4:
                plt.plot(data['COUNTRY NAME'],data["FEMALE POPULATION"])
                plt.xlabel('Countries')
                plt.ylabel('Number of People In Millions')
                plt.title("Line Graph of Female Population")
                plt.legend()
                plt.show()
            elif ii==5:
                plt.plot(data['COUNTRY NAME'],data["MALE POPULATION"])
                plt.xlabel('Countries')
                plt.ylabel('Number of People In Millions')
                plt.title("Line Graph of Male Population")
                plt.legend()
                plt.show()
            else:
                print('Invalid Choice')
        elif i5==2:
            print('Bar Chart Menu')
            print('1. Plot Bar Graph of All Data')
            print("2. Plot Bar Graph of Countries and Women's Literacy Rate")
            print("3. Plot Bar Graph of Countries and Men's Literacy Rate")
            print("4. Plot Bar Graph of Countries and Female Population")
            print("5. Plot Bar Graph of Countries and Male Population")
            
            ii1=int(input('Enter Your Choice: '))
            if ii1==1:
                data.plot(kind='bar')
                plt.xlabel('Countries')
                plt.ylabel('Number of People In Millions')
                plt.title("Bar Graph of All Data")
                plt.legend()
                plt.show()
            elif ii1==2:
                plt.bar(data['COUNTRY NAME'],data["WOMEN'S LITERACY RATE"])
                plt.xlabel('Countries')
                plt.ylabel('Number of People In Millions')
                plt.title("Bar Graph of Women's Literacy Rate")
                plt.legend()
                plt.show()
            elif ii1==3:
                plt.bar(data['COUNTRY NAME'],data["MEN'S LITERACY RATE"])
                plt.xlabel('Countries')
                plt.ylabel('Number of People In Millions')
                plt.title("Bar Graph of Men's Literacy Rate")
                plt.legend()
                plt.show()
            elif ii1==4:
                plt.bar(data['COUNTRY NAME'],data["FEMALE POPULATION"])
                plt.xlabel('Countries')
                plt.ylabel('Number of People In Millions')
                plt.title("Bar Graph of Female Population")
                plt.legend()
                plt.show()
            elif ii1==5:
                plt.bar(data['COUNTRY NAME'],data["MALE POPULATION"])
                plt.xlabel('Countries')
                plt.ylabel('Number of People In Millions')
                plt.title("Bar Graph of Male Population")
                plt.legend()
                plt.show()
            else:
                print('Invalid Choice')
        elif i5==3:
            print('Horizontal Bar Chart Menu')
            print('1. Plot Horizontal Bar Graph of All Data')
            print("2. Plot Horizontal Bar Graph of Countries and Women's Literacy Rate")
            print("3. Plot Horizontal Bar Graph of Countries and Men's Literacy Rate")
            print("4. Plot Horizontal Bar Graph of Countries and Female Population")
            print("5. Plot Horizontal Bar Graph of Countries and Male Population")
            
            ii2=int(input('Enter Your Choice: '))
            if ii2==1:
                data.plot(kind='barh')
                plt.xlabel('Countries')
                plt.ylabel('Number of People In Millions')
                plt.title("Horizontal Bar Graph of All Data")
                plt.legend()
                plt.show()
            elif ii2==2:
                plt.barh(data['COUNTRY NAME'],data["WOMEN'S LITERACY RATE"])
                plt.xlabel('Countries')
                plt.ylabel('Number of People In Millions')
                plt.title("Horizontal Bar Graph of Women's Literacy rate")
                plt.legend()
                plt.show()
            elif ii2==3:
                plt.barh(data['COUNTRY NAME'],data["MEN'S LITERACY RATE"])
                plt.xlabel('Countries')
                plt.ylabel('Number of People In Millions')
                plt.title("Horizontal Bar Graph of Men's Literacy rate")
                plt.legend()
                plt.show()
            elif ii2==4:
                plt.barh(data['COUNTRY NAME'],data["FEMALE POPULATION"])
                plt.xlabel('Countries')
                plt.ylabel('Number of People In Millions')
                plt.title("Horizontal Bar Graph of Female Population")
                plt.legend()
                plt.show()
            elif ii2==5:
                plt.barh(data['COUNTRY NAME'],data["MALE POPULATION"])
                plt.xlabel('Countries')
                plt.ylabel('Number of People In Millions')
                plt.title("Horizontal Bar Graph of Male Population")
                plt.legend()
                plt.show()
            else:
                print('Invalid Choice')
        
        elif i5==4:
            print('Histogram Menu')
            print('Plot Histogram of All Data')
            data.plot(kind='hist')
            plt.xlabel('Number of People In Millions')
            plt.ylabel('Countries')
            plt.title("Histogram of All Data")
            plt.show()
        else:
            print('Invalid Choice')
    elif m==7:
        print('Data Analytics')
        print('1. Maximum Value in a Column')
        print('2. Minimum Value in a Column')
        print('3. Sum in Columns')
        print('4. Count Number of Values in Rows')
        print('5. Count Number of Values in Columns')
        
        i6=int(input('Enter Your Choice: '))
        if i6 not in [1,2,3,4,5,6]:
            print('Invalid Choice')
        if i6==1:
            print('Maximum Value in a Column')
            print(data.max(axis=0))
        elif i6==2:
            print('Minimum Value in a Column')
            print(data.min(axis=0))
        elif i6==3:
            print('Sum in Columns')
            print(data.sum(axis=0))
        elif i6==4:
            print('Count Number of Values in Rows')
            print(data.count(axis=1))
        elif i6==5:
            print('Count Number of Values in Columns')
            print(data.count(axis=0))
            
    elif m==8:
        print('Exit')
        break
    else:
        print('Invalid Choice')
