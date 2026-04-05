#
# spec file for package cromite
#
# Copyright (c) 2023 Fei Yang <io@feiyang.eu.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


Name:           cromite-stable
Version:        __CROMITE_VERSION__
Release:        0
Summary:        A Bromite fork with ad blocking and privacy enhancements
License:        GPL-3.0-only
URL:            https://github.com/uazo/cromite
Source0:        https://github.com/uazo/cromite/releases/download/latest/chrome-lin64.tar.gz
Source1:        cromite.desktop
Source2:        cromite.png

%description
Cromite is a Chromium fork based on Bromite with built-in support for ad blocking and an eye for privacy.

%prep
%setup -q -n chrome-lin

%build
find . \( -name 'chrome' -or -name 'chrome_crashpad_handler' -or -name '*.so' \) -exec strip {} \;
sed -i 's#^DESKTOP=".*"#DESKTOP="cromite"#' chrome-wrapper
sed -i 's#^TITLE=".*"#TITLE="Cromite"#' chrome-wrapper

%install
install -dm755 %{buildroot}%{_bindir}
install -dm755 %{buildroot}%{_datadir}/applications
install -dm755 %{buildroot}%{_datadir}/icons/hicolor/192x192/apps
install -dm755 %{buildroot}/opt
ln -s /opt/cromite/chrome-wrapper %{buildroot}%{_bindir}/cromite-stable
install -m644 %{SOURCE1} %{buildroot}%{_datadir}/applications/cromite.desktop
install -m644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/192x192/apps/cromite.png
cp -pr . %{buildroot}/opt/cromite

%post
UPDATE_MENUS="`command -v update-menus 2> /dev/null || true`"
if [ -x "$UPDATE_MENUS" ]; then
  update-menus
fi

# Update cache of .desktop file MIME types. Non-fatal since it's just a cache.
update-desktop-database > /dev/null 2>&1 || true

/usr/sbin/update-alternatives --install /usr/bin/cromite \
  cromite /usr/bin/cromite-stable 200

%preun
if [ "$1" -eq "0" ]; then
  mode="uninstall"
elif [ "$1" -eq "1" ]; then
  mode="upgrade"
fi

if [ "$mode" = "uninstall" ]; then
UPDATE_MENUS="`command -v update-menus 2> /dev/null || true`"
if [ -x "$UPDATE_MENUS" ]; then
  update-menus
fi

# Update cache of .desktop file MIME types. Non-fatal since it's just a cache.
update-desktop-database > /dev/null 2>&1 || true

/usr/sbin/update-alternatives --remove cromite \
  /usr/bin/cromite-stable
fi

%files
/usr/bin/cromite-stable
/usr/share/applications/cromite.desktop
/usr/share/icons/hicolor/192x192/apps/cromite.png
/opt/cromite

%changelog
