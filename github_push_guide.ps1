# GitHub 推送脚本
# 用于将本地仓库推送到 GitHub

Write-Host "=========================================="
Write-Host "  GitHub 推送脚本"
Write-Host "=========================================="
Write-Host ""

$repoPath = "C:\Users\晏昭\WorkBuddy\2026-05-11-task-3\affiliate-skills-hackathon2026"

# 添加 Git 路径（MinGit）
$gitBin = "$env:USERPROFILE\mingw64\bin"
$gitUsrBin = "$env:USERPROFILE\mingw64\usr\bin"
$env:Path = "$gitBin;$gitUsrBin;" + $env:Path

cd $repoPath

# 检查远程仓库
Write-Host "检查远程仓库..."
$remote = git remote get-url origin 2>$null

if ($remote) {
    Write-Host "✅ 远程仓库: $remote"
} else {
    Write-Host "添加远程仓库..."
    git remote add origin https://github.com/Ameko2026/affiliate-skills-hackathon2026.git
}

# 检查 GitHub 认证
Write-Host ""
Write-Host "检查 GitHub 认证状态..."
git config --global credential.helper

Write-Host ""
Write-Host "=========================================="
Write-Host "  推送准备就绪"
Write-Host "=========================================="
Write-Host ""
Write-Host "当前分支: $(git branch --show-current)"
Write-Host "提交数量: $(git rev-list --count HEAD)"
Write-Host ""
Write-Host "下一步操作:"
Write-Host "  1. 安装完整版 Git for Windows（需要 HTTPS 支持）"
Write-Host "     下载: https://git-scm.com/download/win"
Write-Host ""
Write-Host "  2. 或者在 GitHub 网页端手动上传文件"
Write-Host "     参考: github_manual_submit.md"
Write-Host ""
Write-Host "  3. 安装完整 Git 后，运行以下命令推送:"
Write-Host ""
Write-Host "     cd $repoPath"
Write-Host "     git push -u origin master"
Write-Host ""

# 保存推送命令到文件
@"
# 完整 Git 推送命令（安装完整版 Git 后运行）
cd `"$repoPath`"
git push -u origin master
"@ | Out-File -FilePath "$repoPath\push_to_github.bat" -Encoding UTF8

Write-Host "推送命令已保存到: $repoPath\push_to_github.bat"
