from fluent import sender
from fluent import event
import datetime

# Fluentd 설정
logger = sender.FluentSender('fluentd.test', host='localhost', port=24224)

# 로그 데이터 전송
log_data = {
    'log': 'Test log from Python script!',
    'stream': 'stdout',
    'timestamp': datetime.datetime.now().isoformat()
}

# 'fluentd.test' 태그로 로그 전송
try:
    logger.emit('fluentd.test', log_data)
    print("Log sent to Fluentd successfully.")
except Exception as e:
    print(f"Failed to send log to Fluentd: {e}")
