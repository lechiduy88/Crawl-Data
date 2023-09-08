import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv('./car/car.csv')
    df = df[['name','yom','price','origin','status','KMtraveled','color','doorNumber','seatNumber','engine','fuelConsumption']]
    df = df[df.name.notnull()]
    df = df[df.name != "name"]
    df['name'] = [x.split('-')[0] for x in df['name']]
    df['name'] = [x.split('Bán')[1] for x in df['name']]
    df.to_csv('./car/allcar.csv', sep=',', index=False)