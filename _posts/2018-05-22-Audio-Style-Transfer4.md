---
layout: post
title:  "Audio Style Transfer[4] Audio Style Transfer(2017) - Review"
date:   2018-05-22 14:35:00 +0900
categories: [deeplearning, audio, style-transfer, paperreview]
---

## 1. Abstract
- image style transfer를 audio에 변형하여 적용

-----

## 2. Introduction and Related work
- 기존의 audio style transfer과 차이
    - 초기 input을 random noise가 아닌 target content사용
    - style loss만 사용

- 다양한 CNN architecture에 대해서 실험

-----

## 3. Problem setting and Discussion
- style trasnfer
    - random noise부터 시작
    - content image의 구조와 style image의 분포를 학습

- audio를 STFT를 이용하여 spectrogram으로 바꾸면 style transfer와 동일하게 다룰 수 있지만, content만 유지하고 style은 유지하지 않는 문제가 발생
    - audio의 content와 style은 image의 content와 style과 다르기 때문에 같은 것을 적용하면 문제가 됨
    - 또한, audio의 style은 content에 의존적

-----

## 4. Proposed Framework
![style transfer](https://files.slack.com/files-pri/T1J7SCHU7-FAUM8904W/archi.png?pub_secret=fc4b33dde8)
- spectrogram 사용
- content sound부터 시작하여 style sound의 특성을 받아들이는 구조
    - random noise로 시작하지 않고, content sound로 시작
    - 따라서, content loss를 사용하지 않음

# 4.1 Neural network-based approach
- CNN을 통해 style의 stationary sound texture의 특징을 가지는 statistics를 추출
- Gram matrix를 사용한 loss 계산
    - $$L(x:x_{style})$$ = $$\sum_{l} \mid \mid G_{l}(x) - G_{l}(x_{style}) \mid \mid_{F}^2$$
    - $$G_l$$ = $$F_l^T F_l$$
    - $$l$$ = l-th layer

- 다양한 모델 사용
    - VGG-19
    - SoundNet
    - Wide-Shallow-Random network

# 4.2 Auditory-based approach
- VGG와 SoundNet은 statistics를 뽑아내는 것에는 좋지 않은 모델이므로 sound texture를 잘 추출할 새로운 모델이 필요
- 따라서, McDermott and Simoncelli의 접근 방식을 사용

### 4.2.1 McDermott and Simoncelli
- 인간이 소리를 인식하는 것처럼 3개의 네트워크를 구성하는 것
- 각 네트워크에서 통계를 기반으로 audio style을 추출

- cochlear filtering
    - 달팽이관 역할
    - filter를 사용하여 waveform을 acoustic frequency bands로 분해하는 것
    - Mean, variance, skewness of each envelope band

- envelope extraction and compressive nonlinearity
    - 각 frequency band의 envelope를 추출하고 compressive nonlinearity를 적용
    - cross-band correlation


- modulation filtering
    - compressed envelope에 20개의 bandpass modulation filter를 적용하여 분해하는 것
    - cochlear filtering과 비슷하지만, cochlear filtering은 waveform에 적용
    - Power from each modulation band and cross-band correlation

-----

## 5. Experiments
![result](https://files.slack.com/files-pri/T1J7SCHU7-FATQDTK98/result.png?pub_secret=845b051614)
- VGG는 image를 위한 모델이기 때문에 성능이 좋지않음
- SoundNet은 많은 noise를 포함
- Wide-Shallow-Random network과 McDermott and Simoncelli의 접근방식이 가장 좋은 결과를 보여줌

-----

## 6. Conclusion
- Wide-Shallow-Random network과 human auditory system의 영감을 받은 McDermott and Simoncelli 모델이 가장 성공적이었다.

-----

## 7. Reference
- [https://arxiv.org/abs/1710.11385](https://arxiv.org/abs/1710.11385)
