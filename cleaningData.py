import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv('D:\C\Crawl_data\Crawl-Data\car.csv')
    df = df[['name','yom','price','origin','status','KMtraveled','color','doorNumber','seatNumber','engine','gear','fuelConsumption']]
    df = df[df.name.notnull()]
    df = df[df.name != "name"]
    df['name'] = [x.split('-')[0] for x in df['name']]
    df['name'] = [x.split('Bán')[1] if 'Bán' in x else x for x in df['name']]
    df.to_csv('clean_car.csv', sep=',', index=False)