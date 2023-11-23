
# github 활용
## github 내 특정 파일 제외해서 pull하기
`.gitignore` 외에 특정 브랜치에서 특정 파일을 pull하지 않기 위해서는 `sparse-checkout` 또는 `--skip-worktree` 등을 사용할 수 있습니다. 이 중에서 `--skip-worktree`는 특정 파일의 변경사항을 무시하도록 설정하는 방법입니다.

아래는 특정 브랜치에서 특정 파일을 `pull`할 때 `--skip-worktree`를 사용하는 예시입니다.

```bash
# 원격 저장소의 변경사항을 가져올 때 특정 파일을 pull하지 않도록 설정
git update-index --skip-worktree path/to/your/file

# 변경사항을 가져옴
git pull origin your-branch
```

그러나 이 방법은 로컬에서 해당 파일에 대한 변경사항을 추적하지 않도록 설정하는 것이며, 이 파일이 원격 저장소에서 변경된 경우에는 적용되지 않을 수 있습니다. 원격 저장소에서도 변경을 무시하려면 `.git/info/exclude`에 파일을 추가하거나, 해당 파일을 `.gitignore`에 추가하여 커밋하지 않도록 하는 것이 좋습니다.

## github 에서 독립적으로 동일한 파일 관리
환경설정(config.json, settings.py 등) 파일을 제외하고 동일한 코드를 push/pull 할 때 발생하는 파일관리 이슈를 해결하고자 한다. 

`main` 브랜치에 local 환경의 코드를 push 하고, `cloud_server` 브랜치에 pull해서 반영할 때, 동일한 이름을 지닌 파일은 `main` 브랜치에 작성한 것으로 갱신된다. 이 때, Django의 `settings.py` 등 로컬 환경과 클라우드 환경에서 다르게 유지되는 파일은 독립적으로 운용할 수 있도록 코드를 작성하고 싶었다.

`.gitignore`를 쓸 경우, 환경설정 파일이 아예 github에 업로드가 되지 않아 해결책이 되지 않는다. 구글 드라이브 등으로 별도 관리하는 방법도 있겠지만, 아무래도 복잡해져서 다른 방법을 찾고자 했다.

### 해결법
`cloud_server` 브랜치에 `.gitattributes` 파일을 추가하여 다음 내용을 작성한다.
```bash
**/config.json merge=cloud_server
**/settings.py merge=cloud_server
```
`cloud_server`에서 `main` 브랜치 내용을 가져와 pull할 때, 지정된 파일은 `cloud_server`에 있는 내용으로 `merge`가 된다.

`API/config/settings.py`등 특정 폴더만을 넣고 싶다면 아래와 같이 작성하면 된다.
```bash
API/config/settings.py merge=cloud_server
```

### 참고 블로그
  - https://sasohan.github.io/2022/03/24/merge-strategies-using-git-attributes/