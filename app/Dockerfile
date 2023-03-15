FROM python:3.6.13-slim

WORKDIR /app
COPY requirements.txt /app
COPY mypage.html /app
RUN pip install --upgrade pip &&  python -m pip install -r requirements.txt

EXPOSE 5000

COPY . /app
COPY entrypoint.sh /
ENTRYPOINT ["/bin/sh", "/entrypoint.sh"]
