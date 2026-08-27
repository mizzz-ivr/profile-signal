# Profile Signal

公開GitHub Activityから、モジュール式のGitHub Profile README Widgetを自動生成するツールです。

[English](./README.md) · [Wiki](https://github.com/mizzz-ivr/profile-signal/wiki) · [Releases](https://github.com/mizzz-ivr/profile-signal/releases)

## 主なWidget

`LIVE SIGNAL` · `TODAY` · `CURRENT FOCUS` · `DEV PULSE` · `NOW BUILDING` · `ACTIVITY STREAM` · `DEV RECAP`

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
