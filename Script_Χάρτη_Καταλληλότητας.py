import numpy as np
from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry

# Ορίζουμε το layer της κλίσης (πρέπει να είναι επιλεγμένο στο QGIS)
layer = iface.activeLayer()
entries = []

# Ρυθμίσεις για τον υπολογιστή Raster
rast = QgsRasterCalculatorEntry()
rast.ref = 'slope@1'
rast.raster = layer
rast.bandNumber = 1
entries.append(rast)

# Η φόρμουλα: 0-15 μοίρες = 1 (Πράσινο), 15-30 = 2 (Κίτρινο), >30 = 3 (Κόκκινο)
expression = '("slope@1" <= 15) * 1 + (("slope@1" > 15) AND ("slope@1" <= 30)) * 2 + ("slope@1" > 30) * 3'

output = 'C:/users/Public/suitability_map.tif' # Άλλαξε το path αν χρειάζεται
calc = QgsRasterCalculator(expression, output, 'GTiff', layer.extent(), layer.width(), layer.height(), entries)
calc.processCalculation()

# Φόρτωση του αποτελέσματος
iface.addRasterLayer(output, "Χάρτης Καταλληλότητας")