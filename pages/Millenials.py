import streamlit as st
import pandas as pd
import plotly.express as px

# Chart 1. Millenial and Old Gen: Digital and Traditional Channels
data1 = {'Generation': ['Millenials', 'Older Generations'],
        'Traditional': [56.72961631, 83.63517168],
        'Digital': [43.27038369, 16.364828]}

millenialChannels = pd.DataFrame(data1)

st.title('Younger Generations are shifting to Digital Channels')

# bar chart
fig1 = px.bar(millenialChannels, 
              x=['Digital', 'Traditional'], 
              y='Generation', 
              orientation='h', 
              title='Millenials vs. Older Generations'
            )

fig1.update_xaxes(title_text='Percentage')
fig1.update_layout(legend_title_text='Channel')

# displays the bar chart in Streamlit
st.plotly_chart(fig1)


# Chart 2. Transaction Amounts between the Generations
data2 = {'Generation': ['Millenials', 'Older Generations'],
        'Transactions': [4308.225644, 5145.923554]
        }

transactionAmount = pd.DataFrame(data2)

st.title('Millenials make smaller Transaction Amounts...')

# bar chart
fig2 = px.bar(transactionAmount, 
              x='Transactions', 
              y='Generation', 
              orientation='h'
            )

fig2.update_xaxes(title_text='Transaction Amount')

# displays the bar chart in Streamlit
st.plotly_chart(fig2)


# Chart 3. Frequency of Transactions between the Generations
data3 = {'Generation': ['Millenials', 'Older Generations'],
        'Frequency': [114.5447923, 73.24264317]
        }

transactionFrequency = pd.DataFrame(data3)

st.title('But Millenials Conduct more Frequent Transactions')

# bar chart
fig3 = px.bar(transactionFrequency, 
              x='Frequency', 
              y='Generation', 
              orientation='h'
            )

fig3.update_xaxes(title_text='Transaction Frequency')

# displays the bar chart in Streamlit
st.plotly_chart(fig3)