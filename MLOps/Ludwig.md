## Ludwig 중 오류 발생
- 오류 내용
```bash
...
...
  File "C:\Users\dltjf\Developments\2. 업무 개발 코드\04 챗봇 서비스\env\lib\site-packages\yaml\scanner.py", line 116, in check_token
    self.fetch_more_tokens()
  File "C:\Users\dltjf\Developments\2. 업무 개발 코드\04 챗봇 서비스\env\lib\site-packages\yaml\scanner.py", line 255, in fetch_more_tokens
    return self.fetch_plain()
  File "C:\Users\dltjf\Developments\2. 업무 개발 코드\04 챗봇 서비스\env\lib\site-packages\yaml\scanner.py", line 679, in fetch_plain
    self.tokens.append(self.scan_plain())
  File "C:\Users\dltjf\Developments\2. 업무 개발 코드\04 챗봇 서비스\env\lib\site-packages\yaml\scanner.py", line 1290, in scan_plain
    ch = self.peek(length)
  File "C:\Users\dltjf\Developments\2. 업무 개발 코드\04 챗봇 서비스\env\lib\site-packages\yaml\reader.py", line 91, in peek
    self.update(index+1)
  File "C:\Users\dltjf\Developments\2. 업무 개발 코드\04 챗봇 서비스\env\lib\site-packages\yaml\reader.py", line 153, in update
    self.update_raw()
  File "C:\Users\dltjf\Developments\2. 업무 개발 코드\04 챗봇 서비스\env\lib\site-packages\yaml\reader.py", line 178, in update_raw
    data = self.stream.read(size)
UnicodeDecodeError: 'cp949' codec can't decode byte 0xe2 in position 5393: illegal multibyte sequence
```
- 발생 위치
```bash
  File "C:\Users\dltjf\Developments\2. 업무 개발 코드\04 챗봇 서비스\env\lib\site-packages\ludwig\schema\metadata\__init__.py", line 33, in <module>
    ENCODER_METADATA = _load("encoders.yaml")
```
- 해결방안
```python
# open()에 'r',encoding='utf-8' 추가
# yaml 유니코드 문제
def _load(fname: str) -> Dict[str, Any]:
    with open(os.path.join(_CONFIG_DIR, fname), 'r',encoding='utf-8') as f:
        return _to_metadata(yaml.safe_load(f))
```

## Ludwig - GPU support 문제
- 오류내용
```bash
C:\Users\dltjf\Developments\2. 업무 개발 코드\04 챗봇 서비스\env\lib\site-packages\bitsandbytes\cextension.py:34: UserWarning: The installed version of bitsandbytes was compiled without GPU support. 8-bit optimizers, 8-bit multiplication, and GPU quantization are unavailable.
  warn("The installed version of bitsandbytes was compiled without GPU support. "
'NoneType' object has no attribute 'cadam32bit_grad_fp32'
```
- 액션
    - env에서 cuda설정이 안되어서 발생하는 문제 같음
    - anaconda를 사용해서 env를 재생성. anaconda는 별도의 독립적인 cuda를 사용할 수 있도록 지원해주므로, 이쪽을 사용하는 것이 좋다고 판단됐음.
- 참고 블로그
    - https://blog.lablup.com/en/posts/2023/07/28/bitsandbytes/

