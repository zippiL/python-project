from FileOperation import FileOperation
from SalesData import SalesData
import pandas as pd

if __name__ == '__main__':
    sales_data_analyzer = FileOperation(data=None)
    sales_data_analyzer.read_excel("YafeNof.csv")
    df = sales_data_analyzer.data
    check = SalesData(data=df)
    # ex 4
    check.eliminate_duplicates()
    # ex 5
    print(check.calculate_total_sales())
    # ex 6
    print(check.calculate_total_sales_per_month())
    # ex 7
    print(check.identify_best_selling_product())
    # ex 8
    print(check.identify_month_with_highest_sales())
    # ex 9
    print(check.analyze_sales_data())
    # ex 10
    print(check.add_to_dict())
    # ex 11
    print(check.calculate_cumulative_sales())
    # ex 12
    check.add_90_percent_values_column()
    # ex 13
    check.bar_chart_category_sum()
    # ex 14
    mean, median, second_max = check.calculate_mean_quantity()
    print("Mean:", mean)
    print("Median:", median)
    print("Second Maximum:", second_max)
    # ex 15
    filtered_data_1 = check.filter_by_sellings_or_and_1()
    print(check.filter_by_sellings_or_and_2())
    # ex 16
    check.divide_by_2()
    # ex 17
    specific_columns = ['Quantity', 'Price']  # Example of specific columns
    specific_stats = check.calculate_stats(columns=specific_columns)
    print("\nStatistics for specific columns:")
    print(specific_stats)

    # ------ Task 7 -------
    # 3
    result = check.random_value("Teilim")
    print("Random value:", result[0])
    print("Total units ordered for", "Teilim" + ":", result[1])
    print("Maximum total amount for an order:", result[2])
    # ex 5
    param1 = 10
    param2 = {"tag": "NAME", "VALUE": "John"}
    param3 = "Hello"
    param4 = {"tag": "AGE", "VALUE": 25}
    param5 = 42
    result = check.process_params(param1, param2, param3, param4, param5)
    print("Resulting dictionary:", result)
    # task 7 ex 6
    print(check.data.head(3))  # הצגת שלוש שורות ראשונות
    print(check.data.tail(2))  # הצגת שתי שורות אחרונות
    print(check.data.sample(1))  # הצגת שורה אקראית
    # ex 7
    # check.data.map(check.print_numeric_value)
    # ------------ task 6
    check.plot_sales_data()
    check.plot_sales_data_product()
    check.create_scatter_plot()
    check.plot_sales_data_with_seaborn()
    check.plot_sales_data_product_with_seaborn()

