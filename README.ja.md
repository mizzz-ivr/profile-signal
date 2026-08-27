# Profile Signal

公開GitHub Activityから、モジュール式のGitHub Profile README Widgetを自動生成するツールです。

[English](./README.md) · [サンプル](./examples/sample-profile/README.md) · [Wiki](https://github.com/mizzz-ivr/profile-signal/wiki) · [Releases](https://github.com/mizzz-ivr/profile-signal/releases)

## 主なWidget

`LIVE SIGNAL` · `TODAY` · `CURRENT FOCUS` · `DEV PULSE` · `NOW BUILDING` · `ACTIVITY STREAM` · `DEV RECAP`

導入前でも生成後の見た目を確認できるよう、固定データを使った[サンプルProfile](./examples/sample-profile/README.md)を用意しています。サンプル値はドキュメント用で、実アカウントのActivityではありません。

## 更新頻度

標準配布では、重い集計とLatest Signalsを分離します。

- **フル更新 — 3時間ごと**: TODAY / Search API集計、DEV PULSE、Repository Health / CI、Weekly / Monthly履歴、DEV RECAP、全有効Widget
- **Latest Signals更新 — 30分ごと**: `LIVE SIGNAL`、`CURRENT FOCUS`、`ACTIVITY STREAM` のみ

30分Workflowは公開GitHub Eventsを使い、CIや履歴などの重いstateを保持したまま、live-facingな部分だけを更新します。表示内容に変化がなければcommitしません。

GitHub Public Events自体に反映遅延があり得るため、`ACTIVITY STREAM` はリアルタイム保証ではなく「GitHubから取得できた最新の公開Signal」として扱います。

## 導入

1. [Releases](https://github.com/mizzz-ivr/profile-signal/releases)から `profile-signal-vX.Y.Z.zip` をダウンロード
2. `<username>/<username>` のrootへ展開
3. `.github/profile-signal.yml` のusernameを変更
4. commit / push
5. **Actions → Profile Signal → Run workflow** を1回実行

runtimeは利用者Repository内の `.profile-signal/` に入り、フル更新は `uses: ./.profile-signal` で実行されます。

Release ZIPには、30分更新用の `.github/workflows/profile-signal-stream.yml` も含まれます。

標準構成はpublic-onlyで、PATやAPI Keyは不要です。

## Preset

`minimal` · `standard` · `full` · `terminal` · `compact` · `developer` · `activity` · `oss`

## License

MIT Licenseです。[LICENSE](./LICENSE)を参照してください。
