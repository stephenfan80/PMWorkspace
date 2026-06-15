# product_agent Codex 插件提交说明

插件目录：`plugins/product-agent`

构建命令：

```bash
bin/product-agent-build-plugin
```

提交前检查：

```bash
bin/product-agent-gen-skill-docs check
bin/product-agent-eval run --suite core
python3 -m json.tool plugins/product-agent/.codex-plugin/plugin.json >/dev/null
```

提交前还要用本地禁止词清单检查旧项目名、旧 skill 入口和旧命令前缀；不应出现命中。
