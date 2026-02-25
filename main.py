from sea_level_predictor import draw_plot


def main():
   fig = draw_plot()
   fig.savefig("sea_level_plot.png")
   print("Saved sea_level_plot.png")


if __name__ == "__main__":
    main()
