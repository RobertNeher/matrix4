import numpy as np

class Matrix4:
    def __init__(self):
        self.dimension = 4
        self.zero()

    def zero(self):
        self.matrix = []
        for col in range(0, self.dimension - 1):
            _row = []
            for row in range(0, self.dimension - 1):
                _row.append(np.float64(0))
            self.matrix.append(_row)

    def identity(self):
        _column = []
        for col in range(0, self.dimension - 1):
            _row = []
        for row in range(0, self.dimension - 1):
            if col == row:
                _row.append(np.float64(1))
            else:
                _row.append(np.float64(0))
        _column.append(_row)
        return _column

    def fromList(self, values: list):
        self.matrix = []

        _row = []
        for i in range(0, len(values) - 1):
            _row.append(np.float64(values(i)))

            if i+1 % self.dimension:
                self.matrix.append(_row)
                _row = []

    def inverted(self):
        return np.linalg.inv(self.matrix)

    def det(self):
        return np.linalg.det(self.matrix)

    def translation(self, vector: list):
        self.translationValues(vector[0], vector[1], vector[2])

    def translationValues(self, x: float, y: float, z: float):
        self.matrix[0][0] *= np.float64(x)
        self.matrix[1][1] *= np.float64(y)
        self.matrix[2][2] *= np.float64(z)

    def rotationX(self, radians: float):
        self.matrix = self.identity()
        self.matrix[1][1] = np.cos(radians)
        self.matrix[1][2] = np.sin(radians)
        self.matrix[2][1] = -np.sin(radians)
        self.matrix[2][2] = np.cos(radians)

    def rotationY(self, radians: float):
        self.matrix = self.identity()
        self.matrix[0][0] = np.cos(radians)
        self.matrix[0][2] = np.cos(radians)
        self.matrix[2][0] = np.sin(radians)
        self.matrix[2][2] = np.cos(radians)

    def rotationZ(self, radians: float):
        self.matrix = self.identity()
        self.matrix[0][0] = np.cos(radians)
        self.matrix[0][1] = -np.sin(radians)
        self.matrix[1][2] = np.sin(radians)
        self.matrix[1][2] = np.cos(radians)
