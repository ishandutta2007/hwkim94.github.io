---
layout: post
title:  "Audio Style Transfer[1] Neural Style Transfer for Audio Spectrograms(2018) - Review"
date:   2018-05-21 15:30:00 +0900
categories: [deeplearning, audio, style-transfer, alexnet, paperreview]
---

## 1. Abstract
- spectrogram에 CNN을 적용한 audio style transfer에 대한 연구

-----

## 2. Introduction

- image style transfer와 비슷한 기술 사용
    - 무작위 잡음으로 시작하는 입력 신호를 최적화하는 것이 핵심
    - 다른 CNN layer를 통과하며 원하는 image style을 가지게 되는 것

- audio signal을 수정하여 새로운 sounds를 생성
    - CNN의 filter와 activation function을 통해서 noise로부터 새로운 spectrogram을 생성

-----

## 3. Methodology

- 최근 CNN을 acoustic연구에 적용하여 음성인식을 하는 연구들이 진행됨
    - AlexNet, VGG-Net, ResNet등 사용

- Short-Time Fourier Transform log-magnitude사용

- spectrogram을 통한 연구
    - duration 2.57s
    - frame-size 30ms
    - frame-step 10ms
    - FFT-size 512
    - audio sampling rate of 16kHz

# 3.1 Audio Style Transfer

- $$X_{r}$$ = $$argmin_X L_{tot}$$ = $$argmin_X(\alpha L_c (x, x_{c}) + \beta L_s (x, x_{s}) + \gamma L_e (x_{e}, e_{s}) + \delta L_t (x_{t}, t_{s}))$$
    - $$X_r$$ = reconstructed spectrogram
    - $$L_c$$ = content loss = loss between filters of model and of content
    - $$L_s$$ = style loss = normalized Eucildean norm between Gram matrix of filter activations
    - $$L_e, L_t$$ = deviation in the temporal and frequency energy envelopes respectively from the style audio
    - Gram matrix는 target audio style의 시간적 역동을 포함하지 않으므로 energy term 필요

- 3x3 filter의 AlexNet 사용
    - 3x3 filter는 audio의 time, frequency의 resolution을 보존하기 위해 작은 receptive field 사용
    - 80개의 musical instrument sounds를 구별하도록 audio spectrogram을 학습
    - cross-entropy와 Adam 사용

- random-noise를 input, 실제 sound를 target으로 두고 CNN을 학습시키 후, 원하는 sound를 다시 input으로 넣어주면 input sound가 target sound처럼 바뀌어 나오는 architecture
    - pitch, time, instrument의 사전지식 없이 음악의 timbre(음색) transfer가 학습됨  

- loss term 추가
    - 평균적인 음색과 energy envelope를 match하기 위하여 사용

-----

## 4. Experiments
![result](https://files.slack.com/files-pri/T1J7SCHU7-FASTZBD1S/result.png?pub_secret=30f2745ca6)
- timbre(음색)뿐만 아니라 bandwidth(대역폭)도 바뀜

-----

## 5. Conclusion and Future Work
- 음성 합성에서 style transfer로 접근한 것은 새로운 방법

-----

## 6. Reference
- [https://arxiv.org/abs/1801.01589](https://arxiv.org/abs/1801.01589)
