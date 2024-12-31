import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Trường Cao đẳng y tế Huế')
st.header('Danh sách đăng kí tuyển sinh 2025')
st.subheader('1. Số liệu tổng quát')

### --- LOAD DATAFRAME
excel_file = 'datafull.xlsx'
sheet_name = 'DATA'


df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='B:W',
                   header=1)

st.dataframe(df)

# --- PHÂN TÍCH SỐ LIỆU PHÂN BỐ THEO TỈNH NƠI SINH

st.subheader('2. Phân bố theo Tỉnh nơi sinh')
# --- STREAMLIT SELECTION
noi_sinh = df['Nơi sinh'].unique().tolist()

noi_sinh_selection = st.multiselect('Nơi sinh:',
                                    noi_sinh,
                                    default=noi_sinh)

# --- FILTER DATAFRAME BASED ON SELECTION
mask = df['Nơi sinh'].isin(noi_sinh_selection)
number_of_result = df[mask].shape[0]
st.markdown(f'*Số lượng sinh viên: {number_of_result}*')

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped = df[mask].groupby(by=['Nơi sinh']).count()[['Giới tính']]
df_grouped = df_grouped.rename(columns={'Giới tính': 'Số lượng'})
df_grouped = df_grouped.reset_index()

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped,
                   x='Nơi sinh',
                   y='Số lượng',
                   text='Số lượng',
                   color_discrete_sequence = ['#F63366']*len(df_grouped),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)

# --- DISPLAY IMAGE & DATAFRAME
#col1, col2 = st.columns(2)
#image = Image.open('images/survey.jpg')
#col1.image(image,
#        caption='Designed by slidesgo / Freepik')
#col2.dataframe(df[mask])


# --- PHÂN TÍCH SỐ LIỆU PHÂN BỐ THEO NGÀNH ĐĂNG KÍ NV1
st.subheader('3. Phân bố theo ngành nguyện vọng 1')
# --- STREAMLIT SELECTION
nv1 = df['Ngành đăng kí nguyện vọng 1'].unique().tolist()


nv1_selection = st.multiselect('Nguyện vọng 1:',
                                    nv1,
                                    default=nv1)
# --- FILTER DATAFRAME BASED ON SELECTION
nv1_mask = df['Ngành đăng kí nguyện vọng 1'].isin(nv1_selection)
number_of_nv1 = df[nv1_mask].shape[0]
st.markdown(f'*Số lượng sinh viên: {number_of_nv1}*')

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped_nv1 = df[nv1_mask].groupby(by=['Ngành đăng kí nguyện vọng 1']).count()[['Giới tính']]
df_grouped_nv1 = df_grouped_nv1.rename(columns={'Giới tính': 'Số lượng'})
df_grouped_nv1 = df_grouped_nv1.reset_index()

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped_nv1,
                   x='Ngành đăng kí nguyện vọng 1',
                   y='Số lượng',
                   text='Số lượng',
                   color_discrete_sequence = ['#339900']*len(df_grouped_nv1),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)

# --- DISPLAY IMAGE & DATAFRAME
col1, col2 = st.columns(2)
image = Image.open('images/survey.jpg')
col1.image(image,
        caption='Designed by slidesgo / Freepik')
col2.dataframe(df_grouped_nv1)

# --- PLOT PIE CHART
pie_chart = px.pie(df_grouped_nv1,
                title='Biểu đồ pie phân bố theo ngành',
                values='Số lượng',
                names='Ngành đăng kí nguyện vọng 1')

st.plotly_chart(pie_chart)





# --- PHÂN TÍCH SỐ LIỆU PHÂN BỐ THEO CÁN BỘ TƯ VẤN
st.subheader('4. Phân bố theo cán bộ tư vấn')
# --- STREAMLIT SELECTION
cbtv = df['Cán bộ tư vấn'].unique().tolist()


cbtv_selection = st.multiselect('Cán bộ tư vấn:',
                                    cbtv,
                                    default=cbtv)
# --- FILTER DATAFRAME BASED ON SELECTION
cbtv_mask = df['Cán bộ tư vấn'].isin(cbtv_selection)
number_of_cbtv = df[cbtv_mask].shape[0]
st.markdown(f'*Số lượng sinh viên: {number_of_cbtv}*')

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped_cbtv = df[cbtv_mask].groupby(by=['Cán bộ tư vấn']).count()[['Giới tính']]
df_grouped_cbtv = df_grouped_cbtv.rename(columns={'Giới tính': 'Số lượng'})
df_grouped_cbtv = df_grouped_cbtv.reset_index()

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped_cbtv,
                   x='Cán bộ tư vấn',
                   y='Số lượng',
                   text='Số lượng',
                   color_discrete_sequence = ['#0000FF']*len(df_grouped_cbtv),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)

# --- PLOT PIE CHART
pie_chart = px.pie(df_grouped_cbtv,
                title='Biểu đồ pie phân bố theo cán bộ tư vấn',
                values='Số lượng',
                names='Cán bộ tư vấn')

st.plotly_chart(pie_chart)





# --- PHÂN TÍCH SỐ LIỆU PHÂN BỐ THEO TRƯỜNG THPT
st.subheader('5. Phân bố theo trường THPT')
# --- STREAMLIT SELECTION
THPT = df['Tên trường THPT'].unique().tolist()


THPT_selection = st.multiselect('Tên trường THPT:',
                                    THPT,
                                    default=THPT)
# --- FILTER DATAFRAME BASED ON SELECTION
THPT_mask = df['Tên trường THPT'].isin(THPT_selection)
number_of_THPT = df[THPT_mask].shape[0]
st.markdown(f'*Số lượng sinh viên: {number_of_THPT}*')

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped_THPT = df[THPT_mask].groupby(by=['Tên trường THPT']).count()[['Giới tính']]
df_grouped_THPT = df_grouped_THPT.rename(columns={'Giới tính': 'Số lượng'})
df_grouped_THPT = df_grouped_THPT.reset_index()

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped_THPT,
                   x='Tên trường THPT',
                   y='Số lượng',
                   text='Số lượng',
                   color_discrete_sequence = ['#663366']*len(df_grouped_THPT),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)

# --- PLOT PIE CHART
pie_chart = px.pie(df_grouped_THPT,
                title='Biểu đồ pie phân bố theo Tên trường THPT',
                values='Số lượng',
                names='Tên trường THPT')

st.plotly_chart(pie_chart)






# --- PHÂN TÍCH SỐ LIỆU PHÂN BỐ THEO CÂU HỎI KHẢO SÁT
st.subheader('6. Phân bố theo câu hỏi khảo sát')
# --- STREAMLIT SELECTION
CTLKS = df['Câu trả lời'].unique().tolist()


CTLKS_selection = st.multiselect('Câu trả lời:',
                                    CTLKS,
                                    default=CTLKS)
# --- FILTER DATAFRAME BASED ON SELECTION
CTLKS_mask = df['Câu trả lời'].isin(CTLKS_selection)
number_of_CTLKS = df[CTLKS_mask].shape[0]
st.markdown(f'*Số lượng sinh viên: {number_of_CTLKS}*')

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped_CTLKS = df[CTLKS_mask].groupby(by=['Câu trả lời']).count()[['Giới tính']]
df_grouped_CTLKS = df_grouped_CTLKS.rename(columns={'Giới tính': 'Số lượng'})
df_grouped_CTLKS = df_grouped_CTLKS.reset_index()

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped_CTLKS,
                   x='Câu trả lời',
                   y='Số lượng',
                   text='Số lượng',
                   color_discrete_sequence = ['#663366']*len(df_grouped_CTLKS),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)

# --- PLOT PIE CHART
pie_chart = px.pie(df_grouped_CTLKS,
                title='Biểu đồ pie phân bố theo Câu trả lời',
                values='Số lượng',
                names='Câu trả lời')

st.plotly_chart(pie_chart)