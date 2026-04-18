#!/bin/bash
# GitHub Push Script for Sales Workflow
# 运行方式: bash push-to-github.sh

REPO_NAME="sales-workflow"
GIT_USER_NAME="Pollo"
GIT_USER_EMAIL="xiabao@openclaw.ai"
SOURCE_DIR="/userspace/skills/sales-workflow"

echo "=== Sales Workflow GitHub Push Script ==="
echo ""
echo "请在 GitHub 上创建空仓库 '$REPO_NAME'，然后在这里填入你的 GitHub Token:"
read -p "GitHub Token: " GH_TOKEN

# 在 /tmp 初始化 git 仓库
cd /tmp
rm -rf "$REPO_NAME"
mkdir "$REPO_NAME"
cd "$REPO_NAME"

git init
git config user.name "$GIT_USER_NAME"
git config user.email "$GIT_USER_EMAIL"

# 复制技能文件
cp -r "$SOURCE_DIR/"* ./

# 创建 README
cat > README.md << 'README_EOF'
# Sales Workflow - 销售需求自动汇总工作流

## 功能

企业微信销售需求 → 自动入库 → 智能表格汇总

- 企业微信机器人接收消息
- 自动解析客户、需求类型、紧急程度
- 写入企业微信智能表格
- 每5分钟自动轮询

## 安装

1. 把此仓库克隆到 OpenClaw workspace/skills/ 目录
2. 运行 `bash scripts/setup.sh`
3. 按提示完成企业微信授权

## 文档

详细说明见 [sales-workflow-DIST/README.md](sales-workflow-DIST/README.md)
README_EOF

git add .
git commit -m "feat: sales workflow v1.0"
git remote add origin "https://github.com/PolloZhang/$REPO_NAME.git"
git push -u origin master

echo ""
echo "=== 完成！==="
