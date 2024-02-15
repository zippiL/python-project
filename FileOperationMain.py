# This is a sample Python script.
from FileOperation import FileOperation
from SalesData import SalesData



if __name__ == '__main__':
    sales_data_analyzer = FileOperation(data=None)

    # Read data from an Excel file
    # sales_data_analyzer.read_excel("YafeNof.csv")
    #
    # print(sales_data_analyzer.data)
    #
    # df = sales_data_analyzer.data
    #
    # sales_data_analyzer.save_to_excel(df, "new.csv")
    #
    # df = sales_data_analyzer.data
    # sales_data_analyzer.polar_plot()
    sales_data_analyzer.violin_plot()
    sales_data_analyzer.box_plot()
    sales_data_analyzer.line_plot()
    # sales_data_analyzer.line_plot_with_seaborn()
    # sales_data_analyzer.violin_plot_with_seaborn()
    # sales_data_analyzer.box_plot_with_seaborn()
    # sales_data_analyzer.polar_plot_with_seaborn()




    # Perform analysis


    # Print analysis results
    print("Analysis results:")

    # Save data to CSV

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
