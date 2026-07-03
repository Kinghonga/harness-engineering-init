# harness-engineering-init

让 AI Agent 的 harness engineering 真正"跑起来"的标准 skill。

## 为什么

大多数 harness 死于同一原因：结构搭好了，"记录半"（检查点 / 失败轨迹）勉强手动跑，而"进化半"（轨迹 → Critic 分析 → 失败模式 → 规则更新）一次都没跑。这个 skill 把进化半当作重点，用健康检查让沉默失败可见，并诚实标注各平台触发能力的上限。

核心理念：**init 是 5 分钟，让 loop 活着才是活。**

## 安装

把本目录拷到你的 AI 客户端 skills 目录：

```bash
# opencode
cp -r harness-engineering-init ~/.config/opencode/skills/

# Claude Code
cp -r harness-engineering-init ~/.claude/skills/
```

## 用法

安装后，对 agent 说 "harness"、"检查 harness"、"搭一下 harness engineering" 等即可触发。skill 会按阶段引导：

1. **健康检查**（只读）— loop 是否还活着
2. **Init** — 仅在 `.harness/` 不存在时脚手架
3. **检查点** — 任务开始时记录
4. **验证 + 轨迹 + 基线** — 失败时记录，首次记基线只看 delta
5. **Critic** — 分析轨迹 → 失败模式（通常死掉的那半）★
6. **进化** — 成功 3 次的流程编译成脚本

## 文件

| 文件 | 作用 |
|---|---|
| `SKILL.md` | 主工作流（frontmatter + 阶段化指令） |
| `TEMPLATES.md` | 检查点 / 轨迹 / 失败模式 / 记忆 / 基线 模板 |
| `PLATFORMS.md` | 各平台触发器 + 能力天花板 |

## 平台说明

loop 逻辑在任何能读写文件的 agent 上可用。自动触发取决于平台能力，天花板不等（Claude Code > opencode > 无 hook 工具）。不承诺跨平台同等确定性，详见 `PLATFORMS.md`。

## 许可

MIT
