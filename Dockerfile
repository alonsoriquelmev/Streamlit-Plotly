FROM python:3.10

EXPOSE 8501

WORKDIR /app

COPY . ./

RUN pip install --upgrade pip
RUN pip install streamlit 
RUN pip install pandas 
RUN pip install numpy 
RUN pip install plotly==5.11.0

CMD streamlit run main.py --server.fileWatcherType none