# Release Checklist

Use this checklist before publishing a new release.

## Pre-Release Checks

- [ ] Review open pull requests and merge only focused, reviewed changes.
- [ ] Run repository checks:

  ```bash
  python3 scripts/check_templates.py
  ```

- [ ] Confirm README quick links are current.
- [ ] Confirm `docs/TEMPLATE_INDEX.md` includes newly added templates.
- [ ] Confirm `CONTRIBUTING.md` still matches maintainer expectations.
- [ ] Update `CHANGELOG.md` with the release date and summary.

## Release Steps

1. Create a version tag:

   ```bash
   git tag vX.Y.Z
   git push origin vX.Y.Z
   ```

2. Create a GitHub release from the tag.
3. Include release notes with:
   - user-facing improvements;
   - maintainer workflow improvements;
   - template or documentation changes;
   - known limitations or deferred work.

## Post-Release Checks

- [ ] Confirm the release page renders correctly on GitHub.
- [ ] Confirm the tag points to the intended commit.
- [ ] Confirm repository checks pass on `main`.
- [ ] Open follow-up issues for deferred maintenance work.
