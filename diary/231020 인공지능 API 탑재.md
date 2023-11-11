# 231018 mlflow와 인공지능 API 테스트

## 상황
- 인공지능 학습 관리를 위해 꾸준히 mlflow를 도입하고 있음
- mlflow에서 artifacts를 인식하지 못하는 문제 발생
- 학습관리가 원큐로 되지 않아서 너무 불편하다. 테스트해야할 것이 진짜 너무너무 많음.
    - 현재 작업하고있는 학습은 시험인증 항목 중 '재현율'이 있음
    - 학습/테스트 코드를 분리해놨기 때문에 재현율에 대한 실험을 별도로 하는게 번거로움
- 인공지능 API 테스트를 하기 위해 백엔드 담당자에게 테스트서버에 업로드를 요청하였으나 예상보다 일정이 늦어짐
- 플랫폼 개발자가 API 테스트를 진행해야하기 때문에, 급한대로 API를 배포할 필요가 있음

## 분석
- mlflow의 artifacts의 경로에 이상이 있음을 확인함
- 학습/테스트 코드의 통합 필요성
    - 단발적인 확인을 위해서는 두 코드를 분리해도 큰 문제가 없으나, 코드가 완성된 단계에서 해당 절차를 진행하는 것은 번거로울 것으로 판단됨
- API 테스트를 내부망 환경에서 진행할 수 있는 방법을 모색
    - 우리 회사는 내부망을 사용하고 있으므로 로컬 서버 접속이 자유로움
    - API 테스트를 플랫폼 개발자가 빨리 진행하여야 일정에 차질이 없으므로, 클라우드 담당자가 업로드 하기 전에 테스트 환경을 빠르게 구축하는 것이 중요함

## 액션
- mlflow의 artifact 경로 수정
  - 해당 문제를 해결하기 위해서는 backserver의 tracking 기능이 별도로 필요한 것으로 보임
  - 기초적인 mlflow의 실행부터 다시금 정리함
  - 해당 코드를 사용했을 떄 경로문제가 수정되는 이유를 추후 검토할 필요가 있음
- mlflow 코드 내부에 재현율에 따른 코드 작성
    ```python
    # 데이터 생성용 코드
    test_dataset = pd.read_csv("../data/4_experiments/ecg_test_set.csv")

    X_dataset_0, y_dataset_0 = get_labeled_dataset(test_dataset, 0)
    X_dataset_1, y_dataset_1 = get_labeled_dataset(test_dataset, 1)
    X_dataset_2, y_dataset_2 = get_labeled_dataset(test_dataset, 2)
    X_dataset_3, y_dataset_3 = get_labeled_dataset(test_dataset, 3)
    X_dataset_4, y_dataset_4 = get_labeled_dataset(test_dataset, 4)
    X_dataset_5, y_dataset_5 = get_labeled_dataset(test_dataset, 5)    
    ```
    ```python
    # 데이터 생성을 위한 함수
    def make_x_y_set(dataset: pd.DataFrame):
        '''
        x, y 데이터셋 생성
        dataset.iloc[:,0:125]: ECG 수치
        dataset['label']: 라벨값
        '''
        X_dataset = dataset.iloc[:,:125]
        y_dataset = dataset['label']

        X_dataset = np.array(X_dataset)
        X_dataset = X_dataset.reshape(-1,125,1)
        y_dataset = np.array(y_dataset)
        y_dataset = tf.keras.utils.to_categorical(y_dataset, 6)

        return X_dataset, y_dataset

    def get_labeled_dataset(dataset: pd.DataFrame, label: int):
        dataset = dataset[dataset['label'] == label]
        X_dataset, y_dataset = make_x_y_set(dataset)
        return X_dataset, y_dataset
    
    ```
    ```python
    # mlflow 코드
    import mlflow


    mlflow.set_experiment("ECG_analysis_(ECGNet)")

    with mlflow.start_run():

        mlflow.tensorflow.autolog()
        with tf.device('/device:GPU:0'): 
            model.fit(X_train,y_train,epochs=500,batch_size=128, validation_data=(X_val, y_val), callbacks = [checkpoint])


        model.load_weights(checkpoint_path)

        preds = model.predict(X_test)
        preds = np.round(preds)

        eval_acc = model.evaluate(X_test, y_test)[1]
        auc_score = roc_auc_score(y_test, preds, multi_class='raise')

        recall_01 = model.evaluate(X_dataset_1, y_dataset_1)[1]
        recall_02 = model.evaluate(X_dataset_2, y_dataset_2)[1]
        recall_03 = model.evaluate(X_dataset_3, y_dataset_3)[1]
        recall_04 = model.evaluate(X_dataset_4, y_dataset_4)[1]
        recall_05 = model.evaluate(X_dataset_5, y_dataset_5)[1]

        print("eval_acc: ", eval_acc)
        print("auc_score: ", auc_score)

        mlflow.tensorflow.mlflow.log_metric('eval_acc', eval_acc)
        mlflow.tensorflow.mlflow.log_metric('auc_score', auc_score)

        mlflow.tensorflow.mlflow.log_metric('recall_label_1', recall_01)
        mlflow.tensorflow.mlflow.log_metric('recall_label_2', recall_02)
        mlflow.tensorflow.mlflow.log_metric('recall_label_3', recall_03)
        mlflow.tensorflow.mlflow.log_metric('recall_label_4', recall_04)
        mlflow.tensorflow.mlflow.log_metric('recall_label_5', recall_05)

        model_name = f'ECGNet_model_acc_{eval_acc}'
        mlflow.tensorflow.log_model(model, model_name, keras_model_kwargs={"save_format": "h5"})

    mlflow.end_run()
    ```
- API 로컬 환경에서 배포
    - 내부망의 경우, 내부 IP 주소를 활용하여 배포가 가능함
    - django서버 config.settings에서 ALLOWED_HOSTS에 내 컴퓨터의 내부 ip와 백엔드 개발자의 내부 ip를 등록함
    ```python
    ALLOWED_HOSTS = ["localhost", "192.168.0.149", "192.168.0.20"]
    ```
    - 이후 `python manage.py runserver 192.168.0.20:8000` 실행

## 회고
- 직면한 문제가 여럿 있었으나, 시간 내에 전부 해결할 수 있었다. 이전보다 버그 및 이슈 해결 속도가 월등히 빨라졌음!
- 협업에 필요한 것은 완성도보다는 시간 엄수라는 것을 새삼 상기하였음. 불안정하더라도 최소 조건으로 먼저 협업할 수 있는 환경을 만들어야함
- 그렇다고해서 부정확한 결과물을 전달해야하는 것은 아님. 80%정도의 완성도로, 마감은 지키는 것을 목표로 진행하자.
- mlflow에 조금 더 적응을 한 것 같다. 익숙해지면 정리해서 회사 내부에서 사용할 수 있도록 배포해야겠음.