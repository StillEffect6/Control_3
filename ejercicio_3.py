import matplotlib.pyplot as plt
import numpy as np


#grafico promedios de fila
row = {1: 0.5, 2: 0.61875, 3: 0.346875, 4: 0.375, 5: 0.45625, 6: 0.58125, 7: 0.5843750000000001, 8: 0.47500000000000003, 9: 0.41875, 10: 0.3125, 11: 0.525, 12: 0.32187499999999997, 13: 0.49687499999999996, 14: 0.29374999999999996, 15: 0.521875, 16: 0.478125}

column = {1: 0.6187499999999999, 2: 0.49999999999999994, 3: 0.34687500000000004, 4: 0.38750000000000007, 5: 0.45624999999999993, 6: 0.5812499999999998, 7: 0.5843750000000001, 8: 0.4749999999999999, 9: 0.41874999999999996, 10: 0.29999999999999993, 11: 0.5249999999999999, 12: 0.321875, 13: 0.496875, 14: 0.29375, 15: 0.521875, 16: 0.478125}

plt.bar(column.keys(),column.values())


plt.show()