from application import advisor
from config import DevelopmentConfig



if __name__ == '__main__':
    advisor(config=DevelopmentConfig(),app_name="advisor").run()
