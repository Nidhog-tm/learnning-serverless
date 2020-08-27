#!/bin/bash

# python3の仮想環境を有効化する。
# ワークスペースの中だけで pip install ができるようになるため
# 環境を汚さないようにすることができる。
# 使用する方はコメントアウトを外して使用してください。
python3 -m venv .venv
source .venv/bin/activate
echo test

# lambdaディレクトリ配下のディレクトリを取得し、
# 各ディレクトリ中の build/* にアップロードする対象のソースコードを格納する。
for dir in `ls -l | awk '$1 ~ /d/ {print $9 }' `
do
  if [ ${dir} != "lib" ] && [ ${dir} != "tests" ]; then
    echo "[INFO] ${dir}のディレクトリをビルドします。";

    rm -rf ${dir}/build/;
    mkdir ${dir}/build/;

    if [ -e ${dir}/requirements.txt ]; then
      echo "[INFO] ライブラリをrequirements.txtを参照して${dir}/build/にインストールします。";
      pip install -r ${dir}/requirements.txt -t ${dir}/build/;
    fi

    echo "[INFO] プロダクトコードを${dir}/build/にコピーします。"
    cp ${dir}/*.py ${dir}/build/;
    cp ${dir}/*.yaml ${dir}/build/;
    for d in `ls -l ${dir} | awk '$1 ~ /d/ {print $9 }' `
    do
      if [ ${d} != "build" ] && [ ${d} != "__pycache__" ]; then
        cp -r ${dir}/${d} ${dir}/build/;
      fi
    done

    if [ -e ${dir}/tests/ ]; then
      mkdir ${dir}/build/tests;
      cp ${dir}/tests/*.py ${dir}/build/tests/;
    fi
  fi
done