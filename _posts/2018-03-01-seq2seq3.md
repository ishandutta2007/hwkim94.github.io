---
layout: post
title:  "Seq2Seq[3] A Persona Based Neural Conversation Model(2016) - Review"
date:   2018-03-01 20:00 +0900
categories: [deeplearning, rnn, lstm, seq2seq, nlp, paperreview]
---

## 1. Abstract
**발화자의 정보나 스타일과 같은 특성을 반영하는 대화 모델, 뿐만 아니라 두 대화자의 특성을 공유할 수도 있음**

-----

## 2. Introduction
![problem](https://files.slack.com/files-pri/T1J7SCHU7-F9HJRQ4F8/problem.png?pub_secret=1931f7f57e)
- 비슷한 질문에 대답이 일관적이지 않은 문제를 해결하기 위한 모델
- *persona*를 대화에 참가하는 사람 혹은 기계의 특성으로 정의
    - 배경 지식, 개인 정보, 대화 방식 등 identity로 구성되어 있다고 볼 수 있음
- Seq2Seq 기반의 2개의 모델 제시
    - Speaker Model
    - Speaker - Adressee Model

-----

## 3. Related Work
- SMT
- LSTM
- Seq2Seq

-----

## 4. [Seq2Seq](https://hwkim94.github.io/deeplearning/rnn/lstm/seq2seq/nlp/paperreview/2018/02/25/seq2seq2.html)
- $$p(Y \mid X)$$ = $$\prod_{t=1}^{n_{y}} p(y_{t} \mid x_{1}, \cdots , x_{t}, y_{1}, \cdots , y_{t-1})$$

-----

## 5. Personalized Response Generation
# 5.1 Notation
- $$M$$ = $$(m_{1}, \cdots , m_{I})$$ = message
- $$R$$ = $$(r_{1}, \cdots , r_{J}, EOS)$$ = response
- $$V$$ = vocabulary size
- $$K$$ = embedding size

# 5.2 Speaker Model
![model](https://files.slack.com/files-pri/T1J7SCHU7-F9HK1P0NA/model.png?pub_secret=5492b3efe4)
- respondent가 하나인 모델, 즉, 사람이 질문하면 컴퓨터가 대답을 하는 모델
- respondent의 age, gender, personal information 등의 정보를 enconding한 speaker $$i$$'s encoding vector $$v_{i}$$를 사용
    - respondent의 대답 내용과 스타일에 영향을 주게 됨
- **training set에 없더라도 정보를 추론할 수 있음**
    - 비슷한 speaker끼리 cluster를 형성하므로

1. model
    - $$\begin{bmatrix}
i_{t}\\ 
f_{t}\\ 
o_{t}\\
g_{t}\end{bmatrix}$$ = $$\begin{bmatrix}
\sigma\\ 
\sigma\\ 
\sigma\\
tanh\end{bmatrix} W \cdot \begin{bmatrix}
h_{t-1}\\ 
x_{t}\\ 
v_{i}\end{bmatrix}$$

    - $$c_{t}$$ = $$f_{t} \cdot c_{t-1} + i_{t} \cdot g_{t}$$
    - $$h_{t}$$ = $$o_{t} \cdot tanh(c_{t})$$

2. 질문 부분
    - message $$M$$을 LSTM에 넣어 질문에 대한 hidden state 생성
    - 질문이 끝나는 EOS부분부터 $$v_{i}$$를 넣어줌

3. 대답 부분
    - previous hidden state로 인해 생겨난 target과 speaker embedding $$v_{i}$$를 current time step에 넣어줌
    - 즉, previous hidden state $$h_{t-1}$$, current input $$y_{t-1}$$, speaker embedding $$v_{i}$$를 사용하여 current target $$y_{t}$$를 만들어냄 
    - $$v_{i}$$는 speaker $$i$$가 등장하는 모든 대화에서 공유됨
    - 따라서, 아래의 방식으로 학습된 $$v_{i}$$를 제공한다면, $$v_{i}$$의 정보를 파악할 수 있음

4. 학습 부분
    - $$v_{i}$$도 back propagation으로 같이 학습됨
    - **직접 encoding을 시키지는 않았지만, 학습과정에서 정보들이 $$v_{i}$$에 포함되게 됨**
    - **따라서, age, gender, personal information 등 비슷한 특성을 가진 speaker끼리 cluster를 구성**
    - **따라서, 직접적인 정보가 주어지지 않았더라도, cluster에 있는 다른 speaker의 정보로부터 추론 가능**
    - ex) speaker $$i$$의 거주지 정보가 training set에는 없지만, British로 거주지에 대해 질문하는 상황
    - ex) $$v_{i}$$ 주변에는 British 대화 정보를 포함하여 여러 정보들이 비슷한 speaker들로 cluster가 구성되어있음
    - ex) 주변 speaker와 비슷한 vector를 가지므로, 다른 speaker들이 거주지 정보가 어느정도 $$v_{i}$$에 녹아들게 됨

# 5.3 Speaker-Addressee Model
- 질문한 사람에 따라서 대답이 달라짐
- $$V_{i,j}$$ = $$tanh(W_{1}v_{i} + W_{2}v_{j})$$
    - $$v_{i}$$와 $$v_{j}$$의 선형 결합으로 interactive representation $$V_{i,j}$$를 만듦

1. model
    - $$\begin{bmatrix}
i_{t}\\ 
f_{t}\\ 
o_{t}\\
g_{t}\end{bmatrix}$$ = $$\begin{bmatrix}
\sigma\\ 
\sigma\\ 
\sigma\\
tanh\end{bmatrix} W \cdot \begin{bmatrix}
h_{t-1}\\ 
x_{t}\\ 
V_{i,j}\end{bmatrix}$$

    - $$c_{t}$$ = $$f_{t} \cdot c_{t-1} + i_{t} \cdot g_{t}$$
    - $$h_{t}$$ = $$o_{t} \cdot tanh(c_{t})$$

# 5.4 Decoding and Reranking
### 5.4.1 Decoding
- Beam search 사용
    - 각 time step마다 가장 가능성 있는 B개의 target에서 확장하며, 다시 그 중에서 확률이 가장 높은 B개만 추려내는 것

### 5.4.2 Reranking
- 'I don't know'문제를 막기위해서 실행
- Beam search 과정에서 가능성 높은 B개를 Reranking
- $$log(p(R \mid M,v)) + \lambda log(p(M \mid R)) + \gamma \mid R \mid$$ .
    - $$p(R \mid M,v)$$ = 질문 $$M$$과 응답자 $$v$$가 주어졌을 때, 대답 $$R$$이 나올 확률
    - $$p(M \mid R)$$ = 대답 $$R$$이 나왔을 때, 질문 $$M$$이 나올 확률
    - $$\mid R \mid$$ = 응답의 길이


-----

## 6. Dataset
- Twitter Persona Dataset
- Twitter Sordoni Dataset
- Television Series Transcripts

-----

## 7. Experiments
# 7.1 Evaluation
- BLEU score
- Perplexity

# 7.2 Baseline
![base](https://files.slack.com/files-pri/T1J7SCHU7-F9GUATZAR/base.png?pub_secret=e22c94d464)

# 7.3 Results
### 7.3.1 Twitter
![result1](https://files.slack.com/files-pri/T1J7SCHU7-F9GMVDQ83/result1.png?pub_secret=876fa7e86e)

### 7.3.2 TV series
![result2](https://files.slack.com/files-pri/T1J7SCHU7-F9GMVE7C3/result2.png?pub_secret=17f6f9080f)

# 7.4 Qualitative Analysis
### 7.4.1 Diverse Responses by Different Speakers
#### 7.4.1.1 Speaker Model
![result3](https://files.slack.com/files-pri/T1J7SCHU7-F9HM04V7G/result3.png?pub_secret=4c1c28e29f)
#### 7.4.1.2 Speaker-Addressee Model
![result4](https://files.slack.com/files-pri/T1J7SCHU7-F9GNJ2EBV/result4.png?pub_secret=70bb629f80)

### 7.4.2 Human Evaluation
persona model이 대답에 있어서 조금 더 안정적

-----

## 8. Conclusion
speaker의 정보를 같이 담으므로 일반적인 대화의 정보를 어느정도 손실 가능

-----

## 9. Reference
- [https://arxiv.org/abs/1603.06155](https://arxiv.org/abs/1603.06155)
- Ybigta deepNLP-study
