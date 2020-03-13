import matplotlib.pylab as plt
import FinanceDataReader as fdr

df = fdr.DataReader('AAPL', '2001')
print(df)
