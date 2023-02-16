import pandas as pd

class file_splitter:
    def __init__(self):
        self._path = './'
        self._filename = ''
        self._rData = pd.DataFrame()
        self._fData = pd.DataFrame()
        self._criteria = ''
        self._crit_value = ''
        self._file1 = pd.DataFrame()
        self._file2 = pd.DataFrame()

    # get/set

    @property
    def fData(self):
        return self._fData
    
    @fData.setter
    def fData(self, fData):
        self._fData = fData

    @property
    def rData(self):
        return self._rData
    @rData.setter
    def rData(self, rData):
        self._rData = rData

    @property
    def criteria(self):
        return self._criteria
    
    @criteria.setter
    def criteria(self, criteria):
        self._criteria = criteria

    @property
    def crit_value(self):
        return self._crit_value
    
    @crit_value.setter
    def crit_value(self, crit_value):
        self._crit_value = crit_value

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename):
        self._filename = filename

    # main

    def load_data(self, file):

        self._path = file
            
        try:
            self._filename = self._path[self._path.rfind('/')+1:]
        except AttributeError:
            self._filename = file.name

        self.rData = pd.read_excel(self._path)
        self.rData[self.criteria] = self.rData[self.criteria].apply(lambda x: x.strip())


    def filter(self):
        self.fData = self.rData[(self.rData[self._criteria]==self._crit_value)]
        self.fData.index = range(len(self.fData))

    def split(self):
        cut_position = len(self.fData) // 2

        self._file1 = pd.DataFrame(self.fData[(self.fData.index < cut_position)])
        self._file2 = pd.DataFrame(self.fData[(self.fData.index >= cut_position)])

    def export_local(self):

        self._file1.to_excel(f'1_{self._filename}')
        self._file2.to_excel(f'2_{self._filename}')