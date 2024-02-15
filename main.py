# This is a sample Python script.
from FileOperation import FileOperation
from SalesData import SalesData

if __name__ == '__main__':
    sales_data_analyzer = FileOperation(data=None)

# ----------------- Task 1--------------------------
    # ex 1
    sales_data_analyzer.read_excel("YafeNof.csv")

    print(sales_data_analyzer.data)
    # ex 2
    df = sales_data_analyzer.data

    sales_data_analyzer.save_to_excel(df, "new.csv")
    # ex 2 Task 7
    sales_data_analyzer.read_file("", "csv")
    check = SalesData(data=df)
    # ------------------ Task 6--------------------------
    sales_data_analyzer.polar_plot()
    sales_data_analyzer.violin_plot()
    sales_data_analyzer.box_plot()
    sales_data_analyzer.line_plot()
    sales_data_analyzer.polar_plot_with_seaborn()
    sales_data_analyzer.line_plot_with_seaborn()
    sales_data_analyzer.violin_plot_with_seaborn()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
