<script setup>
import { Model } from 'survey-core'
import {ElMessageBox} from "element-plus";

defineProps({
  msg: String,
})

const introduction = `<h2>欢迎您参加我的问卷调查</h2>
<p>感谢您抽出宝贵的时间参与我的调查。本问卷调查是Zhong在早稻田大学大学院·基干理工学研究科 情报理工・情报通信专攻的修士毕业论文的一部分。为保证您的浏览体验，请您尽量使用PC/iPad等宽屏设备进行查看，感谢您的支持！</p>
<h3>问卷简介</h3>
<p>本次调查旨在收集您对SIMD（单指令·多数据）以及信息可视化方面的认知。或许您对于这些概念十分陌生，但是不必担心，您不必为此问卷调查学习任何新的知识或了解任何专用术语，只需在您的认知范围内填写即可。由于本研究涉及编程可视化及编程教育，所以初学者或无编程经验的者的意见通常更具有参考价值。</p>
<h3>调查过程说明</h3>
<p>问卷大约需要5～10分钟来完成，如果您是计算机专业的学生可能根据个人能力花费更多时间，感谢您的协助！所有的问题都是匿名的，您的个人信息将得到严格保密。请尽可能诚实地回答问题，没有对或错的答案。需要注意的是，您的反馈可能出现在最终的论文中，请您知悉；如果您有所顾虑或不希望自己的意见出现在公开的论文中，您可以不必填写。</p>
<h3>属于您的权利</h3>
<p>参与本次调查完全是自愿的。如果您在调查过程中感到不适或过多的专业用语让您感到困惑，您可以随时退出。</p>
<h3>感谢您的参与</h3>
<p>再次感谢您的参与，这将对我完成毕业论文有很大的帮助！如果您做好准备，请点击下方的“开始调查”按钮开始填写问卷。</p>
`

const surveyJson = {
  pages: [
    {
      name: "introduction",
      elements: [
        {
          type: "html",
          html: introduction
        }
      ]
    },
    {
      name: "page1",
      elements: [
        {
          type: "html",
          html: "<h2>个人认知</h2>本页主要调查您对计算机学科以及编程概念的认知。您不必为此调查问卷学习任何新的知识，按照您目前的认知作答即可！"
        },
        {
          type: "radiogroup",
          name: "question1",
          title: "您是否是计算机专业（包括专科、本科、研究生或博士）的学生？",
          choices: [
            "是的",
            "不是",
          ],
          isRequired: true,
        },
        {
          type: "radiogroup",
          name: "question2",
          title: "您是否在任何学习阶段进行过编程的学习或参与过学校的编程课程？（只要您参加了课程，即使您没有通过该学科的最终测试，您也应当选择“参加过”）",
          choices: [
            "参加过学校的课程",
            "自学过编程",
            "没有学习过任何编程相关的知识",
          ],
          isRequired: true,
        },
        {
          type: "radiogroup",
          name: "question3",
          title: "您对于“汇编语言”的概念熟悉吗？",
          choices: [
            "很熟悉",
            "曾经详细了解过，但记不清了",
            "听说过，但没有深入了解",
            "完全不了解",
          ],
          isRequired: true,
        },
        {
          type: "radiogroup",
          name: "question4",
          title: "您对于“SIMD（单指令·多数据）”的概念熟悉吗？",
          choices: [
            "很熟悉",
            "曾经详细了解过，但记不清了",
            "听说过，但没有深入了解",
            "完全不了解",
          ],
          isRequired: true,
        },
        {
          type: "radiogroup",
          name: "question5",
          title: "您是否了解过可视化在编程领域的应用？提示：包括可视化的编程教学软件（如苹果的Playground、Scratch等）和专业的可视化编程软件（如Unity和虚幻引擎提供的可视化编程功能等）",
          choices: [
            "很熟悉，使用过相关的软件",
            "听说过，但没有使用过",
            "没有听说过，也没有使用过",
          ],
          isRequired: true,
        }
      ]
    },
    {
      name: "page2",
      elements: [
        {
          type: "html",
          html: "<h2>代码识别-C语言</h2>本页主要调查您对C语言代码的认知，难度由低至高。如果本页的内容让您感到困惑，您不必为此调查问卷学习任何新的知识或了解相关语言，按照您目前的认知作答即可；如果您曾编写过代码或者是计算机专业的学生，请您尽力了解代码的含义，在此阶段您可以借助互联网进行相关文档的查询，但请不要借助大语言模型来辅助理解，谢谢您的配合！"
        },
        {
          type: "html",
          html: `<h3>关于如何回答问题</h3>num1、num2和result中各保存了【1】个数字，您应当尝试回答出它们之中保存的数字是什么。`
        },
        {
          type: "html",
          html: `<h4>代码片段1</h4>
<pre><code>
#include &lt;stdio.h&gt;
int main() {
    int num1 = 6, num2 = 8;
    int result = num1 + num2;
    // 此时result中存储了什么值？
    // 以下为输出，无需您理解
    printf("%d\\n", result);
    return 0;
}
</code></pre>
`
        },
        {
          type: "radiogroup",
          name: "question6",
          title: "您能够理解上面C语言[代码片段1]吗？提示：您知道result最终输出为什么值吗？并且能够明白该值是如何计算得来的吗？",
          choices: [
            "能理解，很简单",
            "能理解，但查阅了相关文档",
            "即使查阅了相关文档，也只能知道大概含义，不能解释所有语句",
            "虽然没有专业背景，但是我能够猜到大概的意思",
            "完全不理解",
          ],
          isRequired: true,
        },
        {
          type: "html",
          html: `<h3>关于如何回答问题</h3>array1、array2和array3中各保存了【4】个数字，您应当尝试回答出它们之中保存的数字分别是哪四个数字。`
        },
        {
          type: "html",
          html: `<h4>代码片段2</h4>
<pre><code>
#include &lt;stdio.h&gt;
int main() {
    double array1[] = {1.0, 2.0, 3.0, 4.0};
    double array2[] = {5.0, 6.0, 7.0, 8.0};
    double array3[4];
    for (int i = 0; i < 4; ++i) {
        array3[i] = array1[i] + array2[i];
    }
    // 此时array3中存储了什么值？
    // 以下为输出，无需您理解
    for (int i = 0; i < 4; ++i) {
        printf("%lf\\n", array3[i]);
    }
    return 0;
}
</code></pre>
`
        },
        {
          type: "radiogroup",
          name: "question7",
          title: "您能够理解上面C语言[代码片段2]吗？提示：您知道array3最终输出为什么值吗？并且能够明白该值是如何计算得来的吗？",
          choices: [
            "能理解，很简单",
            "能理解，但查阅了相关文档",
            "即使查阅了相关文档，也只能知道大概含义，不能解释所有语句",
            "虽然没有专业背景，但是我能够猜到大概的意思",
            "完全不理解",
          ],
          isRequired: true,
        },
        {
          type: "html",
          html: `<h4>代码片段3</h4>
<pre><code>
#include &lt;stdio.h&gt;
#include &lt;immintrin.h&gt;
int main() {
    __m256d array1 = _mm256_setr_pd(1.0, 2.0, 3.0, 4.0);
    __m256d array2 = _mm256_setr_pd(5.0, 6.0, 7.0, 8.0);
    __m256d array3 = _mm256_add_pd(array1, array2);
    // 此时array3中存储了什么值？
    // 以下为输出，无需您理解
    double* res = (double*)\&array3;
    for (int i = 0; i < 4; ++i) {
        printf("%lf\\n", res[i]);
    }
    return 0;
}
</code></pre>
`
        },
        {
          type: "radiogroup",
          name: "question8",
          title: "您能够理解上面C语言[代码片段3]中_mm256_add_pd函数进行了什么操作吗？提示：您知道array3最终输出为什么值吗？并且能够明白该值是如何计算得来的吗？",
          choices: [
            "能理解，很简单",
            "能理解，但查阅了相关文档",
            "即使查阅了相关文档，也只能知道大概含义，不能解释所有语句",
            "虽然没有专业背景，但是我能够猜到大概的意思",
            "完全不理解",
          ],
          isRequired: true,
        },
        {
          type: "html",
          html: `<h4>代码片段4</h4>
<pre><code>
#include &lt;stdio.h&gt;
#include &lt;immintrin.h&gt;
int main() {
    __m256d array1 = _mm256_setr_pd(1.0, 2.0, 3.0, 4.0);
    __m256d array2 = _mm256_setr_pd(5.0, 6.0, 7.0, 8.0);
    __m256d array3 = _mm256_permute2f128_pd(array1, array2, 0x21);
    // 此时array3中存储了什么值？
    // 以下为输出，无需您理解
    double* res = (double*)\&array3;
    for (int i = 0; i < 4; ++i) {
        printf("%lf\\n", res[i]);
    }
    return 0;
}
</code></pre>
`
        },
        {
          type: "radiogroup",
          name: "question9",
          title: "您能够理解上面C语言[代码片段4]中_mm256_permute2f128_pd函数进行了什么操作吗？提示：您知道array3最终输出为什么值吗？并且能够明白该值是如何计算得来的吗？",
          choices: [
            "能理解，很简单",
            "能理解，但查阅了相关文档",
            "即使查阅了相关文档，也只能知道大概含义，不能解释所有语句",
            "虽然没有专业背景，但是我能够猜到大概的意思",
            "完全不理解",
          ],
          isRequired: true,
        },
      ]
    },
    {
      name: "page3",
      elements: [
        {
          type: "html",
          html: "<h2>代码识别-汇编语言</h2>本页主要调查您对汇编语言代码的认知，难度均较高。如果本页的内容让您感到困惑，您不必为此调查问卷学习任何新的知识或了解相关语言，按照您目前的认知作答即可；如果您曾接触过汇编语言或是想挑战自己的计算专业学生，请您尽力了解代码的含义，在此阶段您可以借助互联网进行相关文档的查询，但请不要借助大语言模型来辅助理解，谢谢您的配合！"
        },
        {
          type: "html",
          html: `<h3>关于如何回答问题</h3>ymm0、ymm1和ymm2中各保存了【4】个数字，您应当尝试回答出它们之中保存的数字分别是哪四个数字。`
        },
        {
          type: "html",
          html: `<h4>代码片段5</h4>
<pre><code>
section .data
array1 dq 1.0, 2.0, 3.0, 4.0
array2 dq 5.0, 6.0, 7.0, 8.0
array3 dq 0.0, 0.0, 0.0, 0.0

section .text
global _start
_start:
    vmovapd ymm0, [array1]
    vmovapd ymm1, [array2]
    vaddpd ymm2, ymm0, ymm1 ; 此处进行了什么操作？
    vmovapd [array3], ymm2
    ; 此时ymm0，ymm1，ymm2寄存器中分别存储了什么数据？
    ; 以下为exit系统调用，无需您理解
    xor rdi, rdi
    mov rax, 60
    syscall
</code></pre>
`
        },
        {
          type: "radiogroup",
          name: "question10",
          title: "您能够理解上面汇编语言[代码片段5]中vaddpd指令执行了什么操作吗？提示：您知道ymm0、ymm1和ymm2寄存器最终为什么值吗？并且能够明白该值是如何计算得来的吗？",
          choices: [
            "能理解，很简单",
            "能理解，但查阅了相关文档",
            "即使查阅了相关文档，也只能知道大概含义，不能解释所有语句",
            "虽然没有专业背景，但是我能够猜到大概的意思",
            "完全不理解",
          ],
          isRequired: true,
        },
        {
          type: "html",
          html: `<h4>代码片段6</h4>
<pre><code>
section .data
array1 dq 1.0, 2.0, 3.0, 4.0
array2 dq 5.0, 6.0, 7.0, 8.0
array3 dq 0.0, 0.0, 0.0, 0.0

section .text
global _start
_start:
    vmovapd ymm0, [array1]
    vmovapd ymm1, [array2]
    vperm2f128 ymm2, ymm0, ymm1, 0x21 ; 此处进行了什么操作？
    vmovapd [array3], ymm2
    ; 此时ymm0，ymm1，ymm2寄存器中分别存储了什么数据？
    ; 以下为exit系统调用，无需您理解
    xor rdi, rdi
    mov rax, 60
    syscall
</code></pre>
`
        },
        {
          type: "radiogroup",
          name: "question11",
          title: "您能够理解上面汇编语言[代码片段6]中vperm2f128指令执行了什么操作吗？提示：您知道ymm0、ymm1和ymm2寄存器最终为什么值吗？并且能够明白该值是如何计算得来的吗？",
          choices: [
            "能理解，很简单",
            "能理解，但查阅了相关文档",
            "即使查阅了相关文档，也只能知道大概含义，不能解释所有语句",
            "虽然没有专业背景，但是我能够猜到大概的意思",
            "完全不理解",
          ],
          isRequired: true,
        },
      ]
    },
    {
      name: "page4",
      elements: [
        {
          type: "html",
          html: "<h2>静态可视化</h2>本页使用静态可视化针对第三页的汇编代码中设问的指令进行了解释，请您尝试理解可视化内容，并思考下面的问题。如果前两页的代码让您感到困惑，请不要灰心，该页的内容本质与编程语言均无联系，在本页的回答中您作为初学者或新手给出的答案将更具参考价值，非常感谢您的耐心！"
        },
        {
          type: "html",
          html: `<h3>关于如何回答问题</h3>ymm0、ymm1和ymm2中各保存了【4】个数字，您应当尝试回答出它们之中保存的数字分别是哪四个数字。例如，在下面的图形中，ymm0保存了数字2.0, 4.0, 6.0, 8.0。<img src="/survey/v.svg" alt="V" style="width: 90%;">`
        },
        {
          type: "html",
          html: `<h4>代码片段5</h4>
<pre><code>
section .data
array1 dq 1.0, 2.0, 3.0, 4.0
array2 dq 5.0, 6.0, 7.0, 8.0
array3 dq 0.0, 0.0, 0.0, 0.0

section .text
global _start
_start:
    vmovapd ymm0, [array1]
    vmovapd ymm1, [array2]
    vaddpd ymm2, ymm0, ymm1 ; 此处进行了什么操作？
    vmovapd [array3], ymm2
    ; 此时ymm0，ymm1，ymm2寄存器中分别存储了什么数据？
    ; 以下为exit系统调用，无需您理解
    xor rdi, rdi
    mov rax, 60
    syscall
</code></pre>
`
        },
        {
          type: "html",
          html: `<h4>代码片段5的静态可视化</h4><img src="/survey/v1.svg" alt="V1" style="width: 90%;">`
        },
        {
          type: "radiogroup",
          name: "question12",
          title: "上述的静态可视化通过图片的形式对汇编语言[代码片段5]进行了解释。您不必理解什么是寄存器（把他们理解为一个名称即可），根据可视化结果，您知道ymm0、ymm1和ymm2寄存器最终为什么值吗？并且能够明白该值是如何计算得来的吗？",
          choices: [
            "即使没有可视化我已经理解了该代码片段，可视化对我没有任何作用",
            "即使没有可视化我已经理解了该代码片段，但是可视化对我的理解有帮助",
            "看代码片段我只能理解部分代码或猜测代码行为，可视化帮助我理解了ymm0、ymm1和ymm2的结果是如何得出的",
            "看代码片段我完全无法理解代码，可视化帮助我理解了ymm0、ymm1和ymm2的结果是如何得出的",
            "即便有了可视化，我依然不理解ymm0、ymm1和ymm2的结果是什么以及它们是如何得出的",
          ],
          isRequired: true,
        },
        {
          type: "html",
          html: `<h4>代码片段6</h4>
<pre><code>
section .data
array1 dq 1.0, 2.0, 3.0, 4.0
array2 dq 5.0, 6.0, 7.0, 8.0
array3 dq 0.0, 0.0, 0.0, 0.0

section .text
global _start
_start:
    vmovapd ymm0, [array1]
    vmovapd ymm1, [array2]
    vperm2f128 ymm2, ymm0, ymm1, 0x21 ; 此处进行了什么操作？
    vmovapd [array3], ymm2
    ; 此时ymm0，ymm1，ymm2寄存器中分别存储了什么数据？
    ; 以下为exit系统调用，无需您理解
    xor rdi, rdi
    mov rax, 60
    syscall
</code></pre>
`
        },
        {
          type: "html",
          html: `<h4>代码片段6的静态可视化</h4><img src="/survey/v2.svg" alt="V2" style="width: 90%;">`
        },
        {
          type: "radiogroup",
          name: "question13",
          title: "上述的静态可视化通过图片的形式对汇编语言[代码片段6]进行了解释。您不必理解什么是寄存器（把他们理解为一个名称即可），根据可视化结果，您知道ymm0、ymm1和ymm2寄存器最终为什么值吗？并且能够明白该值是如何计算得来的吗？",
          choices: [
            "即使没有可视化我已经理解了该代码片段，可视化对我没有任何作用",
            "即使没有可视化我已经理解了该代码片段，但是可视化对我的理解有帮助",
            "看代码片段我只能理解部分代码或猜测代码行为，可视化帮助我理解了ymm0、ymm1和ymm2的结果是如何得出的",
            "看代码片段我完全无法理解代码，可视化帮助我理解了ymm0、ymm1和ymm2的结果是如何得出的",
            "即便有了可视化，我依然不理解ymm0、ymm1和ymm2的结果是什么以及它们是如何得出的",
          ],
          isRequired: true,
        },
      ]
    },
    {
      name: "page5",
      elements: [
        {
          type: "html",
          html: "<h2>动态可视化</h2>本页使用动态可视化针对第三页的汇编代码中设问的指令进行了解释，请您多次播放动画、尝试理解可视化内容，并思考下面的问题。如果第二页和第三页的代码让您感到困惑，请不要灰心，该页的内容本质与编程语言均无联系，在本页的回答中您作为初学者或新手给出的答案将更具参考价值，非常感谢您的耐心！"
        },
        {
          type: "html",
          html: `<h3>关于如何回答问题</h3>ymm0、ymm1和ymm2中各保存了【4】个数字，您应当尝试回答出它们之中保存的数字分别是哪四个数字。例如，在下面的图形中，ymm0保存了数字2.0, 4.0, 6.0, 8.0。<img src="/survey/v.svg" alt="V" style="width: 90%;">`
        },
        {
          type: "html",
          html: `<h4>代码片段5</h4>
<pre><code>
section .data
array1 dq 1.0, 2.0, 3.0, 4.0
array2 dq 5.0, 6.0, 7.0, 8.0
array3 dq 0.0, 0.0, 0.0, 0.0

section .text
global _start
_start:
    vmovapd ymm0, [array1]
    vmovapd ymm1, [array2]
    vaddpd ymm2, ymm0, ymm1 ; 此处进行了什么操作？
    vmovapd [array3], ymm2
    ; 此时ymm0，ymm1，ymm2寄存器中分别存储了什么数据？
    ; 以下为exit系统调用，无需您理解
    xor rdi, rdi
    mov rax, 60
    syscall
</code></pre>
`
        },
        {
          type: "html",
          html: `<h4>代码片段5的动态可视化（循环播放）</h4><img src="/survey/dv1.gif" alt="DV1" style="width: 90%;">`
        },
        {
          type: "radiogroup",
          name: "question14",
          title: "上述的动态可视化通过动画的形式对汇编语言[代码片段5]进行了解释。您不必理解什么是寄存器（把他们理解为一个名称即可），根据可视化结果，您知道ymm0、ymm1和ymm2寄存器最终为什么值吗？并且能够明白该值是如何计算得来的吗？",
          choices: [
            "即使没有可视化我已经理解了该代码片段，可视化对我没有任何作用",
            "即使没有可视化我已经理解了该代码片段，但是可视化对我的理解有帮助",
            "看代码片段我只能理解部分代码或猜测代码行为，可视化帮助我理解了ymm0、ymm1和ymm2的结果是如何得出的",
            "看代码片段我完全无法理解代码，可视化帮助我理解了ymm0、ymm1和ymm2的结果是如何得出的",
            "即便有了可视化，我依然不理解ymm0、ymm1和ymm2的结果是什么以及它们是如何得出的",
          ],
          isRequired: true,
        },
        {
          type: "html",
          html: `<h4>代码片段6</h4>
<pre><code>
section .data
array1 dq 1.0, 2.0, 3.0, 4.0
array2 dq 5.0, 6.0, 7.0, 8.0
array3 dq 0.0, 0.0, 0.0, 0.0

section .text
global _start
_start:
    vmovapd ymm0, [array1]
    vmovapd ymm1, [array2]
    vperm2f128 ymm2, ymm0, ymm1, 0x21 ; 此处进行了什么操作？
    vmovapd [array3], ymm2
    ; 此时ymm0，ymm1，ymm2寄存器中分别存储了什么数据？
    ; 以下为exit系统调用，无需您理解
    xor rdi, rdi
    mov rax, 60
    syscall
</code></pre>
`
        },
        {
          type: "html",
          // TODO
          html: `<h4>代码片段6的动态可视化（循环播放）</h4><img src="/survey/dv2.gif" alt="DV2" style="width: 90%;">`
        },
        {
          type: "radiogroup",
          name: "question15",
          title: "上述的动态可视化通过动画的形式对汇编语言[代码片段6]进行了解释。您不必理解什么是寄存器（把他们理解为一个名称即可），根据可视化结果，您知道ymm0、ymm1和ymm2寄存器最终为什么值吗？并且能够明白该值是如何计算得来的吗？",
          choices: [
            "即使没有可视化我已经理解了该代码片段，可视化对我没有任何作用",
            "即使没有可视化我已经理解了该代码片段，但是可视化对我的理解有帮助",
            "看代码片段我只能理解部分代码或猜测代码行为，可视化帮助我理解了ymm0、ymm1和ymm2的结果是如何得出的",
            "看代码片段我完全无法理解代码，可视化帮助我理解了ymm0、ymm1和ymm2的结果是如何得出的",
            "即便有了可视化，我依然不理解ymm0、ymm1和ymm2的结果是什么以及它们是如何得出的",
          ],
          isRequired: true,
        },
      ]
    },
    {
      name: "page6",
      elements: [
        {
          type: "html",
          html: "<h2>总结</h2>本页对前几页的问题进行总结，非常感谢您能够阅读到这里！"
        },
        {
          type: "radiogroup",
          name: "question16",
          title: "例题中的代码片段3～6均使用了SIMD计算，即在单条指令中同时处理多个数据（如：进行批量计算或对数据进行混排等），您在理解这些代码的时候是否感到比理解非SIMD代码更有挑战？例如您可以想像以下场景：计算1, 2, 3与7, 8, 9分别对应项相乘后的结果，非SIMD计算会分别计算1*7, 2*8, 3*9，而SIMD计算会在同时计算三个乘法。",
          choices: [
            "理解SIMD计算对我来讲更有挑战",
            "理解非SIMD计算对我来讲更有挑战",
            "二者对我来讲没有任何区别",
            "我没有接触过编程，但我认为SIMD计算更难",
            "我没有接触过编程，但我认为非SIMD计算更难",
            "我没有接触过编程，但我认为它们二者没有区别",
          ],
          isRequired: true,
        },
        {
          type: "radiogroup",
          name: "question17",
          title: "您认为，通过图片或动画而不是代码是否会帮助您理解编程语言代码的具体含义？",
          choices: [
            "可视化能辅助我更快的把握代码的含义",
            "可视化对于我理解代码没有任何帮助",
            "我没接触过编程，但是通过可视化我理解了本问卷中的例题",
            "我没接触过编程，通过可视化我仍然没有理解了本问卷中的例题",
          ],
          isRequired: true,
        },
        {
          type: "radiogroup",
          name: "question18",
          title: "您认为，通过图片或动画而不是代码是否会帮助您理解SIMD计算的过程（即本问卷中展示的例题）？",
          choices: [
            "可视化能辅助我更快的把握代码的含义",
            "可视化对于我理解代码没有任何帮助",
            "我没接触过编程，但是通过可视化我理解了本问卷中的例题",
            "我没接触过编程，通过可视化我仍然没有理解了本问卷中的例题",
          ],
          isRequired: true,
        },
        {
          type: "radiogroup",
          name: "question19",
          title: "对于【简单】代码或您【已经完全掌握】的用法：纯代码、静态可视化（图片）和动态可视化（动画）相比，下面的哪个描述与您的想法最为贴近？",
          choices: [
            "阅读纯代码最有助于我理解代码的含义",
            "静态可视化最有助于我理解代码的含义",
            "动态可视化最有助于我理解代码的含义",
          ],
          isRequired: true,
        },
        {
          type: "radiogroup",
          name: "question20",
          title: "对于【复杂】代码或您【没有完全掌握】的用法：纯代码、静态可视化（图片）和动态可视化（动画）相比，下面的哪个描述与您的想法最为贴近？",
          choices: [
            "阅读纯代码最有助于我理解代码的含义",
            "静态可视化最有助于我理解代码的含义",
            "动态可视化最有助于我理解代码的含义",
          ],
          isRequired: true,
        },
        {
          type: "comment",
          name: "question21",
          title: "【可选】如果您是计算机专业的学生或计算机领域的从业人员，请您写下您对于“可视化”的理解或者您对于“可视化能否在编程领域辅助程序员进行思考”的理解；如果您没有接触过编程，请您针对“可视化能否辅助人类对于抽象问题的思考”发表见解。再次感谢您的配合！",
        },
      ]
    }
  ],
  showProgressBar: "top",
  firstPageIsStarted: true,
  startSurveyText: "开始调查",
  pageNextText: "下一页",
  pagePrevText: "上一页",
  completeText: "提交"
}

const survey = new Model(surveyJson)
survey.onComplete.add((sender) => {
  saveSurveyResults(
    "https://ch.gabzhong.dev/survey-data",
    sender.data
  )
})

const saveSurveyResults = (url, json) => {
  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json;charset=UTF-8'
    },
    body: JSON.stringify(json)
  })
  .then(response => {
    if (response.ok) {
      //
    } else {
      ElMessageBox.alert('服务器错误！' + '\n请您检查网络连接后尝试重新填写问卷，十分抱歉！', '错误', {
        confirmButtonText: '好',
        callback: () => {},
      })
    }
  })
  .catch(error => {
    ElMessageBox.alert('错误: ' + error + '\n请您尝试重新填写问卷，十分抱歉！', '错误', {
      confirmButtonText: '好',
      callback: () => {},
    })
  })
}
</script>

<template>
  <el-container>
    <el-header height="80px"><h1>{{ msg }}</h1></el-header>
    <el-main><SurveyComponent :model="survey" /></el-main>
    <el-footer>
      <div style="text-align: center;">
        本问卷由 Vue3 + SurveyJS + ElementPlus 制作
      </div>
    </el-footer>
  </el-container>
</template>

<style scoped>
</style>
