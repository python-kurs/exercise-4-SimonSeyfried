#sorry dafür, dass ich ein file in dem Zustand abgebe, mir ist bekannt,
#dass ich Lücken habe, würde aber trotzdem versuchen den Kurs weiter
#zu machen und noch nicht aufgeben. Dementsprechend versuche ich
#auch iwie Punkte in den Hausaufgaben zu sammeln...



import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates



# Import both data tables into python using pandas. Set the index column to "MESS_DATUM" and parse the column values as dates. [1P]

garmisch  = pd.read_csv("E:/Eigene Dokumente/GitHub/exercise-4-SimonSeyfried/data/produkt_klima_tag_20171010_20190412_01550.txt", parse_dates=["MESS_DATUM"], index_col="MESS_DATUM", sep=";", na_values="-999")

garmisch.head()

zugspitze = pd.read_csv("E:/Eigene Dokumente/GitHub/exercise-4-SimonSeyfried/data/produkt_klima_tag_20171010_20190412_05792.txt", parse_dates=["MESS_DATUM"], index_col="MESS_DATUM", sep=";", na_values="-999")

zugspitze.head()



# Clip the tables to the year 2018: [1P]

garmisch  = garmisch.loc["2018-01-01":"2018-12-31"]

garmisch.head()

zugspitze = zugspitze.loc["2018-01-01":"2018-12-31"]

zugspitze.head()


# Resample the temperature data to monthly averages (" TMK") and store them in simple lists: [1P]

# TMK = Tagesmitteltemperatur

garmisch_agg  = garmisch.loc[:, [" TMK"]].resample("1M").agg({" TMK": "mean"})

garmisch_agg.head(12)

garmisch_agg.to_csv("E:/Eigene Dokumente/GitHub/exercise-4-SimonSeyfried/data/garmisch_temp_mean_month.txt")



zugspitze_agg = zugspitze.loc[:, [" TMK"]].resample("1M").agg({" TMK": "mean"})

zugspitze_agg.head(12)

zugspitze_agg.to_csv("E:/Eigene Dokumente/GitHub/exercise-4-SimonSeyfried/data/zugspitze_temp_mean_month.txt")


# Define a plotting function that draws a simple climate diagram
# Add the arguments as mentioned in the docstring below [1P]
# Set the default temperature range from -15°C to 20°C and the precipitation range from 0mm to 370mm [1P]
def create_climate_diagram(df, temp_col, title, filename, temp_min=-15, temp_max=20, prec_min=0, prec_max=370):
    """
    Draw a climate diagram.
    
    Parameters
    ----------
    df : pd.DataFrame
        Dataframe with values to plot from
    temp_col : str
        Name of temperature column
    prec_col : str
        Name of precipitation column
    title : String
        The title for the figure
    filename : String
        The name of the output figure
    temp_min : Number
        The minimum temperature value to display
    temp_max : Number
        The maximum temperature value to display
    prec_min : Number
        The minimum precipitation value to display
    prec_max : Number
        The maximum precipitation value to display

    Returns
    -------
    The figure
    
    """


    #df = pd.read_csv("C:/Users/Simon/Desktop/exercise-4-SimonSeyfried/exercise-4-SimonSeyfried/data/produkt_klima_tag_20171010_20190412_01550.txt", parse_dates=["MESS_DATUM"], index_col="MESS_DATUM", sep=";", na_values="-999")
    
    df = df.loc["2018-01-01":"2018-12-31"]
    
    df_agg = df.loc[:, [" TMK", " RSK" ]].resample("1M").agg({" TMK": "mean"," RSK":"sum"})

    fig = plt.figure(figsize=(10,8))
    plt.rcParams['font.size'] = 16
    
    ax2 = fig.add_subplot(111)
    ax1 = ax2.twinx()

    # Draw temperature values as a red line and precipitation values as blue bars: [1P]
    # Hint: Check out the matplotlib documentation how to plot barcharts. Try to directly set the correct
    #       x-axis labels (month shortnames).
    
    ax2.bar(df[ RSK],color="blue",label="Niedershlag")
    ax1.plot(df[ TMK],color="red",label="Temperature")
    
    
    #plt.plot(tabelle.air_temperature)
    #plt.show()

    fig = plt.figure(figsize=(10,8))
    plt.rcParams['font.size'] = 16


    # Set appropiate limits to each y-axis using the function arguments: [1P]
    ax2.set_xlim(("2018-01-31","2018-12-31"))
    ax1.set_xlim(("2018-01-31","2018-12-31"))
    
    # Set appropiate labels to each y-axis: [1P]
    ax2.set_ylabel("Niederschlag (°C)")
    ax1.set_ylabel("Temperatur (°C)")
    
    # Give your diagram the title from the passed arguments: [1P]
    plt.title(titel)

    # Save the figure as png image in the "output" folder with the given filename. [1P]
    plt.savefig(C:/User/Simon/Documents/GitHub/exercise-4-SimonSeyfried/output.png)
    return fig

# Use this function to draw a climate diagram for 2018 for both stations and save the result: [1P]
create_climate_diagram(...)
create_climate_diagram(...)
