## Memory optimization using Quantization

Quantization is technique to reduce precision of model weights and activations to decrease the size and thus reducing memory usage for training and inference.

FP32 data format:

* Sign: 1 bit
* Exponent: 8 bits
* Mantissa: 23 bits

Formula: 

$$
V = (-1)^{\text{sign}} \times 2^{(\text{exponent} - \text{bias})} \times 1.\text{mantissa}
$$

Features of a data format:
* Dynamic range: Interval of representable numbers (Min value and Max value).
* Precision: Distance between two neighboring values. low distance = high precision.


### FP16 (Half precision)
Represnting model weights and activations as 16 bit floating point. It has lower precision and lower dynamoc range compared to FP32.

FP16 data format:

* Sign: 1 bit
* Exponent: 5 bits
* Mantissa: 10 bits


### BFLOAT16
Bfloat16 is a custom 16-bit floating point format for machine learning. Bfloat16 maintains the same dynamic range as FP32. Precision is lower in comparison to FP32 and FP16.

BFLOAT16 data format:

* Sign: 1 bit
* Exponent: 8 bits
* Mantissa: 7 bits


**Reference:** https://cloud.google.com/blog/products/ai-machine-learning/bfloat16-the-secret-to-high-performance-on-cloud-tpus


### Post training Quantization
Quantizing model paramaters (weights and activations) after training the model.

#### Dynamic Quantization
Values at each hidden layer are collected and quantization is performed based on distribution of the values. Each layer will have different scaling factor and zero point.

#### Static Quantization
Scaling factor and zero point is calculated only once and is applied to all hidden layers. This reduces computations during inference while is less accurate.

### Quantization aware training
Quantization is performed as part of training where fake quants are introduced to represent quantized outputs. This is useful where loss minimization is done considering the quantized outputs.

**Reference:** https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization

