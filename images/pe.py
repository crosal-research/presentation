import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("../data/data.xlsx", sheetname="price_to_earnings",
                   index_col=0)
df["Ave"] = df.iloc[:, [0]].mean()[0]
df.columns = ["Price to Earnings", "Average"]

# charts
def gen_chart(df, title, y_title, date_ini):
    """"""
    plt.style.use("ggplot")
    df_final = df[df.index >= date_ini]

    # Choose colors from http://colorbrewer2.org/ under "Export"
    fig = plt.figure()
    ax = fig.add_subplot(111)
    df_final.iloc[:, 1].plot(ax=ax, style="--", color='red', linewidth=2, legend=True)
    df_final.iloc[:, 0].plot(ax=ax, color='orange', linewidth=2, legend=True)


    # labels labels
    for label in ax.xaxis.get_ticklabels():
        label.set_fontsize(14)
    for label in ax.yaxis.get_ticklabels():
        label.set_fontsize(14)

    # title
    ax.set_title(title, fontsize=24)
    ax.title.set_position([.5,1.03])
    ax.set_ylabel(y_title)
    ax.set_xlabel('')

    #margins
    ax.margins(0.0, 0.2)
    ax.set_xlim(ax.get_xlim()[0]-5, ax.get_xlim()[1]+ 5)

    #legend
    ax.legend(loc='upper left', fontsize=16)

    # label
    fig.tight_layout()
    return fig

# vix
date_ini = "1950-01-01"
fig_cli = gen_chart(df, "S&P CAPE", "x Earnings", date_ini)
plt.savefig("./price_to_earnings.png")
