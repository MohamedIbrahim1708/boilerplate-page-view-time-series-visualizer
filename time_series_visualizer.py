import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to draw line plot
def draw_line_plot(df):
    df_line = df.copy()
    df_line.index = pd.to_datetime(df_line.index)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df_line.index, df_line['value'], color='r')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.savefig('line_plot.png')
    return fig

# Function to draw bar plot
def draw_bar_plot(df):
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    fig = df_bar.plot(kind='bar', figsize=(10, 5)).get_figure()
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=[month[:3] for month in df_bar.columns])
    plt.xticks(rotation=45)
    plt.savefig('bar_plot.png')
    return fig

# Function to draw box plot
def draw_box_plot(df):
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], 
                order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    
    plt.savefig('box_plot.png')
    return fig

# Importing data and setting index
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

# Cleaning data
df_clean = df[(df['value'] >= df['value'].quantile(0.025)) & 
              (df['value'] <= df['value'].quantile(0.975))]

# Drawing plots
draw_line_plot(df_clean)
draw_bar_plot(df_clean)
draw_box_plot(df_clean)
