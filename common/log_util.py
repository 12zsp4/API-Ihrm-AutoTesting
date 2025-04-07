import logging
import os
from datetime import datetime

def get_logger(log_name="test"):
    # 日志目录（你自定义的路径）
    log_dir = r"D:\Python\pythonProject\SelfStudy\FrameWork\apiAutoFramworkIhrm\log"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 日志文件名：带时间戳
    log_filename = f"{log_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    log_path = os.path.join(log_dir, log_filename)

    # 日志格式（符合你的要求）
    log_format = '%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(log_format)

    # 创建 logger
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)

    # 防止日志重复输出
    if not logger.handlers:
        # 文件处理器
        fh = logging.FileHandler(log_path, encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        # 控制台处理器
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger


if __name__ == '__main__':
    log = get_logger("api_test")
    log.info("接口测试开始")
    log.error("测试失败，响应码不正确")
