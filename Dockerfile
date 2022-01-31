FROM python:3.8
EXPOSE 8501
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["streamlit","run"]
CMD ["main.py"]

