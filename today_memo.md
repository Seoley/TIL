## 페이지 안내
- 그날 공부한 것을 무작위로 기록
- 기록한 것 중 어느정도 정보값이 쌓인 것은 각 분야 카테고리별 폴더에 정리할 것

## 메모 내용

### docstring 작성
https://jh-bk.tistory.com/15


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

  # 231123
  ## Python을 이용해 파일을 local에서 EC2로 업로드하는 법
  - https://repost.aws/questions/QUAECsXArNQv2DcHMt0OOWTw/how-to-upload-file-from-local-machine-to-an-ec2-instance-planning-to-use-aws-sdk-via-python

  # 231124
  ## Docker 볼륨 생성 및 연동
  - https://velog.io/@ckstn0777/%EB%8F%84%EC%BB%A4-%EB%B3%BC%EB%A5%A8
  ```bash
  # 볼륨 생성
  docker 
  docker volume create --name myvolume
  docker volume ls
  ```

  ## Volume 마운트
  - https://www.daleseo.com/docker-volumes-bind-mounts/

  ## 코드 메모
  ``` DockerFile
  version: '3.5'
  services:
    chatbot_api:
      build: 
        context: .
        dockerfile: ./API/Dockerfile
      command: sh -c "cd API && gunicorn config.wsgi:application --bind 0.0.0.0:8000"
      volumes: 
        - alzam_ai:/childcare_chatbot
      expose:
        - "8000"
    chatbot_mlops:
      build: 
        context: .
        dockerfile: ./MLOps/Dockerfile
      command: sh -c "cd MLOps && gunicorn config.wsgi:application --timeout 1200 --bind 0.0.0.0:8001"
      volumes: 
        - alzam_ai:/childcare_chatbot
      expose:
        - "8001"
  volumes:
    alzam_ai:
  ```

  ## docker 네트워크
  - https://velog.io/@choidongkuen/%EC%84%9C%EB%B2%84-Docker-Network-%EC%97%90-%EB%8C%80%ED%95%B4

  ## Volume을 사용하여 디렉토리 공유
  - https://ko.linux-console.net/?p=7805
  - 도커를 마운트해서 공유 가능. `마운트`의 개념을 확실히 이해해보자.

  ## Docekr의 sqlite3 설치
  ```DockerFile
  # SQLite3 설치
  RUN apt-get update && apt-get install -y sqlite3
  ```

  ## Docker에서 django 리로드

  ## 설정파일 관리법(django)
  - https://mingrammer.com/ways-to-manage-the-configuration-in-python/

  ## Django의 main앱 명명 토론
  - https://www.reddit.com/r/django/comments/anirli/discussion_what_to_call_the_main_app_in_your/