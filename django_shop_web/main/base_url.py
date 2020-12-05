import os

if os.name=="nt":
    base_url="http://web:8000/"
elif os.name=="posix":
    base_url="http://web:8000/"#可調整成自己提供的網站網域例www.example.com