import io
import unittest
import pandas as pd
import numpy as np
from SalesData import SalesData
import sys


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # ניצור DataFrame דומה לנתוני המכירות לשימוש בבדיקות
        self.data = pd.DataFrame({
            'Product': ['A', 'B', 'C', 'A', 'B'],
            'Quantity': [10, 20, 30, 40, 50],
            'Date': ['01.01.2022', '01.02.2022', '01.03.2022', '01.01.2022',
                     '01.02.2022'],
            'Total': [100, 200, 300, 400, 500],
            'Price': [10, 20, 30, 40, 50]
        })
        self.sales_data = SalesData(self.data)

    def test_eliminate_duplicates(self):
        self.sales_data.eliminate_duplicates()
        self.assertEqual(len(self.sales_data.data), len(self.data.drop_duplicates()))

    def test_calculate_total_sales(self):
        total_sales = self.sales_data.calculate_total_sales()
        expected_totals = self.data.groupby('Product')['Quantity'].sum().reset_index()
        pd.testing.assert_frame_equal(total_sales, expected_totals)

    def test_identify_best_selling_product(self):
        # בדיקה שהפונקציה מזהה את המוצר הנמכר ביותר
        best_selling_product = self.sales_data.identify_best_selling_product()
        expected_best_selling = self.data.groupby('Product')['Quantity'].sum().reset_index().nlargest(1, 'Quantity')
        pd.testing.assert_frame_equal(best_selling_product, expected_best_selling)

    def test_calculate_total_sales_per_month(self):
        # בדיקה שהפונקציה מחשבת סכום מכירות לכל חודש
        total_sales_per_month = self.sales_data.calculate_total_sales_per_month()
        expected_totals = self.data.groupby(pd.to_datetime(self.data['Date'], format='%d.%m.%Y').dt.strftime('%B'))[
            'Quantity'].sum().reset_index()
        pd.testing.assert_frame_equal(total_sales_per_month, expected_totals)

    def test_identify_month_with_highest_sales(self):
        # בדיקה שהפונקציה מזהה את החודש עם המכירות הגבוהות ביותר
        month_with_highest_sales = self.sales_data.identify_month_with_highest_sales()
        expected_month = self.data.groupby(pd.to_datetime(self.data['Date'], format='%d.%m.%Y').dt.strftime('%B'))[
            'Quantity'].sum().reset_index().nlargest(1, 'Quantity')
        pd.testing.assert_frame_equal(month_with_highest_sales, expected_month)

    def test_analys_sales_data(self):
        # בדיקה שהפונקציה מחזירה את התוצאות הנכונות של ניתוח נתוני מכירות
        analysis_results = self.sales_data.analys_sales_data()
        self.assertIsInstance(analysis_results, dict)
        self.assertIn('best_selling_product', analysis_results)
        self.assertIn('month_with_highest_sales', analysis_results)

    def test_add_to_dict(self):
        # בדיקה שהפונקציה מוסיפה נתונים נוספים למילון הניתוח
        extended_analysis = self.sales_data.add_to_dict()
        self.assertIsInstance(extended_analysis, dict)
        self.assertIn('minimest selling', extended_analysis)
        self.assertIn('avg_sales_by_month', extended_analysis)

    def test_calculate_cumulative_sales(self):
        cumulative_sales = self.sales_data.calculate_cumulative_sales()
        expected_cumulative = self.data.pivot_table(index='Product', columns=pd.to_datetime(self.data['Date'],
                                                                                            format='%d.%m.%Y').dt.month,
                                                    values='Total', aggfunc=np.sum, fill_value=0)
        pd.testing.assert_frame_equal(cumulative_sales, expected_cumulative)

    def test_add_90_percent_values_column(self):
        self.sales_data.add_90_percent_values_column()
        self.assertIn('90%_Values', self.sales_data.data.columns)

    def test_bar_chart_category_sum(self):
        self.assertIsNone(self.sales_data.bar_chart_category_sum())  # נבדוק רק שאין שגיאות בפעולה

    def test_divide_by_2(self):
        self.sales_data.divide_by_2()
        self.assertIn('BlackFridayPrice', self.sales_data.data.columns)

    def test_calculate_stats(self):
        stats = self.sales_data.calculate_stats()
        self.assertIsInstance(stats, dict)
        # נבדוק עבור כל אחת מהעמודות שיש נתונים נומריים במסד הנתונים
        numeric_columns = self.data.select_dtypes(include=[np.number]).columns
        for col in numeric_columns:
            self.assertIn(col, stats)
            self.assertIn('max', stats[col])
            self.assertIn('sum', stats[col])
            self.assertIn('absolute_values', stats[col])
            self.assertIn('cumulative_max', stats[col])

    def test_random_value(self):
        product_name = 'A'
        result_array = self.sales_data.random_value(product_name)
        self.assertIsInstance(result_array, list)
        self.assertEqual(len(result_array), 3)  # אמור להחזיר ערך רנדומלי, סכום יחידות הזמנה ומחיר מקסימלי
        self.assertGreaterEqual(result_array[0], result_array[1])  # הערך הרנדומלי צריך להיות לפחות כמו סכום ההזמנות

    def test_process_params(self):
        result_dict = self.sales_data.process_params({'tag': 'tag1', 'VALUE': 'value1'}, 'value2', 'value3')
        self.assertIsInstance(result_dict, dict)
        self.assertIn('tag1', result_dict)
        self.assertEqual(result_dict['tag1'], 'value1')


if __name__ == '__main__':
    unittest.main()
