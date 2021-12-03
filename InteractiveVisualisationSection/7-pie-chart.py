import pandas
from datetime import datetime
from pytz import utc
import justpy as jp
fig_fmt = """{
    chart: {
    
        type: 'pie'
    },
    title: {
        text: 'Browser market shares in January, 2018'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
"""
data = pandas.read_csv("reviews.csv", parse_dates=["Timestamp"])
share = data.groupby(['Course Name'])["Rating"].count()


def app():
    # Zainicjowanie strony w frameworku Quasar # main component
    wp = jp.QuasarPage()
    # Nagłówek (a = do jakiej strony)
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews",
                 classes='''text-h2  text-center q-pt-md
''')  # heading 1
    # pointer1
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis:",
                 )
    hc = jp.HighCharts(
        a=wp, options=fig_fmt)
    # v1, v2 musza byc w petli dlatego poniewaz lista sklada sie ze slownikow
    # zawierajacych key1:nazwa kursu, key2:ilosc obejrzec. Dlatego trzeba
    # do kazdego klucza1 dopisac nazwe kursu i do klucza2 count() tej nazwy
    hc_data = [{"name": v1, "y": v2}for v1, v2 in zip(share.index, share)]
    hc.options.series[0].data = hc_data
    return wp


jp.justpy(app)
