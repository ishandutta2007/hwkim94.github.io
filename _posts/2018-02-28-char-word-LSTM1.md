---
layout: post
title:  "char-word LSTM[1] Character Word LSTM Language Models(2017) - Review"
date:   2018-02-28 23:00:00 +0900
categories: [deeplearning, rnn, lstm, nlp, paperreview]
---

## 1. Abstract
- word-char CNN은 Perplexity가 낮을 뿐만 아니라, parameter의 수도 적다는 장점이 있다.
- character information은 word의 구조적 유사성을 알려주기 때문에 OOV(out-of-vocabulary)를 다룰 때에도 유리하다.
- word embedding과 char embedding을 concatenate로 합치는 방식  

-----

## 2. Introduction
- 기존 NN based Language Model의 단점
    - 학습을 시키는데는 많은 양의 데이터가 필요하기 때문에, infrequent word에 대해서는 성능이 좋지 않다.
    - 단어의 구조를 살펴볼 수 없다.
- subword information을 반영하는 것이 중요하다.
    - word/char embedding을 concatenate
    - subword의 구조뿐만 아니라, 순서도 같이 vector로 표현됨
- word embedding 차원을 줄이고, 그 부분을 char embedding으로 대신하여 전체적인 dimension은 유지하는 방식으로 parameter수를 줄임

-----

## 3. Related Work
- RNN-LM
- NMT
- BLSTM
- charCNN

-----

## 4. Character-Word LSTM language model
![model](https://files.slack.com/files-pri/T1J7SCHU7-F9GULD7CP/model.png?pub_secret=425d280297)
- one-hot encoded word과 one-hot encoded char를 각각 embedding시켜 concatenate
- $$e_{t}^{T}$$ = $$[(W_{w} \times w_{t})^{T};(W_{c}^{1} \times c_{t}^{1})^{T}; \cdots ; (W_{c}^{n} \times c_{t}^{n})^{T} ]$$ 
    - one-hot encoded word과 one-hot encoded char를 각각 embedding시켜 concatenate
    - character도 다른 matrix로 각각 embedding시키므로 character의 순서, 위치의 중요성도 같이 학습 가능

- 모든 character를 넣어주는 것이 아니라, n개의 character만 사용
    - word의 character가 n개보다 많으면 앞의 n개만 사용하고, 부족하면 zero-padding
    - OOV word를 잘 대처할 수 있도록 설계

# 4.1 Order of the characters
- character가 추가되는 순서를 forward, backward, both로 모두 시도해봄
- 언어마다 단어에서 중요한 부분의 위치가 다르므로, 언어마다 character를 넣어주는 방향을 다르게 해야함
    - English, Dutch의 경우 suffix(접미사)가 중요한 역할을 하므로, character를 backward로 넣어주는 것이 성능이 더 좋음

# 4.2 Weight Sharing
- CW LSTM
    - $$e_{t}^{T}$$ = $$[(W_{w} \times w_{t})^{T};(W_{c}^{1} \times c_{t}^{1})^{T}; \cdots ; (W_{c}^{n} \times c_{t}^{n})^{T} ]$$ 
    - character마다 다른 matrix로 embedding하는 방식, 
    - 같은 character라도 위치에 따라서 사용되는 방식이 다를 것이므로, 각각 embedding해야함
    - ex) 영어에서 's'가 마지막으로 사용되면 '복수'의 의미를 가지게 됨

- Weight Sharing
    - $$e_{t}^{T}$$ = $$[(W_{w} \times w_{t})^{T};(W_{c} \times c_{t}^{1})^{T}; \cdots ; (W_{c} \times c_{t}^{n})^{T} ]$$ 
    - 각 character를 같은 matrix로 embedding하는 방식, 즉, weight sharing

# 4.3 Number of parameters
- word LSTM
    - #parameter = $$V \times E$$
    - $$V$$ = vocabulary size, $$E$$ = word embedding size

- char-word LSTM
    - #parameter = $$V \times (E - n \times E_{c}) + n \times ( C \times E_{c})$$
    - $$C$$ = character size, $$E_{c}$$ = character embedding size, $$n$$ = 사용되는 character의 수
    - #word-vocabulary $$V$$가 #char-vocabulary $$C$$보다 훨씬 많으므로 parameter가 많이 감소함

- weight sharing char-word LSTM
    - #parameter = $$V \times (E - n \times E_{c}) + C \times E_{c}$$ 

-----

## 5. Experiments
# 5.1 Setup
- small model : 2-layer with 200 hidden unit
- large model : 2-layer with 650 hidden unit
- embedding layer size는 hidden layer size와 같은
- data set
    - English : PTB
    - Dutch : CGD
    - data set의 크기를 비슷하게하여 두 언어에 대해서 성능비교
    - 대/소문자 구별하는 것과 하지 않는 것에 대하여 성능비교

# 5.2 Baseline models
![result1](https://files.slack.com/files-pri/T1J7SCHU7-F9G6V3BMG/result1.png?pub_secret=7cbc42c947)
- parameter를 줄이면서도 성능을 높일 수 있는지 확인하기 위하여 2개의 비교 모델을 만들었음
    - 같은 hidden unit을 가진 LSTM, parameter가 더 많게 됨(small model의 경우 200개, large model의 경우 650개의 hidden unit)
    - 비슷한 수의 parameter를 가진 LSTM(small model의 경우 175개, large model의 경우 475개의 hidden unit)

# 5.3 English
### 5.3.1 Baseline model vs CW-LSTM model
![result2](https://files.slack.com/files-pri/T1J7SCHU7-F9H8L74MD/result2.png?pub_secret=7d7c8028f8)
![result4](https://files.slack.com/files-pri/T1J7SCHU7-F9H8NK807/result4.png?pub_secret=b7b6bf08a4)
- 비슷한 수의 unit을 가진 2-layer LSTM과는 성능이 비슷했다.
- 비슷한 수의 parameter를 가진 2-layer LSTM보다는 성능이 좋았다. 
- **character를 너무 많이 넣는 것은 word embedding의 정보를 줄이기 때문에 오히려 성능이 좋지 않음**
    - word embedding size가 char embedding size보다 커야함

### 5.3.2 Forward-order char vs Backward-order char vs Both-order char
![result3](https://files.slack.com/files-pri/T1J7SCHU7-F9H2LR686/result3.png?pub_secret=4a3972ed76)
- **처음과 끝 3자리씩 넣어주는 Both-order가 성능이 제일 좋다.**
- Backward-order가 Forward-order보다 성능이 조금 더 좋다.

# 5.4 Dutch
![result5](https://files.slack.com/files-pri/T1J7SCHU7-F9G6KBH44/result5.png?pub_secret=a321c16316)
- 형태소가 많으므로 character structure를 넣어주는 것이 유리
- 영어에서 보다 더 좋은 성능을 보여줌
- 중요한 정보가 어미에 많이 있으므로, Backward-order가 더 성능이 좋음

# 5.5 Random CW models
![result6](https://files.slack.com/files-pri/T1J7SCHU7-F9FLGDB1P/result6.png?pub_secret=59d34df7ec)
- 성능이 좋은 이유가 정말 character 정보를 넣어줘서인지 조사하기 위하여 character embedding 자리에 random noise를 넣어줌
- **Baseline보다 성능이 안좋아짐, 즉, character 정보를 넣어주는 것이 subword structure를 반영할 수 있어서 성능이 좋음**

# 5.6 Sharing weights
![result7](https://files.slack.com/files-pri/T1J7SCHU7-F9FLHSM7T/result7.png?pub_secret=22dc1ef0e2)
- weight sharing을 하지않은 것이 성능이 더 좋다.
    - character가 위치에 따라서 가지는 의미가 다르다는 것을 학습 가능

# 5.7 Dealing with out-of-vocabulary words
- OOV를 실제 단어로 matching시킬 확률이 증가

-----

## 6. Conclusion and Future work
- character의 정보를 반영하여 성능이 좋았졌다.
- embedding 방식을 바꾸어 parameter수를 많이 줄였다.
- character embedding size가 너무 크지않도록 조절해야한다.
- 언어에 따라 character를 넣어주는 순서를 바꿔야한다.
- character는 위치에 따라 다른 정보를 가지므로, 각각 embedding해야 한다.

-----

## 7. Reference
- [https://arxiv.org/abs/1704.02813](https://arxiv.org/abs/1704.02813)
- [https://godongyoung.github.io/%EB%94%A5%EB%9F%AC%EB%8B%9D/2018/01/24/Character-Word-LSTM-Language-Models-%EB%85%BC%EB%AC%B8-%EB%A6%AC%EB%B7%B0.html](https://godongyoung.github.io/%EB%94%A5%EB%9F%AC%EB%8B%9D/2018/01/24/Character-Word-LSTM-Language-Models-%EB%85%BC%EB%AC%B8-%EB%A6%AC%EB%B7%B0.html)
- Ybigta deepNLP-study

