---
layout: post
title:  "Audio Style Transfer[5] A Universal Music Translation Network(2018) - Review"
date:   2018-05-25 14:30:00 +0900
categories: [deeplearning, audio, style-transfer, paperreview]
---

## 1. Abstract 
- 음악의 musical instruments, genres, style을 바꾸는 model 제시
    - WaveNet Autoencoder 기반
    - 예를 들면, piano곡을 violin곡으로 transfer

-----

## 2. Introduction
- autoregressive and unsupervised
    - previous time step $$t$$의 결과를 이용하여 다음 time step $$t+1$$의 결과를 예측

- single universal encoder
    - 모든 data에 대해서 같은 encoder를 적용
    - 적은 network를 학습하므로 효율적
    - autoencoder 기반이므로 학습시에 다른 domain을 같이 처리하지 않지만, 하나의 encoder로 모든 data를 학습하므로 다른 domain으로 convert 가능
    - 따라서, single encoder architecture에서는 domain-specific information이 encoding되지 않도록 처리해야 함

- domain confusion network
    - encoder가 input signal(donain)을 memorizing하지 못하게 하기 위한 방법
    - 즉, encoding vector가 악기 등 domain을 표현할 수 없도록 만드는 역할
    - 예를 들면, timbre(음색) 등 기존 악기에 대한 domain information을 제외하고 '악보' 등의 정보만 추출하는 것. 왜냐하면 기존 악기에 대한 정보가 encoding에 남아있다면, 새로운 악기에 대한 연주를 generation했을 때 기존의 악기의 연주가 남게 됨. 따라서, 기존 악기에 대한 information을 지우고, 악보에 대한 정보만 가진 채로 새로운 악기에 대한 연주를 generation해야 함

- random local pitch modulation을 통한 input audio 왜곡(distort)
    - 마찬가지로, encoder가 input signal을 memorizing하지 못하게 하기 위한 방법
    - domain에 없던 새로운 input에도 대응할 수 있기 위해서는 memorization에 의존하여 encoding하는 것이 아니라, input 그 자체의 정보를 그때그때 encoding해야 함

- 왜곡되지 않은 original input을 복구하는 denoising autoencoder처럼 학습
    - distorted signal은 원래 input set(domain)에 없는 것이므로, network는 매번 새로운 input(out-of-domain)을 원하는 domain으로 바꾸는 것을 학습하게 됨 
    - input signal을 계속 사용할 수 없으므로, 즉, memorizing이 불가능하므로 encoding이 높은 수준으로 학습됨
    - 따라서, encoder는 domain에 없는 새로운 input signal을 잘 encoding 가능
    - 최종적으로, encoding된 정보를 가지고 decoder에서 원하는 domain의 특징을 가진 새로운 signal을 generation

-----

## 3. Previous Work
- Domain Transfer
- Audio Synthesis
- Style Transfer

-----

## 4. Method
![architecture](https://files.slack.com/files-pri/T1J7SCHU7-FAURMPBUZ/arcitecture.png?pub_secret=fca380d562)
- 각 악기(domain)마다 autoencoder 학습
    - encoder는 공유 

- input data는 randomly augmented(증음) 
    - encoder가 domain을 memorizing할 수 없게 하여, high-level semantic features만 추출하기 위하여 사용

- domain confusion network
    - encoding 결과가 domain-specific하지 않게 만드기 위하여 사용

- softmax-based reconstruction loss
    - 8-bit $$\mu$$-law encoding을 통한 양자화(quantization)
    - 즉, softmax를 사용하기 위하여 역속적인 wave를 discrete하게 표현하여 예측

# 4.1 WaveNet Autoencoder
- WaveNet Autoencoder
    - WaveNet like Dilated convolution Encoder
    - WaveNet Decoder
    - domain confusion network와 encoder/decoder가 경쟁적으로 학습

### 4.1.1 Encoder
![encoder](https://files.slack.com/files-pri/T1J7SCHU7-FAW73GPHT/autoencoder.png?pub_secret=d4d5645bcb)
- any sequence에 적용 가능한 dilated convolutional network 
- 3 blocks of 10 residual-layers
- ×12.5 down sampling

### 4.1.2 Domain Confusion Layer
- training에서만 사용
- encoding vector의 domain을 맞추도록 학습하여, encoder가 domain관련한 정보를 encoding하지 않는 방향으로 학습하게 만듦

### 4.1.3 Decoder
- 4 blocks of 10 residual-layers
- autoregressive
- training에는 previous time step의 결과물이 아니라 원래 sample을 feed하여 학습
- $$p(x_N)$$ = $$\prod_{i} p(x_i \mid x_1, \cdots, x_{N-1}, embedding)$$를 최대화하기 위하여 학습

# 4.2 Audio Input Augmentation(증음)
- Augmentation
    - pitch를 국소적으로(locally) 변화시키는 방법 사용
    - generalization과 higher-level information을 유지하기 위한 방법

# 4.3 Training and Losses Used
- Autoencoder loss = $$\sum_{j} \sum_{s^j} L(D^j(E(O(s^j, r))), s^j)$$
    - noise가 추가된 sample을 잘 복구하도록 학습

- Domain Confusion Network $$C$$'s loss = $$\sum_{j} \sum_{s^j} L(C(E(O(s^j, r))), j)$$
    - encoding vector의 domain을 맞추도록 학습

- Total loss = $$\sum_{j} \sum_{s^j} L(D^j(E(O(s^j, r))), s^j) - \lambda L(C(E(O(s^j, r))), j)$$
    - encoder/decoder는 $$\lambda L(C(E(O(s^j, r))), j)$$는 크게 만들고, $$\sum_{j} \sum_{s^j} L(D^j(E(O(s^j, r))), s^j)$$는 작게 만들도록 학습이 된다.
    - 하지만, domain confusion network $$C$$는 원래의 domain을 잘 맞추도록 학습이 되므로 $$\lambda L(C(E(O(s^j, r))), j)$$가 작아지게 학습이 되어 autoencoder loss는 커지게 된다.
    - 즉, encoder는 domain confusion network가 원래의 domain을 맞추지 못하도록 domain-specific information을 포함하지 않게 학습되며, decoder는 domain에 대한 정보가 거의 없는 encoding vector를 input domain sample로 복구하도록 학습이 된다.
    - 따라서 encoder를 통해 encoding된 vector는 domain-specific 정보 없이 semantic feature만 가지게 되고, decoder는 semantic feature만 가지고 domain의 정보를 추가하여 원래의 audio를 복구하게 된다.
    - $$s^j$$ = sample from domain $$j$$
    - $$O(s, r)$$ = ramdom augmentation procedure to sample $$s$$ with random seed $$r$$
    - $$E$$ = shared domain
    - $$D^j$$ = WaveNet decoder for domain $$j$$
    - $$C$$ = domain classification network 
    - $$L$$ = cross entropy loss

# 4.4 Network during Inference
- result output = $$s^j$$ = $$D^j E(s)$$
    - sample $$s$$를 domain $$j$$의 autoencoder에 적용

-----

## 5. Experiments
# 5.1 Training
- domain
    - Mozart’s 46 symphonies
    - Haydn’s 27 string quartets
    - J.S Bach’s cantatas for orchestra, chorus and soloists
    - J.S Bach’s organ works
    - Beethoven’s 32 piano sonatas
    - J.S Bach’s keyboard works, played on Harpsichord

# 5.2 Evaluation of translation quality
![result1](https://files.slack.com/files-pri/T1J7SCHU7-FAVC7TR50/result1.png?pub_secret=4a1115a508)
- E, M, A = 실험을 위한 실제 professional musician
- NCC = Normalized Cross Correlation
- DTW = Dynamic Time Warping


# 5.3 Lineup experiment
![result2](https://files.slack.com/files-pri/T1J7SCHU7-FAV5K5ALU/result2.png?pub_secret=f6a1eb0fcd)
- model의 output과 실제 sample을 구분하는 실험
    - 얼마나 자연스러운지를 실험 가능

# 5.4 Semantic blending
- DJ처럼 서로 다른 segment를 섞어보는 실험
    - 1개의 domain 으로 부터 5초짜리 segment $$i, j$$를 각각 추출
    - encoder를 통해 encoding하여 $$e_i, e_j$$생성
    - 앞의 3.5초는 $$e_i$$를 사용하고, 뒤의 1.5초는 (1-t/1.5)*$$e_i$$ + t/1.5*$$e_j$$, t $$\in$$ [0, 1.5] 
    - 따라서, 3.5초부터는 뒤로 갈수록 segment $$j$$의 특징을 가지게 됨
    - decoder로 generation
    - 결과적으로, 자연스럽게 두 segment가 blending됨

# 5.5 NSynth pitch experiments
![result3](https://files.slack.com/files-pri/T1J7SCHU7-FAV5K651S/result3.png?pub_secret=32e74972a1)
- NSynth audio dataset의 악기별 encoding된 pitch의 상관관계를 확인해본 실험
    - audio dataset에 대한 두 악기의 pitch가 비슷하게 encoding됨
    - 즉, 악기에 대한 특성(domain-specific)은 encoding되지 않음
    - 곡 그 자체에 대한 정보만 encoding되기 때문에 decoder를 통해서 다른 악기에 대한 audio를 generation 가능

-----

## 6. Discussion
- universal encoder는 music data에서 악보를 뽑아내는 것과 같이, 필요한 정보를 잘 뽑아내는 기능을 가지고 있다.

-----

## 7. Reference
- [https://arxiv.org/abs/1805.07848](https://arxiv.org/abs/1805.07848)
- [https://arxiv.org/abs/1704.01279](https://arxiv.org/abs/1704.01279)
- [https://arxiv.org/abs/1505.07818](https://arxiv.org/abs/1505.07818)
- [https://www.youtube.com/watch?v=vdxCqNWTpUs](https://www.youtube.com/watch?v=vdxCqNWTpUs)
