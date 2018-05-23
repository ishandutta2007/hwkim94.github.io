---
layout: post
title:  "Distributed DL[2] Large Scale Distributed Deep Networks(2012) - Review"
date:   2018-05-16 15:30:00 +0900
categories: [distributed-computing, deeplearning, paperreview]
---

## 1. Abstract
- TensorFlow의 전신인 DistBelief를 공개한 논문
- large-scale distributed training을 위한 algorithm 소개
    - Downpour SGD, Sandblaster L-BFGS

-----

## 2. Introduction
- DL의 경우 parameter와 data 등 scale이 커지면 accuracy도 높아짐
- GPU를 사용하면 학습속도가 빨라짐
    - 하지만, data의 용량이 너무 커서 GPU 혹은 CPU 용량에 적합하지 않아 사용이 불가능할 수도 있음
    - model의 scale을 낮춰 학습시키는 방법도 있지만, scale을 크게하는 것이 성능이 좋음

- 따라서, cluster환경을 통한 distributed learning을 framework인 DistBelief를 통해 제시
    - Model Parallelism within(via multi-threading) & across(via message passing) machine
    - Data Parallelism

- Downpour SGD
    - asynchronous SGD
    - Adagrad adaptive learning rates와 결합될 경우, nonconvex optimization에서도 좋은 성능

- L-BFGS
    - 다양한 종류의 SGD보다 성능이 훨씬 좋거나 비슷

- model의 size가 커질 경우, GPU보다 훨씨 빠름
- parameter의 개수가 커질 경우, ImageNet에서 state-of-the-art

-----

## 3. Previous work
- machine learning algorithm
- convex
- distributing gradient computation
- Model Parallelism, Data Parallelism
- MapReduce, GraphLab

-----

## 4. Model parallelism
![Model parallelism](https://files.slack.com/files-pri/T1J7SCHU7-FAR4KPHSS/mp.png?pub_secret=12c6aad9a2)

- model을 partition들로 나누어 각각 연산하는 것
    - 자신의 partition에 없는 다른 node(neuron)의 연산은 해당 node가 속해있는 partition을 담당하는 machine이 연산
    - 각 node의 연산 결과를 다른 node로 전달할 때, machine들간의 communication 발생

- large-scale model의 경우, 많은 parameter를 가지기 때문에 높은 연산비용을 가지게됨
    - Model Parallelism을 사용할 경우, network비용(communication 비용)이 기존 비용을 넘어설 때까지 분산처리 가능
    - fully-connected structure model보다 local-connected structure model이 적합

-----

## 5. Distributed optimization algorithms
![Distributed optimization](https://files.slack.com/files-pri/T1J7SCHU7-FAR4KN6NS/dis.png?pub_secret=fa296ba9be)
- Data Parallelism을 기반으로 여러 개의 model replicas 학습
    - Model Parallelism만으로는 large-scale model의 학습 시간을 단축하는 것이 불가
    - 각각의 분산된 data마다 model을 복제하여 각각 학습한 뒤 parameter 공유

- 비동기적으로 학습되어야 함
    - 즉, 다른 model replica의 학습 speed에 상관없이 학습되어야함
    - parameter server 활용

# 5.1 Downpour SGD
- SGD
    - 각 epoch마다 모든 mini-batch의 gradient가 순차적으로 적용되는 알고리즘
    - 학습이 sequential하게 진행되므로 large-scale model에 부적합

- Downpour SGD
    - 여러 개의 model replicas를 통하여 비동기적으로(asynchronous) 학습
    - data를 여러 개의 partition으로 나눈 후, 각 partition마다 model을 복제(replica)
    - 각 model replica은 Model Parallelism을 통해 여러 node에 의해 학습됨 
    - 각 replica의 학습 결과(gradient)는 parameter server로 전송
    - parameter server도 여러 shard로 나누어져 각 shard가 담당하는 parameter를 update
    - 따라서, 각 machine은 자기가 연산한 parameter 관계있는 server shard와 communicate
    - update된 parameter를 다시 해당 model replica로 보내서 다시 학습 
    
- 다른 replicas에 상관없이 학습되므로 다른 machine이 작동을 멈춰도 영향을 받지 않음
- 최적화 절차에 추가적인 stochasticity(확률)이 도입됨
    - parameter server는 계속 update되므로 각 replicas의 parameter는 실질적으로 out-of-date
    - 각 model replicas는 update된 parameter를 가져오는 작업과 gradient를 server로 보내는 작업을 다른 thread로 처리하므로, 각 timestamp의 parameter가 안정적이지 않음(inconsistency) 
    - 따라서, Adagrad의 adaptive learning rate procedure를 적용하면 non-convex 상황에 효과적
    - adaptive learning rate 학습의 안정성을 부여하여 non-convex에서 다양한 방향으로 안정적으로 학습하게됨

- adaptive learning rate procedure
    - $$lr_{i,k}$$ = $$\frac{\gamma}{\sum_{j=1}^{K} {\mid \mid \bigtriangledown w_{i,j} \mid \mid}^2}$$
    - $$lr_{i,k}$$ = i-th parameter's learning rate
    - $$K$$ = current iteration
    - $$\gamma$$ = constant learning rate
    - 각 parameter마다 learning rate를 다르게 하는 것
    - gradient update가 큰 parameter는 점점 학습속도가 감소하고, 작은 parameter는 점점 학습속도가 증가

# 5.2 Sandblaster L-BFGS
- Coordinator가 작업을 전반적으로 관리
    - 최적화 알고리즘 L-BFGS 내재
    - Data Parallelism을 하지 않음
    - 각 model replicas에 일정 양의 data를 분배하고, 더 빠르게 data를 학습시키는 replicas에 더 많은 data 분배
    - 따라서, faster model replicas는 slower model replicas보다 더 많은 학습을 진행하게 됨 
    - MapReduce의 backup task와 비슷
    
- BFGS
    - NewtonRaphson Algorithm은 Hessian Matrix의 inverse를 통하여 Newton's method를 반복하며 최적화하는 기법
    - 하지만, data가 많아진다면 Hessian Matrix의 inverse를 구하는 것은 불가능
    - 따라서, Hessian Matrix를 근사하여 구하게 됨
    - $$h_n(d)$$ = $$f(x_n) + d^T g_n + \frac{1}{2} d^T H_n d$$ = n-th quadratic approximation
    - $$\bigtriangledown h_n(x_{n})$$ = $$g_n$$, $$\bigtriangledown h_n(x_{n-1})$$ = $$g_{n-1}$$
    - $$\bigtriangledown h_n(x_{n}) - \bigtriangledown h_n(x_{n-1})$$ = $$g_n - g_{n-1}$$
    - $$H_n (x_n - x_{n-1})$$ = $$g_n - g_{n-1}$$ 를 만족
    - 즉, $$min(\mid \mid H_{n+1}^{-1} - H_n^{-1} \mid \mid)$$과 $$x_n - x_{n-1}$$ = $$H_{n+1}^{-1}(g_n - g_{n-1})$$를 만족하는 $$H_{n+1}^{-1}$$을 찾아내는 알고리즘
    - $$g_n$$ = n-th gradient
    - $$H_n$$ = n-th Hessian Matrix

- L-BFGS
    - BFGS에서 모든 $$n$$에 대해서 update하지 않고, 가장 최근의 $$m$$개에 대해서만 update하는 것

- DownpourSGD는 높은 frequency, bandwidth parameter synchronization을 요구하지만, Sandblaster L-BFGS는 각 coordinator에 의해 분배된 batch를 학습할 때만 parameter를 가져오고, 계산이 완료된 gradient중 일부분만 server로 보내므로 상대적으로 낮은 frequency, bandwidth parameter synchronization을 요구

-----

## 6. Experiments
# 6.1 Model parallelism benchmarks
![result1](https://files.slack.com/files-pri/T1J7SCHU7-FAQM535E1/fig3.png?pub_secret=796c394e0f)
- Model parallelism을 할 때, 한 model을 partition하는 core의 수가 많아질수록 학습속도가 빨라진다.

# 6.2 Optimization method comparisons
![result2](https://files.slack.com/files-pri/T1J7SCHU7-FAQ13B6MP/fig4.png?pub_secret=7fa1bb9b4a)
- DownpourSGD with Adagrad의 성능이 제일 좋았으며, Sandblaster L-BFGS의 성능이 뒤를 이었다.

# 6.3 Application to ImageNet
![result3](https://files.slack.com/files-pri/T1J7SCHU7-FAQAE2X1A/fig5.png?pub_secret=1436c530ea)
- 적은 개수의 core를 사용할 때는 GPU보다 느리지만, core의 수가 늘어나면 GPU보다 학습속도가 훨씬 빨라진다.

-----

## 7. Conclusions
**cluster of machines to train even modestly sized deep networks significantly faster than a GPU**

-----

## 8. Reference
- [http://www.cs.toronto.edu/~ranzato/publications/DistBeliefNIPS2012_withAppendix.pdf](http://www.cs.toronto.edu/~ranzato/publications/DistBeliefNIPS2012_withAppendix.pdf)
- [http://aria42.com/blog/2014/12/understanding-lbfgs](http://aria42.com/blog/2014/12/understanding-lbfgs)
