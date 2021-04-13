from setuptools import setup

setup(
    name = 'dPCkCalc',
    version = '0.0.x',
    description = '',
    py_modules = ["PcCalc", "Visualization"],
    install_requires = ["numpy", "igraph", "matplotlib", "descartes", "shapely", "geopandas", "seaborn"],
    package_dir = {'': 'dPCkCalc'}
)