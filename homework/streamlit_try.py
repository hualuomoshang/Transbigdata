#%%

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#%%

road_id_list=[137,1143,1191,1199,1200]
true_speed=pd.read_csv('true_speed.csv',index_col=0)
pred_speed=pd.read_csv('pred_speed.csv',index_col=0)
option=st.selectbox('Select Road ID',true_speed.columns)
pred_color=st.selectbox('SELECT Pred Color',['orange','green','blue','red',])
true_color=st.selectbox('SELECT True Color',['green','red','blue','orange'])

#%%
fig,ax=plt.subplots()
ax.plot(true_speed.loc[:,option],color=true_color)
ax.plot(pred_speed.loc[:,option],color=pred_color)
st.pyplot(fig)
# st.pyplot(pred_speed.loc[:,option])
# df=pd.concat((pred_speed.loc[:,option],true_speed.loc[:,option]),axis=1)
# df.columns=['pred','true']
# st.line_chart(df)
#%%


