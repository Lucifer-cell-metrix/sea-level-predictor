import unittest
import pandas as pd
from sea_level_predictor import load_data, predict, draw_plot, fit_linear_model


class TestSeaLevel(unittest.TestCase):
    def test_load(self):
        df = load_data("epa-sea-level.csv")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)

    def test_fit_predict(self):
        coeffs = fit_linear_model()
        self.assertIsNotNone(coeffs)
        p2050 = predict(2050, coeffs)
        self.assertIsInstance(p2050, float)

    def test_draw_plot(self):
        fig = draw_plot()
        from matplotlib.figure import Figure
        self.assertIsInstance(fig, Figure)


if __name__ == "__main__":
    unittest.main()
