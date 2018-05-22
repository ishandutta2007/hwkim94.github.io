---
layout: post
title:  "Audio Style Transfer[3] Music Style Transfer: A Position Paper(2018) - Review"
date:   2018-05-22 13:45:00 +0900
categories: [deeplearning, audio, style-transfer]
---

## 1. Abstract
- image와는 달리 audio는 더 많은 특성을 가지고 있기 때문에, audio style transfer라는 것은 그 정의가 모호함. 따라서, 이 논문에서는 audio style transfer에 대해서 정의를 제시

-----

## 2. Introduction
# 2.1 Background of Automated Music Generation
- 사람들은 computer generation music이 natural & creative하기를 바라지만, 실제로 이런 결과를 만들지는 못했다. 

# 2.2 Music Style Transfer: Importance & Challenges
- style transfer는 music contents와 music style를 섞어 human-like한 새로운 음악을 generate
- 하지만, music style이라는 것은 너무 애매모호한 정의
    - 너무 많은 representation이 존재

- high level feature
    - tonality and chord sequence 등
- low level feature
    - sound texture and timbre 등

-----

## 3. Multi-level and Multi-modal Representation
# 3.1 Score(악보) Representation
![score](https://files.slack.com/files-pri/T1J7SCHU7-FAT33SEQG/score.png?pub_secret=9a8b194007)
- 악보는 음악의 tonality, chord, pitch, timing, dynamics등의 여러 특성을 encoding해둔 것
- 하지만, 각 symbol은 모두 discrete하기 때문에 generate하는 것이 어려움

# 3.2 Performance Control Representation
![midi](https://files.slack.com/files-pri/T1J7SCHU7-FATPK7YQJ/midi.png?pub_secret=eccfd0b03d)
- 악보가 실제로 연주되는 것을 encoding
- 주로 MIDI로 표현
    - 각 note는 pitch, dynamics, onset(starting time), duration등의 정보를 포함하고 있음

- 악보와는 다르게 timing and dynamics information이 자세하게 표현되어 있음
- phrase, repetition, chord progression 등 구조적 정보가 flatten됨

- 하지만, 악기에 대한 정보가 없으므로 music이 아닌 middle-level abstraction에 해당

# 3.3 Sound Representation
![sound](https://files.slack.com/files-pri/T1J7SCHU7-FATTLP65T/wave.png?pub_secret=503a1d8420)
- waveform, spectrogram 등으로 표현
- timbre, articulation, nuances 등 다른 것들은 표현하지 못하는 정보가 담겨있음
- Score, Performance Control의 모든 정보가 포함되어있음

# 3.4 Representation, Content, and Style
![table](https://files.slack.com/files-pri/T1J7SCHU7-FATGW29KN/table.png?pub_secret=538361107e)
- music content
    - abstraction 정보 
    - lower level부터 higher level까지의 정보를 추출

- music style
    - interpretation and realization 정보
    - higher level부터 lower level까지의 정보를 추출

- 각 level에 대한 정보를 따로 다룬 후, 합치는 것이 좋음

-----

## 4. Music Style Transfer: A Precise Definition and Related Work 
# 4.1 Timbre(음색) Style Transfer
- sound representation에 적용되어 timbre 만 바꾸고, performance control의 content는 유지하는 것
    - 예를 들어, 트럼펫의 소리만 플룻의 소리로 바꾸는 것
    - sound synthesis와 유사

# 4.2 Performance Style Transfer
- performance control representation에 적용되어 score content는 유지하고 control 정보를 바꾸는 것
    - 예를 들어, 'Summertime'에 대한 Louis Armstrongs의 interpretation을 Miles Davis 것으로 바꾸는 것
    - expressive performance rendering과 유사

# 4.3 Composition Style Transfer
- melody contour와 structural functions of harmony를 유지하면서 score feature를 바꾸는 것
    -  예를 들어, variation, improvisation, re-harmonization등의 편곡

-----

## 5. Future Directions of Music Style Modeling
- 원하는 style을 뽑아내고, 원하는 content에 붙이는 것을 정확하게 해야한다.
 
-----

## 6. Conclusion
- audio style transfer를 하기 위해서는 music representation이 multi-level, multi-modal이라는 것을 인지하고, 많은 특성이 있다는 것을 알아야함
- 구체적으로 바꾸려는 style이 어떤것인지 정의하고 모델링을 진행해야함 
    - timbre style transfer, performance style transfer, composition style transfer

-----

## 7. Reference
- [https://arxiv.org/abs/1803.06841](https://arxiv.org/abs/1803.06841)
