from curses.panel import version
from setuptools import setup #setup 파일이 있으면 pip로 설치 가능하다

setup(
    name ="myapi", #이 이름으로 패키지 설치
    version = "0.0.1",
    description = "my api lib",
    url = "https://github.com/tail97/api_project.git",
    author= "hanJeongHun",
    author_email= "hanjeonghun169@gmail.com",
    packages = ["my_api"],
    install_requires = [
        "requests"
    ]
)