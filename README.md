[English](#english) | [中文](#中文)

![tests](https://github.com/Kinghonga/harness-engineering-init/actions/workflows/test.yml/badge.svg)
![license](https://img.shields.io/badge/license-MIT-blue)
![standard](https://img.shields.io/badge/agent--skills-standard-7b1fa2)

---

<a id="english"></a>

# harness-engineering-init

> Adopt and sustain the harness-engineering paradigm on any project.

A standard agent skill that helps you establish the `.harness/` loop, keep it alive with a read-only health check, and make it self-improving — so AI agent engineering stays on track instead of drifting.

## The problem

Teams set up AI-agent harnesses (`.harness/` with checkpoints, traces, memory) expecting the agent to learn from failures. Reality: the **recording half** (checkpoints + traces) limps along manually, while the **evolution half** (traces → Critic analysis → failure patterns → rule updates) **never runs once**. The harness becomes a beautiful graveyard — structure without a pulse. And because nothing reports its health, the failure is **silent**.

This skill fixes exactly that:

- Makes a dead loop **visible** (read-only health check)
- Treats the evolution half as **the point**, not an afterthought
- Is **honest** about what each agent platform can auto-enforce

**Core idea: init is five minutes. Keeping the loop alive is the job.**

## What it does

```
health check → init → checkpoint → verify+trace+baseline → Critic ★ → evolve
  (read-only)  (if absent) (task start)    (on failure)       (the part that dies)
```

1. **Health check** — is the loop alive? (read-only, run freely)
2. **Init** — scaffold `.harness/` only if absent
3. **Checkpoint** — record when a task starts
4. **Verify + trace + baseline** — on failure, record the trace; capture a baseline the first time and treat only **deltas** as signal (pre-existing debt is noise)
5. **Critic** — analyze traces into failure patterns → propose rule updates ★
6. **Evolve** — compile repeated flows into deterministic scripts

## Install

Follows the open [Agent Skills](https://agentskills.io/specification) standard. Works on every major AI coding agent — only the directory differs:

| Platform | Global | Project |
|---|---|---|
| opencode | `~/.config/opencode/skills/` | `.agents/skills/` |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| Codex | `~/.agents/skills/` | `.agents/skills/` |
| Trae | `~/.trae/skills/` | `.trae/skills/` |

```bash
cp -r harness-engineering-init ~/.config/opencode/skills/   # opencode
cp -r harness-engineering-init ~/.claude/skills/            # Claude Code
cp -r harness-engineering-init ~/.agents/skills/            # Codex
cp -r harness-engineering-init ~/.trae/skills/              # Trae
```

`.agents/skills/` is the cross-platform project-level standard dir — Codex and opencode read it natively, Trae supports it via a settings toggle.

## Usage

Say **"check harness"**, **"set up harness engineering"**, or just **"harness"**. The skill auto-loads on any task matching its description and walks the agent through the phases above.

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | Main workflow — frontmatter + phased instructions |
| `TEMPLATES.md` | Checkpoint / trace / failure-pattern / memory / baseline templates |
| `PLATFORMS.md` | Per-platform triggers & honest capability ceilings |

## Platform honesty

The loop logic runs on any agent that reads/writes files. **Auto-firing** it depends on platform hooks, and ceilings differ — Claude Code (force-resume) > opencode (file-change detect) > Trae/Codex (soft). No false promises of uniform determinism. See `PLATFORMS.md`.

## License

MIT

---

<a id="中文"></a>

# harness-engineering-init

> 在任意项目上落地并持续运转 harness engineering 范式。

一个标准 agent skill，帮你建立 `.harness/` 循环、用只读健康检查让它活着、并自我改进——让 AI agent 工程不跑偏，而非随性漂移。

## 问题在哪

团队给 AI agent 搭 harness（`.harness/` 含检查点、轨迹、记忆），指望 agent 从失败中学习。现实是：**记录半**（检查点+轨迹）勉强手动跑，而**进化半**（轨迹→Critic 分析→失败模式→规则更新）**一次都没跑**。harness 沦为漂亮的坟墓——有骨架没脉搏。而且没人报告它的健康，失败是**沉默的**。

这个 skill 正是修这个：

- 让死循环**可见**（只读健康检查）
- 把进化半当作**重点**，不是事后补丁
- **诚实**标注每个平台能自动强制到什么程度

**核心理念：init 是 5 分钟，让 loop 活着才是活。**

## 它做什么

```
健康检查 → init → 检查点 → 验证+轨迹+基线 → Critic ★ → 进化
 (只读)   (无则建) (任务起)    (失败时)      (会死的那半)
```

1. **健康检查** — loop 是否活着？（只读，随便跑）
2. **Init** — 仅 `.harness/` 不存在时脚手架
3. **检查点** — 任务开始时记录
4. **验证+轨迹+基线** — 失败时记轨迹；首次记基线，之后只把 **delta** 当信号（既有债务是噪声）
5. **Critic** — 把轨迹分析成失败模式 → 提议规则更新 ★
6. **进化** — 重复流程编译成确定性脚本

## 安装

采用开放 [Agent Skills](https://agentskills.io/specification) 标准。各大 agent 通用，只差目录：

| 平台 | 全局 | 项目级 |
|---|---|---|
| opencode | `~/.config/opencode/skills/` | `.agents/skills/` |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| Codex | `~/.agents/skills/` | `.agents/skills/` |
| Trae | `~/.trae/skills/` | `.trae/skills/` |

```bash
cp -r harness-engineering-init ~/.config/opencode/skills/   # opencode
cp -r harness-engineering-init ~/.claude/skills/            # Claude Code
cp -r harness-engineering-init ~/.agents/skills/            # Codex
cp -r harness-engineering-init ~/.trae/skills/              # Trae
```

`.agents/skills/` 是跨平台项目级标准目录——Codex 和 opencode 原生读取，Trae 可通过设置开关启用。

## 用法

说 **"检查 harness"**、**"搭一下 harness engineering"** 或 **"harness"**。skill 在匹配的任务上自动加载，引导 agent 走完上述阶段。

## 文件

| 文件 | 作用 |
|---|---|
| `SKILL.md` | 主工作流 — frontmatter + 阶段化指令 |
| `TEMPLATES.md` | 检查点 / 轨迹 / 失败模式 / 记忆 / 基线 模板 |
| `PLATFORMS.md` | 各平台触发器 + 诚实的能力天花板 |

## 平台诚实

loop 逻辑在任何能读写文件的 agent 上可用。**自动触发**取决于平台 hook，天花板不等——Claude Code（强制 resume）> opencode（文件变动检测）> Trae/Codex（软触发）。不虚假承诺跨平台同等确定性。见 `PLATFORMS.md`。

## 许可

MIT
