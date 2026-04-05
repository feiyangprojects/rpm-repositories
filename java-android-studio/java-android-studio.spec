# Standard JPackage naming and versioning defines.
%global featurever      0
%global interimver      99
#global updatever       99
%global buildver        99
# priority must be 6 digits in total
#global priority        3505
%global priority        0
%global javaver         %{featurever}
%ifarch ppc s390
%global _jvmdir /usr/lib/jvm
%global bits 32
%endif
%ifarch x86_64 ia64 s390x
%global _jvmdir /usr/lib64/jvm
%global bits 64
%endif
%global java_bootstrap 1

Name:           stub
Version:        1.0.0
Release:        0
Summary:        Stub package
License:        Unlicense

%description
Stub package

%package        -n java-%{javaver}-android-studio
Summary:        Stub for package java-%{javaver}-android-studio
Group:          Development/Languages/Java
Version:        %{featurever}.%{interimver}.%{?updatever:%{updatever}}%{!?updatever:0}.%{?patchver:%{patchver}}%{!?patchver:0}
Requires:       android-studio
Requires:       java-%{javaver}-android-studio-headless = %{version}-%{release}
%if 0%{?suse_version} > 1315 || 0%{?java_bootstrap}
%if 0%{?bits} == 64
Provides:       libjawt.so()(64bit)
Provides:       libawt_xawt.so()(64bit)
Provides:       libsplashscreen.so()(64bit)
%else
Provides:       libjawt.so
Provides:       libawt_xawt.so
Provides:       libsplashscreen.so
%endif
Provides:       java = %{javaver}
Provides:       java-%{javaver} = %{version}-%{release}
Provides:       java-openjdk = %{version}-%{release}
Provides:       jre = %{javaver}
Provides:       jre-%{javaver} = %{version}-%{release}
Provides:       jre-%{javaver}-openjdk = %{version}-%{release}
Provides:       jre-openjdk = %{version}-%{release}
# Standard JPackage extensions provides.
Provides:       java-fonts = %{version}
# Required at least by fop
Provides:       java-%{bits} = %{javaver}
Provides:       java-%{javaver}-%{bits}
Provides:       java-openjdk-%{bits} = %{version}-%{release}
Provides:       jre-%{bits} = %{javaver}
Provides:       jre-%{javaver}-%{bits}
Provides:       jre-%{javaver}-openjdk-%{bits} = %{version}-%{release}
Provides:       jre-openjdk-%{bits} = %{version}-%{release}
Provides:       jre1.10.x
Provides:       jre1.3.x
Provides:       jre1.4.x
Provides:       jre1.5.x
Provides:       jre1.6.x
Provides:       jre1.7.x
Provides:       jre1.8.x
Provides:       jre1.9.x
%endif

%description    -n java-%{javaver}-android-studio
Stub for package java-%{javaver}-android-studio.

%files          -n java-%{javaver}-android-studio

%package        -n java-%{javaver}-android-studio-headless
Summary:        Stub for package java-%{javaver}-android-studio-headless
Group:          Development/Languages/Java
Version:        %{featurever}.%{interimver}.%{?updatever:%{updatever}}%{!?updatever:0}.%{?patchver:%{patchver}}%{!?patchver:0}
Requires:       android-studio
# Post requires update-alternatives to install tool update-alternatives.
Requires(post): update-alternatives
# Postun requires update-alternatives to uninstall tool update-alternatives.
Requires(postun): update-alternatives
%if 0%{?suse_version} > 1315 || 0%{?java_bootstrap}
# Standard JPackage base provides.
Provides:       java-%{javaver}-headless = %{version}-%{release}
Provides:       java-headless = %{javaver}
Provides:       java-openjdk-headless = %{version}-%{release}
Provides:       jre-%{javaver}-headless = %{version}-%{release}
Provides:       jre-%{javaver}-openjdk-headless = %{version}-%{release}
Provides:       jre-headless = %{javaver}
Provides:       jre-openjdk-headless = %{version}-%{release}
# Standard JPackage extensions provides.
Provides:       jaas = %{version}
Provides:       java-sasl = %{version}
Provides:       jce = %{version}
Provides:       jdbc-stdext = 4.3
Provides:       jndi = %{version}
Provides:       jndi-cos = %{version}
Provides:       jndi-dns = %{version}
Provides:       jndi-ldap = %{version}
Provides:       jndi-rmi = %{version}
Provides:       jsse = %{version}
%endif

%description    -n java-%{javaver}-android-studio-headless
Stub for package java-%{javaver}-android-studio-headless.

%post           -n java-%{javaver}-android-studio-headless
ext=.gz
update-alternatives \
  --install %{_bindir}/java java %{_libexecdir}/android-studio/jbr/bin/java %{priority} \
  --slave %{_jvmdir}/jre jre %{_libexecdir}/android-studio/jbr \
  --slave %{_bindir}/keytool keytool %{_libexecdir}/android-studio/jbr/bin/keytool \
  --slave %{_bindir}/rmiregistry rmiregistry %{_libexecdir}/android-studio/jbr/bin/rmiregistry

update-alternatives \
  --install %{_jvmdir}/jre-android-studio \
  jre_android-studio %{_libexecdir}/android-studio/jbr %{priority}
update-alternatives \
  --install %{_jvmdir}/jre-%{javaver} \
  jre_%{javaver} %{_libexecdir}/android-studio/jbr %{priority}

%postun         -n java-%{javaver}-android-studio-headless
if [ $1 -eq 0 ]
then
  if test -f /proc/sys/fs/binfmt_misc/jarexec
  then
    echo '-1' > /proc/sys/fs/binfmt_misc/jarexec
  fi
  update-alternatives --remove java %{_libexecdir}/android-studio/jbr/bin/java
  update-alternatives --remove jre_android-studio %{_libexecdir}/android-studio/jbr
  update-alternatives --remove jre_%{javaver} %{_libexecdir}/android-studio/jbr
fi

%files          -n java-%{javaver}-android-studio-headless

%package        -n java-%{javaver}-android-studio-devel
Summary:        Stub for package java-%{javaver}-android-studio-devel
# Require base package.
Group:          Development/Languages/Java
Version:        %{featurever}.%{interimver}.%{?updatever:%{updatever}}%{!?updatever:0}.%{?patchver:%{patchver}}%{!?patchver:0}
Requires:       java-%{javaver}-android-studio = %{version}-%{release}
# Post requires update-alternatives to install tool update-alternatives.
Requires(post): update-alternatives
# Postun requires update-alternatives to uninstall tool update-alternatives.
Requires(postun): update-alternatives
%if 0%{?suse_version} > 1315 || 0%{?java_bootstrap}
# Standard JPackage devel provides.
Provides:       java-%{javaver}-devel = %{version}
Provides:       java-devel = %{javaver}
Provides:       java-devel-openjdk = %{version}
Provides:       java-sdk = %{javaver}
Provides:       java-sdk-%{javaver} = %{version}
Provides:       java-sdk-%{javaver}-openjdk = %{version}
Provides:       java-sdk-openjdk = %{version}
%endif

%description    -n java-%{javaver}-android-studio-devel
Stub for package java-%{javaver}-android-studio-devel.

%post           -n java-%{javaver}-android-studio-devel
ext=.gz
update-alternatives \
  --install %{_bindir}/javac javac %{_libexecdir}/android-studio/jbr/bin/javac %{priority} \
  --slave %{_bindir}/javadoc javadoc %{_libexecdir}/android-studio/jbr/bin/javadoc \
  --slave %{_bindir}/jcmd jcmd %{_libexecdir}/android-studio/jbr/bin/jcmd \
  --slave %{_bindir}/jdb jdb %{_libexecdir}/android-studio/jbr/bin/jdb \
  --slave %{_bindir}/jhsdb jhsdb %{_libexecdir}/android-studio/jbr/bin/jhsdb \
  --slave %{_bindir}/jinfo jinfo %{_libexecdir}/android-studio/jbr/bin/jinfo \
  --slave %{_bindir}/jmap jmap %{_libexecdir}/android-studio/jbr/bin/jmap \
  --slave %{_bindir}/jps jps %{_libexecdir}/android-studio/jbr/bin/jps \
  --slave %{_bindir}/jrunscript jrunscript %{_libexecdir}/android-studio/jbr/bin/jrunscript \
  --slave %{_bindir}/jstack jstack %{_libexecdir}/android-studio/jbr/bin/jstack \
  --slave %{_bindir}/jstat jstat %{_libexecdir}/android-studio/jbr/bin/jstat \
  --slave %{_bindir}/jwebserver jwebserver %{_libexecdir}/android-studio/jbr/bin/jwebserver

update-alternatives \
  --install %{_jvmdir}/java-android-studio \
  java_sdk_android-studio %{_libexecdir}/android-studio/jbr %{priority}
update-alternatives \
  --install %{_jvmdir}/java-%{javaver} \
  java_sdk_%{javaver} %{_libexecdir}/android-studio/jbr %{priority}

%postun         -n java-%{javaver}-android-studio-devel
if [ $1 -eq 0 ]
then
  update-alternatives --remove javac %{_libexecdir}/android-studio/jbr/bin/javac
  update-alternatives --remove java_sdk_android-studio %{_libexecdir}/android-studio/jbr
  update-alternatives --remove java_sdk_%{javaver} %{_libexecdir}/android-studio/jbr
fi

%files          -n java-%{javaver}-android-studio-devel
