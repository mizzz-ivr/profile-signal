# Profile Signal — 導入手順

Profile Signal は、Release ZIPを自分のGitHub Profile Repositoryへ展開して利用する self-contained runtime です。

- Releases: https://github.com/mizzz-ivr/profile-signal/releases
- Wiki: https://github.com/mizzz-ivr/profile-signal/wiki
- English README: https://github.com/mizzz-ivr/profile-signal#readme
- 日本語README: https://github.com/mizzz-ivr/profile-signal/blob/main/README.ja.md

推奨導入方法は **Release ZIP** です。`mizzz-ivr/mizzz-ivr` はLive Demo / Dogfooding環境として扱います。

## 必要条件

- `<username>/<username>` 形式のpublic GitHub Profile Repository
- GitHub Actionsが有効
- WorkflowがRepository contentsへ書き込める設定
- 標準public-onlyモードではAPI Key / Secret不要

## インストール

1. [Releases](https://github.com/mizzz-ivr/profile-signal/releases)から最新の `profile-signal-<version>.zip` を取得します。
2. ZIPをProfile Repositoryのrootへ展開します。
3. `.github/profile-signal.yml` を開きます。
4. `YOUR_GITHUB_USERNAME` を自分のGitHub loginへ変更します。
5. preset / theme / widget overrideを選びます。
6. 展開したファイルをcommit / pushします。
7. **Actions → Profile Signal → Run workflow** を1回実行します。
8. README / `assets/` / `data/` の生成結果を確認します。

Release ZIPは以下を追加し、既存README自体は含みません。

```text
.profile-signal/
├─ action.yml
├─ LICENSE
├─ presets/
│  ├─ minimal.yml
│  ├─ standard.yml
│  ├─ full.yml
│  ├─ terminal.yml
│  ├─ compact.yml
│  ├─ developer.yml
│  ├─ activity.yml
│  └─ oss.yml
├─ src/
│  ├─ orchestrator.py
│  ├─ preset_runtime.py
│  └─ stream_runtime.py
└─ scripts/
   ├─ update-profile-activity.py
   ├─ profile_signal.py
   ├─ update-profile-signal.py
   ├─ profile_signal_operations.py
   └─ profile_signal_history.py

.github/
├─ profile-signal.yml
└─ workflows/
   ├─ profile-signal.yml
   └─ profile-signal-stream.yml

PROFILE_SIGNAL_INSTALL.md
PROFILE_SIGNAL_VERSION
```

## 更新頻度

配布版では2つのWorkflowを役割分担させます。

### フル更新

`.github/workflows/profile-signal.yml`

- 3時間ごと
- TODAY
- DEV PULSE
- NOW BUILDING / PROJECT HEALTH
- CI SIGNAL
- DEV RECAP / Weekly / Monthly / Achievements
- 全Widgetの整合更新

### Latest signals更新

`.github/workflows/profile-signal-stream.yml`

- 30分ごと (`:07` / `:37`)
- LIVE SIGNAL
- CURRENT FOCUS
- ACTIVITY STREAM
- 既存のCI / History / Health stateは保持
- 変化が無ければcommitしない

GitHub Public EventsにはGitHub側の反映遅延があり得るため、ACTIVITY STREAMはリアルタイム保証ではなく「取得できた最新の公開Signal」として表示します。

## Preset

### 基本Preset

- `minimal` — LIVE SIGNAL + CURRENT FOCUS
- `standard` — LIVE SIGNAL + TODAY + CURRENT FOCUS + DEV PULSE
- `full` — 全Widget
- `terminal` — 全Widget + terminal theme既定

### 用途別Preset

- `compact` — TODAY + CURRENT FOCUS。短く現在地だけ表示
- `developer` — LIVE SIGNAL + CURRENT FOCUS + DEV PULSE + NOW BUILDING + ACTIVITY STREAM
- `activity` — TODAY + DEV PULSE + ACTIVITY STREAM + DEV RECAP
- `oss` — LIVE SIGNAL + CURRENT FOCUS + NOW BUILDING + ACTIVITY STREAM + DEV RECAP

Preset定義は `.profile-signal/presets/*.yml` に分離されています。既存Presetの意味は破壊的に変更せず、新しい用途は新Presetとして追加する方針です。

個別WidgetはPreset選択後も上書きできます。

```yaml
preset: developer

widgets:
  dev_recap:
    enabled: true
```

## Theme

- `signal`
- `minimal`
- `terminal`

Presetは表示するWidget構成と既定Theme、Themeは見せ方を担当します。

## README挿入位置

`auto_insert_markers: true` の場合、有効Widgetのmarkerが無ければ自動挿入します。

標準Release設定では `insert_before` を空にしており、利用者READMEの見出しを勝手に推測せず末尾へ追加します。

特定見出しの前へ配置する例:

```yaml
readme:
  auto_insert_markers: true
  insert_before: "## About me"
```

## GitHub Actions書き込み権限

WorkflowによるREADME更新にはRepository contentsへのwrite権限が必要です。

GitHub UIでは通常:

```text
Settings → Actions → General → Workflow permissions → Read and write permissions
```

を確認します。

## 更新

新しいReleaseへ更新する前に、現在のRepositoryをcommitしてRollback可能な状態にしてください。

1. 新しいRelease ZIPを取得します。
2. `.profile-signal/` を新runtimeへ差し替えます。
3. `.github/profile-signal.yml` は原則維持します。
4. Release Notesでconfig migrationが指定された場合のみ設定を変更します。
5. `profile-signal.yml` / `profile-signal-stream.yml` のWorkflow template差分を確認します。
6. `Profile Signal` を手動実行し、生成diffを確認します。

## アンインストール

1. `.profile-signal/` を削除します。
2. `.github/profile-signal.yml` を削除します。
3. `.github/workflows/profile-signal.yml` と `.github/workflows/profile-signal-stream.yml` を削除します。
4. READMEのProfile Signal marker blockを必要に応じて削除します。
5. 不要なら `assets/` と `data/` の生成履歴を削除します。

## Privacy

Profile Signal v0.xでは以下が必須です。

```yaml
privacy:
  public_only: true
```

Private Repository情報を取得して後段でmaskする設計にはしません。

## License

`mizzz-ivr/profile-signal` のOSS本体はMIT Licenseです。Repository rootの `LICENSE` と、Release ZIP内の `.profile-signal/LICENSE` にLicense本文を含めます。

利用者自身のProfile README・画像・第三者素材などは、それぞれの所有者・ライセンスに従い、Profile SignalのMIT Licenseが自動的に適用されるものではありません。
