from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import numpy as np
import pandas as pd
import matplotlib as pl
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset into a dataframe with a comma separator
df_tvs = pd.read_csv("C:\\Vasu-Dell\\MiniProject-ADS\\ads_jan24_miniproject2_vasu_jk\\miniproject\\data\\amazon_television_data.csv", sep=",")

class Api(TemplateView):
    
    def getData(request):
        return HttpResponse(df_tvs.to_html(classes='table table-bordered'))
    
    def getBarGraph(request):
        # Count the number of TV brands
        brand_counts = df_tvs['Brand'].value_counts()
        
        # Filter the top N brands
        top_n = 5  # Specify the number of top brands you want to keep
        top_brands = brand_counts.head(top_n)
        
        # Increase the plot size and adjust font size
        plt.figure(figsize=(10, 10))  # Set the desired figure size (width, height)
        plt.rcParams['xtick.labelsize'] = 12  # Adjust the font size of the x tick labels
        plt.rcParams['ytick.labelsize'] = 12  # Adjust the font size of the y tick labels

        # Plot the count of TV brands
        plt.bar(top_brands.index, top_brands.values)

        # Add labels and title to the plot
        plt.xlabel('TV Brand', fontsize=14)
        plt.ylabel('Count', fontsize=14)
        plt.title('Count of TV top 5 Brands', fontsize=16)

        # Rotate the x-axis labels if needed
        plt.xticks(rotation=45)
        
        # Display the plot
        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response