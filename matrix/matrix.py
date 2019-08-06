class Matrix(object):
    def __init__(self, matrix_string):
        self.lines = matrix_string.splitlines()
        for idx, line in enumerate(self.lines):
            self.lines[idx] = line.split()

    def row(self, index):
        rowList = []
        for char in self.lines[index - 1]:
            rowList.append(int(char))
        return rowList

    def column(self, index):
        columnList = []
        for line in self.lines:
            columnMember = int(line[index - 1])
            columnList.append(columnMember)
        return columnList