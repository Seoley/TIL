## 페이지 안내
- 그날 공부한 것을 무작위로 기록
- 기록한 것 중 어느정도 정보값이 쌓인 것은 각 분야 카테고리별 폴더에 정리할 것

## 메모 내용

### docstring 작성
https://jh-bk.tistory.com/15

### github 내 특정 파일 제외해서 pull하기
`.gitignore` 외에 특정 브랜치에서 특정 파일을 pull하지 않기 위해서는 `sparse-checkout` 또는 `--skip-worktree` 등을 사용할 수 있습니다. 이 중에서 `--skip-worktree`는 특정 파일의 변경사항을 무시하도록 설정하는 방법입니다.

아래는 특정 브랜치에서 특정 파일을 `pull`할 때 `--skip-worktree`를 사용하는 예시입니다.

```bash
# 원격 저장소의 변경사항을 가져올 때 특정 파일을 pull하지 않도록 설정
git update-index --skip-worktree path/to/your/file

# 변경사항을 가져옴
git pull origin your-branch
```

그러나 이 방법은 로컬에서 해당 파일에 대한 변경사항을 추적하지 않도록 설정하는 것이며, 이 파일이 원격 저장소에서 변경된 경우에는 적용되지 않을 수 있습니다. 원격 저장소에서도 변경을 무시하려면 `.git/info/exclude`에 파일을 추가하거나, 해당 파일을 `.gitignore`에 추가하여 커밋하지 않도록 하는 것이 좋습니다.

### Ludwig 중 오류 발생
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

### Ludwig - GPU support 문제
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

### github 에서 독립적으로 동일한 파일 관리
- 참고 블로그
  - https://sasohan.github.io/2022/03/24/merge-strategies-using-git-attributes/
  - 위의 이거 내가 딱 찾으려고 했던 그거임!!!

### Anaconda CUDA 설치
- 발생 에러
```bash
  File "C:\Users\dltjf\anaconda3\envs\chatbot_env\lib\site-packages\bitsandbytes\cextension.py", line 20, in <module>
    raise RuntimeError('''
RuntimeError:
        CUDA Setup failed despite GPU being available. Please run the following command to get more information:

        python -m bitsandbytes

        Inspect the output of the command and see if you can locate CUDA libraries. You might need to add them
        to your LD_LIBRARY_PATH. If you suspect a bug, please take the information from python -m bitsandbytes
        and open an issue at: https://github.com/TimDettmers/bitsandbytes/issues
```
- 참고 블로그
  - https://docs.nvidia.com/cuda/cuda-quick-start-guide/index.html
    - cuda 설치
  - https://otugi.tistory.com/334
    - cudatoolkit 설치
- 검색 키워드 `anaconda set ld_library_path`
  - 

### bitsandbytes 관련 에러
```bash
The following directories listed in your path were found to be non-existent: {WindowsPath('C')}
C:\Users\dltjf\anaconda3\envs\chatbot_env\lib\site-packages\bitsandbytes\cuda_setup\main.py:166: UserWarning: C:\Users\dltjf\anaconda3\envs\chatbot_env did not contain ['libcudart.so', 'libcudart.so.11.0', 'libcudart.so.12.0'] as expected! Searching further paths...
  warn(msg)
The following directories listed in your path were found to be non-existent: {WindowsPath('/etc/bash.bashrc')}
The following directories listed in your path were found to be non-existent: {WindowsPath('BASH_ENV/u')}
CUDA_SETUP: WARNING! libcudart.so not found in any environmental path. Searching in backup paths...
The following directories listed in your path were found to be non-existent: {WindowsPath('/usr/local/cuda/lib64')}
DEBUG: Possible options found for libcudart.so: set()
CUDA SETUP: PyTorch settings found: CUDA_VERSION=118, Highest Compute Capability: 8.6.
CUDA SETUP: To manually override the PyTorch CUDA version please see:https://github.com/TimDettmers/bitsandbytes/blob/main/how_to_use_nonpytorch_cuda.md
CUDA SETUP: Loading binary C:\Users\dltjf\anaconda3\envs\chatbot_env\lib\site-packages\bitsandbytes\libbitsandbytes_cuda118.so...
argument of type 'WindowsPath' is not iterable
CUDA SETUP: Problem: The main issue seems to be that the main CUDA runtime library was not detected.
CUDA SETUP: Solution 1: To solve the issue the libcudart.so location needs to be added to the LD_LIBRARY_PATH variable
CUDA SETUP: Solution 1a): Find the cuda runtime library via: find / -name libcudart.so 2>/dev/null
CUDA SETUP: Solution 1b): Once the library is found add it to the LD_LIBRARY_PATH: export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:FOUND_PATH_FROM_1a
CUDA SETUP: Solution 1c): For a permanent solution add the export from 1b into your .bashrc file, located at ~/.bashrc
CUDA SETUP: Solution 2: If no library was found in step 1a) you need to install CUDA.
CUDA SETUP: Solution 2a): Download CUDA install script: wget https://github.com/TimDettmers/bitsandbytes/blob/main/cuda_install.sh
CUDA SETUP: Solution 2b): Install desired CUDA version to desired location. The syntax is bash cuda_install.sh CUDA_VERSION PATH_TO_INSTALL_INTO.
CUDA SETUP: Solution 2b): For example, "bash cuda_install.sh 113 ~/local/" will download CUDA 11.3 and install into the folder ~/local
...
RuntimeError:
        CUDA Setup failed despite GPU being available. Please run the following command to get more information:

        python -m bitsandbytes

        Inspect the output of the command and see if you can locate CUDA libraries. You might need to add them
        to your LD_LIBRARY_PATH. If you suspect a bug, please take the information from python -m bitsandbytes
        and open an issue at: https://github.com/TimDettmers/bitsandbytes/issues
```
- 해결법
  - `pip install bitsandbytes-windows`
  - bitsandbytes가 window에서 쓸 수 없어서 발생한 문제

- 어떻게 알아냈느냐?
  - `LD_LIBRARY_PATH`를 추가해도 문제가 발생함
  - ` libcudart.so`가 없어서 발생한 문제임을 확인. 그런데 `libcudart.so`는 mac/linux에서만 사용 가능함.
  - https://github.com/TimDettmers/bitsandbytes/issues/857
  - `pip install https://github.com/jllllll/bitsandbytes-windows-webui/releases/download/wheels/bitsandbytes-0.41.1-py3-none-win_amd64.whl`