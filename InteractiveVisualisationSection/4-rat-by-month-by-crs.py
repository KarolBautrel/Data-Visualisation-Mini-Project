import pandas
from datetime import datetime
from pytz import utc
import justpy as jp
# nalezalo usuanc linijke z "backgroundColor, bo byla napisana w javascripcie"
chart_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Rating courses by month and course'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 0,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Rating '
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' '
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}"""

data = pandas.read_csv("reviews.csv", parse_dates=["Timestamp"])
data["Month"] = data["Timestamp"].dt.strftime('%Y-%m')
month_average_crs = data.groupby(['Month', 'Course Name'])[
    "Rating"].count().unstack()


def app():
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
    hc.options.xAxis.categories = list(month_average_crs.index)
    # z racji tego, ze data w tym grafie jest podzielona na slowniki w liscie w nastepujacy sposob - klucz 1 : nazwa, klucz2 : wartosci
    # to musimy tak wprowadzic dane, aby dla kazdego klucz1:nazwa kursu wyswietlalo klucz2:wszystkie wartosci srednich
    # musimy zrobic to dynamicznie, stworzyc liste ze slownikami
    # v1 oraz v2 dlatego, poniewaz sa to wartosci zmienne, v2 to lista
    # pęta od date : wyswietla kazda kolumne wartości średnich przypisanych do aktualnie obslugiwanej kolumny o nazwie przypisanej do v1
    # petla name:v1 i columna v1 bedzie podmieniana na kazda wartosc z month.average_crs.columns
    # KOMENDA => Dodaje do name pierwsza wartosci i zaczyna dodawac do date wszystkie wartosci srednich ze zmiennej v1, jak skonczy to robi tak z kolejna
    # nazwa.
    hc_data = [{"name": v1, "data": [v2 for v2 in month_average_crs[v1]]}
               for v1 in month_average_crs.columns]

    hc.options.series = hc_data  # przypisanie wyzej uzyskanych danych do series plota
    return wp


jp.justpy(app)
