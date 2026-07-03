[English](#english) | [中文](#中文)

---

<a id="english"></a>

# harness-engineering-init

> A standard agent skill that makes AI-agent harness engineering actually run — not just get scaffolded.

Most harnesses die the same way: structure gets scaffolded, the "recording half" (checkpoints + failure traces) limps along manually, and the "evolution half" (traces → Critic analysis → failure patterns → rule updates) never runs once. This skill treats the evolution half as the point, makes silent failure visible, and is honest about per-platform trigger limits.

**Core idea: init is five minutes; keeping the loop alive is the job.**

## Install

The skill follows the open [Agent Skills](https://agentskills.io/specification) standard — a directory with `SKILL.md` (YAML `name` + `description` + markdown body). It works across all major AI coding agents; only the install directory differs:

| Platform | Global | Project |
|---|---|---|
| opencode | `~/.config/opencode/skills/` | `.agents/skills/` |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| Codex | `~/.agents/skills/` | `.agents/skills/` |
| Trae | `~/.trae/skills/` | `.trae/skills/` (or enable `.agents/skills/`) |

```bash
# opencode
cp -r harness-engineering-init ~/.config/opencode/skills/

# Claude Code
cp -r harness-engineering-init ~/.claude/skills/

# Codex
cp -r harness-engineering-init ~/.agents/skills/

# Trae — or import via Settings → Rules & Skills → Import File
cp -r harness-engineering-init ~/.trae/skills/
```

`.agents/skills/` is the cross-platform project-level standard dir — Codex and opencode read it natively, and Trae supports it via a settings toggle.

## Usage

Once installed, trigger it with phrases like "harness", "check harness", "set up harness engineering". The skill guides the agent through:

1. **Health check** (read-only) — is the loop alive?
2. **Init** — scaffold `.harness/` only if absent
3. **Checkpoint** — record when a task starts
4. **Verify + trace + baseline** — record on failure; capture a baseline the first time and treat only deltas as signal
5. **Critic** — analyze traces → failure patterns (the half that usually dies) ★
6. **Evolve** — compile repeated flows into scripts

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | Main workflow (frontmatter + phased instructions) |
| `TEMPLATES.md` | Checkpoint / trace / failure-pattern / memory / baseline templates |
| `PLATFORMS.md` | Per-platform triggers & capability ceilings |

## Platform note

The loop logic works on any agent that can read/write files. **Auto-firing** the loop (instead of relying on the agent remembering) depends on platform hook capability, and ceilings differ (Claude Code > opencode > Trae/Codex). The skill does not promise uniform determinism across platforms — see `PLATFORMS.md`.

## License

MIT

---

<a id="中文"></a>

# harness-engineering-init

> 一个让 AI Agent 的 harness engineering 真正"跑起来"的标准 skill。

大多数 harness 死于同一原因：结构搭好了，"记录半"（检查点 + 失败轨迹）勉强手动跑，而"进化半"（轨迹 → Critic 分析 → 失败模式 → 规则更新）一次都没跑。这个 skill 把进化半当作重点，让沉默失败可见，并诚实标注各平台触发能力的上限。

**核心理念：init 是 5 分钟，让 loop 活着才是活。**

## 安装

skill 采用开放的 [Agent Skills](https://agentskills.io/specification) 标准——一个目录 + `SKILL.md`（YAML `name` + `description` + markdown 正文）。各大 AI 编码 agent 通用，差的只是安装目录：

| 平台 | 全局 | 项目级 |
|---|---|---|
| opencode | `~/.config/opencode/skills/` | `.agents/skills/` |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| Codex | `~/.agents/skills/` | `.agents/skills/` |
| Trae | `~/.trae/skills/` | `.trae/skills/`（或启用 `.agents/skills/`） |

```bash
# opencode
cp -r harness-engineering-init ~/.config/opencode/skills/

# Claude Code
cp -r harness-engineering-init ~/.claude/skills/

# Codex
cp -r harness-engineering-init ~/.agents/skills/

# Trae —— 也可通过 设置 → Rules & Skills → Import File 导入
cp -r harness-engineering-init ~/.trae/skills/
```

`.agents/skills/` 是跨平台项目级标准目录——Codex 和 opencode 原生读取，Trae 可通过设置开关启用。

## 用法

安装后，用 "harness"、"检查 harness"、"搭一下 harness engineering" 等触发。skill 会按阶段引导：

1. **健康检查**（只读）— loop 是否还活着
2. **Init** — 仅在 `.harness/` 不存在时脚手架
3. **检查点** — 任务开始时记录
4. **验证 + 轨迹 + 基线** — 失败时记录；首次记基线，之后只把 delta 当信号
5. **Critic** — 分析轨迹 → 失败模式（通常死掉的那半）★
6. **进化** — 重复流程编译成脚本

## 文件

| 文件 | 作用 |
|---|---|
| `SKILL.md` | 主工作流（frontmatter + 阶段化指令） |
| `TEMPLATES.md` | 检查点 / 轨迹 / 失败模式 / 记忆 / 基线 模板 |
| `PLATFORMS.md` | 各平台触发器 + 能力天花板 |

## 平台说明

loop 逻辑在任何能读写文件的 agent 上可用。**自动触发**循环（而非靠 agent 记得）取决于平台 hook 能力，天花板不等（Claude Code > opencode > Trae/Codex）。skill 不承诺跨平台同等确定性——详见 `PLATFORMS.md`。

## 许可

MIT
