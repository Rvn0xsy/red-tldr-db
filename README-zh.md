# Red TL;DR Database

[English](./README.md) | [简体中文](./README-zh.md)

## 什么是 Red TL;DR Database ?

Red TL;DR Database 是一组为 [red-tldr](https://github.com/Rvn0xsy/red-tldr) 提供搜索的文本数据，如果你还不知道 [red-tldr](https://github.com/Rvn0xsy/red-tldr) ，请阅读 [说明文档](http://payloads.online/red-tldr/) 尝试体验一下。

## 如何使用这些数据？

你可以使用`git clone`命令将数据同步到本地，未来可以使用`git pull`命令持续更新

```bash
$ git clone https://gthub.com/Rvn0xsy/red-tldr-db ~/red-tldr-db/
```

## 提交贡献

red-tldr 是一个免费且开源的项目，我们欢迎任何人为其开发和进步贡献力量。

- 在使用过程中出现任何问题，可以通过 issues 来反馈。
- Bug 的修复可以直接提交 [Pull Request](https://github.com/Rvn0xsy/red-tldr-db/pulls) 到 dev 分支。
- 如果是增加新的功能特性，请先创建一个 [issues](https://github.com/Rvn0xsy/red-tldr-db/issues) 并做简单描述以及大致的实现方法，提议被采纳后，就可以创建一个实现新特性的 [Pull Request](https://github.com/Rvn0xsy/red-tldr-db/pulls) 。
- 欢迎对说明文档做出改善，帮助更多的人使用 [red-tldr](https://github.com/Rvn0xsy/red-tldr/) ，特别是英文文档。
- 贡献代码请提交 PR 至 dev 分支，main 分支仅用于发布稳定可用版本。
- 如果你有任何其他方面的问题或合作，欢迎发送邮件至 rvn0xsy@gmail.com 。

**提醒：和项目相关的问题最好在 [issues](https://github.com/Rvn0xsy/red-tldr-db/issues) 中反馈，这样方便其他有类似问题的人可以快速查找解决方法，并且也避免了我们重复回答一些问题。**

### 如何提交自己的关键字？

red-tldr-db 的数据格式非常简单，你可以自定义添加想要搜索的结果：

```yaml
name: search-name
tags: [keyword,key]
data: |
  DATA
```

### 字段说明

* name: 文件名称
* tags: 搜索关键字，支持多个
* data: 搜索的结果（将会打印到终端上）

定义完成数据后，先创建一个 [issues](https://github.com/Rvn0xsy/red-tldr-db/issues) 并做简单描述以及大致的实现方法，提议被采纳后，就可以创建一个实现新特性的 [Pull Request](https://github.com/Rvn0xsy/red-tldr-db/pulls) 。