---
layout: post
title:  "BLSTM-CNN-CRF[1] End-to-End Sequence Labeling via Bi-directional LSTM-CNNs-CRF(2016) - Review"
date:   2018-02-29 13:00:00 +0900
categories: [deeplearning, rnn, cnn, lstm, charcnn, nlp, paperreview]
---

## 1. Abstract
**과거의 sequence labeling 작업에는 전문지식을 요구했지만, 이 논문에서는 BLSTM, CNN, CRF를 이용하여 사전작업이 없는 end-to-end model을 제시**

-----

## 2. Introduction
POS-tagging, NER 분야에 대해서 sequence labeling 실험

-----

## 3. NN Architecture
# 3.1 [charCNN](https://hwkim94.github.io/deeplearning/cnn/charcnn/nlp/paperreview/2018/02/27/charCNN2.html)
![cnn](https://files.slack.com/files-pri/T1J7SCHU7-F9HME6355/cnn.png?pub_secret=f2be846acb)

# 3.2 BLSTM
### 3.2.1 [LSTM](https://hwkim94.github.io/deeplearning/rnn/lstm/nlp/paperreview/2018/02/21/LSTM1.html)
![lstm](https://files.slack.com/files-pri/T1J7SCHU7-F9G0NS33J/lstm.png?pub_secret=871f71a7a8)

### 3.2.2 [BLSTM](https://hwkim94.github.io/deeplearning/rnn/lstm/nlp/paperreview/2018/02/21/BLSTM1.html)
LSTM 2개를 사용하여 seqeuence를 forward, backward 방향으로 각각 넣은 후 concatenate하여 사용
 
# 3.3 CRF(Conditional Random Field)
- **labeling을 할 때, 독립적으로 decoding하는 것이 아니라 주변의 정보를 파악하여 주변과의 상관관계를 파악는 것이 좋음**
    - ex) POS-tagging작업에서 형용사 뒤에는 동사보다 명사가 많이 등장
- CRF는 두 개의 연속적인 label들의 상호작용만 고려
    - Viterbi algorithm으로 효율적으로 최적화 가능

- $$p(y \mid x;W,b)$$ = $$\frac{ \prod_{i=1}^{n} \Psi_{i} (y_{i-1}, y_{i}, x) }{\sum_{y' \in Y(x)} \prod_{i=1}^{n} \Psi_{i} (y'_{i-1}, y'_{i}, x) }$$
    - $$x$$ = $$(x_{1}, x_{2}, \cdots, x_{n})$$ = input sequence
    - $$y$$ = $$(y_{1}, y_{2}, \cdots, y_{n})$$ = output label sequence
    - $$Y(x)$$ = 가능한 모든 label sequence의 집합
    - $$W_{y_{i-1}, y_{i}}, b_{y_{i-1}, y_{i}}$$ = weight, bias corresponding to label pair $$(y_{i-1}, y_{i})$$
    - $$W_{y_{i-1}, y_{i}}$$ = 이전 step에서 $$y_{i-1}$$가 나왔을 때, input $$x_{i}$$가 $$y_{i}$$일 확률을 구하는 것에 사용
    - $$W_{y_{i-1}, y_{i}}$$는 $$y_{i-1}$$가 나왔을 때, $$y_{i}$$가 나올 확률을 구하는 것에 사용되므로, 공유 되는 것
    - ex) $$W_{adj, noun}$$는 이전 label이 adj일때, 다음 label이 noun이 나올 확률을 구하는 것에 사용됨
    - $$\Psi_{i} (y_{i-1}, y_{i}, x)$$ = $$exp(W_{y_{i-1}, y_{i}}^{T} x_{i} + b_{y_{i-1}, y_{i}})$$
    - $$\Psi_{i} (y_{i-1}, y_{i}, x)$$는 이전 label $$y_{i-1}$$과 현재 input $$x_{i}$$가 주어졌을 때, $$y_{i}$$가 나올 확률을 의미
    - 즉, 최종적으로 $$x$$가 주어졌을 때, $$y$$의 구성요소 $$y_{i}$$가 나올 확률들을 곱하여 최종적으로 $$y$$가 나올 확률을 구함. 이때, $$y_{i}$$가 나올 확률은 $$y_{i-1}$$에 따라 달라짐

- $$max L(W,b)$$ = $$max \sum log(p(y \mid x;W,b))$$
    - log-likelihood를 최대화하는 방향으로 $$W,b$$를 조정하며 CRF학습

- $$\widehat{y}$$ = $$argmax_{y \in Y(x)} (p(y \mid x;W,b))$$
    - 실제로 예측할 때는, $$Y(x)$$ 중에서 가장 확률이 큰 것을 선택

# 3.4 BLSTM-CNN-CRF
![model](https://files.slack.com/files-pri/T1J7SCHU7-F9GHUET6X/model.png?pub_secret=1585e74268)
- input $$x$$를 word embedding과 charCNN을 통한 embedding을 concatenate하여 vector 생성
- 위에서 생성된 vector를 BLSTM에 넣어준 후, 새로운 vector를 생성
- CRF에서는 이전에 뭐가 나왔는지 고려하여 각각의 경우마다 존재하는 $$W_{y_{i-1}, y_{i}}$$를 vector에 곱해서 모든 가능한 경우의 수에 대한 확률을 구한 후, 가장 가능성이 큰 것을 출력

-----

## 4. NN Training
# 4.1 Parameter Initialization
### 4.1.1 Word Embedding
- 100dim-GloVe, 300dim-Word2Vec, 50dim-Senna에 대해서 실험
### 4.1.2 Char Embedding
- 30dim-Uniformed sampled vector from range &&[-\sqrt\frac{3}{dim},+\sqrt\frac{3}{dim}]&&
### 4.1.3 Weight Matrices and Bias Vectors
- Uniformly sampled from range $$[-\sqrt\frac{3}{dim},+\sqrt\frac{3}{dim}]$$

# 4.2 Optimization Algorithm
- SGD
- gradient norm을 5보다 작도록 유지
### 4.2.1 Early Stopping
- 가장 성능이 좋은 parameter가 나오면 학습을 중단
### 4.2.2 Fine Tuning
- gradient를 update하는 과정에서 embedding도 함께 update
### 4.2.3 Dropout Training
- charCNN과, BLSTM에 dropout 적용
# 4.3 Tuning Hyper-Parameter
![params](https://files.slack.com/files-pri/T1J7SCHU7-F9G4X1U65/param.png?pub_secret=6e81f82edd)

-----

## 5. Experiment
# 5.1 Data Set
![dataset](https://files.slack.com/files-pri/T1J7SCHU7-F9G4X1FED/dataset.png?pub_secret=5bebbae6e3)

# 5.2 Main Results
![result1](https://files.slack.com/files-pri/T1J7SCHU7-F9GLH6PT6/result1.png?pub_secret=8c8a228f56)

# 5.3 Comparison with previous word
### 5.3.1 POS tagging
![result2](https://files.slack.com/files-pri/T1J7SCHU7-F9G4XN94Z/result2.png?pub_secret=f8627944a6)

### 5.3.2 NER
![result3](https://files.slack.com/files-pri/T1J7SCHU7-F9GJ92J4T/result3.png?pub_secret=fe580d22e3)

# 5.4 Word Embedding
![result4](https://files.slack.com/files-pri/T1J7SCHU7-F9G1ZHD24/result4.png?pub_secret=bc03e1130f)
- word embedding을 하는 것이 성능에 좋으며, 그 중 GloVe가 가장 성능이 좋다.

# 5.5 Effect of Dropout
![result5](https://files.slack.com/files-pri/T1J7SCHU7-F9G1ZHMG8/result5.png?pub_secret=d1da19279d)
- dropout을 해주는 것이 성능이 더 좋다.

# 5.6 OOV Error Analysis
![result6](https://files.slack.com/files-pri/T1J7SCHU7-F9HGRPMML/result7.png?pub_secret=fbb8d64f77)
- IV : in vocabulary
- OOTV : out-of-training vocabulary, embedding은 되었지만 training set에 없는 단어
- OOEV : out-of-embedding vocabulary, training set에는 있지만 embedding은 안되어 있음
- OOBV : out-of-both vocabulary

-----

## 6. Related Work
- BLSTM-CRF
- LSTM-CNN


-----

## 7. Conclusion
**sequence labeling task에서 성능이 가장 좋은 end-to-end 모델이다.**

-----

## 8. Reference
- [https://arxiv.org/abs/1603.01354](https://arxiv.org/abs/1603.01354)
- [https://zzozzolev.github.io/2016/lstm/cnn/crf/sequence-labeling/End-to-end-Sequence-Labeling-via-Bi-directional-LSTM-CNNs-CRF/](https://zzozzolev.github.io/2016/lstm/cnn/crf/sequence-labeling/End-to-end-Sequence-Labeling-via-Bi-directional-LSTM-CNNs-CRF/)
- [https://ratsgo.github.io/machine%20learning/2017/11/10/CRF/](https://ratsgo.github.io/machine%20learning/2017/11/10/CRF/)
- Ybigta deepNLP-study
