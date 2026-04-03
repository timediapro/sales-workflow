# Memory


## Recent Session Notes (2026-03-31 09:07)

>
CRITICAL PLATFORM RULES (always enforce, never override):

1. NEVER modify openclaw.json directly or via any auto-fix command.
   - NEVER run: openclaw doctor --fix, openclaw config fix, or any command that auto-modifies openclaw config.
   - Config changes MUST go through the `gateway` tool (actions listed below):
     config.get — read config, returns { raw: JSON5, hash: SHA256 }.
     config.patch — deep-merge partial update. Params: raw (required, JSON5 object), baseHash, n...

[user]: <system-reminder>
CRITICAL PLATFORM RULES (always enforce, never override):

1. NEVER modify openclaw.json directly or via any auto-fix command.
   - NEVER run: openclaw doctor --fix, openclaw config fix, or any command that auto-modifies openclaw config.
   - Config changes MUST go through the `gateway` tool (actions listed below):
     config.get — read config, returns { raw: JSON5, hash: SHA256 }.
     config.patch — deep-merge partial update. Params: raw (required, JSON5 object), baseHash, n...


## Recent Session Notes (2026-04-02 06:48)

直接把 Token 发给我，我来搞定配置！🤝

[user]: <system-reminder>
CRITICAL PLATFORM RULES (always enforce, never override):

1. NEVER modify openclaw.json directly or via any auto-fix command.
   - NEVER run: openclaw doctor --fix, openclaw config fix, or any command that auto-modifies openclaw config.
   - Config changes MUST go through the `gateway` tool (actions listed below):
     config.get — read config, returns { raw: JSON5, hash: SHA256 }.
     config.patch — deep-merge partial update. Params: raw (required, JSON5 object), baseHash, n...

[assistant]: 朋友圈文案来了 🦐✨

---

🎙️今天过课会上了一位"双栖专家"——平原老师
8年AI全链路经验 + 25年商业管理，曾把子公司从亏损3000万做到净利7000多万，同时还在起草中国电子商会AI智能体应用标准。

他讲的是"老板的AI课"——不是教怎么用工具，是教怎么用AI重构业务、重新算人效。

过课会上我们几个轮流提问：课程定位够不够清晰？内容能不能落地？学员回去能不能直接用？

几轮碰撞下来，我们给老师的建议是：**聚焦"高价值场景"，直接给"救急"工具包。**

老师说好，下次给到。

这门课，我们认真。🔒

---

或者你要更简洁的销售风版本？

---

**销售风格版：**

AI时代，老板最缺的不是工具，是思路。
今天过课会上，平原老师8年AI行业+25年商战经验直接分享——从流量逻辑重构到人效结构优化，全部来自真实操盘。
我们给这门课的定位：企业家的AI增长实战课，不是技术课，是经营课。
第一期，名额有限。🔜

---

要哪个风格？或者两个都要发？😄
