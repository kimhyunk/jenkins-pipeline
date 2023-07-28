#!/usr/bin/env bash

# 현재 디렉토리를 기준으로 상위 "apps" 디렉토리 경로를 찾음
current_dir=$(pwd)
apps_dir=""

while [[ "$current_dir" != "/" ]]; do
    if [[ -d "$current_dir" ]]; then
        apps_dir="$current_dir"
        break
    fi
    current_dir=$(dirname "$current_dir")
done

if [[ -z "$apps_dir" ]]; then
    echo "상위 'apps' 디렉토리를 찾을 수 없습니다."
    exit 1
fi

echo "상위 'apps' 디렉토리 경로: $apps_dir"

# 상위 "apps" 디렉토리의 디렉토리 목록을 가져오는 함수
function get_directory_list() {
    local dir_list=()
    local i=0
    while IFS= read -r -d '' dir; do
        dir_list[i++]="$dir"
    done < <(find "$1" -mindepth 1 -maxdepth 1 -type d -print0)
    echo "${dir_list[@]}"
}

# 디렉토리 선택 프롬프트
directories=($(get_directory_list "$apps_dir"))

if [[ ${#directories[@]} -eq 0 ]]; then
    echo "상위 'apps' 디렉토리 안에 디렉토리가 없습니다."
    exit 1
fi

echo "디렉토리 목록:"
for ((i=0; i<${#directories[@]}; i++)); do
    echo "$((i+1)). ${directories[i]}"
done

selected_directory=""
while [[ -z "$selected_directory" ]]; do
    read -rp "번호로 선택할 디렉토리를 입력하세요: " selection
    if [[ "$selection" =~ ^[0-9]+$ ]] && ((selection > 0 && selection <= ${#directories[@]})); then
        selected_directory="${directories[$((selection-1))]}"
    else
        echo "유효한 번호를 선택하세요."
    fi
done

echo "선택된 디렉토리: $selected_directory"

# sed -i '' '/selected_directory=/{n;d;}'  .env
sed -i '' "s/selected_directory=.*/selected_directory=/" .env
sed -i '' "s/selected_directory=/selected_directory=${selected_directory//\//\\/}/g" .env

docker-compose up falinux-services-supercom-backend-dev
