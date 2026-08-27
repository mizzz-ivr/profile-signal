[English](Home) | [日本語](Home-ja)

# Profile Signal Wiki

Profile Signal は、公開 GitHub Activity をもとに GitHub Profile README を自動更新するための self-contained runtime です。

推奨導入方法は **GitHub Release の ZIP を、自分の GitHub Profile Repository に展開して使う方法**です。

```text
GitHub Release ZIP
        ↓
<username>/<username>
        ↓
.profile-signal/
.github/profile-signal.yml
.github/workflows/profile-signal.yml
        ↓
uses: ./.profile-signal
```

導入後は利用者自身のRepository内だけでruntimeを実行し、GitHub ActionsからREADMEを更新します。

## Source of Truth

`v0.3.0` 以降のProfile Signal本体・Release・Issue・Wikiは、専用Repository `mizzz-ivr/profile-signal` で管理します。

`mizzz-ivr/mizzz-ivr` はProfile Signalを実際に使っているLive Demo / Dogfooding環境です。

## 主な特徴

- public-only
- API Secret / PAT 不要
- GitHub Actions による定期更新
- README の既存本文は ZIP 展開時に上書きしない
- 8種類のPreset
- English / 日本語ドキュメント
- MIT License

## Wiki

- [導入手順](Installation-ja)
- [設定リファレンス](Configuration-ja)
- [プリセットとテンプレート](Presets-ja)
- [ライセンス](License-ja)

## 主な表示

現在の runtime では以下の Widget を組み合わせられます。

- LIVE SIGNAL
- TODAY
- CURRENT FOCUS
- DEV PULSE
- NOW BUILDING
- ACTIVITY STREAM
- DEV RECAP

表示内容は `preset` を起点にしつつ、`widgets` で個別に上書きできます。

## 配布方針

Release ZIP を標準導入経路とします。利用者自身の Profile Repository にruntimeを保持するため、実行コードを確認しやすく、配布元Repositoryへ実行時依存しません。
