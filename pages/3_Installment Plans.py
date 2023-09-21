import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Millennials’ elevated frequency use of installment plans :bar_chart:')
st.markdown('Contrasting Millenials and Older Generations.')

st.markdown('#### Younger Generations Tend to use installment plans significantly more')


#--------------------------------
# Chart 1.
data1 = {'Generation': ['Millennial', 'Older Generations'],
        'numberTransact': [8.333333333, 1.43472023]
        }

numTransaction = pd.DataFrame(data1)

# bar chart
fig1 = px.bar(numTransaction, 
              x='Generation', 
              y='numberTransact',
              title='Special Installment Plan Retail Purchase'
            )

fig1.update_yaxes(title_text='Number of Transactions per 1000 customers')
fig1.update_layout(title_font=dict(size=22))

# displays the bar chart in Streamlit
st.plotly_chart(fig1)
