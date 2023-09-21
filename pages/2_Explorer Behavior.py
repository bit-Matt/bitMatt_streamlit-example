import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Younger Customers exhibit Explorer Behavior in their Spending :money_with_wings:')
st.markdown('Contrasting Millenials and Older Generations.')


#--------------------------------
# Chart 1.
data1 = {'Generation': ['Millennial', 'Older Generations'],
        'Average': [7.945570971, 5.718518519]
        }

averageTransaction = pd.DataFrame(data1)

# bar chart
fig1 = px.bar(averageTransaction, 
              x='Generation', 
              y='Average',
              title='Younger Generations are more curious'
            )

fig1.update_yaxes(title_text='Average No. of Different Merchants visited per Customer')
fig1.update_layout(title_font=dict(size=26))

# displays the bar chart in Streamlit
st.plotly_chart(fig1)


#--------------------------------
# Chart 2.
data2 = {'Generation': ['19-21', '22 - 24', '25 - 27', '28 - 30', '31 - 33', '34 - 36', '37 - 39', '40 - 42', '43 - 45', '46 - 48', '49 - 51', '52 - 54', '55 - 57', '58 - 60', '61 - 63', '64 - 66', '67 - 69', '70 - 72', '73 - 75', '76 - 78', '79 - 81'],
        'Average': [11.42857143, 9.146666667, 8.720930233, 7.588050314, 7.225806452, 5.536121673, 5.983050847, 5.878787879, 6.28, 5.943181818, 6, 6.147058824, 4.459016393, 5.333333333, 4.888888889, 4.25, 4.714285714, 0, 0, 0, 0]
        }

averageTransaction = pd.DataFrame(data2)

# bar chart
fig2 = px.bar(averageTransaction, 
              x='Generation', 
              y='Average',
              title=' '
            )

fig2.update_yaxes(title_text='Average No. of Different Merchants visited per Customer')
fig2.update_xaxes(title_text='Age Group')
fig2.update_layout(title_font=dict(size=26))

# displays the bar chart in Streamlit
st.plotly_chart(fig2)
st.markdown('They transact with a much wider variety of merchants compared to older generations.')


#--------------------------------
# Chart 3.
data3 = {'Merchant': ['MERCHANT 103', 'MERCHANT 37', 'MERCHANT 29', 'MERCHANT 33', 'MERCHANT 73', 'MERCHANT 7', 'MERCHANT 68', 'MERCHANT 13', 'MERCHANT 22', 'MERCHANT 81'],
        'Percent': [2.4403959, 2.462888, 2.5416104, 2.6090868, 2.8902384, 3.0026991, 3.2388664, 3.6099865, 4.4984256, 4.7008547]
        }

merchantPrefer = pd.DataFrame(data3)

# bar chart
fig3 = px.bar(merchantPrefer, 
              x='Percent', 
              y='Merchant', 
              orientation='h',
              title='Millennials Merchant preferences differ from the Older Generations'
            )

fig3.update_xaxes(title_text='Percentage')
fig3.update_yaxes(title_text='Older Generations')
fig3.update_layout(title_font=dict(size=22))

# displays the bar chart in Streamlit
st.plotly_chart(fig3)

#--------------------------------
# Chart 4.
data4 = {'Merchant': ['MERCHANT 73', 'MERCHANT 68', 'MERCHANT 4', 'MERCHANT 7', 'MERCHANT 22', 'MERCHANT 13', 'MERCHANT 81', 'MERCHANT 5', 'MERCHANT 37', 'MERCHANT 34'],
        'Percent': [2.3755075, 2.4035096, 2.4548467, 2.7068652, 2.8282074, 2.8702105, 3.0428898, 5.3390582, 6.3471321, 6.804499]
        }

merchantPrefer2 = pd.DataFrame(data4)

# bar chart
fig4 = px.bar(merchantPrefer2, 
              x='Percent', 
              y='Merchant', 
              orientation='h',
              title=' '
            )

fig4.update_xaxes(title_text='Percentage')
fig4.update_yaxes(title_text='Millennials')
fig4.update_layout(title_font=dict(size=22))

# displays the bar chart in Streamlit
st.plotly_chart(fig4)


#--------------------------------
# Chart 5.
data5 = {'Age': ['19-21', '22 - 24', '25 - 27', '28 - 30', '31 - 33', '34 - 36', '37 - 39', '40 - 42', '43 - 45', '46 - 48', '49 - 51', '52 - 54', '55 - 57', '58 - 60', '61 - 63', '64 - 66', '67 - 69', '70 - 72', '73 - 75', '76 - 78', '79 - 81'],
        'Average': [1.497652582, 1.591656131, 1.673241852, 1.75, 1.78125, 1.734421365, 1.818574514, 1.809917355, 1.88209607, 1.769230769, 1.765957447, 1.820512821, 1.754385965, 1.578947368, 1.5, 1.923076923, 1.571428571, 2, 0, 0, 0]
        }

differentBanks1 = pd.DataFrame(data5)
st.markdown('#### Except for Bank choices')

# bar chart
fig5 = px.bar(differentBanks1, 
              x='Age', 
              y='Average',
              title='Recipient Banks (incoming instapay transactions)'
            )

fig5.update_yaxes(title_text='Average No. of Different Banks visited per Customer')
fig5.update_xaxes(title_text='Age Group')

# displays the bar chart in Streamlit
st.plotly_chart(fig5)


#--------------------------------
# Chart 6.
data6 = {'Age': ['19-21', '22 - 24', '25 - 27', '28 - 30', '31 - 33', '34 - 36', '37 - 39', '40 - 42', '43 - 45', '46 - 48', '49 - 51', '52 - 54', '55 - 57', '58 - 60', '61 - 63', '64 - 66', '67 - 69', '70 - 72', '73 - 75', '76 - 78', '79 - 81'],
        'Average': [1.537344398, 1.693625771, 1.820731097, 1.820870536, 1.85789129, 1.778501629, 1.767466111, 1.691025641, 1.701627486, 1.684073107, 1.498489426, 1.47, 1.468253968, 1.598930481, 1.569620253, 1.392592593, 1.258426966, 1.31147541, 1.2, 1.363636364, 1.384615385]
        }

differentBanks2 = pd.DataFrame(data6)

# bar chart
fig6 = px.bar(differentBanks2, 
              x='Age', 
              y='Average',
              title='Source Banks (outgoing instapay transactions)'
            )

fig6.update_yaxes(title_text='Average No. of Different Banks visited per Customer')
fig6.update_xaxes(title_text='Age Group')

# displays the bar chart in Streamlit
st.plotly_chart(fig6)


#--------------------------------
# Chart 7.
data7 = {'Bank': ['ELEPHANT', 'CAT', 'HORSE', 'DOG', 'HUMAN'],
        'Percent': [4.541631623, 5.466778806, 5.971404542, 18.41883936, 45.50042]
        }

bank1 = pd.DataFrame(data7)
st.markdown('#### They also choose almost the same banks')


# bar chart
fig7 = px.bar(bank1, 
              x='Percent', 
              y='Bank', 
              orientation='h',
              title='Recipient Banks (incoming instapay transactions)'
            )

fig7.update_xaxes(title_text='Percentage')
fig7.update_yaxes(title_text='Older Generations')

# displays the bar chart in Streamlit
st.plotly_chart(fig7)


#--------------------------------
# Chart 8.
data8 = {'Bank': ['ELEPHANT', 'CAT', 'HORSE', 'DOG', 'HUMAN'],
        'Percent': [5.356080143, 6.328109502, 6.407458838, 15.96905376, 46.83594525]
        }

bank2 = pd.DataFrame(data8)

# bar chart
fig8 = px.bar(bank2, 
              x='Percent', 
              y='Bank', 
              orientation='h',
              title=' '
            )

fig8.update_xaxes(title_text='Percentage')
fig8.update_yaxes(title_text='Millennials')

# displays the bar chart in Streamlit
st.plotly_chart(fig8)


#--------------------------------
# Chart 9.
data9 = {'Bank': ['HORSE', 'ELEPHANT', 'CAT', 'DOG', 'HUMAN'],
        'Percent': [6.101978267, 7.216494845, 8.275285595, 13.31847311, 47.25550293]
        }

bank3 = pd.DataFrame(data9)

# bar chart
fig9 = px.bar(bank3, 
              x='Percent', 
              y='Bank', 
              orientation='h',
              title='Source Banks (outgoing instapay transactions)'
            )

fig9.update_xaxes(title_text='Percentage')
fig9.update_yaxes(title_text='Older Generations')

# displays the bar chart in Streamlit
st.plotly_chart(fig9)

#--------------------------------
# Chart 10.
data10 = {'Bank': ['ELEPHANT', 'HORSE', 'CAT', 'DOG', 'HUMAN'],
        'Percent': [4.936288682, 5.375307849, 7.581111468, 9.776207303, 53.303351]
        }

bank4 = pd.DataFrame(data10)

# bar chart
fig10 = px.bar(bank4, 
              x='Percent', 
              y='Bank', 
              orientation='h',
              title=' '
            )

fig10.update_xaxes(title_text='Percentage')
fig10.update_yaxes(title_text='Millennials')

# displays the bar chart in Streamlit
st.plotly_chart(fig10)