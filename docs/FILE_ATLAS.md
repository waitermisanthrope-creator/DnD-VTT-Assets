## Verified six-theme delivery

Current catalogv8 includes six1.2.1 packs for Unity1.00.30 and six real native previews, published39886887017 and independently verified. sources/dice-native-render-v1.json pins app30/source da5a40354c6854ebf57b6f35f823080d9fd42b47/index22bd94b490c5dfd431af6914a57ecb2ccb0ead9201bab810c5dc2450040f33db. v7 trial29 and v6 stable28 unchanged. Details docs/DICE_THEMES.md.

## Corrected trial catalog —2026-10-23

- catalog/v8/index.json — six1.2.1 updates, requires10030; v7 remains failed-visual29 trial, v6 remains28.
- Existing source-sheet/faces producer mirrors corner U to match corrected exterior frame; original source art retained.
- Existing native preview producer now supports6-set v8 with exact app render-index pin; final descriptor awaits reviewed30 renders.

## Test-six source additions —2026-10-23

- sources/dice-materials/test-six-v1/source-sheet.png — reference-authored12 material regions; not3D preview.
- sources/dice-materials/test-six-v1/faces.json — actual DiceGeometry face values/corner UV/opposite labels.
- sources/dice-materials/test-six-v1/provenance.json — art origin and distribution scope.
- tools/package_dice_themes.py --experiments — existing producer, immutable1.2 packages and catalogv7.
- catalog/v7/index.json — activated only after public payload hash verification by existing pipeline.

# Атлас всех файлов DnD-VTT-Assets — для ИИ и разработчиков

**Назначение:** точная карта каждого Git-отслеживаемого файла этого репозитория на момент 22.10.2026, + новые служебные файлы из текущего комплекта документации. Снимок построен из рекурсивного Git-дерева ветки `main`; для уже подготовленного `docs/FILE_ATLAS.md` размер указан `—` до коммита. **Всего записей: 45**. Файлы в GitHub Releases, сгенерированные бинарники и отсутствующие в Git файлы сюда не входят. При новых коммитах проверяй фактическое дерево и актуализируй атлас.

**Как использовать:** новому автору/ChatGPT сначала прочитать `README.md` и `AGENTS.md`. Для создания модов главным учебником является `DnD-VTT-Content/docs/MOD_AUTHOR_GUIDE.md`. Для поиска «где живёт X» используй таблицу ниже; не дублируй существующий файл или ID. Для конфликтов таблицы с кодом/каталогом приоритет у **текущих файлов**.

## Категории и границы

- **Каталог Unity1.00.24+:** `catalog/v5/index.json` (106 позиций); v4 (75 позиций) сохранён для1.00.23. Исторические `v1/v2/v3` не переписывать.
- **Физические пакеты:** `packages/*.json` содержит карты, цвета, примитивы. Многие графические JSON-пакеты и JPEG-превью живого каталога находятся в **GitHub Releases**, а не в `packages/` Git-дерева. Отсутствие такого файла в этом списке не означает пропажу скачивания.
- **Источники:** `sources/` + `migration/` содержат исходную лицензионную документацию/историю, **не** являются готовыми подписанными AssetBundles.
- **Сборка:** `tools/` и `.github/workflows/` относятся к подготовке доверенных релизов/предпросмотров. Для реальных 3D-моделей нужны платформенные AssetBundles, проверка Unity и лицензии.
- **Связь с Unity:** URL живого каталога и проверка установленных ресурсов находятся в `LegacySessionPanel.ContentManager.cs` и `WorkshopStore.cs` экспериментальной ветки приложения.

Количество файлов по верхним разделам: `.github` — 4; `.gitignore` — 1; `AGENTS.md` — 1; `catalog` — 4; `docs` — 5; `migration` — 5; `packages` — 12; `README.md` — 1; `schemas` — 3; `sources` — 5; `tools` — 4.

## Полная инвентаризация

| № | Путь | Размер Git blob | Роль / назначение |
|---:|---|---:|---|
| 1 | `.github/workflows/owner-appearance-release.yml` | 2779 B | GitHub Actions: owner appearance release; действия по сборке/публикации источников или предпросмотров. |
| 2 | `.github/workflows/quaternius-source-release.yml` | 1124 B | GitHub Actions: quaternius source release; действия по сборке/публикации источников или предпросмотров. |
| 3 | `.github/workflows/reviewed-source-release.yml` | 1012 B | GitHub Actions: reviewed source release; действия по сборке/публикации источников или предпросмотров. |
| 4 | `.github/workflows/workshop-previews-release.yml` | 2367 B | GitHub Actions: workshop previews release; действия по сборке/публикации источников или предпросмотров. |
| 5 | `.gitignore` | 19 B | Правила исключения локальных/сгенерированных файлов из Git. |
| 6 | `AGENTS.md` | — | Правила поведения ИИ при создании модификаций; стартовая инструкция для ChatGPT. |
| 7 | `catalog/v1/index.json` | 1574 B | Индекс Assets v1; исторический снимок для совместимости со старыми клиентами; не изменять устаревшие версии без причины. |
| 8 | `catalog/v2/index.json` | 10887 B | Индекс Assets v2; исторический снимок для совместимости со старыми клиентами; не изменять устаревшие версии без причины. |
| 9 | `catalog/v3/index.json` | 75648 B | Индекс Assets v3; исторический снимок для совместимости со старыми клиентами; не изменять устаревшие версии без причины. |
| 10 | `catalog/v4/index.json` | 103140 B | Индекс Assets v4; исторический снимок для совместимости со старыми клиентами; не изменять устаревшие версии без причины. |
| 11 | `docs/ASSET_PIPELINE.md` | 2398 B | Стадии доверенной сборки/распространения графических ресурсов и AssetBundles. |
| 12 | `docs/FILE_ATLAS.md` | — | Этот полный реестр путей и назначений файлов; обновлять при изменении дерева. |
| 13 | `docs/LICENSE_REVIEW.md` | 2830 B | Проверка лицензий и происхождения сторонних графических источников. |
| 14 | `docs/OWNER_APPEARANCE.md` | 1172 B | Происхождение и условия использования ресурсов оформления владельца. |
| 15 | `docs/TEST-PACKAGES.md` | 307 B | Условия происхождения и лицензии демонстрационных оригинальных пакетов. |
| 16 | `migration/main-assets-inventory.json` | 138743 B | Инвентаризация визуальных ресурсов исходного приложения; справочник миграции. |
| 17 | `migration/owner-appearance.json` | 15706 B | Реестр упаковки исходного оформления владельца и атрибуции. |
| 18 | `migration/quaternius-source-release.json` | 47480 B | Метаданные происхождения/публикации исходников Quaternius. |
| 19 | `migration/reviewed-source-release.json` | 1107 B | Список проверенных исходников для опубликованного набора. |
| 20 | `migration/verified-copies-v1.json` | 2003 B | Соответствие проверенных копий исходным ресурсам/хешам. |
| 21 | `packages/demo.appearance.amber.json` | 722 B | Оформление/цвета/связанные изображения: **Янтарное оформление карты**; id demo.appearance.amber; запись есть в текущем каталоге. |
| 22 | `packages/demo.model.markers.json` | 877 B | Простые модели-примитивы: **Геометрические маркеры**; id demo.model.markers; запись есть в текущем каталоге. |
| 23 | `packages/dnd.appearance.map-surfaces.json` | 9628 B | Оформление/цвета/связанные изображения: **Поверхности карт — новые процедурные текстуры**; id dnd.appearance.map-surfaces; запись есть в текущем каталоге. |
| 24 | `packages/dnd.map.3d-castle-black-rose-v740030.json` | 328830 B | Карта с геометрией/объектами: **Замок Чёрной Розы · 4 этажа**; id dnd.map.3d-castle-black-rose-v740030; запись есть в текущем каталоге. |
| 25 | `packages/dnd.map.3d-castle-v740019.json` | 199925 B | Карта с геометрией/объектами: **Замок Серебряной стражи**; id dnd.map.3d-castle-v740019; запись есть в текущем каталоге. |
| 26 | `packages/dnd.map.3d-house-v740019.json` | 47682 B | Карта с геометрией/объектами: **Дом травницы**; id dnd.map.3d-house-v740019; запись есть в текущем каталоге. |
| 27 | `packages/dnd.map.3d-stress-test-all.json` | 197972 B | Карта с геометрией/объектами: **3D СТРЕСС-ТЕСТ — ВСЕ ТЕКСТУРЫ И МЕБЕЛЬ**; id dnd.map.3d-stress-test-all; запись есть в текущем каталоге. |
| 28 | `packages/dnd.map.3d-stress-v740026.json` | 864469 B | Карта с геометрией/объектами: **Стресс-карта 72×72 · все объекты**; id dnd.map.3d-stress-v740026; запись есть в текущем каталоге. |
| 29 | `packages/dnd.map.3d-tavern-v740019.json` | 65207 B | Карта с геометрией/объектами: **Таверна «Медный грифон»**; id dnd.map.3d-tavern-v740019; запись есть в текущем каталоге. |
| 30 | `packages/dnd.map.3d-test-dungeon.json` | 39922 B | Карта с геометрией/объектами: **3D Тестовая карта — комнаты и свет**; id dnd.map.3d-test-dungeon; запись есть в текущем каталоге. |
| 31 | `packages/dnd.map.3d-town-v740019.json` | 151675 B | Карта с геометрией/объектами: **Городок Каменный мост**; id dnd.map.3d-town-v740019; запись есть в текущем каталоге. |
| 32 | `packages/dnd.map.3d-village-v740019.json` | 74458 B | Карта с геометрией/объектами: **Деревня у реки**; id dnd.map.3d-village-v740019; запись есть в текущем каталоге. |
| 33 | `README.md` | 4231 B | Обзор и статус реестра, ограничения и ссылки для разработчиков. |
| 34 | `schemas/asset-pack-v1.schema.json` | 1643 B | Схема описания ассетов/платформ; не является содержимым runtime-пакета. |
| 35 | `schemas/catalog-entry-v1.schema.json` | 2876 B | JSON Schema каталожной записи (обязательные поля манифеста, URL, платформа, SHA-256). |
| 36 | `schemas/catalog-entry-v3.schema.json` | 3209 B | JSON Schema каталожной записи (обязательные поля манифеста, URL, платформа, SHA-256). |
| 37 | `sources/app/assets/3d/makehuman/LICENSE.ASSETS.md` | 6962 B | Лицензионные условия исходных MakeHuman/Quaternius-ресурсов. |
| 38 | `sources/app/assets/3d/makehuman/README.md` | 1510 B | Справочное описание происхождения source-ассетов; не распространять без проверки лицензии. |
| 39 | `sources/app/assets/3d/makehuman/skins/young_caucasian_female/young_caucasian_female.mhmat` | 1464 B | Исходный материал кожи MakeHuman; не самостоятельный мод для загрузки из приложения. |
| 40 | `sources/app/assets/3d/makehuman/skins/young_caucasian_male/young_caucasian_male.mhmat` | 1462 B | Исходный материал кожи MakeHuman; не самостоятельный мод для загрузки из приложения. |
| 41 | `sources/quaternius-fantasy-props-standard/License_Standard.txt` | 837 B | Справочное описание происхождения source-ассетов; не распространять без проверки лицензии. |
| 42 | `tools/package_owner_appearance.py` | 3221 B | Инструмент подготовки/упаковки исходных ассетов или JPEG-предпросмотров; не runtime-контент. |
| 43 | `tools/package_quaternius_sources.py` | 1683 B | Инструмент подготовки/упаковки исходных ассетов или JPEG-предпросмотров; не runtime-контент. |
| 44 | `tools/package_reviewed_sources.py` | 1650 B | Инструмент подготовки/упаковки исходных ассетов или JPEG-предпросмотров; не runtime-контент. |
| 45 | `tools/package_workshop_previews.py` | 4255 B | Инструмент подготовки/упаковки исходных ассетов или JPEG-предпросмотров; не runtime-контент. |

## Правила для ChatGPT

1. Объясни человеку, как устроены каталоги и пакеты, **на примере реального файла из этого списка**. Прочитай руководство и смежные схемы.
2. Всегда найди ID в актуальном каталоге, прежде чем создавать новый файл. Для изменения одной расы не переписывай сотни других записей.
3. Изменения в `packages/` и `catalog/` должны соответствовать друг другу по ID, версии, доступному URL, точной длине и SHA-256. Выдуманные хеши/результаты тестов запрещены.
4. Отмечай, что проверено фактически, а что ещё нужно проверить устройством. Не обещай совместимость для неизвестных эффектов Unity.
5. Публикация в `main` — публикация для **всех пользователей**, не приватный тестовый режим. Черновик до публикации держи в рабочей ветке.

## Icon-linked dice extension (2026-10-22)

`catalog/v5/index.json` adds31 sets for generator-capable Unity1.00.24+.
`tools/package_dice_themes.py` produces `packages/dnd.dice.icon.{01..30,default}.json`.
`docs/DICE_THEMES.md` documents parameters, physical collisions and limits.
The31 recipes total15,143 bytes; original icon dependencies and v4 remain unchanged.

### Additional tracked dice files

| Path | Bytes | Purpose |
|---|---:|---|
| `catalog/v5/index.json` | 150475 | Generator-capable client catalog; v4 preserved |
| `docs/DICE_THEMES.md` | 2273 | Generator, physical collision and preview contract |
| `packages/dnd.dice.icon.01.json` | 477 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.02.json` | 478 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.03.json` | 490 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.04.json` | 492 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.05.json` | 487 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.06.json` | 488 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.07.json` | 479 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.08.json` | 493 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.09.json` | 499 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.10.json` | 493 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.11.json` | 496 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.12.json` | 487 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.13.json` | 490 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.14.json` | 495 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.15.json` | 492 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.16.json` | 485 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.17.json` | 495 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.18.json` | 486 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.19.json` | 481 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.20.json` | 495 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.21.json` | 488 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.22.json` | 494 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.23.json` | 489 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.24.json` | 484 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.25.json` | 479 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.26.json` | 489 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.27.json` | 485 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.28.json` | 492 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.29.json` | 493 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.30.json` | 477 | Full icon-linked dice recipe |
| `packages/dnd.dice.icon.default.json` | 495 | Full icon-linked dice recipe |
| `tools/package_dice_themes.py` | 4601 | Reproducible recipe/hash/catalog producer |

### Actual dice geometry previews

| Path | Bytes | Purpose |
|---|---:|---|
| `sources/dice-preview-geometry-v1.json` | 822526 | Actual exported C# meshes, source commit and recipe SHA; offline schematic rendering only |
| `tools/dice_geometry_preview.py` | 2188 | Bounded320x200 triangle projection used by existing preview publisher |

- sources/dice-materials/gothic-atlas-v1.png — generated game UV atlas; see provenance-v1.json.
- sources/dice-materials/provenance-v1.json — reference/packaging/license provenance.
- catalog/v6/index.json — activated by existing appearance publisher after public SHA checks; v5 preserved.

- sources/dice-native-render-v1.json — exact reviewed Unity1.00.28 native render index/source/run/31 recipe hashes; consumed by existing preview publisher.

### 2026-10-23 tray producer extension

- `tools/package_dice_themes.py --trays`: four bounded native tray recipes and v9 candidate catalog; no new competing producer.
- `.github/workflows/owner-appearance-release.yml`: immutable upload/public SHA validation, then v9 activation; v8 and six1.2.1 dice unchanged.
- `schemas/catalog-entry-v3.schema.json`: additive dice-tray imageKind.

### 2026-10-23 reviewed native32 preview activation

- `catalog/v9/index.json`: existing107payloads plus4native tray recipes; ten native32 preview/description metadata updates, no payload mutation.
- `sources/dice-native-render-v1.json`: exact reviewed app32/source/run/index pin, ten package SHA/profile mappings.
- `tools/package_workshop_previews.py --native-dice`: v9 supports six material and four tray native captures; older v6/v7/v8 modes retained.
- `.github/workflows/workshop-previews-release.yml`: existing publisher verifies new ten public JPEGs then activatesv9.

### 2026-10-23 reviewed native34 preview pin

Existing sources/dice-native-render-v1.json now pins reviewed34/source24b2a477/run39952385083/indexfc8ad8922b789acbde3772e3ae950968eb4b1d0f488526995f77af0483885762. Existing preview publisher derives ten new immutable JPEGs and verifies public bytes before catalogv9 metadata activation. Six1.2.1 materials/four1.0.0 tray payloads, all existing IDs and old native32 JPEGs remain unchanged. README/AGENTS/docs/DICE_THEMES.md identify current34 correction and device-QA boundary. No new producer or file format.

## Verified native34 delivery evidence

Existing preview publisher39956772016/job120424443608 SUCCESS, catalogv9 activationd279bae0a337418f8a086cce9794b99e14bddc1a. All ten actual public JPEGs147551bytes independently downloaded and SHA/size/dimensions checked; both plain/cache-busted catalogs equal independently regenerated34 metadata.111payload records unchanged. App34 activation7ea3934398628b4ad5717086e36bb766784f5bc2 and both public feed forms10034 verified. APK original v2/v3 signature retained. Physical phone and interactive desktop QA remain owner work.

## Полные сборники, клиент10036+, 23.10.2026

- `packages/dnd.collections.icons-1.0.0.json`, `packages/dnd.collections.wallpapers-1.0.0.json`, `packages/dnd.collections.dice-1.0.0.json`, `packages/dnd.collections.dice-trays-1.0.0.json`, `packages/dnd.collections.maps-1.0.0.json`, `packages/dnd.collections.models-1.0.0.json`, `packages/dnd.collections.surfaces-1.0.0.json`: семь корневых групп всех111 исходных модов.
- `sources/mod-category-collections-1.0.0.json`: точные ID состава.
- `catalog/v9/index.json`:118 записей, исходные111 не менялись; v1–v8 сохранены.
- Генератор/верификатор/схема находятся в Content: `tools/build_mod_collections.py`, `tools/verify_mod_collections.py`, `schemas/mod-collection-v1.schema.json`. Новые метаданные не копируют исходные арты и не меняют их права.
