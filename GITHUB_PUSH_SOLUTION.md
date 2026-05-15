# GitHub Push 解决方案
# 问题：MinGit 缺少 remote-https helper，无法直接 push

## 方案一：安装 GitHub CLI（推荐，无需 admin 权限）

1. 下载：https://github.com/cli/cli/releases/download/v2.63.2/gh_2.63.2_windows_amd64.msi
2. 双击安装（用户级安装，无需 admin）
3. 重新打开 PowerShell，运行：
   ```
   gh auth login
   ```
   - 选择 GitHub.com
   - 选择 HTTPS
   - 选择 Login with web browser（会给出代码）
4. 然后运行：
   ```
   cd C:\Users\晏昭\WorkBuddy\2026-05-11-task-3\affiliate-skills-hackathon2026
   git push -u origin master
   ```

## 方案二：使用 curl + GitHub API 手动创建 commit

如果你不想安装额外软件，可以用 curl 推送。

### 步骤 1：生成 Personal Access Token
1. 访问 https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. 选择 scopes: repo (完全控制)
4. 复制生成的 token

### 步骤 2：运行推送脚本
```powershell
# 设置 token（替换 YOUR_TOKEN_HERE）
$env:GITHUB_TOKEN = "YOUR_TOKEN_HERE"

# 运行推送
$repoPath = "C:\Users\晏昭\WorkBuddy\2026-05-11-task-3\affiliate-skills-hackathon2026"
cd $repoPath

# 获取最新 commit
$commitSha = & "C:\Users\晏昭\mingw64\bin\git.exe" rev-parse HEAD

# 获取仓库信息
$owner = "Ameko2026"
$repo = "affiliate-skills-hackathon2026"
$branch = "master"

# 创建 refs
$headers = @{
    "Authorization" = "token $env:GITHUB_TOKEN"
    "Accept" = "application/vnd.github.v3+json"
}

# 获取当前 refs
$refResp = Invoke-RestMethod -Uri "https://api.github.com/repos/$owner/$repo/git/refs/heads/$branch" -Headers $headers -Method GET
$currentTreeSha = $refResp.object.sha

# 更新 refs 到最新 commit
$updateBody = @{
    sha = $commitSha
    force = $false
} | ConvertTo-Json

Invoke-RestMethod -Uri "https://api.github.com/repos/$owner/$repo/git/refs/heads/$branch" -Headers $headers -Method PATCH -Body $updateBody -ContentType "application/json"

Write-Host "Push completed!"
```

## 方案三：手动使用 Git Bash（如果有）

如果你能找到完整版 Git Bash：
```bash
cd C:\Users\晏昭\WorkBuddy\2026-05-11-task-3\affiliate-skills-hackathon2026
git push -u origin master
```

---

## 当前状态
- ✅ Git 已安装 (MinGit 2.54.0)
- ✅ PATH 已配置（需要重启终端生效）
- ✅ github_push_guide.ps1 已提交
- ✅ 所有本地 commit 就绪
- ⏳ 等待推送到 GitHub
