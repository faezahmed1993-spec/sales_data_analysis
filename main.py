from flask import Flask, render_template
import data_initialization
import pandas as pd
import matplotlib
matplotlib.use('Agg') # Agg allows matplotlib to render images without opening a GUI window (for web server application)

import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def home():
    df = data_initialization.initialize_data()

    total_sales_by_dealsize = df.groupby('DEALSIZE')['SALES'].sum().reset_index(name='TOTAL_SALES')

    plt.figure()
    plt.bar(total_sales_by_dealsize['DEALSIZE'], total_sales_by_dealsize['TOTAL_SALES'])
    plt.title('Deal Size-wise Total Sales')
    plt.xlabel('Deal Size')
    plt.ylabel('Total Sales')
    plt.savefig('static/dealsize_sales.png')
    #plt.show()
    plt.close()

    total_sales_by_year = df.groupby('YEAR_ID')['SALES'].sum().reset_index(name='TOTAL_SALES')

    plt.figure()
    plt.pie(total_sales_by_year['TOTAL_SALES'], labels=total_sales_by_year['YEAR_ID'], autopct='%1.1f%%')
    plt.title('Year-wise Total Sales')
    plt.legend(total_sales_by_year['YEAR_ID'])
    plt.savefig('static/year_sales.png')
    #plt.show()
    plt.close()

    total_sales_by_product = df.groupby('PRODUCTLINE')['SALES'].sum().reset_index(name='TOTAL_SALES')


    plt.figure(figsize=[8,6])
    plt.plot(total_sales_by_product['PRODUCTLINE'], total_sales_by_product['TOTAL_SALES'])
    plt.title('Product Line-wise Total Sales')
    plt.xlabel('Product Line')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=10)
    plt.savefig('static/productline_sales.png')
    #plt.show()
    plt.close()



    df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

    month_by_total_sales = df.groupby('MONTH_ID')['SALES'].sum().reset_index(name='TOTAL_SALES')

    plt.figure()
    plt.bar(month_by_total_sales['MONTH_ID'], month_by_total_sales['TOTAL_SALES'])
    plt.title('Month-wise Total Sales')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.savefig('static/month_sales.png')
    #plt.show()
    plt.close()

    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True, port=5000)