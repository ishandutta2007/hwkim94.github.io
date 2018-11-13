---
layout: post
title:  "Video Style Transfer[1] Artistic style transfer for videos(2016) - Review"
date:   2018-11-13 11:10:00 +0900
categories: [deeplearning, video, style-transfer, paperreview]
---

## 1. Abstract
- 연속적이고 안정적인 video style transfer를 위한 새로운 initialization과 loss 제안

-----

## 2. Introduction
- style transfer for image
    - content image와 style image에 CNN을 적용

# 2.1 style transfer for video
![fig1](https://files.slack.com/files-pri/T1J7SCHU7-FE1C825HP/fig1.png?pub_secret=6d437b8dbd)
- 일반적인 style transfer를 video의 frame에 각각 적용하면 frame별로 다르게 학습되어 discontinuous하기 때문에 stable하지 않다는 문제 발생

- white noise feature map
    - white noise로 부터 generated image를 생성

- temporal consistency
    - 자연스러운(smooth) 장면 전환(frame transition)을 위해서 두 frame의 deviation(편차)에 penalty를 적용
    - 단순한 image의 deviation에 편차에 penalty를 적용하는 것이 아니라, point trajectory에 penalty를 적용하는 optical flow 기법 사용
    - 즉, frame에서 사라진 물체에 대해서는 penalty를 적용하지 않고, 계속 화면에 존재하는(trajectory에 존재하는) 물체에만 penalty 적용

- long-term consistency
    - 만약 어떤 물체가 화면에 가려졌다가(occuluded) 다시 등장하게 된다면, 그 부분의 style이 기본과는 다르게 새로 학습되는 문제 발생
    - long term motion estimate를 통해 물체의 재등장시 frame간의 style을 같게 유지해줌

- multi-pass algorithm
    - image의 boundary에 content image에 없는 artifact(물체)가 생기는 경우가 존재
    - image에서는 크게 상관이 없지만, video에서는 중앙쪽으로 카메라가 움직이면서 기존의 content와 증폭되는 문제 발생
    - video의 forward/backward 방향을 번갈아가며 처리하는 multi-pass algorithm 방식으로 해결

-----

## 3. Related Work
- Style transfer using deep networks
- Painted animations

-----

## 4. Style Transfer in still images
- content loss
    - CNN을 통해 output의 feature map이 content image와 비슷해지도록 함
    - $$L_{content}$$ = $$\sum_{l \in num(layers)} \frac{1}{N_l M_l} \sum_{i,j} (F_{ij}^l - P_{ij}^l)^2$$
    - $$N_l, M_l$$ = size of $$l$$-th layer feature map
    - $$F_{ij}^l$$ = original image를 layer에 통과시켰을 때, output의 각 pixel값
    - $$P_{ij}^l$$ = generated image를 layer에 통과시켰을 때, output의 각 pixel값
    - 즉, 각 layer마다 content image와 generated image의 모양(content)가 얼마나 차이나는지를 loss로 사용

- style loss
    - output과 style image의 correlation을 통해 style이 비슷하도록 encoding
    - $$L_{style}$$ = $$\sum_{l \in num(layers)} \frac{1}{N_l^2 M_l^2} \sum_{i,j} (G_{ij}^l - A_{ij}^l)^2$$
    - $$N_l, M_l$$ = size of $$l$$-th layer feature map
    - $$A_{ij}^l$$ = $$\sum_{k=1}^{M_l} S_{ik}^l S_{jk}^l$$ = style image의 Gram Matrix
    - $$G_{ij}^l$$ = $$\sum_{k=1}^{M_l} F_{ik}^l F_{jk}^l$$ = gernerated image의 Gram Matrix
    - 즉, 각 layer마다 content image와 generated image의 style이 얼마나 차이나는지를 loss로 사용

- total loss
    - &&L_total&& = &&\alpha L_{content} + \beta L_{style}&&

-----

## 5. Style Transfer in videos
# 5.1 Short-term consistency by initialization
- 만약 연속적인 frame이 각각 다른 Gaussian noise로 부터 initialization될 경우, 두 frame이 서로 다른 local minima로 수렴하여 flickering 문제(같은 부분에 다른 style이 적용되는 문제)가 발생

- $$i$$-th generated image를 $$(i+1)$$-th frame의 initialization로 사용
    - 변화가 없는 부분은 그대로 style이 적용되고, 새로 등장하거나 변화되는 부분은 새롭게 학습
    - 하지만, motion이 있는 경우에는 움직이는 부분에 initialization이 부정확하게 되는 문제가 발생

- optical flow 적용
    - original image의 frame에서 측정된 optical flow field를 $$i$$-th generated image에 적용하여 $$(i+1)$$-th frame의 initialization로 사용
    - $$x^(i+1)$$ = $$\omega_i^{i+1} (x^i)$$
    - $$\omega$$ = optical flow field
   
# 5.2 Temporal consistency loss
- 인접한 장면의 일관성을 위해서 연속된 두 frame에 penalty를 부여
    - 이를 위해서는 물체가 사라진건지 아닌지에 대한 것과 motion에 대한 detection이 필요

- disocclusion object(가려지지 않은 object,즉, 화면에 지속적으로 존재하는 object)
    - object disocclusion을 판단 위하여 forward/backward 방형의 optical flow를 확인
    - disocclusion이 발생하지 않는 area는 forward/backward 방형의 optical flow가 거의 반대이기 때문에, disocclusion인 부분은 아래의 부등식이 성립
    - $$\mid \tilde{w} + \hat{w} {\mid}^2 $$ > $$0.01 ( \mid \tilde{w} {\mid}^2 + \mid \hat{w} {\mid}^2) + 0.5$$
    - $$w$$ = $$(u,v)$$ = forward 방향의 optical flow
    - $$\hat{w}$$ = $$(\hat{u}, \hat{v})$$ = backward 방향의 optical flow
    - $$\tilde{w}(x,y)$$ = $$w((x,y) + \hat{w}(x,y))$$

- motion boundary
    - $$\mid \bigtriangledown \hat{u} {\mid}^2 + \mid \bigtriangledown \hat{v} {\mid}^2$$ > $$0.01\mid \hat{w} {\mid}^2 + 0.002$$
    - 위의 공식을 이용하여 motion detection을 함

- temporal consistency loss
    - frame에서 optical flow가 변화없는 곳에 적용되어 deviation에 penalty를 적용
    - $$L_{temporal}(x, z, c)$$ = $$\frac{1}{D} \sum_{D}^{k=1} c_k \cdot (x_k - z_k)^2$$
    - $$c$$ = per-pixel weight $$\in [0,1]^D$$ 
    - $$D$$ = $$W \times H \times C$$

- short-term loss
    - $$L_{short-term}^i$$ = $$\alpha L_{content}^i + \beta L_{style}^i + \gamma {L_{temporal}}_{i-1}^i$$
    - $${L_{temporal}}_{i-1}^i$$ = $$L_{temporal}(x^i, \omega_{i-1}^{i} (x^{i-1}), c^{(i-1,i)})$$
    - $$c^{(i-1,i)}$$= disoclussion 혹은 motion boundary가 있는 곳은 0, 아니면 1
    - $$\omega_{i-1}^{i}$$ = optical flow field from $$(i-1)$$-th frame to $$i$$-th frame

# 5.3 Long-term consistency loss
- 물체가 가려졌다가(occluded) 다시 등장하는(disoccluded) 경우, style이 변하는 문제가 발생
    - previous frame만 확인하는 것이 아니라, 더 멀리 있는 frame도 확인할 수 있는 long-term loss 적용

- long-term loss
    - $$L_{long-term}^i$$ = $$\alpha L_{content}^i + \beta L_{style}^i + \gamma \sum_{j \in J} {L_{temporal}}_{i-j}^i$$
    - $${L_{temporal}}_{i-j}^i$$ = $$L_{temporal}(x^i, \omega_{i-j}^{i} (x^{i-j}), c_{long}^{(i-j,i)})$$
    - $$J$$ = $$i$$-th frame이 고려해야하는 frame의 index set
    - $$c_{long}^{(i-j,i)}$$ = $$max(c^(i-j, i) - \sum_k c^{(i-k), i}, 0)$$

- 우선 short-term loss를 적용한 후, long-term loss 적용

# 5.4 Multi-pass algorithm
![fig2](https://files.slack.com/files-pri/T1J7SCHU7-FE20LQ1L2/fig2.png?pub_secret=6f04b8f0ea)
- boundary가 다른 부분에 비해 학습이 잘 되지 않는다는 문제가 존재
    - camera가 움직이면서 image boundary가 화면의 중심으로 오게 될 경우, 낮은 quality의 output을 보여줌 
    - image sequence를 다양한 방향과, multiple-pass로 학습을 시키는 방식으로 해결

- multiple-pass algorithm
    - 우선 각 frame을 독립적으로 학습시킨 후, non-disoccluded한 image끼리 섞어서 optimization
    - 이때, optimization은 forward/backward 방향 모두에 대해서 학습
    - ![image](https://files.slack.com/files-pri/T1J7SCHU7-FE3CM2S4W/1.png?pub_secret=076b767ddf)

-----

## 6. Experiments
# 6.1 Implementation details
![style transfer](https://files.slack.com/files-pri/T1J7SCHU7-FE26GTPEZ/style_transfer.png?pub_secret=6ff8e50db7)
- 기존의 style transfer처럼 VGG-19 기반의 model
    - $$relu4-2$$의 output을 content loss에 사용
    - $$relu1-1$$, $$relu2-1$$, $$relu3-1$$, $$relu4-1$$, $$relu5-1$$의 output을 style loss에 사용

- L-BFGS를 통해 optimization
    - 50 iteration 동안 0.01% 이상 감소하지 않으면 학습을 중단
    - 처음 image에는 2000~3000 iteration, 그 이후의 image는 400~800 iteration

- parameter for loss
    - $$\alpha$$ = 1, $$\beta$$ = 20, $$\gamma$$ = 200 for $$350 \times 450$$
    - $$\alpha$$ = 1, $$\beta$$ = 40, $$\gamma$$ = 200 for $$768 \times 432$$
    - $$\alpha$$ = 1, $$\beta$$ = 100, $$\gamma$$ = 400 for $$1024 \times 436$$

- multi-pass algorithm
    - $$\delta$$ = 0.5
    - 100 iteration for pass
    - 10개 정도의 pass가 좋은 성능 

- optical flow
    - DeepMatching, DeepFlow, EpicFlow 사용

- Sintel dataset 사용


### 6.1.1 Runtime
- style transfer
    - GPU를 사용하여 frame당 3분 소요

- optical flow
    - CPU를 사용하여 frame당 3분 소요
    - 병렬처리 가능

# 6.2 Short-term consistency
![table1](https://files.slack.com/files-pri/T1J7SCHU7-FE26H0SKF/table1.png?pub_secret=444586bd03)

# 6.3 Long-term consistency and multi-pass algorithm
![fig3-4](https://files.slack.com/files-pri/T1J7SCHU7-FE32458DV/fig3.png?pub_secret=477d3fd450)

-----

## 7. Conclusion
- 새로운 loss를 도입하여 video에 style transfer를 자연스럽게 적용

-----

## 8. Reference
- [https://arxiv.org/abs/1604.08610](https://arxiv.org/abs/1604.08610)
- [https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf)
- [https://youtu.be/vQk_Sfl7kSc](https://youtu.be/vQk_Sfl7kSc)
- [https://en.wikipedia.org/wiki/Optical_flow](https://en.wikipedia.org/wiki/Optical_flow)
