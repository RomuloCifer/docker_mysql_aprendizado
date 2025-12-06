from dotenv import load_dotenv
load_dotenv()
import os
from typing import Final # garante que as variaveis não vão mudar.

MYSQL_ROOT_PASSWORD: Final[str] =os.getenv("MYSQL_ROOT_PASSWORD", "")
MYSQL_DATABASE: Final[str]= os.getenv("MYSQL_DATABASE", "")
MYSQL_USER: Final[str]= os.getenv("MYSQL_USER", "")
MYSQL_PASSWORD: Final[str]= os.getenv("MYSQL_PASSWORD", "")
MYSQL_HOST: Final[str]= os.getenv("MYSQL_HOST", "localhost")