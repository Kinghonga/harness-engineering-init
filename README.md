[English](#english) | [中文](#中文)

![tests](https://github.com/Kinghonga/harness-engineering-init/actions/workflows/test.yml/badge.svg)
![license](https://img.shields.io/badge/license-MIT-blue)
![standard](https://img.shields.io/badge/agent--skills-standard-7b1fa2)

---

<a id="english"></a>

# harness-engineering-init

> Adopt and sustain the harness-engineering paradigm on any AI coding project.

A standard agent skill that scaffolds the `.harness/` loop, keeps it alive with a read-only health check, and makes it self-improving — so agent engineering stays on track instead of drifting. **Init is five minutes; keeping the loop alive is the job.**

## What is harness engineering?

It's the practice of encoding a project's architecture constraints, conventions, and verification gates into the repo itself — an `AGENTS.md` entry point, a `.harness/` memory store, and pre-verification checks — so an AI coding agent works reliably from what it can **see and verify**, not what it **remembers**. The aim is a self-improving loop: every failure is recorded, analyzed into a pattern, and fed back as a rule, so the next agent inherits the lessons.

## What it does

- **Health check** ★ — one read-only pass tells you whether the loop is alive or silently dead. Most harness skills scaffold and never look back; this one does.
- **Init** — scaffolds `.harness/` (checkpoints, traces, memory) only when absent; never re-scaffolds an existing one
- **Checkpoints & traces** — records task starts and failure post-mortems with root cause and fix
- **Baseline-aware verification** — captures the pre-existing violation count once, then treats only deltas as signal, so old debt doesn't drown new work
- **Critic** — analyzes failure traces into reusable failure-pattern memory and proposes rule updates; this is the learning step teams most often skip
- **Evolve** — compiles workflows that succeed 3+ times into deterministic scripts

## Project layout

After init, your project gains a `.harness/` directory alongside `AGENTS.md`:

```
your-project/
├── AGENTS.md              # entry point — points agents to .harness/
└── .harness/
    ├── baseline.json      # snapshot of pre-existing violations; only deltas count as signal
    ├── tasks/             # task checkpoints — what was done, decided, verified
    │   └── {name}-{date}.md
    ├── trace/             # failure post-mortems — error, root cause, fix
    │   └── failure-{type}-{date}.md
    └── memory/
        ├── episodic/      # one-off lessons ("this bit us once")
        ├── failures/      # Critic output — recurring failure patterns + rule proposals
        │   └── {pattern}.md
        └── procedural/    # repeatable workflows compiled into scripts
```

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

Say **"check harness"**, **"set up harness engineering"**, or just **"harness"**. The skill auto-loads on any matching task and walks the agent through:

```
health check → init → checkpoint → verify+trace+baseline → Critic → evolve
  (read-only)  (if absent) (task start)    (on failure)        (self-improve)
```

## How it works

The loop logic runs on any agent that reads/writes files. **Auto-firing** it depends on platform hooks, and ceilings differ — Claude Code (force-resume) > opencode (file-change detect) > Trae/Codex (soft). No false promises of uniform determinism. See [PLATFORMS.md](PLATFORMS.md).

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | Main workflow — frontmatter + phased instructions |
| `TEMPLATES.md` | Checkpoint / trace / failure-pattern / memory / baseline templates |
| `PLATFORMS.md` | Per-platform triggers & capability ceilings |

## License

MIT

---

<a id="中文"></a>

# harness-engineering-init

> 在任意 AI 编码项目上落地并持续运转 harness engineering 范式。

一个标准 agent skill，搭起 `.harness/` 循环、用只读健康检查让它活着、并自我改进——让 agent 工程不跑偏，而非随性漂移。**init 是 5 分钟，让 loop 活着才是活。**

## 什么是 harness engineering？

把项目的架构约束、规范和验证闸门编码进仓库的实践——一个 `AGENTS.md` 入口、一个 `.harness/` 记忆存储、一套预验证检查——让 AI 编码 agent 靠**看见与验证**可靠工作，而非靠**记忆**。目标是自我改进的循环：每次失败被记录、分析成模式、回写为规则，下一个 agent 继承这些教训。

## 它做什么

- **健康检查** ★——一次只读扫描告诉你循环是活着还是已沉默死亡。多数 harness skill 搭完就不再回头看；这个会。
- **Init**——仅在不存在时脚手架 `.harness/`（检查点、轨迹、记忆）；已有的不重复建
- **检查点与轨迹**——记录任务起点，以及失败复盘（含根因与修复）
- **基线感知验证**——首次记下既有违规数，之后只把增量当信号，老债务不淹没新改动
- **Critic**——把失败轨迹分析成可复用的失败模式记忆，并提议规则更新；这是团队最常跳过的“学习”步骤
- **进化**——成功 3 次以上的流程编译成确定性脚本

## 项目布局

init 之后，你的项目会在 `AGENTS.md` 旁多出一个 `.harness/` 目录：

```
your-project/
├── AGENTS.md              # 入口 — 指向 .harness/
└── .harness/
    ├── baseline.json      # 既有违规快照；只把增量当信号
    ├── tasks/             # 任务检查点 — 做了什么、决策、验证结果
    │   └── {name}-{date}.md
    ├── trace/             # 失败复盘 — 错误、根因、修复
    │   └── failure-{type}-{date}.md
    └── memory/
        ├── episodic/      # 一次性教训（“这个坑过一次”）
        ├── failures/      # Critic 产出 — 反复出现的失败模式 + 规则提议
        │   └── {pattern}.md
        └── procedural/    # 编译成脚本的可复用流程
```

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

说 **"检查 harness"**、**"搭一下 harness engineering"** 或 **"harness"**。skill 在匹配的任务上自动加载，引导 agent 走完：

```
健康检查 → init → 检查点 → 验证+轨迹+基线 → Critic → 进化
 (只读)   (无则建) (任务起)    (失败时)        (自我改进)
```

## 工作原理

loop 逻辑在任何能读写文件的 agent 上可用。**自动触发**取决于平台 hook，天花板不等——Claude Code（强制 resume）> opencode（文件变动检测）> Trae/Codex（软触发）。不虚假承诺跨平台同等确定性。见 [PLATFORMS.md](PLATFORMS.md)。

## 文件

| 文件 | 作用 |
|---|---|
| `SKILL.md` | 主工作流 — frontmatter + 阶段化指令 |
| `TEMPLATES.md` | 检查点 / 轨迹 / 失败模式 / 记忆 / 基线 模板 |
| `PLATFORMS.md` | 各平台触发器 + 能力天花板 |

## 许可

MIT
