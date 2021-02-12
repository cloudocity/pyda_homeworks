import pandas as pd

url = 'http://www.cbr.ru/currency_base/monthly/'
#pd.read_html('http://www.cbr.ru')[0]

valut = pd.read_html(url)[0]
data = pd.DataFrame(valut)
print(type(data))

#pd.DataFrame(valut)