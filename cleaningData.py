import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv('./car/car/car.csv', error_bad_lines=False)
    df = df[['name','price','origin','status','KMtraveled','color','doorNumber','engine','fuelConsumption']]
    df = df[df.name.notnull()]
    df.to_csv('./car/allcar.csv', sep='\t', encoding='utf-8')