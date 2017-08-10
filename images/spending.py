import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("../data/data.xlsx", sheetname="spending",
                   index_col=0, dec=',', skiprows=[0, 1])
df.columns = ['Total outlays','ss', 'cs', 'comp', 'cpi']

dcpi = df.cpi/df.cpi[-1]

df_new = df.iloc[:,:-1].div(df.cpi/df.cpi[-1], axis=0)

df_cum = df_new.rolling(window=12).sum()
df_cum.dropna(inplace=True)

df_final = df_cum.iloc[:, [0]]
df_final['recurring'] = df_cum.iloc[:, 1:].sum(axis=1)


# charts
def gen_chart(df, title, y_title, date_ini):
    """"""
    plt.style.use("ggplot")
    df_final = df[df.index >= date_ini]

    # Choose colors from http://colorbrewer2.org/ under "Export"
    fig = plt.figure()
    ax = fig.add_subplot(111)
    df_final.iloc[:, 1].plot(ax=ax, style="-", color='red', linewidth=2, legend=True)
    df_final.iloc[:, 0].plot(ax=ax, style="--", color='orange', linewidth=2, legend=True)


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
    ax.legend(loc='lower right', fontsize=16)

    # label
    fig.tight_layout()
    return fig

# fig
date_ini = "2010-01-01"
fig_cli = gen_chart(df_final, "Central Govern't Oultlays", "R$mn (Real Terms)", date_ini)
plt.savefig("./spending.png")
