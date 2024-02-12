from altair import Chart, Tooltip
from pandas import DataFrame



def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    graph = (Chart(df, title=f"{y} by {x} for {target}")
                .mark_circle(size=100)
                .encode(
                    x=x,
                    y=y,
                    color=target,
                    tooltip=Tooltip(df.columns.to_list())
            ))

    # Chart configurations
    properties = {
        'width': 500,
        'height': 500,
        'background': '#252525',
        'padding': 50
        }
    txt_color = 'grey'
    graph = (graph.configure(
                background=properties['background'],
                padding=properties['padding']
                )
                .configure_axis(
                    gridColor=txt_color,
                    labelColor=txt_color,
                    tickColor=txt_color,
                    titleColor=txt_color
                    )
                .configure_title(
                    fontSize=25,
                    color=txt_color
                    )
                .properties(
                    width=500,
                    height=500
                    )
                .configure_legend(
                    labelColor=txt_color,
                    titleColor=txt_color
                    ))

    return graph
