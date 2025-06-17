# Supermarket-Analysis
This project provides a detailed data analysis of supermarket sales using Python and an Excel-based dataset. It includes data preprocessing, performance analysis, and insightful visualizations to understand trends across categories, regions, segments, and products.

## 📂 Dataset

- **File**: `Market_Dataset.csv` (renamed conceptually as Supermarket Data)
- **Records**: 9,994 sales entries
- **Attributes**: Sales, Profit, Discount, Customer Segment, Ship Mode, Category, Region, State, etc.

---

## 🧰 Technologies Used

- **Python 3**
- **Pandas** – data manipulation
- **Matplotlib** & **Seaborn** – data visualization
- **Jupyter** – IDE

---

## 🔍 Analysis Performed

The following insights and plots are included in the Python analysis:

# 📅 Time-Based Trends
## ✅ Monthly Sales Trend
### Definition: 
Tracks total sales aggregated for each month across all years.

### How to Calculate:

- Convert the Order Date field to a date format.

- Extract the month from the date.

- Group the dataset by month.

- Sum the Sales values for each month.

### Formula:
**Monthly Sales = Sum of Sales for each Month (across all years)**

### Purpose:
To identify seasonal patterns, peak months, and periods of low revenue.


## ✅ Monthly Profit Trend

### Definition:
Measures total profit earned per month over the entire dataset.

### How to Calculate:
- Convert Order Date to datetime format.

- Extract the month from Order Date.

- Group the data by month.

- Sum up the Profit values for each month.

### Formula:
**Monthly Profit = Sum of Profit for each Month (across all years)** 

### Purpose:
Helps determine the profitability trend and compare it against sales to find cost efficiency.


# 🛍️ Category & Product Insights
## ✅ Sales by Category

### Definition:
Aggregates total sales value across each major product category.

### How to Calculate:
- Group the dataset by the Category field.

- Sum the Sales for each category.

### Formula:
**Sales by Category = Sum of Sales for each unique Category**

### Purpose:
To identify which product categories generate the most revenue.


## ✅ Top 10 Products by Sales

### Definition:
Identifies the ten individual products that contributed the most to total sales.

### How to Calculate:
- Group data by Product Name.

- Sum the Sales for each product.

- Sort the results in descending order.

- Select the top 10 products.

### Formula:
**Top Products = Top 10 Product Names by Total Sales Amount**

### Purpose:
To pinpoint best-selling items and optimize inventory or marketing strategies.

# 🌍 Regional & Customer Segmentation
## ✅ Sales by Region

### Definition:
Total sales aggregated by geographical region.

### How to Calculate:
- Group data by Region.

- Sum the Sales value for each region.

### Formula:
**Sales by Region = Sum of Sales per Region**

### Purpose:
Assists in understanding which regions are most profitable or need strategic focus.

## ✅ Sales by Segment

### Definition:
Measures revenue contributions from different customer segments such as Consumer, Corporate, and Home Office.

### How to Calculate:
- Group data by Segment.

- Sum the Sales per segment.

### Formula:
**Sales by Segment = Sum of Sales for each Customer Segment**

### Purpose:
To identify which customer groups are more valuable and refine marketing targeting.

## ✅ Ship Mode Distribution

### Definition:
Distribution of orders by different shipping methods like Standard Class, Second Class, etc.

### How to Calculate:
- Count the number of orders for each unique Ship Mode.

### Formula:
**Ship Mode Distribution = Count of Orders grouped by Ship Mode**

### Purpose:
Helps understand logistics usage and customer preferences for shipping methods.


# 💰 Profitability & Discount Impact
## ✅ Profit by State

### Definition:
Total profit generated from each state.

### How to Calculate:
- Group data by State.

- Sum the Profit values for each state.

### Formula:
**Profit by State = Sum of Profit per State**

### Purpose:
Highlights which states are generating or losing profit, helping with strategic business expansion.

## ✅ Sales vs Profit (Scatter Plot by Category)

### Definition:
A visual representation showing the relationship between sales and profit for each transaction, categorized.

### How to Calculate:
- Use each record as a point on a scatter plot.

- Set Sales on the x-axis and Profit on the y-axis.

- Use color/hue to differentiate Category.

### Purpose:
To detect patterns like high sales with low profit or losses, which may indicate over-discounting or inefficiencies.

## ✅ Discount Impact on Profit (Boxplot)

### Definition:
Measures how different levels of discounts affect profit margins.

### How to Calculate:
- Group data based on Discount values.

- Analyze the distribution of Profit within each discount group using a boxplot.

### Purpose:
To determine if offering high discounts consistently reduces profit and to find optimal discount levels.

---
