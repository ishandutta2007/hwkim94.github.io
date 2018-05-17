---
layout: post
title:  "Distributed DL[1] Parallel and Distributed Deep Learning(2016) - Review"
date:   2018-05-16 01:30:00 +0900
categories: [distributed-computing, deeplearning]
---

## 1. Abstract
- 병렬/분산처리 환경에서의 DL 경험적 연구
- Data Parallelism의 synchronous/asynchronous weight update algorithms 탐구
    - Parallel SGD, ADMM, Downpour SGD 등

-----

## 2. Introduction
# 2.1 Deep Learning
- DL은 data의 g correlation structures을 비지도학습으로 찾아내는 것에 적합
    - NLP, Computer Vision에 적합

- data의 정보가 각 layer에 weight의 형태로 분산되어있고, 이 정보들을 합쳐서 원하는 목적을 이루는 형태의 모델

# 2.2 Need for Parallel and Distributed Algorithms in Deep Learning
- DL의 경우 parameter가 너무 많아지므로 학습시키는 시간이 너무 오래 걸림
    - 따라서, 병렬처리 및 분산처리가 필수적 

-----

## 3. Parallel and Distributed Methods
# 3.1 Local Training 
- multi-core processing
    - 각 layer마다 다른 core가 담당하여, 각 layer의 연산을 동시에 처리하는 방법 
    - 각 core마다 mini-batch의 SGD를 수행하는 방법

- GPU 사용
    - matrix multiplication과 같이 intensive computation에 유리

- multi-core processing, GPU 모두 사용
    - 모든 core가 GPU를 공유하여 intensive computation을 GPU에서 처리

# 3.2 Distributed training
- Data Parallelism
    - data가 너무 큰 경우, 각 node에 분산하여 저장
    - 즉, 각 node에서 모델을 학습시키고 제일 weight의 평균이나 제일 좋은 모델을 뽑는 방식으로 모델을 최종선택

- Model Parallelism
    - model이 너무 큰 경우, 각 node마다 처리하는 layer를 분산하여 처리
    - 즉, 각 node에서 맡은 model의 일부분을 처리한 후 합쳐서 다음 layer를 맡은 node로 넘겨주는 방식

-----

## 4. Empirical analysis: CPU versus GPU time
# 4.1 Parallel Implementation of Convolution in Caffe
- CNN의 경우 하나의 kernel이 하나의 image를 slide하는 형태
    - convolution이 발생하는 image의 부분을 각각의 vector로 만든 후, 이 vector들을 쌓아서 matrix형태로 만듦

- CNN의 한 layer에서 사용되는 filter가 많으므로 filter도 matrix의 형태가 됨
- 최종적으로 이 matrix들을 multiplication해주면 한 layer에서의 convolution 결과가 나옴
- ex) kernal size = $$2 \times 2$$이고, stride=1 인 convolution
    - $$v_1$$ = $$(image_{1,1}, image_{1,2}, image_{2,1}, image_{2,2})$$
    - $$v_2$$ = $$(image_{1,2}, image_{1,3}, image_{2,2}, image_{2,3})$$ ...
    - $$k_1$$ = $$(k_{1,1}, k_{1,2}, k_{2,1}, k_{2,2})$$
    - $$V$$ = $$\begin{bmatrix} v_1\\ v_2\\ v_3\\ \cdots \end{bmatrix}$$
    - $$K$$ = $$\begin{bmatrix} k_{1}^T \mid k_{2}^T \mid k_{3}^T \mid \cdots \end{bmatrix}$$
    - $$convoluion(image)$$ = $$VK$$

# 4.2 Results
- GPU가 CPU보다 훨씬 성능이 좋음

### 4.2.1 Convolution Layer
![result1](https://files.slack.com/files-pri/T1J7SCHU7-FAQSD9E3H/result1.png?pub_secret=8c999d97df)

### 4.2.2 Fully Connected Layer 
![result2](https://files.slack.com/files-pri/T1J7SCHU7-FAP4GRGMN/result2.png?pub_secret=b8fa158594)

-----

## 5. Stochastic Gradient Descent
- Gradient Descent
    - $$w$$ = $$w - \alpha \bigtriangledown_{w} L_{total}$$
    - $$L_{total}$$ = $$\frac{1}{n} \sum{L_i}$$, 즉, 모든 data의 loss의 합
    - $$L_i$$ = $$-f_{y_i} + log \sum e^{f_i}$$, data의 loss는 logistic loss function
    - 즉, gradient descent는 모든 data의 loss의 평균을 구하여 1번만 descent하는 방식
    - 따라서, 최적화하기 위해서 엄청 많은 descent가 필요하므로 비효율적

- Stochastic Gradient Descent
    - $$w$$ = $$w - \alpha \bigtriangledown_{w} L_{mini batch}$$
    - $$L_{mini batch}$$ = $$\frac{1}{m} \sum{L_i}$$, 즉, mini batch의 loss의 합
    - SGD는 각 mini batch의 loss의 평균만을 이용해 gradient를 계산하여 weight를 update
    - 따라서, batch의 수 만큼 gradient를 update하게 됨

-----

## 6. Data Parallelism
# 6.1 Synchronous(동기화) Update
![data](https://files.slack.com/files-pri/T1J7SCHU7-FAPS9NR3L/sgd.png?pub_secret=71b1ed88c4)
- 모든 mini-batch의 gradient는 같은 weight를 사용하여 계산됨 
- 모든 mini-batch의 gradient가 계산될 때까지 기다림
- gradient를 통합하여 weight update(synchronization)를 한 후, weight를 각 node에 다시 복사

### 6.1.1 Parallel SGD
- Assumption(가정)
    - 각 node에 분산되어있는 data가 균일하지 않다
    - loss function이 convex하다는 가정하의 알고리즘
    - 너무 강력한 가정을 하고 있다는 점이 단점

- Algorithm Design
    - 각 node의 data가 전체 data set을 representative할 수 있도록 shuffle
    - 각 node에서 data들로 SGD를 수행하여 각 node에 있는 모델의 weight update
    - 각 node의 weight를 driver로 보내 평균을 구한 후, 모든 node들로 재분배하여 다시 학습

### 6.1.2 Alternating Direction Method of Multipliers SGD(ADMM SGD)
- Algorithm Design
    - 각 node에서 data들로 SGD를 수행하여 각 node에 있는 모델의 weight update
    - 각 node의 weight를 driver로 보낸 후, driver에서 ADMM algorithm으로 weight update
    - 모든 node들로 weight 재분배

- ADMM algorithm : 라그랑주 승수법을 활용한 최적화 방식
    - 각 node에서 update된 weight는 loss function $$f_{k}(x_{k}) = loss_k$$를 성립
    - 따라서, driver의 weight로 만들어진 loss function $$f$$는 $$f(x_{k}) = loss_k$$를 만족하는 제약조건을 가지게 됨
    - 즉, $$f(x_{k}) = loss_k$$를 만족하고, 전체 data $$x = \sum{x_{k}}$$에 대하여 loss function의 값 $$f(x)$$를 최소화하는 최적화 문제
    - 라그랑주 승수법을 통하여 전체 data $$x$$에 대해 loss function $$f(x)$$를 최소화하는 weight를 찾아낼 수 있음

- Parallel SGD의 경우, data를 shuffle하는 과정에서 bottleneck현상이 발생
    - ADMM SGD은 shuffle과정이 없음

# 6.2 Asynchronous Update
![Asynchronous](https://files.slack.com/files-pri/T1J7SCHU7-FAQ0DKL9Y/as.png?pub_secret=42b429272c)
- Synchronous update의 단점
    - parameter server의 parameter가 update되기 전에 모든 node의 gradient가 계산될 때까지 기다려야함
    - bandwidth(대역폭)이 제한되어 있으므로, weight를 순차적으로 update해야함
    - communication bottleneck 현상이 발생하므로 비효율적

- Asynchronous update의 해결책
    - 다른 mini-batch에 복사된 model replicas에 상관없이 gradient가 update
    - parameter server의 shard끼리도 독립적으로 weight update

### 6.2.1 Downpour SGD
- Algorithm Design
    - parameter server는 shard(조각)으로 나누어져 있으며, 각 shard마다 담당하는 parameter가 다름 
    - node끼리 묶여 각 group으로 구성하고, 모델의 parameter를 각 group에 복사
    - group 내에서 각 node마다 담당하는 parameter가 다르도록 Model Parallelism
    - 각 group에 있는 data들을 사용하여 loss를 계산하고, 각 node에서 담당하는 parameter에 대해서만 gradient를 계산
    - group에 있는 node에서 gradient 계산이 끝나면 종합하여 parameter server로 보냄
    - parameter server에서는 각 node가 담당하는 parameter를 보유한 shard에서만 update 진행
    - 해당 shard에서 새로운 weight를 계산하여 다시 node로 보냄

- 위의 과정이 다양한 group에서 진행되므로, 각 node들은 parameter server를 통해 비동기적으로 parameter를 공유

-----

## 7. Conclusion and Future Work
- data set의 크기와 model의 크기가 커질수록 학습시간이 오래 걸리게되므로 parallel/distributed 환경에서 학습해야한다. 

-----

## 8. Reference
- [https://web.stanford.edu/~rezab/classes/cme323/S16/projects_reports/hedge_usmani.pdf](https://web.stanford.edu/~rezab/classes/cme323/S16/projects_reports/hedge_usmani.pdf)
- [https://m.blog.naver.com/PostView.nhn?blogId=sogangori&logNo=220512373842&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F](https://m.blog.naver.com/PostView.nhn?blogId=sogangori&logNo=220512373842&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F)
- [http://kiss.kstudy.com/thesis/thesis-view.asp?key=3564716](http://kiss.kstudy.com/thesis/thesis-view.asp?key=3564716)
