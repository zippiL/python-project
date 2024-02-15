import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class FileOperation:

    def __init__(self, data):
        self.data = data


    def read_excel(self, file_path: str):
        self.data = pd.read_csv(file_path)
    def line_plot(self):
        self.data.plot.line(subplots=True)
        plt.show()
    def box_plot(self):
        plt.figure(figsize=(10, 6))
        self.data.boxplot(column=['Quantity', 'Price', 'Total'], by='Product')
        plt.title('Boxplot of Product Orders')
        plt.xlabel('Product')
        plt.ylabel('Value')
        plt.suptitle('')
        plt.grid(True)
        plt.show()
    def violin_plot(self):
        plt.figure(figsize=(10, 6))
        plt.violinplot(self.data['Quantity'], vert=False, widths=0.9)
        plt.title('Distribution of Units Ordered')
        plt.xlabel('Number of Units')
        plt.ylabel('Product')
        plt.yticks([1], ['Units'])
        plt.grid(True)
        plt.show()

    def polar_plot(self):
        product_counts = self.data['Product'].value_counts()

        # יצירת סכמת Polar Plot
        plt.figure(figsize=(8, 8))
        angles = np.linspace(0, 2 * np.pi, len(product_counts), endpoint=False).tolist()
        values = product_counts.tolist()
        angles += angles[:1]
        values += values[:1]
        plt.polar(angles, values, marker='o')
        plt.title('Polar Plot of Product Orders')
        plt.xticks(angles[:-1], product_counts.index)
        plt.show()

    def polar_plot_with_seaborn(self):
        """
        Plot polar plot using Seaborn.
        """
        try:
            product_counts = self.data['Product'].value_counts()

            # Create polar plot using Seaborn
            plt.figure(figsize=(8, 8))
            sns.barplot(x=product_counts.index, y=product_counts.values, palette='viridis')
            plt.title('Polar Plot of Product Orders')
            plt.xlabel('Product')
            plt.ylabel('Count')
            plt.show()
        except Exception as e:
            print("An error occurred while plotting polar plot with Seaborn:", e)

    def line_plot_with_seaborn(self):
        """
        Plot sales data using Seaborn.
        """
        try:
            # Create line plot using Seaborn
            plt.figure(figsize=(10, 6))
            sns.lineplot(data=self.data, dashes=False)
            plt.title('Line Plot of Product Orders')
            plt.xlabel('Date')
            plt.ylabel('Value')
            plt.show()
        except Exception as e:
            print("An error occurred while plotting line plot with Seaborn:", e)

    def box_plot_with_seaborn(self):
        """
        Plot box plot using Seaborn.
        """
        try:
            # Plot box plot using Seaborn
            plt.figure(figsize=(10, 6))
            sns.boxplot(data=self.data, x='Product', y='Value')
            plt.title('Boxplot of Product Orders')
            plt.xlabel('Product')
            plt.ylabel('Value')
            plt.grid(True)
            plt.show()
        except Exception as e:
            print("An error occurred while plotting box plot with Seaborn:", e)

    def violin_plot_with_seaborn(self):
        """
        Plot violin plot using Seaborn.
        """
        try:
            # Plot violin plot using Seaborn
            plt.figure(figsize=(10, 6))
            sns.violinplot(data=self.data, x='Product', y='Quantity', inner=None)
            plt.title('Distribution of Units Ordered')
            plt.xlabel('Product')
            plt.ylabel('Number of Units')
            plt.grid(True)
            plt.show()
        except Exception as e:
            print("An error occurred while plotting violin plot with Seaborn:", e)
    def save_to_excel(self, data, file_name: str):
        data.to_csv(file_name)


    def read_file(self, file_path: str, file_type: str):
        try:
            if file_type == 'csv':
                return self.read_csv(file_path)
            else:
                with open(file_path, 'r') as file:
                    content = file.read()
                return content

        except FileNotFoundError:
            error_message = f"<Leah&Tamar, {datetime.now()}> The file {file_path} was not found <Leah&Tamar>"
            print(error_message)
            return None

        except Exception as e:
            error_message = f"<Leah&Tamar, {datetime.now()}> An error occurred while reading file: {e} <Leah&Tamar>"
            print(error_message)
            return None
