#!/bin/bash
# =============================================================================
# Script helper untuk push backup ke GitHub
# Cara pakai: bash push-to-github.sh "Pesan commit di sini"
# =============================================================================

set -e

# Load credentials
TOKEN_FILE="/home/z/my-project/.config/github-token.env"
if [ ! -f "$TOKEN_FILE" ]; then
  echo "ERROR: File token tidak ditemukan di $TOKEN_FILE"
  echo "Buat dulu dengan format:"
  echo "  GITHUB_USERNAME=<username>"
  echo "  GITHUB_REPO=<repo>"
  echo "  GITHUB_PAT=<pat>"
  echo "  GITHUB_REPO_URL=<url>"
  exit 1
fi

source "$TOKEN_FILE"

REPO_DIR="/home/z/my-project/riset-backup"
cd "$REPO_DIR" || { echo "ERROR: Folder $REPO_DIR tidak ada"; exit 1; }

COMMIT_MSG="${1:-Update backup $(date +'%Y-%m-%d %H:%M:%S')}"

echo "=== STATUS SEBELUM COMMIT ==="
git status -s

echo ""
echo "=== ADD & COMMIT ==="
git add .
git commit -m "$COMMIT_MSG" 2>&1 | tail -3 || echo "Tidak ada perubahan untuk di-commit"

echo ""
echo "=== PUSH KE GITHUB ==="
# Set remote dengan PAT (sementara)
git remote set-url origin "https://${GITHUB_USERNAME}:${GITHUB_PAT}@github.com/${GITHUB_USERNAME}/${GITHUB_REPO}.git"

# Push
git push origin main 2>&1 | tail -5

# Bersihkan PAT dari config (keamanan)
git remote set-url origin "https://github.com/${GITHUB_USERNAME}/${GITHUB_REPO}.git"

echo ""
echo "=== SELESAI ==="
echo "Lihat hasil: https://github.com/${GITHUB_USERNAME}/${GITHUB_REPO}"
