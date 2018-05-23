---
layout: post
title:  "WaveNet[1] WaveNet: A Generative Model for Raw Audio(2016)	 - Review"
date:   2018-05-23 18:10:00 +0900
categories: [deeplearning, wavenet, paperreview]
---

## 1. Abstract
- WaveNet은 raw audio waveform을 generation하는 neural network
    - raw audio : 가공되지않은 형태의 압축안된 오디오를 저장하기 위한 컴퓨터 포맷
    - probabilistic, autoregressive한 모델
    - 즉, audio sample의 확률분포는 바로 이전 순간의 조건부로 결정됨

-----

## 2. Introduction
- PixelCNN 기반의 모델
- 주체가 있는 raw speech signal을 generation
    - 많은 speaker가 있는 대화에서 대화자의 특성을 파악하고, 전환가능
    - speaker가 바뀌면 목소리도 바뀌게 됨

- dilation을 사용한 architecture
    - long-range dependency를 위하여 넓은 receptive field 확보 

- 음악 generation에도 사용됨

-----

## 3. WaveNet
- raw audio waveform을 직접적으로 생성하는 모델
- $$p(x)$$ = $$\prod_{t=1}^{T} p(x_{t} \mid x_{1} , \cdots , x_{t-1})$$
    - waveform $$x$$ = $$(x_1 , \cdots , x_T)$$

- PixelCNN 기반
    - CNN을 통하여 조건부확률 modeling
    - pooling layer 없음
    - input과 output의 차원이 같음
    - log-likelihood 사용

- autoregressive
    - 학습한 결과를 다시 input으로 사용

# 3.1 Dilated Causal Convolution
### 3.1.1 Causal Convolution
![causal](https://files.slack.com/files-pri/T1J7SCHU7-FAVEDPQDC/dilation1.png?pub_secret=4b75a2a08f)
- model이 순서를 침범하지 않음, 즉,data의 order를 유지하며 학습
    - masked convolution이므로, time step $$t$$의 output은 $$t$$ 이전의 데이터만 학습가능

- 각 time step의 연산은 병렬적으로 처리됨, 즉, recurrent하지 않은 구조
    - RNN보다 빠름

### 3.1.2 Dilated Causal Convolution
![dilate](https://files.slack.com/files-pri/T1J7SCHU7-FAUHK55S6/dilation2.png?pub_secret=ddf3e45a15)
- causal convolution의 단점
    - 넓은 receptive field를 가지기 위해서는 layer의 수가 많아지거나 filter의 크기가 커져야 함
    - computational cost의 증가

- dilation
    - 바로 인접한 input에 filter를 적용하지 않고, 일정 간격을 건너 뛰며 filter를 적용하는 것
    - 연산량을 늘리지 않고, receptive field를 늘릴 수 있음

# 3.2 Softmax Distribution
- softmax distribution
    - 각 sample에 대해서 조건부확률을 구하기 위하여 사용
    - categorical distribution이 더 flexible하고, 어떠한 가정도 하지않으므로 모델링에 더 쉽기 때문에 연속적인 data에 대해서도 성능이 좋음

- $$\mu$$-law companding transformation
    - $$f(x_t)$$ = $$sign(x_t) \frac{ln(1 + \mu \mid x_t \mid)}{ln(1 + \mu)}$$
    - softmax로만 data를 예측하면 하면 너무 많은 경우의 수가 생기므로, data에 quantization 수행
    - non-linear quantization
    - 256개의 값으로 quantize

# 3.3 Gated Activation Unit
- Pixel CNN에서 제시한 gated activation unit 사용
    - $$z$$ = $$tanh(W_{f,k} \ast x) \odot \sigma (W_{g,k} \ast x)$$
    - $$W_{f}$$ = convolution filter of filter
    - $$W_{g}$$ = convolution filter of gate
    - $$x$$ = data
    - $$\ast$$ = convolution
    - $$\odot$$ = element-wise multiplication

# 3.4 Residual and Skip Connection
![residual](https://files.slack.com/files-pri/T1J7SCHU7-FAUHDGMD0/residual.png?pub_secret=59bcbdbcc6)
- 학습속도를 높이고, 깊은 모델을 학습시키기 위해 skip connection 사용

# 3.5 Conditional WaveNet
- $$p(x \mid h)$$ = $$\prod_{t=1}^{T} p(x_{t} \mid x_{1} , \cdots , x_{t-1}, h)$$
    - 새로운 조건 $$h$$가 추가될 경우의 조건부 확률
    - 즉, 다른 input을 추가해주는 방식으로 WaveNet의 생성결과에 characteristic을
    - 예를 들어, multi-speaker 상황에서 각 speaker identity를 추가적인 input으로 제공가능
    - 예를 들어, TTS(text-to-speech)에서는 text를 추가적인 input으로 제공가능

### 3.5.1 Global Conditioning
- $$z$$ = $$tanh(W_{f,k} \ast x + V_{f,k}^T h) \odot \sigma (W_{g,k} \ast x + V_{g,k}^T h)$$
    - $$h$$ = single latent representation
    - $$V_{f,k}$$ = learnable linear projection

- single representation $$h$$가 모든 output $$z$$에 영향을 주는 것 
- TTS의 speaker embedding 등에 사용

### 3.5.1 Local Conditioning
- $$z$$ = $$tanh(W_{f,k} \ast x + V_{f,k} \ast y) \odot \sigma (W_{g,k} \ast x + V_{g,k} \ast y)$$
    - audio보다 낮은 frequency를 가진 time series $$h_t$$ 존재
    - transposed convolution을 이용하여 $$y$$ = $$f(h)$$ 생성
    - $$y$$는 audio signal과 같은 resolution

- 여러가지의 representation을 넣어주어 각 output마다 받는 영향이 다름

# 3.6 Context Stacks
- receptive field를 넓히기 위한 방법
    - dilation stage의 증가
    - dilation factor의 증가
    - layer 및 filter의 크기 증가

- Context Stacks
    - receptive field를 넓히기 위한 추가적인 모듈
    - 더 낮은 resolution에서 작동
    - 적은 parameter로 더 이전의 signal을 학습가능

-----

## 4. Experiments
# 4.1 Multi-Speaker Speech Generation
- non-existent, human language-like words를 자연스러운 소리로 intonation
- speaker를 one-hot encoding하여 characterize 가능
- breathing and mouth movements등 voice 그 자체의 특성도 학습

# 4.2 Text-to-Speech
![result](https://files.slack.com/files-pri/T1J7SCHU7-FAUMF0WPP/result1.png?pub_secret=ca9540c028)

# 4.3 Music
- receptive field를 넓히는 것이 음악에 더 가까운 generation 생성 
- 음악에 대한 정보 등의 tag를 input으로 추가해주는 것이 더 좋은 성능을 보여줌
    - 만약 그렇지 않은 경우, 여러가지 음향이 섞이며 generation 생성

# 4.4 Speech Recognition
- 원래는 generative model이지만, Speech Recognition에서도 좋은 성능

- WaveNet for Speech Recognition
    - dilated convolution 이후에 mean-pooling layer추가
    - 2개의 loss term 사용

-----

## 5. Conclusion
- audio signal처리에서는 long-range temporal dependency가 중요
- 새로운 representation input을 추가하는 방식으로 characterize 가능

-----

## 6. Reference
- [https://arxiv.org/abs/1609.03499](https://arxiv.org/abs/1609.03499)
- [https://yangyangii.github.io/speechsynthesis/2017/12/30/PixelCNN-WaveNet.html](https://yangyangii.github.io/speechsynthesis/2017/12/30/PixelCNN-WaveNet.html)
