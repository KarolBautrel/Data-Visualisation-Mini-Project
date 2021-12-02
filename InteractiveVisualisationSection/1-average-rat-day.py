import pandas
from datetime import datetime
from pytz import utc
import justpy as jp
# wrzucamy kod uzyskany z Highchart do zmiennej w formie stringa
chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average rating by Day'
    },
    subtitle: {
        text: 'By whole courses'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: '"Ratings'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Dates'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: ' {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: true
            }
        }
    },
    series: [{
        name: 'Temperature',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""
data = pandas.read_csv("reviews.csv", parse_dates=["Timestamp"])
data["Day"] = data["Timestamp"].dt.date
day_average = data.groupby(["Day"]).mean()


def app():
    # Zainicjowanie strony w frameworku Quasar # main component
    wp = jp.QuasarPage()
    # Nagłówek (a = do jakiej strony)
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews",
                 classes='''text-h2  text-center q-pt-md
''')  # heading 1
    # pointer1
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis:",
                 classes="""text-h5 q-pl-lg  q-pt-lg""")
    hc = jp.HighCharts(
        a=wp, options=chart_def)  # options to przypisanie stringa z Highchart
    # Hierarchicznie mozemy dochodzic do zawartosci stringa z jsa, poniewaz jest on podobny do dict
    #hc.options.title.text = "Average rating by Day"
    #hc.options.subtitle.text = " By whole courser "
    #hc.options.xAxis.title.text = "Ratings"
    #hc.options.yAxis.title.text = "Dates"
   # hc.options.tooltip.pointFormat = "{point.y}"
    # z racji tego, ze oryginalnie day_average_index nie jest czytany przez hc jako liczby, to musimy stworzyc nowy klucz w
    # xAxis i dodac do niego day_average.index przekonwertowany na liste
   # hc.options.xAxis.categories = list(day_average.index)
    # zmiana daty, series[0], poniewaz series to lista w ktorej jest dictionary
   # hc.options.series[0].name = "Rating"
    hc.options.series[0].data = list(
        list(day_average["Rating"]))
    return wp


# funkcja odpowiadajaca za wygenerowanie strony, jako argument przyjmuje funkcje, która buduje strone
jp.justpy(app)
