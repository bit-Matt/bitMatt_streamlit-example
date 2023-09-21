import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Increased Digital Inclination among Millennials, Leading to greater Transaction Frequency :chart_with_upwards_trend:')
st.markdown('Contrasting Millennials and Older Generations.')

#--------------------------------
# Chart 1. Millennial and Old Gen: Digital and Traditional Channels
data1 = {'Generation': ['Older Generations', 'Millennials'],
        'Traditional': [83.63517168, 56.72961631],
        'Digital': [16.364828, 43.27038369]}

millennialChannels = pd.DataFrame(data1)

# bar chart
fig1 = px.bar(millennialChannels, 
              x=['Digital', 'Traditional'], 
              y='Generation', 
              orientation='h', 
              title='Younger Generations are shifting to Digital Channels'
            )

fig1.update_xaxes(title_text='Percentage')
fig1.update_layout(legend_title_text='Channel', title_font=dict(size=26))

# displays the bar chart in Streamlit
st.plotly_chart(fig1)
st.markdown('Note:')
st.markdown('Milliennials - customers below 40 years of age.')
st.markdown('Older Generations - customers 40 years of age and above')


#--------------------------------
# Chart 2. Transaction Amounts between the Generations
data2 = {'Generation': ['Older Generations', 'Millennials'],
        'Transactions': [5145.923554, 4308.225644]
        }

transactionAmount = pd.DataFrame(data2)

# bar chart
fig2 = px.bar(transactionAmount, 
              x='Transactions', 
              y='Generation', 
              orientation='h',
              title='Millennials make smaller Transaction Amounts...'
            )

fig2.update_xaxes(title_text='Amount in Php')
fig2.update_layout(title_font=dict(size=26))

# displays the bar chart in Streamlit
st.plotly_chart(fig2)


#--------------------------------
# Chart 3.
data3 = {'Generation': ['Older Generations', 'Millennials'],
        'Frequency': [73.24264317, 114.5447923]
        }

transactionFrequency = pd.DataFrame(data3)

# bar chart
fig3 = px.bar(transactionFrequency, 
              x='Frequency', 
              y='Generation', 
              orientation='h',
              title='But Millennials Conduct more Frequent Transactions'
            )

fig3.update_xaxes(title_text='Transaction Frequency')
fig3.update_layout(title_font=dict(size=26))

# displays the bar chart in Streamlit
st.plotly_chart(fig3)
st.markdown('Note: Transaction count is the number of transactions made by a customer from April to June 2023.')


#--------------------------------
# Chart 4.
data4 = {'Channel': ['Digital', 'Traditional'],
        'Average': [158.2826408, 72.11807072]
        }

averageTransaction = pd.DataFrame(data4)

# bar chart
fig4 = px.bar(averageTransaction, 
              x='Channel', 
              y='Average',
              title='Digitally Inclined Customers make significantly more Transactions'
            )

fig4.update_yaxes(title_text='Average Transaction Count Per Customer')
fig4.update_layout(title_font=dict(size=24))

# displays the bar chart in Streamlit
st.plotly_chart(fig4)
st.markdown('Note: Transaction count is the number of transactions made by a customer from April to June 2023.')


#--------------------------------
# Chart 5.
data5 = {'Generation': ['Older Generations', 'Millennials'],
        'Amount': [296704.9723, 436189.6271]
        }

moneyTransacted = pd.DataFrame(data5)

# bar chart
fig5 = px.bar(moneyTransacted, 
              x='Amount', 
              y='Generation', 
              orientation='h',
              title='Overall Millennials transact more money in total'
            )

fig5.update_xaxes(title_text='Amount in Php')
fig5.update_layout(title_font=dict(size=26))

# displays the bar chart in Streamlit
st.plotly_chart(fig5)