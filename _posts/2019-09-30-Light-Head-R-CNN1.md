---
layout: post
title:  "Light-Head R-CNN[1] Light Head R CNN: In Defense of Two Stage Object Detector(2017) - Review"
date:   2018-09-23 01:30:00 +0900
categories: [deeplearning, cnn, image-detection, r-cnn, paperreview]
---

## 1. Abstract
- 'two-stage detector는 왜 느릴까?' 라는 고찰
    - body(region proposal) 이후에 heavy head(bounding box regression, label classification)한 구조를 가짐
    - 예를 들어, Faster R-CNN의 경우 body 이후에 각각의 RoI에 대하여 2개의 fc layer가 존재

-----

## 2. Introduction
![fig1](https://files.slack.com/files-pri/T1J7SCHU7-FD37VKG3B/fig1.png?pub_secret=f827238e50)
- one-stage detector
    - bounding box와 label을 하나의 layer를 통해 예측
    - 빠르다는 장점

- two-stage detector
    - body(region proposal)와 head(recognition of proposal)로 구성
    - 느리지만 좋은 성능

- two-stage detector의 단점
    - backbone network 이후에 heavy head를 가지기 때문에 연산량이 많아 속도에 큰 영향을 가짐
    - 예를 들어, Faster R-CNN은 per-region proposal이므로 각각의 RoI에 2개의 fc layer 존재
    - 예를 들어, R-FCN은 비록 모든 RoI의 연산은 공유하지만 여전히 모델 규모에 따라 연산량이 크게 증가

- Light-Head R-CNN
    - efficient accurate two-stage detector
    - large-kernel separable convolution을 적용하여 light head(thin feature maps)을 가짐

-----

## 3. Related works
- R-CNN 계열
- FPN
- SPPnet
- YOLO
- SSD

-----

## 4. Our Approach
![fig2](https://files.slack.com/files-pri/T1J7SCHU7-FD41C3QS1/fig2.png?pub_secret=15f785aa9e)
# 4.1 Light-Head R-CNN
- R-CNN subnet과 ROI warping으로 구성

### 4.1.1 R-CNN subnet(head)
- Faster R-CNN
    - 각각의 RoI마다 2개의 fc layer를 가지므로 성능이 좋지만, 연산량이 많아서 속도가 느림
    - 연산량을 줄이기 위하여 위치정보를 고려하지 않는 global average pooling을 사용

- R-FCN
    - 각각의 RoI마다 연산은 없기 때문에 Faster R-CNN보다 속도는 빠르지만, 성능이 좋지않음
    - RoI-wise computation을 대신하여 많은 score map을 가지기 때문에 연산량이 결코 적지는 않음
    - position-sensitive pooling 이후에 global average pooling을 사용 

- Light-Head R-CNN
    - Faster R-CNN과 R-FCN의 trade-off를 고려
    - 가볍고 단순한 1개의 fc layer 사용

### 4.1.2 Thin feature maps for RoI warping
- thin feature map
    - RoI wrapping을 하기 전에 CNN을 통해 얇은(small channel number) feature map을 생성
    - backbone network의 feature map이 아니라 생성된 얇은 feature map에 RoI wrapping
    - 성능을 올려주며, 연산량을 절감하여 속도도 빨라짐

- RoI warping
    - RSRoI pooling
    - RoI pooling

# 4.2 Light-Head R-CNN for Object Detection
- 모델 크기에 따라 L, S로 version을 나눔
    - L : high performance
    - S : effectiveness and efficiency

### 4.2.1 Basic feature extractor
- backbone network(basic feature extractor)
    - L : ResNet-101
    - S : Xception-like model

### 4.2.2 Thin feature maps
![fig3](https://files.slack.com/files-pri/T1J7SCHU7-FD3REL2P4/fig3.png?pub_secret=2b503955fa)
- 5-th convolution block에 separable convolution 적용
    - $$K$$=15를 사용하여 receptive field가 넓어짐
    - 연산량이 적어짐 

### 4.2.3 R-CNN subnet(head)
- 1개의 fc layer로 구성
- 2개의 sibling fc layer로 이어짐
    - bounding box regression
    - label classification

### 4.2.4 RPN
- 4-th convolution block의 feature map 사용
- anchor box
    - 15개 사용

- NMS
    - NMS를 통하여 overlapping proposal을 통합
    - RoI wrapping을 하기 전에 proposal을 줄이는 역할

- IoU threshold
    - 0.7 이상 : positive label
    - 0.3 이하 : negative label

-----

## 5. Experiments
# 5.1 Implementation Details
- mini-batch = 2
    - zero padding으로 크기를 맞춰줌
- horizontal flipping

# 5.2 Ablation Experiments
### 5.2.1 Baselines
![table1](https://files.slack.com/files-pri/T1J7SCHU7-FD386CWBB/table1.png?pub_secret=cf6299bff5)

### 5.2.2 Thin feature maps for RoI warping
![fig4](https://files.slack.com/files-pri/T1J7SCHU7-FD41S6ATX/fig4.png?pub_secret=be485289af)
- thin feature map의 성능을 확인하기 위하여 R-FCN을 변형하여 실험
    - thin feature map을 통하여 feature map의 수를 3969개에서 490개로 줄임
    - 마지막 prediction layer를 fc layer로 바꿈

- RSRoI Pooling을 위한 feature map의 수가 80% 정도 줄었지만, 성능은 비슷함
- FPN을 사용할 경우, 효과적으로 feature를 통합할 수 있음

### 5.2.2.1 Large separable convolution
![table3](https://files.slack.com/files-pri/T1J7SCHU7-FD3LC551S/table3.png?pub_secret=ba10fd6876)
- separable convolution에서 large kernel을 사용하는 것이 더 좋은 성능

### 5.2.3 R-CNN subnet
![table4](https://files.slack.com/files-pri/T1J7SCHU7-FD3462E80/table4.png?pub_secret=3c0ef3353d)

# 5.3 Light-Head R-CNN: High Accuracy
![table5](https://files.slack.com/files-pri/T1J7SCHU7-FD34CCPEU/table5.png?pub_secret=64cc2c144a)

# 5.4 Light-Head R-CNN: High Speed
![table8](https://files.slack.com/files-pri/T1J7SCHU7-FD41VBPHT/table8.png?pub_secret=0c659c5bf8)

-----

## 6. Conclusion
- two-stage detector임에도 light-head를 사용하여 속도가 빠르고, 성능도 좋음

-----

## 7. Reference
- [https://arxiv.org/abs/1711.07264](https://arxiv.org/abs/1711.07264)
- [https://github.com/MagmaTart/Paper-Reading/blob/master/summarys/Light-Head-R-CNN.md](https://github.com/MagmaTart/Paper-Reading/blob/master/summarys/Light-Head-R-CNN.md)
