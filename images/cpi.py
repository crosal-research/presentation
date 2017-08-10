import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("../data/data.xlsx", sheetname="US_EU_CPI",
                   index_col=0, skiprows=[0, 1]).dropna()

dc = df.iloc[:, [1]].pct_change(periods=1)*100*12
dc['yoy'] = df.iloc[:, [1]].pct_change(periods=12)*100
dc['target'] = 2.0
dc.dropna(inplace=True)
dc.columns = ['mom (Annualized)', 'yoy', 'target']

de = df.iloc[:, [0]].pct_change(periods=1)*100*12
de['yoy'] = df.iloc[:, [0]].pct_change(periods=12)*100
de['target'] = 2.0
de.dropna(inplace=True)
de.columns = ['mom (Annualized)', 'yoy', 'target']


# charts
def gen_chart(df, title, y_title, date_ini):
    """"""
    plt.style.use("ggplot")
    df_final = df[df.index >= date_ini]


    fig = plt.figure()
    ax = fig.add_subplot(111)
    df_final.iloc[:, 1].plot(ax=ax, style="-o", color='red', linewidth=2, legend=True)
    df_final.iloc[:, 0].plot(ax=ax, style="-o", color='orange', linewidth=2, legend=True)
    df_final.iloc[:, 2].plot(ax=ax, style="--", color='blue', linewidth=1, legend=True)


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
    ax.legend(loc='lower left', fontsize=16)

    # label
    fig.tight_layout()
    return fig

# cpi
date_ini = "2013-01-01"
fig_cli = gen_chart(dc, "CPI Inflation - US", "%", date_ini)
plt.savefig("./cpi.png")

fig_cli_eu = gen_chart(de, "CPI Inflation - EU", "%", date_ini)
plt.savefig("./cpi_eu.png")
