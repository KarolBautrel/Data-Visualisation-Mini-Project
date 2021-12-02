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
        text: 'Average rating by Week'
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
data["Week"] = data["Timestamp"].dt.strftime('%Y-%U')
week_average = data.groupby(["Week"]).mean()


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
        a=wp, options=chart_def)

    hc.options.xAxis.categories = list(week_average.index)

   # hc.options.series[0].name = "Rating"
    hc.options.series[0].data = list(
        list(week_average["Rating"]))
    return wp


jp.justpy(app)
