import signal
import sys

def sig_handler(signum, frame):
    # 执行自定义操作
    print("Ctrl+C interrupt detected. Exiting...")
    # sys.exit()

# 注册 Ctrl+C 信号处理程序
signal.signal(signal.SIGINT, sig_handler)

# 主程序逻辑
try:
    while True:
        # 执行你的代码逻辑
        pass
except KeyboardInterrupt:
    # 捕获 Ctrl+C 中断信号，执行自定义操作
    print("Keyboard interrupt detected. Exiting...")
    sys.exit()