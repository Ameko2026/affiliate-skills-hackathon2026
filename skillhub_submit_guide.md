# SkillHub 提交指南

## 提交前准备

确保以下文件已准备就绪：

### Skill 1: partner-memory-system
```
skills/partner-memory-system/
├── SKILL.md              ✅ 已创建
└── partner_memory.py     ✅ 已创建
```

### Skill 2: relationship-health-score
```
skills/relationship-health-score/
├── SKILL.md              ✅ 已创建
└── relationship_health.py   ✅ 已创建
```

---

## 方式 1：CLI 提交（推荐）

### 步骤 1：安装 SkillHub CLI

```bash
# 如果是 OpenClaw 平台
npm install -g @openclaw/cli

# 或者使用 npx（无需安装）
npx clawhub-cli init
```

### 步骤 2：登录

```bash
clawhub login
# 按提示输入用户名和密码
```

### 步骤 3：提交 Skill

```bash
# 提交 partner-memory-system
npx clawhub publish \
  --skill skills/partner-memory-system \
  --version 1.0.0 \
  --tag "ai-organization-behavior"

# 提交 relationship-health-score
npx clawhub publish \
  --skill skills/relationship-health-score \
  --version 1.0.0 \
  --tag "ai-organization-behavior"
```

### 步骤 4：验证提交

```bash
# 查看已提交的 Skill
clawhub list

# 查看具体 Skill 详情
clawhub info partner-memory-system
```

---

## 方式 2：Web UI 提交

### 步骤 1：访问 SkillHub

打开 SkillHub 网页端（请使用实际的 SkillHub URL）

### 步骤 2：登录账号

使用你的 SkillHub 账号登录

### 步骤 3：创建新 Skill

1. 点击 "Create New Skill" 或 "+" 按钮
2. 填写基本信息：
   - **Skill Name**: `partner-memory-system`
   - **Display Name**: `🧠 AI Partner Memory System`
   - **Category**: `ai-organization-behavior`
   - **Version**: `1.0.0`
   - **Tags**: `partner-management`, `ai-memory`, `relationship`

3. 上传文件：
   - 上传 `SKILL.md`
   - 上传 `partner_memory.py`

4. 点击 "Publish"

### 步骤 4：重复提交第二个 Skill

对 `relationship-health-score` 重复上述步骤

---

## 方式 3：REST API 提交

### 步骤 1：获取 API Token

在 SkillHub 平台的设置页面生成 API Token

### 步骤 2：准备 ZIP 包

```bash
cd affiliate-skills-hackathon2026

# 打包 partner-memory-system
zip -r partner-memory-system.zip skills/partner-memory-system/

# 打包 relationship-health-score
zip -r relationship-health-score.zip skills/relationship-health-score/
```

### 步骤 3：调用 API 提交

```bash
# 提交 partner-memory-system
curl -X POST https://api.skillhub.example/v1/skills \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: multipart/form-data" \
  -F "name=partner-memory-system" \
  -F "display_name=AI Partner Memory System" \
  -F "category=ai-organization-behavior" \
  -F "version=1.0.0" \
  -F "file=@partner-memory-system.zip"

# 提交 relationship-health-score
curl -X POST https://api.skillhub.example/v1/skills \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: multipart/form-data" \
  -F "name=relationship-health-score" \
  -F "display_name=AI Relationship Health Score" \
  -F "category=ai-organization-behavior" \
  -F "version=1.0.0" \
  -F "file=@relationship-health-score.zip"
```

---

## Skill 信息速查表

### Skill 1: partner-memory-system

| 字段 | 值 |
|------|-----|
| **name** | `partner-memory-system` |
| **display_name** | `🧠 AI Partner Memory System` |
| **version** | `1.0.0` |
| **category** | `ai-organization-behavior` |
| **description** | AI 记住每个 Partner 的多维度特征 |
| **tags** | partner-management, ai-memory, relationship |
| **author** | [Company] |
| **platform** | workbuddy |

### Skill 2: relationship-health-score

| 字段 | 值 |
|------|-----|
| **name** | `relationship-health-score` |
| **display_name** | `💗 AI Relationship Health Score` |
| **version** | `1.0.0` |
| **category** | `ai-organization-behavior` |
| **description** | AI 实时评估每个 Partner 的关系健康度 |
| **tags** | partner-management, health-score, relationship, alert |
| **author** | [Company] |
| **platform** | workbuddy |

---

## 提交后验证

### 检查 Skill 是否可见

提交成功后，尝试：
1. 在 SkillHub 搜索框搜索 `partner-memory`
2. 查看 Skill 详情页面
3. 确认版本号显示为 `1.0.0`

### 测试 Skill 运行

部分平台支持直接在网页端测试：
```bash
# 如果平台支持命令行测试
clawhub run partner-memory-system --action query --partner_id test_partner
```

---

## 常见问题

### Q: 提交失败怎么办？

1. 检查网络连接
2. 确认 API Token 有效
3. 检查文件格式是否正确（UTF-8 编码）
4. 查看错误提示信息

### Q: 版本号如何管理？

遵循 SemVer 规范：
- `1.0.0` → 首次发布
- `1.0.1` → 修复 Bug
- `1.1.0` → 新增功能
- `2.0.0` → 破坏性变更

### Q: 如何更新已提交的 Skill？

```bash
# 修改文件后，重新提交（使用新版本号）
npx clawhub publish --skill skills/partner-memory-system --version 1.1.0
```

---

*生成时间：2026-05-15*
