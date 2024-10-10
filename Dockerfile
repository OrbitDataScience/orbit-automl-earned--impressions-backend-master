# Use uma imagem base do Python
FROM python:3.9

# Crie e configure um diretório de trabalho no contêiner
WORKDIR /app

# Copie o código do seu aplicativo Flask para o contêiner
COPY . /app

# Instale as dependências do aplicativo Flask (se houver um requirements.txt)
RUN pip install --upgrade pip

RUN pip install numpy

RUN pip install -r requirements.txt

# Ative o ambiente virtual (se estiver usando um)
# RUN source venv/bin/activate

# Exponha a porta em que o aplicativo Flask está sendo executado no contêiner
EXPOSE 5000


# Configure o comando para iniciar o servidor Flask
#CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
CMD ["python", "app.py"]


#To RUN THE CONTAINER:
#docker run -p 5000:5000 container-name