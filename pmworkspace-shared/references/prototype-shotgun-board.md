# Prototype Shotgun Board

Prototype Shotgun Board 用来比较多方案，但不改变 image-2 输出规则：一个方案 + 一个屏幕仍然是一张独立图片。

## 记录方式

生成或计划生成每个图片单元前，平台脚本可用时登记：

```bash
pmw-prototype-board add \
  --scheme "<方案名>" \
  --screen "<屏幕任务>" \
  --brief-version "<产品简报版本>" \
  --goal "<主目标>" \
  --anti-metric "<反指标>" \
  --non-fiction "<不可虚构项>" \
  --image "<图片路径或 URL，可为空>"
```

用户反馈后记录评分：

```bash
pmw-prototype-board score --scheme "<方案名>" --score 4 --note "<用户评论>"
```

查看比较板：

```bash
pmw-prototype-board list
```

## 方案要求

- 多方案必须在产品策略、信息架构、交互模型或信任模型上不同。
- 不把配色、插画、圆角或风格皮肤包装成多方案。
- 默认输出“方案对比表 + 单图清单”，不是拼图。
- 只有用户明确要求展示材料时，才可以额外做展示板。

