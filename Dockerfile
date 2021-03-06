FROM python:3.7.2-alpine3.9
RUN apk add --no-cache python3-dev libstdc++ && \
    apk add --no-cache g++ && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h && \
    pip3 install numpy && \
    pip3 install pandas
COPY . /app
WORKDIR /app
COPY ./original_df.pkl /app/original_df.pkl
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5001 
ENTRYPOINT [ "python" ] 
CMD [ "app.py" ] 

