# Repository Action (Cromite)

## Usage

1. Fill the secrets
2. Start the action
3. Add the repository with `zypper addrepo --priority 80 $URL/cromite cromite`

## Secrets

|Name|Description|
|---|---|
|RPM_GPG_NAME|Name of your GPG certificate ([help manual](https://manpages.opensuse.org/Tumbleweed/rpm/rpmsign.8.en.html#USING_GPG_TO_SIGN_PACKAGES))|
|RPM_GPG_KEY|Base64 encoded GPG public and private key|
|RPM_RCLONE_CONFIG|Base64 encoded Rclone config that includes a `storage` remote|

## Notes

- The homepage of The Cromite project is included in the RPM metadata.
- The Cromite icon is made by GitHub user austinhuang0131 ([#429 (comment)](https://github.com/uazo/cromite/issues/429#issuecomment-1915985115)).
- This action automatically runs at 17:00 on every friday, however if there are security fixes released before that I will manually run them as well.
