import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=True, index_col="date")

# Clean data
number_of_drops = round((df["value"].count() * 2.5) / 100)
df = df.drop(df.nlargest(number_of_drops, "value").index).drop(df.nsmallest(number_of_drops, "value").index)


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(15,5))
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.plot(df)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["month"] = df_bar.index.month
    df_bar["year"] = df_bar.index.year
    df_bar = df_bar.groupby(["year", "month"])["value"].mean()
    df_bar = df_bar.unstack(fill_value=0)

    # Draw bar plot
    fig = df_bar.plot.bar(
        legend=True, figsize=(13, 9), ylabel="Average Page Views", xlabel="Years"
    ).figure
    fig.set_figheight(6)
    fig.set_figwidth(12)
    plt.legend(
        [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ],
        title="Months",
    )




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
