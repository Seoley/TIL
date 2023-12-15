## Logging의 중요성
- 현재 읽고있는 [필독! 개발자 온보딩](https://www.yes24.com/Product/Goods/119108069)서적에서 log의 중요성을 발견함
- `django`에서 `Debug` 모드를 `False`로 했을 때 로그가 필요하다는 것은 알았지만, 실제 도입해 본적이 없음
- 현재 개발중인 API 서버에 log를 올려 테스트하는 작업을 진행함

### django의 default log
- `django`자체에서 log 기능을 지원하고 있음
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        },
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level': 'INFO',
            'encoding': 'utf-8',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / 'logs/main.log',
            'maxBytes': 1024*1024*5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins', 'file'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        'my': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
    }
}
```
- 파이썬 로그의 레벨: `DEBUG` < `INFO` < `WARNING` < `ERROR` < `CRITICAL`
- 각 로그레코드(메세지)는 레벨을 지니고 있음
- `BASE_DIR / 'logs/main.log'` logs 폴더의 main.log에 기입됨 

### Handler
- 로거에 있는 메세지에 어떤 작업을 할지 결정
- 각 로거는 레벨이 적혀있음
- INFO라고 적혀있다면 INFO 이상의 로그만 기입됨(DEBUG는 기입되지 않음)

### 로거 네임 스페이스
```python
# my_app/views.py
logger = logging.getLogger(__name__)
```

```python
LOGGING = {
    # ...
    "loggers": {
        "my_app.views": {...},
    },
}
```
- `my_app`이라는 app에서 발생하는 log만 수집
- https://docs.djangoproject.com/ko/5.0/howto/logging/

## 참고자료
- https://chiefcoder.tistory.com/43
- https://hikoding.tistory.com/49