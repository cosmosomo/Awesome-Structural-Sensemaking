#!/usr/bin/env python3
"""PCA 多取一根轴（二维到三维）多保留多少信息：累计方差和邻域保持。

01-theory/high-dimensional.md 里“PCA 的第三根轴”一表的数字出自这个脚本。它不是文献，也不是案例，是整理者自己算的，
只回答“第三根轴在数据里多带了多少东西”，不回答“人读不读得懂”（那是用户实验的问题，见同一篇文档里的文献表）。

用法:
  python3 -m pip install scikit-learn      # 只有这个脚本需要，CI 不跑
  python3 scripts/pca_axes.py

做法：每个数据集先标准化，再做 PCA；累计方差是前两个、前三个主成分的方差占比之和；邻域保持用
sklearn.manifold.trustworthiness（k=10），取值 0 到 1，越高表示低维里的近邻越真是高维里的近邻。
数据集用 scikit-learn 自带的四个，不联网。
"""
from __future__ import annotations

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.manifold import trustworthiness
from sklearn.preprocessing import StandardScaler

SETS = {
    "iris（4 维，150 点）": datasets.load_iris(),
    "wine（13 维，178 点）": datasets.load_wine(),
    "breast_cancer（30 维，569 点）": datasets.load_breast_cancer(),
    "digits（64 维，1797 点）": datasets.load_digits(),
}


def main() -> None:
    print("| 数据集 | 前两个成分累计方差 | 前三个成分累计方差 | 第三根轴多保留 | 邻域保持（k=10）二维 → 三维 |")
    print("| --- | --- | --- | --- | --- |")
    for name, d in SETS.items():
        x = StandardScaler().fit_transform(d.data)
        r = PCA().fit(x).explained_variance_ratio_
        t2 = trustworthiness(x, PCA(2).fit_transform(x), n_neighbors=10)
        t3 = trustworthiness(x, PCA(3).fit_transform(x), n_neighbors=10)
        print(f"| {name} | {r[:2].sum():.3f} | {r[:3].sum():.3f} | +{r[2]:.3f} | {t2:.3f} → {t3:.3f} |")


if __name__ == "__main__":
    main()
