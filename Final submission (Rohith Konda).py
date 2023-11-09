import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

petrol_data = pd.read_csv('Petrol_dataset_June_20_2022.csv',
               encoding='latin-1')
petrol_data.head()

petrol_data.info()
petrol_data.describe()
petrol_data.shape

# chart -1

#  line chart function  
def plot_price_comparison(data, columns_to_plot, num_rows):
    """
    This function plots a comparison of different price measures across countries using line charts.

    Parameters:
    - data: A pandas DataFrame that contains the data to be plotted.
    - columns_to_plot: A list of strings that represent the column names to be plotted.
    - num_rows: An integer that specifies the number of rows to plot.
    """

    # Setting the index to 'Country' if it's not already set
    if data.index.name != 'Country':
        data = data.set_index('Country')

    plt.figure(figsize=(14, 7))

    # Ensuring that we don't attempt to plot more rows than we have data for
    num_rows = min(num_rows, len(data))

    # Loop through the columns and plot them
    for column in columns_to_plot:
        if column in data.columns:
            plt.plot(data.index[:num_rows], data[column][:num_rows], marker='o', label=column)
        else:
            print(f"Warning: '{column}' is not in the DataFrame. This column will be skipped.")

    # Customize labels and title
    plt.title('Comparison of Different Price Measures Across Countries')
    plt.xlabel('Country')
    plt.ylabel('Value')
    plt.legend()
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Note: We need the actual 'petrol_data' DataFrame and the 'columns_to_plot' list to use this function.
# Here is an example of how you would call this function:
plot_price_comparison(petrol_data, ['Price Per Gallon (USD)', 'Price Per Liter (USD)', 'Price Per Liter (PKR)'], 30)

# chart -2 

# multiple pie charts
 
 

# Clean the 'World Share' column only if it's not already numeric
if petrol_data['World Share'].dtype == object:
    petrol_data['World Share'] = petrol_data['World Share'].str.rstrip('%').astype('float')

# Define the function to create three pie charts in a single figure
def plot_three_pie_charts(df, share_col):
    # Define three subsets for the pie charts
    subset1 = df.nlargest(5, share_col)
    subset2 = df.nlargest(10, share_col).tail(5)
    subset3 = df.nlargest(15, share_col).tail(5)
    
    # Define a color palette
    colors = list(mcolors.TABLEAU_COLORS.values()) * 3  # Extend the color list to ensure unique colors

    # Create subplots
    fig, ax = plt.subplots(1, 3, figsize=(20, 7))  # 1 row, 3 columns for our pie charts

    # Plot the first pie chart
    ax[0].pie(subset1[share_col], labels=subset1['Country'], autopct='%1.1f%%', startangle=140, colors=colors[:5])
    ax[0].set_title('Top 1-5 Countries by World Share')
    ax[0].axis('equal')  # Maintaining an equal aspect ratio guarantees that the pie chart is rendered with circular proportions

    # Plot the second pie chart
    ax[1].pie(subset2[share_col], labels=subset2['Country'], autopct='%1.1f%%', startangle=140, colors=colors[5:10])
    ax[1].set_title('Top 6-10 Countries by World Share')
    ax[1].axis('equal')  # Maintaining an equal aspect ratio guarantees that the pie chart is rendered with circular proportions
 
    # Plot the third pie chart
    ax[2].pie(subset3[share_col], labels=subset3['Country'], autopct='%1.1f%%', startangle=140, colors=colors[10:15])
    ax[2].set_title('Top 11-15 Countries by World Share')
    ax[2].axis('equal')  # Maintaining an equal aspect ratio guarantees that the pie chart is rendered with circular proportions

    # Adjust the layout to prevent the pie charts from overlapping
    plt.tight_layout()

    # Display the charts
    plt.show()

# Call the function to plot three pie charts with the cleaned data
plot_three_pie_charts(petrol_data, 'World Share')
 

# graph 3 

# Check if 'World Share' is a string with percentage signs, and if so, clean it
if petrol_data['World Share'].dtype == object:
    petrol_data['World Share'] = petrol_data['World Share'].str.rstrip('%').astype('float')

# Define the function to create a bar plot with different colors for each bar
def plot_world_share_bar_chart(df):
    # Colors for the bars
    colors = plt.cm.viridis(np.linspace(0, 1, len(df['Country'])))

    # Create a bar chart
    plt.figure(figsize=(14, 7))  # Set the figure size
    bars = plt.bar(df['Country'], df['World Share'], color=colors)
    plt.title('World Share by Country')
    plt.xlabel('Country')
    plt.ylabel('World Share (%)')
    plt.xticks(rotation=90)  # Rotate the x-axis labels to prevent overlap
    
    #Add a legend
    legend_labels = [f"{country}: {world_share}%" for country, world_share in zip(df['Country'], df['World Share'])]
    plt.legend(bars, legend_labels, title='Country World Share', loc='upper right')

    plt.tight_layout()  # Adjust the layout
    
    # Display the chart
    plt.show()

# Select the top 10 countries based on 'World Share'
selected_data = petrol_data.nlargest(10, 'World Share')

# Plot the bar chart with the selected data
plot_world_share_bar_chart(selected_data)



