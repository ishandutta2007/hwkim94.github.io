---
layout: post
title:  "Audio Style Transfer[2]Style Transfer for Prosodic Speech(2017) - Review"
date:   2018-05-22 01:45:00 +0900
categories: [deeplearning, audio, style-transfer]
---

## 1. Abstract
- speech의 spectrogram을 활용하여 image처럼 다루어 style transfer
- accent나 emotion등 high-level prosody(음율)를 표현하는 것은 실패

-----

## 2. Introduction
- image의 style transfer는 한 image의 style, texture 등을 다른 image에 적용하는 것
- speech의 style transfer는 한 사람의 voice를 다른 사람의 voice로 바꾸는 것 

-----

## 3. Background
![style](https://files.slack.com/files-pri/T1J7SCHU7-FAT7FN92Q/istyle.png?pub_secret=11186a37e4)
- Image style transfer 응용
- AutoEncoder

-----

## 4. Dataset
- VCTK corpus
- Short-time Fourier transform을 사용해 audio clip에서 spectrogram 생성

-----

## 5. Method
# 5.1 Autoencoder
![Autoencoder](https://files.slack.com/files-pri/T1J7SCHU7-FASLH0HMF/autoencoder.png?pub_secret=d5e5251f61)
- style transfer는 feature를 추출할 수 있는 pretrained NN이 필요
    - audio에는 labeled된 데이터가 거의 없으므로 spectrogram으로 autoencoder를 학습하여 pretrained NN으로 사용
    - source spectrogram과 recontructed spectrogram의 차이를 줄이도록 학습

- seq2seq기반의 auto encoder와 convolution 기반의 auto encoder 중에서 후자가 더 좋은 성능을 보여줌
 
# 5.2 Style Transfer
![style transfer](https://files.slack.com/files-pri/T1J7SCHU7-FAT0DAM0C/style.png?pub_secret=1aedd0ec5f)
- 각 layer들의 $$L_c$$ 와 $$L_s$$를 계산한 후 각각 합해서 loss로 사용
    - $$L_c$$ = content loss = $$\mid \mid F_{c}^{out} - F_{c} \mid \mid^{2}$$
    - $$L_s$$ = style loss = $$\mid \mid (F_{s}^{out})^T F_{s}^{out} - (F_{s})^T F_{s} \mid \mid^{2}$$
    - $$F^{out}$$ = NN에 noise를 넣었을 때, 해당 layer에서의 출력값
    - $$F_c$$ = NN에 content image를 넣었을 때, 해당 layer에서의 출력값
    - $$F_s$$ = NN에 style image를 넣었을 때, 해당 layer에서의 출력값

- content loss
    - 각 layer에서 output과 content가 비슷해지도록 조절

- style loss
    - Gram matrix를 통하여 계산됨
    - covariance 분포가 비슷해지도록 조절

- auto encoder
    - shallow layer는 상대적으로 fine-grained and widely-distributed feature등 표면적인 것을 학습
    - deeper layer는 상대적으로 context-sensitive, structural feature등 구체적인 것을 학습
    - 따라서, style loss는 shallow layer에 대해서, content loss는 deeper layer에 대해서 계산

- Adam optimizer가 style과 content spectrogram을 반영한 noise spectrogram의 loss를 최적화 

-----

## 6. Results and Analysis
# 6.1 Autoencoder
![result1](https://files.slack.com/files-pri/T1J7SCHU7-FAUG49AR5/result1.png?pub_secret=e9443a43b5)

# 6.2 Style Transfer
![result2](https://files.slack.com/files-pri/T1J7SCHU7-FATJS5M1B/result2.png?pub_secret=fe5d836e7a)
- model의 성능 향상을 위한 strategy
    - 첫 layer에 dilated convolution을 추가하여 less-local texture를 찾아냄
    - spectrogram의 loss를 log로 계산
    - learning rate decay
    - $$F_c$$와 $$F_s$$의 가중치 조절을 통한 balance 조정
    - Adam Optimizer with Momentum

- model의 generated audio optimization을 위한 strategy
    - Removing batch normalization
    - Using leaky ReLU
    - Computing the gram matrix only across time rather than across time and spectrogram channels
    - Adding an L2 loss regularization
    - Initializing the generated audio to the content spectrogram rather than noise

-----

## 7. Future Work
![gradient](https://files.slack.com/files-pri/T1J7SCHU7-FASU53PED/gradient.png?pub_secret=e69a14420b)
- 학습시에 stable gradient descent를 하지 못했음
- 세밀한 개인차를 표현하기엔 spectrogram이 적합하지 않을수도 있음
- 사람의 accent나 감정 등의 요소들을 더 잘 잡아낼 수 있도록 모델을 구성해야함
- 사람은 음성으로만 대화를 하지 않음

-----

## 8. Conclusion
- spoken prosody를 분석하는 것은 sociolinguistic research에 큰 도움이 될 것이다.

-----

## 9. Reference
- [http://web.stanford.edu/class/cs224s/reports/Anthony_Perez.pdf](http://web.stanford.edu/class/cs224s/reports/Anthony_Perez.pdf)
- [https://www.youtube.com/watch?v=RWro8WzTDSM](https://www.youtube.com/watch?v=RWro8WzTDSM)
- [https://www.popit.kr/neural-style-transfer-%EB%94%B0%EB%9D%BC%ED%95%98%EA%B8%B0/](https://www.popit.kr/neural-style-transfer-%EB%94%B0%EB%9D%BC%ED%95%98%EA%B8%B0/)
