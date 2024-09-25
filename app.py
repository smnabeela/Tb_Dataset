import streamlit as st
import pandas as pd 
import plotly.express as px

st.header('Tb positive Cases')

data = pd.read_csv('mentornow/TB_Burden_Country.csv')

a=data['Year'].unique()
s = st.sidebar.selectbox('Select Year',(a))

df=data[data['Year']==s]
st.write(df)
print(df.columns)

c1,c2,c3 =st.columns(3)
c1.metric(label = 'Total positive cases',value=round(df['Estimated prevalence of TB (all forms) per 100 000 population'].sum(),2))
c1.metric(label = 'Total death from TB',value=round(df['Estimated number of deaths from TB in people who are HIV-positive'].sum(),2))

# df1=pd.DataFrame(data)
df1_data = df.head(10)

sorted = df1_data.sort_values(by='Estimated prevalence of TB (all forms) per 100 000 population',ascending=False)
st.write(sorted)
fig = px.bar(sorted,x='Estimated prevalence of TB (all forms) per 100 000 population',y ='Country or territory name',text='Estimated prevalence of TB (all forms) per 100 000 population')
fig.update_yaxes(autorange="reversed",)
fig.update_xaxes(showticklabels=False,)

st.write(fig)


