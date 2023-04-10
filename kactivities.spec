#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kactivities
Version  : 5.105.0
Release  : 63
URL      : https://download.kde.org/stable/frameworks/5.105/kactivities-5.105.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.105/kactivities-5.105.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.105/kactivities-5.105.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.0 LGPL-2.1 LGPL-3.0 MIT
Requires: kactivities-bin = %{version}-%{release}
Requires: kactivities-data = %{version}-%{release}
Requires: kactivities-lib = %{version}-%{release}
Requires: kactivities-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
In order to properly display the files, use the GNU man command.

%package bin
Summary: bin components for the kactivities package.
Group: Binaries
Requires: kactivities-data = %{version}-%{release}
Requires: kactivities-license = %{version}-%{release}

%description bin
bin components for the kactivities package.


%package data
Summary: data components for the kactivities package.
Group: Data

%description data
data components for the kactivities package.


%package dev
Summary: dev components for the kactivities package.
Group: Development
Requires: kactivities-lib = %{version}-%{release}
Requires: kactivities-bin = %{version}-%{release}
Requires: kactivities-data = %{version}-%{release}
Provides: kactivities-devel = %{version}-%{release}
Requires: kactivities = %{version}-%{release}

%description dev
dev components for the kactivities package.


%package lib
Summary: lib components for the kactivities package.
Group: Libraries
Requires: kactivities-data = %{version}-%{release}
Requires: kactivities-license = %{version}-%{release}

%description lib
lib components for the kactivities package.


%package license
Summary: license components for the kactivities package.
Group: Default

%description license
license components for the kactivities package.


%prep
%setup -q -n kactivities-5.105.0
cd %{_builddir}/kactivities-5.105.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1681144340
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1681144340
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kactivities
cp %{_builddir}/kactivities-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kactivities/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kactivities-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kactivities/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kactivities-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kactivities/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kactivities-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kactivities/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kactivities-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kactivities/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kactivities-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kactivities/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kactivities-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kactivities/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kactivities-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kactivities/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3 || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kactivities-cli

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kactivities.categories
/usr/share/qlogging-categories5/kactivities.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KActivities/KActivities/ActivitiesModel
/usr/include/KF5/KActivities/KActivities/Consumer
/usr/include/KF5/KActivities/KActivities/Controller
/usr/include/KF5/KActivities/KActivities/Info
/usr/include/KF5/KActivities/KActivities/ResourceInstance
/usr/include/KF5/KActivities/KActivities/Version
/usr/include/KF5/KActivities/kactivities/activitiesmodel.h
/usr/include/KF5/KActivities/kactivities/consumer.h
/usr/include/KF5/KActivities/kactivities/controller.h
/usr/include/KF5/KActivities/kactivities/info.h
/usr/include/KF5/KActivities/kactivities/kactivities_export.h
/usr/include/KF5/KActivities/kactivities/resourceinstance.h
/usr/include/KF5/KActivities/kactivities/version.h
/usr/include/KF5/KActivities/kactivities_version.h
/usr/lib64/cmake/KF5Activities/KF5ActivitiesConfig.cmake
/usr/lib64/cmake/KF5Activities/KF5ActivitiesConfigVersion.cmake
/usr/lib64/cmake/KF5Activities/KF5ActivitiesLibraryTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Activities/KF5ActivitiesLibraryTargets.cmake
/usr/lib64/libKF5Activities.so
/usr/lib64/pkgconfig/libKActivities.pc
/usr/lib64/qt5/mkspecs/modules/qt_KActivities.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Activities.so.5
/usr/lib64/libKF5Activities.so.5.105.0
/usr/lib64/qt5/qml/org/kde/activities/libkactivitiesextensionplugin.so
/usr/lib64/qt5/qml/org/kde/activities/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kactivities/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kactivities/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kactivities/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kactivities/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kactivities/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
/usr/share/package-licenses/kactivities/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kactivities/e712eadfab0d2357c0f50f599ef35ee0d87534cb
