# Repository Action (Mesa)

## Usage

1. Fill the secrets
2. Start the action
3. Add the repository with `zypper addrepo --priority 80 $URL/mesa mesa`

## Secrets

|Name|Description|
|---|---|
|OBS_API_URL|API URL for an openSUSE Build Service instance|
|OBS_USER|Username for an openSUSE Build Service instance|
|OBS_PASS|Password for an openSUSE Build Service instance|
|RPM_GPG_NAME|Name of your GPG certificate ([help manual](https://manpages.opensuse.org/Tumbleweed/rpm/rpmsign.8.en.html#USING_GPG_TO_SIGN_PACKAGES))|
|RPM_GPG_KEY|Base64 encoded GPG public and private key|
|RPM_RCLONE_CONFIG|Base64 encoded Rclone config that includes a `storage` remote|

## Notes

- Due to possible patent troll, binary packages are not provided publicly, fork this repository and build it yourself.
- Due to the usage of `osc`, dependencies are fetched from openSUSE Build Service instead of the corresponding repository, ensure "Build Results" is not `blocked` or `unresolvable` on [openSUSE Build Service](https://build.opensuse.org/package/show/openSUSE:Factory/Mesa) before start the action.
- This action only generate a repository for `Mesa`, Packman repository is still required for other utilities.