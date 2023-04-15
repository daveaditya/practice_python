from urllib import request

AAPL_url = "http://real-chart.finance.yahoo.com/table.csv?s=AAPL&d=6&e=3&f=2016&g=d&a=11&b=12&c=1980&ignore=.csv"


def download(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    fw = open("aapl.csv", "w")
    for line in lines:
        fw.write(line + "\n")
    fw.close()


download(AAPL_url)
