from ssl import Options
import justpy as jp
# wrzucamy kod uzyskany z Highchart do zmiennej w formie stringa
chart_def = """
{
    chart: {
        type: 'spline',
        inverted: true
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Altitude'
        },
        labels: {
            format: '{value} km'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Temperature'
        },
        labels: {
            format: '{value}°'
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
        pointFormat: '{point.x} km: {point.y}°C'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
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


def app():
    # Zainicjowanie strony w frameworku Quasar # main component
    wp = jp.QuasarPage(dark=True)
    # Nagłówek (a = do jakiej strony)
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews",
                 classes='''text-h2  text-center q-pt-md
''')  # heading 1
    # pointer1
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis:",
                 classes="""text-h5 q-pl-lg  q-pt-lg""")
    hc = jp.HighCharts(
        a=wp, options=chart_def)  # options to przypisanie stringa z Highchart

    return wp


# funkcja odpowiadajaca za wygenerowanie strony, jako argument przyjmuje funkcje, która buduje strone
jp.justpy(app)
