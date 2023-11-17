# MLops

## NHN cloud에 인공지능 file 업로드하기
- MLOps 구축에 대한 다양한 탐색 진행중
- 로컬 환경에서 인공지능 학습 후, cloud에 file을 업로드 하여 배포하는 방식을 고민함
- `NHN cloud`에서도 `AWS`의 API를 활용할 수 있음을 알게됨
    - https://docs.nhncloud.com/ko/Storage/Object%20Storage/ko/s3-api-guide/
```python
# file 업로드 코드
def upload(self, bucket_name, key, filename):
    try:
        self.s3.upload_file(
            Filename=filename, Bucket=bucket_name, Key=key)
    except ClientError as e:
        raise RuntimeError(e)
```
## 간단히 Django를 실행하기 위한 방법
### 상황
- 현재 개발중인 인공지능 자동학습 탑재 플랫폼은 인공지능 비전문가가 사용함
- 필요에 따라서 개발지식이 없는 유저가 클라이언트가 될 수도 있음
- 개발한 세팅은 docker를 기반으로 구축된 django 패키지를 설치하는 방식으로, 비전문가가 활용할 때 어려움이 있을 것으로 판단됨
- 게임 등 프로그램들의 .exe 파일처럼 더블클릭으로 실행할 수 있는 환경을 만들 수 있지 않을까? 라는 의문에서 시작하여 탐색 진행함

### Django 실행 bat 파일 생성
`ChatGPT 질의응답 기반 기록`
1. 배치 파일 작성

    로컬에서 Django 서버를 실행하는 배치 파일을 작성합니다. 예를 들어, runserver.bat라는 파일을 만들어보겠습니다.

    ```bash
    @echo off
    cd path\to\your\django\project
    call .\venv\Scripts\activate
    python manage.py runserver
    ```

    위의 코드에서 path\to\your\django\project는 Django 프로젝트의 경로로 변경해야 합니다. .\venv\Scripts\activate는 가상 환경을 활성화하는 명령어입니다.

2. 실행 스크립트 작성

    다음으로, 사용자가 더블 클릭하여 실행할 수 있는 스크립트를 작성합니다. 이 스크립트에서는 위에서 작성한 배치 파일을 실행하는 역할을 합니다.

    ```bash
    @echo off
    start cmd /k "runserver.bat"
    ```

    이 스크립트에서 start cmd /k는 새로운 커맨드 프롬프트 창을 열고 해당 창을 유지하도록 하는 역할을 합니다.

3. 더블 클릭으로 실행

    위에서 작성한 실행 스크립트 파일에 더블 클릭하면 새로운 커맨드 프롬프트 창이 열리고 Django 서버가 실행됩니다.

    
4. 알림 추가 (선택 사항)
    사용자에게 Django 서버가 실행되었음을 알리기 위해, 배치 파일이 실행될 때 알림을 추가할 수 있습니다. msg * 명령어를 사용하면 됩니다.


    ```bash
    @echo off
    msg * Django 서버가 실행되었습니다. http://localhost:8000 에 접속하세요.
    cd path\to\your\django\project
    call .\venv\Scripts\activate
    python manage.py runserver
    ```

    이제 사용자가 더블 클릭만으로 Django 서버를 실행할 수 있습니다. 애플리케이션이 간단하고 사용자가 편리하게 실행할 수 있도록 만들어주는 접근 방법입니다.

# Github
## 오픈소스에 기여하기
### 상황
- `Ludwig` 오픈소스를 활용 중, 몇 가지 개선 제안 방안이 생각남
- Pull request를 한번 진행해보고 싶어서 시도해보기로...
- 하지만 역시 한번도 해본 적 없어서 무섭다. 다른 사람들의 사례를 먼저 수집하자!
- 참고자료: https://soniacomp.medium.com/%EC%A3%BC%EB%8B%88%EC%96%B4-%EA%B0%9C%EB%B0%9C%EC%9E%90%EA%B0%80-%EC%98%A4%ED%94%88%EC%86%8C%EC%8A%A4-%EC%BB%A8%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95-117e99540e2d

# 개인 개발 공부
## 개발자는 어떻게 공부하는게 좋을까?
- 근래에 회사 외부에서도 개발 공부를 할 필요성을 느낌
- 그러나 운동이나 영어공부 등 다른 자기계발에 시간을 투자하다보면 개발에 시간을 쓰기가 어려움
- 효율적인 개발자 공부 루틴을 찾고싶어서 이런저런 저널을 찾아보고 있음
- [집에-가면-어떤-공부를-하면-좋을까요](https://blog.novice.io/%EC%83%9D%EA%B0%81/2022/09/18/%EC%A7%91%EC%97%90-%EA%B0%80%EB%A9%B4-%EC%96%B4%EB%96%A4-%EA%B3%B5%EB%B6%80%EB%A5%BC-%ED%95%98%EB%A9%B4-%EC%A2%8B%EC%9D%84%EA%B9%8C%EC%9A%94.html)