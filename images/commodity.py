import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("../data/data.xlsx", sheetname="US_EU_CPI",
                   index_col=0, skiprows=[0, 1], parse_cols=[0,2])
dc = pd.read_excel("../data/data.xlsx", sheetname="commodities",
                   index_col=0, skiprows=[0])
dcon = pd.merge(dc, df, right_index=True, left_index=True, how="outer")
dnew = dcon/dcon.iloc[-1, -1]
dcom = dnew.iloc[:, :-1]
dnorm = ((dcom - dcom.mean()) / dcom.std()).dropna()

dfinal = dnorm.iloc[:, [6, 7, 8]]
dfinal.columns = ["Agriculture", "Metals", "Fuel"]

# charts
def gen_chart(df, title, y_title, date_ini):
    """"""
    plt.style.use("ggplot")
    df_final = df[df.index >= date_ini]


    fig = plt.figure()
    ax = fig.add_subplot(111)
    df_final.iloc[:, 0].plot(ax=ax, style="-", color='red', linewidth=2, legend=True)
    df_final.iloc[:, 1].plot(ax=ax, style="-", color='orange', linewidth=2, legend=True)
    df_final.iloc[:, 2].plot(ax=ax, style="-", color='blue', linewidth=2, legend=True)

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
    ax.set_xlim(ax.get_xlim()[0]-2, ax.get_xlim()[1]+ 2)

    #legend
    ax.legend(loc='upper left', fontsize=16)

    # label
    fig.tight_layout()
    return fig

# cpi
date_ini = "2005-01-01"
fig_cli = gen_chart(dfinal, "Commodities Prices (Real Terms)", "Std. Deviations (0=Average)", date_ini)
plt.savefig("./commodities.png")
