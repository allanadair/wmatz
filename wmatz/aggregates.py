from .types import WeightedPointZ


class WeightedMeanCenterZ(object):
    """
    Weighted mean center.
    """
    def __init__(self):
        self.x_wsum = 0.0
        self.y_wsum = 0.0
        self.z_wsum = 0.0
        self.w_sum = 0.0

    def step(self, point):
        self.x_wsum += point.x * point.weight
        self.y_wsum += point.y * point.weight
        self.z_wsum += point.z * point.weight
        self.w_sum += point.weight

    def finalize(self):
        x_mean = self.x_wsum / self.w_sum
        y_mean = self.y_wsum / self.w_sum
        z_mean = self.z_wsum / self.w_sum
        return WeightedPointZ(x=x_mean, y=y_mean, z=z_mean)


class WeightedMatCenterZ(object):
    """
    Weighted minimum aggregate travel center.
    """
    def __init__(self):
        self.epsilon = 0.001  # Arbitrarily small value that may be modified as needed
        self.points = []

    def step(self, point):
        self.points.append(point)

    def finalize(self):
        if len(self.points) == 1:
            # Do nothing, just return the point
            return self.points[0]

        if len(self.points) == 2:
            # Return the weighted mean center
            return self._first_approximation()

        if len(self.points) > 2:
            # First calculate weighted mean center as our first approximate
            # point, then iterate until we pass the epsilon condition
            approximation = self._first_approximation()
            while True:
                median = self._next_approximation(approximation)
                if median.distance(approximation) < self.epsilon:
                    return median
                # median failed epsilon test and becomes our next approximation
                approximation = median

    def _first_approximation(self):
        mean_center = WeightedMeanCenterZ()
        for pt in self.points:
            mean_center.step(pt)
        return mean_center.finalize()

    def _next_approximation(self, approximation):
        dw_sum, x_dwsum, y_dwsum, z_dwsum = 0.0, 0.0, 0.0, 0.0
        for pt in self.points:
            distance = pt.distance(approximation)
            if distance:  # This condition ensures that distance is not zero
                dweight = pt.weight / distance
                dw_sum += dweight
                x_dwsum += pt.weight * pt.x / distance
                y_dwsum += pt.weight * pt.y / distance
                z_dwsum += pt.weight * pt.z / distance
        x = x_dwsum / dw_sum
        y = y_dwsum / dw_sum
        z = z_dwsum / dw_sum
        return WeightedPointZ(x=x, y=y, z=z)
