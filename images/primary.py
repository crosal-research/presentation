import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("../data/data.xlsx", sheetname="fiscal",
                   index_col=0, dec=',', skiprows=[0, 1])
df = df*(-1)/1000
df["target"] = -139
df['12 months rolling'] = df.iloc[:, [0]].rolling(window=12).sum()
df.dropna(inplace=True)

# charts
def gen_chart(df, title, y_title, date_ini):
    """"""
    plt.style.use("ggplot")
    df_final = df[df.index >= date_ini]

    # Choose colors from http://colorbrewer2.org/ under "Export"
    fig = plt.figure()
    ax = fig.add_subplot(111)
    df_final.iloc[:, 2].plot(ax=ax, style="-", color='red', linewidth=2, legend=True)
    df_final.iloc[:, 1].plot(ax=ax, style="--", color='orange', linewidth=2, legend=True)


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
    ax.legend(loc='lower left', fontsize=16)

    # label
    fig.tight_layout()
    return fig

# fig
date_ini = "2010-01-01"
fig_cli = gen_chart(df, "Primary Surplus", "x Earnings", date_ini)
plt.savefig("./primary.png")
