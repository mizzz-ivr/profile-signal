# Profile Signal

公開GitHub Activityから、モジュール式のGitHub Profile README Widgetを自動生成するツールです。

[English](./README.md) · [Wiki](https://github.com/mizzz-ivr/profile-signal/wiki) · [Releases](https://github.com/mizzz-ivr/profile-signal/releases)

## 主なWidget

`LIVE SIGNAL` · `TODAY` · `CURRENT FOCUS` · `DEV PULSE` · `NOW BUILDING` · `ACTIVITY STREAM` · `DEV RECAP`

## 更新頻度

配布版では役割を分けた2つのWorkflowを入れます。

- **フル更新** — 3時間ごと。TODAY、DEV PULSE、CI/Health、履歴、全Widgetを更新
- **Latest signals更新** — 30分ごと。`LIVE SIGNAL`、`CURRENT FOCUS`、`ACTIVITY STREAM` だけを公開GitHub Eventsから軽量更新

Search API・CI・履歴集計まで30分ごとに回さず、動きがなければcommitもしません。

GitHub Public Events自体に反映遅延があり得るため、`ACTIVITY STREAM` はリアルタイム表示とは表現せず、Latest public signalsとして扱います。

## 導入

1. [Releases](https://github.com/mizzz-ivr/profile-signal/releases)から `profile-signal-vX.Y.Z.zip` をダウンロード
2. `<username>/<username>` のrootへ展開
3. `.github/profile-signal.yml` のusernameを変更
4. commit / push
5. **Actions → Profile Signal → Run workflow** を1回実行

runtimeは利用者Repository内の `.profile-signal/` に入り、`uses: ./.profile-signal` で実行されます。

標準構成はpublic-onlyで、PATやAPI Keyは不要です。

## Preset

`minimal` · `standard` · `full` · `terminal` · `compact` · `developer` · `activity` · `oss`

## License

MIT Licenseです。[LICENSE](./LICENSE)を参照してください。
