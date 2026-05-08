## 最近の活動

<p align="left">
  <img
    src="https://github-readme-activity-graph.vercel.app/graph?username=t-hirata74&theme=github-dark&hide_border=true"
    alt="Contribution graph"
  />
</p>

---

## コントリビューション統計

<p align="left">
  <img
    src="https://streak-stats.demolab.com/?user=t-hirata74&theme=github_dark&hide_border=true"
    alt="GitHub streak"
  />
</p>

---

## 学習ポートフォリオ

<!-- portfolio:start -->
### [service-architecture-lab](https://github.com/t-hirata74/service-architecture-lab)

有名 SaaS のアーキテクチャを **ローカル完結のミニマム実装** で再現し、設計判断を ADR として残す検証用プロジェクト群。各サービスは **backend + frontend (Next.js 16) + ai-worker (Python / FastAPI) + MySQL** の同形構成で、API スタイル / キュー / 認可モデル / 整合性パターンの違いを横断比較できるように整理している。

| プロジェクト | サービス | 主な技術課題 | ステータス | ドキュメント |
| --- | --- | --- | --- | --- |
| [`slack`](https://github.com/t-hirata74/service-architecture-lab/tree/main/slack) | Slack 風リアルタイムチャット | WebSocket fan-out / 既読 cursor 整合性 / Rails ↔ Python 境界 | 🟢 MVP 完成 (E2E 6 件通過) | [README](https://github.com/t-hirata74/service-architecture-lab/blob/main/slack/README.md) ・ [Architecture](https://github.com/t-hirata74/service-architecture-lab/blob/main/slack/docs/architecture.md) ・ [ADR (6)](https://github.com/t-hirata74/service-architecture-lab/tree/main/slack/docs/adr) |
| [`youtube`](https://github.com/t-hirata74/service-architecture-lab/tree/main/youtube) | YouTube 風動画プラットフォーム | 非同期動画変換パイプライン / 状態機械 / Rails ↔ Python 境界 (タグ抽出 / サムネ / レコメンド) / FULLTEXT ngram 検索 / Solid Queue (Redis 不使用) | 🟢 MVP 完成 (RSpec 55 件 + Playwright 4 件通過) | [README](https://github.com/t-hirata74/service-architecture-lab/blob/main/youtube/README.md) ・ [Architecture](https://github.com/t-hirata74/service-architecture-lab/blob/main/youtube/docs/architecture.md) ・ [ADR (6)](https://github.com/t-hirata74/service-architecture-lab/tree/main/youtube/docs/adr) |
| [`github`](https://github.com/t-hirata74/service-architecture-lab/tree/main/github) | GitHub 風 Issue Tracker | 権限グラフ / Issue・PR モデル / CI ステータス集約 / GraphQL field 認可 | 🟢 MVP 完成 (RSpec 75 件 + Playwright 4 件通過) | [README](https://github.com/t-hirata74/service-architecture-lab/blob/main/github/README.md) ・ [Architecture](https://github.com/t-hirata74/service-architecture-lab/blob/main/github/docs/architecture.md) ・ [ADR (4)](https://github.com/t-hirata74/service-architecture-lab/tree/main/github/docs/adr) |
| [`perplexity`](https://github.com/t-hirata74/service-architecture-lab/tree/main/perplexity) | Perplexity 風 RAG 検索 | RAG パイプライン (retrieve / extract / synthesize) / Hybrid retrieval + embedding データ管理 / SSE streaming + 三段階 degradation / 引用整合性の信頼境界 / テスト戦略 / chunk 分割戦略 / rodauth-rails JWT bearer | 🟢 Phase 5 完了 (RSpec 105 + pytest 70 件 / Playwright scaffold / Terraform validate pass / CI 4 ジョブ追加) | [README](https://github.com/t-hirata74/service-architecture-lab/blob/main/perplexity/README.md) ・ [Architecture](https://github.com/t-hirata74/service-architecture-lab/blob/main/perplexity/docs/architecture.md) ・ [ADR (7)](https://github.com/t-hirata74/service-architecture-lab/tree/main/perplexity/docs/adr) |
| [`instagram`](https://github.com/t-hirata74/service-architecture-lab/tree/main/instagram) | Instagram 風タイムライン (Django/DRF) | タイムライン生成戦略 (fan-out on write) / フォローグラフ DB 設計 / Django ORM N+1 + index / DRF TokenAuthentication | 🟢 MVP 完成 (Django pytest 51 + ai-worker pytest 12 + Playwright 実機 3 件通過 / Terraform validate / CI 4 ジョブ) | [README](https://github.com/t-hirata74/service-architecture-lab/blob/main/instagram/README.md) ・ [Architecture](https://github.com/t-hirata74/service-architecture-lab/blob/main/instagram/docs/architecture.md) ・ [ADR (4)](https://github.com/t-hirata74/service-architecture-lab/tree/main/instagram/docs/adr) |
| [`discord`](https://github.com/t-hirata74/service-architecture-lab/tree/main/discord) | Discord 風リアルタイムチャット (Go) | ギルド単位シャーディング + 単一プロセス Hub / goroutine + channel CSP pattern / プレゼンスハートビート / WebSocket fan-out (slack Rails ActionCable との対比) | 🟢 MVP 完成 (Go gateway + WS Hub + Next.js 16 + ai-worker + Playwright fan-out / presence offline 2 ケース通過 / Terraform validate / CI 5 ジョブ) | [README](https://github.com/t-hirata74/service-architecture-lab/blob/main/discord/README.md) ・ [Architecture](https://github.com/t-hirata74/service-architecture-lab/blob/main/discord/docs/architecture.md) ・ [ADR (4)](https://github.com/t-hirata74/service-architecture-lab/tree/main/discord/docs/adr) |
| [`reddit`](https://github.com/t-hirata74/service-architecture-lab/tree/main/reddit) | Reddit 風 forum (FastAPI / async) | コメントツリー (Adjacency List + Materialized Path) / 投票整合性 (votes truth + posts.score 相対加算) / Hot ランキング (Reddit 公式式 + ai-worker APScheduler 60s 再計算) / FastAPI async + SQLAlchemy 2.0 async + aiomysql + HS256 JWT | 🟢 MVP 完成 (FastAPI 32 + ai-worker 19 + Next.js build + Playwright 3 / Terraform validate / CI 5 ジョブ) | [README](https://github.com/t-hirata74/service-architecture-lab/blob/main/reddit/README.md) ・ [Architecture](https://github.com/t-hirata74/service-architecture-lab/blob/main/reddit/docs/architecture.md) ・ [ADR (4)](https://github.com/t-hirata74/service-architecture-lab/tree/main/reddit/docs/adr) |
| [`shopify`](https://github.com/t-hirata74/service-architecture-lab/tree/main/shopify) | Shopify 風 EC プラットフォーム (Rails 8) | モジュラーモノリス (Rails Engine + packwerk) / マルチテナント (`shop_id` row-level scoping) / 在庫の同時減算 (条件付き UPDATE + ledger) / App プラットフォーム (Webhook at-least-once + HMAC + idempotency) | 🟢 MVP 完成 + 高精度レビュー反映 (Phase 1-5 + cart lock! / UNIQUE 制約 / Order#number atomic counter / Solid Queue / Apps API / ai-worker 統合 / RSpec 89 + pytest 7 + Terraform validate / CI 5 ジョブ) | [README](https://github.com/t-hirata74/service-architecture-lab/blob/main/shopify/README.md) ・ [Architecture](https://github.com/t-hirata74/service-architecture-lab/blob/main/shopify/docs/architecture.md) ・ [ADR (4)](https://github.com/t-hirata74/service-architecture-lab/tree/main/shopify/docs/adr) |
| [`zoom`](https://github.com/t-hirata74/service-architecture-lab/tree/main/zoom) | Zoom 風オンライン会議 (Rails 8) | 会議ライフサイクル state machine / ホスト・共同ホスト動的譲渡 (append-only 監査) / 録画→要約 at-least-once パイプライン (結果テーブル UNIQUE 冪等) — WebRTC SFU は scope 外 | 🟢 MVP 完成 (RSpec 67 + pytest 7 + Playwright 2 件通過 / Terraform validate / CI 4 ジョブ) | [README](https://github.com/t-hirata74/service-architecture-lab/blob/main/zoom/README.md) ・ [ADR (3)](https://github.com/t-hirata74/service-architecture-lab/tree/main/zoom/docs/adr) |
| [`calendly`](https://github.com/t-hirata74/service-architecture-lab/tree/main/calendly) | Calendly / Cal.com 風日程調整 (Rails 8 + **Ruby 4**) | availability merge / **同時予約レース防止 (MySQL における `EXCLUDE` 代替)** / RRULE 展開 + timezone 永続化 — 本リポ初の Ruby 4 系プロジェクト | 🟢 MVP 完成 (RSpec 88 + pytest 7 + Playwright 2 件通過 / Terraform validate / CI 5 ジョブ) | [README](https://github.com/t-hirata74/service-architecture-lab/blob/main/calendly/README.md) ・ [Architecture](https://github.com/t-hirata74/service-architecture-lab/blob/main/calendly/docs/architecture.md) ・ [ADR (3)](https://github.com/t-hirata74/service-architecture-lab/tree/main/calendly/docs/adr) |

設計判断はすべて **ADR (Architecture Decision Record)** として記録し、E2E テストは Playwright で gif 化して各 README に埋め込んでいる。プロジェクト一覧は GitHub Actions で `service-architecture-lab` の README から日次自動同期。
<!-- portfolio:end -->



