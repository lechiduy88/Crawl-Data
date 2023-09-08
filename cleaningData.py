import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv('D:\DEBeginner\Project1\car\car\car.csv', error_bad_lines=False)
    df = df[['name','price','origin','status','KMtraveled','color','doorNumber','engine','fuelConsumption']]
    df = df[df.name.notnull()]
    df.to_csv('allcar.csv', sep='\t', encoding='utf-8')