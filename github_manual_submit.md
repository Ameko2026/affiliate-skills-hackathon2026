# GitHub 手动提交指南

## 方式 1：GitHub 网页端（推荐）

### 1. 打开仓库
访问：https://github.com/Ameko2026/affiliate-skills-hackathon2026

### 2. 上传文件

#### 方法 A：拖拽上传
- 进入 `submission/` 目录
- 点击 "Add file" → "Upload files"
- 拖拽需要更新的 4 个文件到上传区域

#### 方法 B：编辑单个文件
- 进入 `submission/` 目录
- 点击要修改的文件
- 点击编辑图标（铅笔）
- 粘贴新内容
- 点击 "Commit changes"

### 3. 提交的文件清单

#### submission/ 目录（4个文件）
| 文件 | 操作 |
|------|------|
| `submission/intro_500words.md` | 覆盖更新 → 版本 v2.0 |
| `submission/ppt_deck.md` | 覆盖更新 → 版本 v7 |
| `submission/video_script.md` | 覆盖更新 → 版本 v3 |
| `submission/technical_doc.md` | 覆盖更新 → 版本 v2.0 |

#### skills/ 目录（2个新目录）
| 目录 | 操作 |
|------|------|
| `skills/partner-memory-system/` | 新建目录 + 上传 2 个文件 |
| `skills/relationship-health-score/` | 新建目录 + 上传 2 个文件 |

### 4. 新建目录

进入 `skills/` → 点击 "Add file" → "Create new file"
- 文件名：`skills/partner-memory-system/SKILL.md`
- 粘贴 `partner-memory-system/SKILL.md` 的内容
- 点击 "Commit new file"

重复以上步骤创建：
- `skills/partner-memory-system/partner_memory.py`
- `skills/relationship-health-score/SKILL.md`
- `skills/relationship-health-score/relationship_health.py`

---

## 方式 2：安装 Git 后命令行提交

### 安装 Git
1. 下载：https://git-scm.com/download/win
2. 安装时选择 "Git Bash Here" 选项

### 提交命令
```bash
# 1. 克隆仓库（如果还没有）
git clone https://github.com/Ameko2026/affiliate-skills-hackathon2026.git
cd affiliate-skills-hackathon2026

# 2. 添加所有更改
git add .

# 3. 提交
git commit -m "Add Layer 5 Skills + update submission docs (v2.0)"

# 4. 推送到 GitHub
git push origin main
```

---

## 方式 3：GitHub CLI

### 安装 GitHub CLI
```powershell
winget install GitHub.cli
```

### 提交命令
```powershell
gh auth login
gh repo clone Ameko2026/affiliate-skills-hackathon2026
cd affiliate-skills-hackathon2026
git add .
git commit -m "Add Layer 5 Skills + update submission docs"
git push
```

---

## 文件内容快速定位

### 需要更新的 submission 文件
请参考本项目中的最新文件内容：
- `affiliate-skills-hackathon2026/submission/intro_500words.md`
- `affiliate-skills-hackathon2026/submission/ppt_deck.md`
- `affiliate-skills-hackathon2026/submission/video_script.md`
- `affiliate-skills-hackathon2026/submission/technical_doc.md`

### 新增的 Layer 5 Skill 文件
- `affiliate-skills-hackathon2026/skills/partner-memory-system/SKILL.md`
- `affiliate-skills-hackathon2026/skills/partner-memory-system/partner_memory.py`
- `affiliate-skills-hackathon2026/skills/relationship-health-score/SKILL.md`
- `affiliate-skills-hackathon2026/skills/relationship-health-score/relationship_health.py`

---

## GitHub 提交 Commit Message

推荐使用以下 Commit Message：

```
Add Layer 5: AI Organization Behavior Skills

- Add partner-memory-system (10-dimension partner memory)
- Add relationship-health-score (0-100 health rating)
- Update submission docs (intro, ppt, video script, technical doc)
- Total: 14 Skills across 5 layers
```

---

*生成时间：2026-05-15*
