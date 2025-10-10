import pandas as pd

def prepare_agriculture_data(input_csv):
    df = pd.read_csv(input_csv)

    agri_df = df.query("`Indicator Code` == 'AG.LND.AGRI.K2'").copy()

    years_to_keep = ["1980", "1990", "2000", "2010", "2020"]

    long_df = agri_df.melt(
        id_vars=["Country Name", "Country Code", "Indicator Name", "Indicator Code"],
        value_vars=years_to_keep,
        var_name="Year",
        value_name="Agricultural land (sq. km)"
    )

    long_df = (
        long_df.dropna(subset=["Agricultural land (sq. km)"])
               .assign(Year=lambda d: d["Year"].astype(int))
               .sort_values(["Country Name", "Year"])
               .reset_index(drop=True)
    )

    long_df.to_csv("Agriculture_Land.csv", index=False)
    return long_df


def create_samples(filtered_df):
    df_2020 = filtered_df[filtered_df["Year"] == 2020]
    small_df = (
        df_2020.drop_duplicates(subset=["Country Name"])
               .sample(n=10, random_state=42)
               .reset_index(drop=True)
    )

    small_df.to_csv("Agriculture_Land_Small.csv", index=False)

    filtered_df.to_csv("Agriculture_Land_Large.csv", index=False)

def main():
    input_csv = "WDICSV.csv" 
    filtered = prepare_agriculture_data(input_csv)
    create_samples(filtered)

if __name__ == "__main__":
    main()
